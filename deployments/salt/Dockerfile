#
# Salt Stack Salt Dev Container
#

FROM ubuntu:16.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get upgrade -y -o DPkg::Options::=--force-confold
RUN apt-get install -y software-properties-common ca-certificates wget curl apt-transport-https python-pip vim

RUN curl https://repo.saltstack.com/apt/ubuntu/16.04/amd64/latest/SALTSTACK-GPG-KEY.pub | apt-key add -
RUN echo 'deb http://repo.saltstack.com/apt/ubuntu/16.04/amd64/latest xenial main' > /etc/apt/sources.list.d/saltstack.list && \
    apt-get update && \
    apt-get install -y salt-minion

RUN pip install salt-lint==0.2.0

RUN sed -i "s|#file_client:.*|file_client: local|" /etc/salt/minion

COPY ./Makefile /Makefile
COPY ./signalfx-agent /srv/salt/signalfx-agent
COPY ./pillar.example /srv/pillar/signalfx-agent.sls
COPY ./entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh

WORKDIR /srv/salt/signalfx-agent

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
