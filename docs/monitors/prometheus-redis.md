<!--- GENERATED BY gomplate from scripts/docs/monitor-page.md.tmpl --->

# prometheus/redis

This monitor scrapes [Prmoetheus Redis
Exporter](https://github.com/oliver006/redis_exporter) metrics and sends
them to SignalFx.  It is a wrapper around the
[prometheus-exporter](./prometheus-exporter.md) monitor that provides a
restricted but expandable set of metrics.


Monitor Type: `prometheus/redis`

[Monitor Source Code](https://github.com/signalfx/signalfx-agent/tree/master/internal/monitors/prometheus/redis)

**Accepts Endpoints**: **Yes**

**Multiple Instances Allowed**: Yes

## Configuration

| Config option | Required | Type | Description |
| --- | --- | --- | --- |
| `host` | **yes** | `string` | Host of the exporter |
| `port` | **yes** | `integer` | Port of the exporter |
| `useHTTPS` | no | `bool` | If true, the agent will connect to the exporter using HTTPS instead of plain HTTP. (**default:** `false`) |
| `skipVerify` | no | `bool` | If useHTTPS is true and this option is also true, the exporter's TLS cert will not be verified. (**default:** `false`) |
| `metricPath` | no | `string` | Path to the metrics endpoint on the exporter server, usually `/metrics` (the default). (**default:** `/metrics`) |
| `sendAllMetrics` | no | `bool` | Send all the metrics that come out of the Prometheus exporter without any filtering.  This option has no effect when using the prometheus exporter monitor directly since there is no built-in filtering, only when embedding it in other monitors. (**default:** `false`) |




## Metrics

The following table lists the metrics available for this monitor. Metrics that are marked as Included are standard metrics and are monitored by default.

| Name | Type | Included | Description |
| ---  | ---  | ---    | ---         |
| `redis_aof_current_rewrite_duration_sec` | gauge |  | aof_current_rewrite_duration_sec metric |
| `redis_aof_enabled` | gauge |  | aof_enabled metric |
| `redis_aof_last_rewrite_duration_sec` | gauge |  | aof_last_rewrite_duration_sec metric |
| `redis_aof_rewrite_in_progress` | gauge |  | aof_rewrite_in_progress metric |
| `redis_aof_rewrite_scheduled` | gauge |  | aof_rewrite_scheduled metric |
| `redis_blocked_clients` | gauge |  | blocked_clients metric |
| `redis_client_biggest_input_buf` | gauge |  | client_biggest_input_buf metric |
| `redis_client_longest_output_list` | gauge |  | client_longest_output_list metric |
| `redis_cluster_enabled` | gauge |  | cluster_enabled metric |
| `redis_command_call_duration_seconds_count` | gauge |  | command_call_duration_seconds_count metric |
| `redis_command_call_duration_seconds_sum` | gauge |  | Total amount of time in seconds spent per command |
| `redis_commands_processed_total` | gauge |  | commands_processed_total metric |
| `redis_config_maxclients` | gauge |  | config_maxclients metric |
| `redis_config_maxmemory` | gauge |  | config_maxmemory metric |
| `redis_connected_clients` | gauge |  | connected_clients metric |
| `redis_connected_slaves` | gauge |  | connected_slaves metric |
| `redis_connections_received_total` | gauge |  | connections_received_total metric |
| `redis_db_avg_ttl_seconds` | gauge |  | Avg TTL in seconds |
| `redis_db_keys` | gauge |  | Total number of keys by DB |
| `redis_db_keys_expiring` | gauge |  | Total number of expiring keys by DB |
| `redis_evicted_keys_total` | gauge |  | evicted_keys_total metric |
| `redis_expired_keys_total` | gauge |  | expired_keys_total metric |
| `redis_exporter_build_info` | gauge |  | redis exporter build_info |
| `redis_exporter_last_scrape_duration_seconds` | gauge |  | The last scrape duration |
| `redis_exporter_last_scrape_error` | gauge |  | The last scrape error status |
| `redis_exporter_scrapes_total` | gauge |  | Current total redis scrapes |
| `redis_instance_info` | gauge |  | Information about the Redis instance |
| `redis_instantaneous_input_kbps` | gauge |  | instantaneous_input_kbps metric |
| `redis_instantaneous_ops_per_sec` | gauge |  | instantaneous_ops_per_sec metric |
| `redis_instantaneous_output_kbps` | gauge |  | instantaneous_output_kbps metric |
| `redis_keyspace_hits_total` | gauge |  | keyspace_hits_total metric |
| `redis_keyspace_misses_total` | gauge |  | keyspace_misses_total metric |
| `redis_latest_fork_usec` | gauge |  | latest_fork_usec metric |
| `redis_loading_dump_file` | gauge |  | loading_dump_file metric |
| `redis_master_repl_offset` | gauge |  | master_repl_offset metric |
| `redis_memory_fragmentation_ratio` | gauge |  | memory_fragmentation_ratio metric |
| `redis_memory_max_bytes` | gauge |  | memory_max_bytes metric |
| `redis_memory_used_bytes` | gauge |  | memory_used_bytes metric |
| `redis_memory_used_lua_bytes` | gauge |  | memory_used_lua_bytes metric |
| `redis_memory_used_peak_bytes` | gauge |  | memory_used_peak_bytes metric |
| `redis_memory_used_rss_bytes` | gauge |  | memory_used_rss_bytes metric |
| `redis_net_input_bytes_total` | gauge |  | net_input_bytes_total metric |
| `redis_net_output_bytes_total` | gauge |  | net_output_bytes_total metric |
| `redis_process_id` | gauge |  | process_id metric |
| `redis_pubsub_channels` | gauge |  | pubsub_channels metric |
| `redis_pubsub_patterns` | gauge |  | pubsub_patterns metric |
| `redis_rdb_changes_since_last_save` | gauge |  | rdb_changes_since_last_save metric |
| `redis_rdb_current_bgsave_duration_sec` | gauge |  | rdb_current_bgsave_duration_sec metric |
| `redis_rdb_last_bgsave_duration_sec` | gauge |  | rdb_last_bgsave_duration_sec metric |
| `redis_rejected_connections_total` | gauge |  | rejected_connections_total metric |
| `redis_replication_backlog_bytes` | gauge |  | replication_backlog_bytes metric |
| `redis_slowlog_length` | gauge |  | Total slowlog |
| `redis_start_time_seconds` | gauge |  | Start time of the Redis instance since unix epoch in seconds |
| `redis_up` | gauge |  | up metric |
| `redis_uptime_in_seconds` | gauge |  | uptime_in_seconds metric |
| `redis_used_cpu_sys` | gauge |  | used_cpu_sys metric |
| `redis_used_cpu_sys_children` | gauge |  | used_cpu_sys_children metric |
| `redis_used_cpu_user` | gauge |  | used_cpu_user metric |
| `redis_used_cpu_user_children` | gauge |  | used_cpu_user_children metric |




