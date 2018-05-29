# Human Genetics Programme Groups

[![Build Status](https://travis-ci.org/wtsi-hgi/hgi-groups.svg?branch=master)](https://travis-ci.org/wtsi-hgi/hgi-groups)
[![Test Coverage](https://codecov.io/gh/wtsi-hgi/hgi-groups/branch/master/graph/badge.svg)](https://codecov.io/gh/wtsi-hgi/hgi-groups)

A simple web interface that provides an overview of project groups
within the Human Genetics Programme.

# Installation

Pull and run the Docker container:

    docker pull mercury/hgi-groups
    docker run -dp 80:5000 \
               -e LDAP_URI=ldap://my.ldap.host:389 \
               -e LDAP_BASE=dc=example,dc=com \
               mercury/hgi-groups

Inside the container, the server runs on port 5000; you may map that to
whatever host port you like. Additionally, the service takes its cue
from two environment variables:

* `LDAP_URI` The URI of your LDAP server, consisting of the schema, host
  and port.

* `LDAP_BASE` The DN of the entry from which you'd like all searches to
  be based.
