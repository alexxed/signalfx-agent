from functools import partial as p

import hashlib
import pytest
import time

from datetime import datetime
from elasticsearch import Elasticsearch
from random import randint

from tests.helpers.agent import Agent
from tests.helpers.assertions import has_datapoint_with_all_dims, has_datapoint_with_metric_name, http_status
from tests.helpers.util import container_ip, run_service, wait_for

AGENT_CONFIG_TEMPLATE = """
    monitors:
    - type: elasticsearch-query
      host: {host}
      port: 9200
      index: {index}
      elasticsearchRequest: {query}
    """


def check_service_status(host):
    assert wait_for(p(http_status, url=f"http://{host}:9200/_nodes/_local", status=[200]), 180), "service didn't start"


def test_elasticsearch_query_simple_metric_aggs():
    with run_service("elasticsearch/6.4.2") as es_container:
        host = container_ip(es_container)
        check_service_status(host)
        write_data(host)

        query = '\'{"query":{"match_all":{}},"aggs":{"avg_cpu_utilization":{"avg":{"field":"cpu_utilization"}}}}\''

        agent_config = AGENT_CONFIG_TEMPLATE.format(host=host, index="metrics", query=query)

        with Agent.run(agent_config) as agent:
            assert wait_for(
                p(
                    has_datapoint_with_all_dims,
                    agent.fake_services,
                    {"index": "metrics", "metric_aggregation_name": "avg_cpu_utilization"},
                )
            ), "Didn't get elasticsearch-query dimensions"
            assert wait_for(
                p(has_datapoint_with_metric_name, agent.fake_services, "avg")
            ), "Didn't get elasticsearch-query metric"


def write_data(host):
    es = Elasticsearch(hosts=[host])

    mappings = {
        "mappings": {
            "properties": {
                "host": {"type": "text", "fielddata": True},
                "service": {"type": "text", "fielddata": True},
                "container_id": {"type": "text", "fielddata": True},
                "cpu_utilization": {"type": "double"},
                "memory_utilization": {"type": "double"},
                "@timestamp": {"type": "date"},
            }
        }
    }

    # create an index to write metrics
    es.indices.create(index="metrics", body=mappings, ignore=400)

    # metrics to mock
    metric_groups = ["cpu", "memory"]

    # dimensions to mock
    dimensions_set = [
        {"host": "nairobi", "service": "android", "container_id": "macbook"},
        {"host": "nairobi", "service": "ios", "container_id": "lenovo"},
        {"host": "helsniki", "service": "android", "container_id": "macbook"},
        {"host": "helsniki", "service": "ios", "container_id": "lenovo"},
        {"host": "madrid", "service": "android", "container_id": "macbook"},
        {"host": "madrid", "service": "ios", "container_id": "lenovo"},
        {"host": "lisbon", "service": "android", "container_id": "macbook"},
        {"host": "lisbon", "service": "ios", "container_id": "lenovo"},
    ]

    i = 0
    while i < 10:
        for dim_set in dimensions_set:
            id_str = ""
            doc = {}
            for mg in metric_groups:
                doc[mg + "_utilization"] = randint(0, 100)

            for dim_key, dim_val in dim_set.items():
                doc[dim_key] = dim_val
                id_str += dim_key + ":" + dim_val + "_"

            doc["@timestamp"] = i

            id_str += str(i)

            hash_object = hashlib.md5(id_str.encode("utf-8"))
            id = hash_object.hexdigest()
            res = es.index(index="metrics", doc_type="_doc", id=id, body=doc)

        i = i + 1
