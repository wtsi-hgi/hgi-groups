# Human Genetics Programme Group Registry

[![Build Status](https://travis-ci.org/wtsi-hgi/hgi-registry.svg?branch=master)](https://travis-ci.org/wtsi-hgi/hgi-registry)
[![Test Coverage](https://codecov.io/gh/wtsi-hgi/hgi-registry/branch/master/graph/badge.svg)](https://codecov.io/gh/wtsi-hgi/hgi-registry)

A simple web interface that provides an overview of project and team
groups within the Human Genetics Programme.

# Installation

Just pull and run the Docker container:

    docker run -dp 80:5000 \
               -e LDAP_URI=ldap://my.ldap.host:389 \
               -e LDAP_BASE=dc=example,dc=com \
               -e EXPIRY=86400 \
               mercury/hgi-registry

Inside the container, the server runs on port 5000; you may map that to
whatever host port you like. Additionally, the service takes its cues
from three environment variables:

* `LDAP_URI` The URI of your LDAP server, consisting of the schema, host
  and port.

* `LDAP_BASE` The DN of the entry from which you'd like all searches to
  be based.

* `EXPIRY` The duration (in seconds) before in-memory LDAP entities are
  refreshed from the LDAP server. This value is optional and defaults to
  3600 (i.e., one hour).

# RESTful API

The data returned from the API is rendered from an internal cache, which
is first populated when a requested entry does not exist. Therefore, the
data returned may be stale and not reflect the true state at any given
time. However, cache entries will be refreshed periodically to minimise
this effect.

## Hypermedia

JSON values that represent links within the graph will be a JSON object
with:

* An `href` entity, containing the URI of the linked resource;
* A `rel` or `rev` (or both) entity, describing the link and reverse
  link relation, respectively;
* An optional `value` entity, that contains further semantic information
  about the link target, without the need for dereferencing.

## Endpoints

### `/groups`

Method | Content Type       | Behaviour
:----- | :----------------- | :-----------------------------------------
`GET`  | `application/json` | Return the identities of every project and team group in the Human Genetics Programme.

#### Schema

Array of group [hypermedia entities](#hypermedia).

### `/groups/<GROUP>`

Method | Content Type       | Behaviour
:----- | :----------------- | :-----------------------------------------
`GET`  | `application/json` | Return the details of the specific group given by `<GROUP>`.

#### Schema

* `id` [Hypermedia entity](#hypermedia) of themself;
* `active` Predicate of whether this is an active group;
* `description` Group description, `null` for unknown;
* `prelims` Array of prelim IDs;
* `pi` [Hypermedia entity](#hypermedia) for the group's PI;
* `owners` Array of [hypermedia entities](#hypermedia) of the group's
  owners;
* `members` Array of [hypermedia entities](#hypermedia) of the group's
  members;
* `last_updated` The timestamp of the last update for this record (in
  ISO8601 format).

### `/people`

Method | Content Type       | Behaviour
:----- | :----------------- | :-----------------------------------------
`GET`  | `application/json` | Return the identities of every user account.

#### Schema

Array of person [hypermedia entites](#hypermedia).

### `/people/<USER_ID>`

Method | Content Type       | Behaviour
:----- | :----------------- | :-----------------------------------------
`GET`  | `application/json` | Return the details of the specific user given by `<USER_ID>`.

#### Schema

* `id` [Hypermedia entity](#hypermedia) of themself;
* `name` Person's full name;
* `mail` Person's e-mail address;
* `title` Person's job title, `null` for unknown;
* `human` Predicate of whether this is a real (human) person;
* `active` Predicate of whether this is an active account;
* `photo` [Hypermedia entity](#hypermedia) of person's photo, if they
  have one;
* `involvement` Array of group [hypermedia entites](#hypermedia) for the
  groups in which the person is involved and their capacity therein;
* `last_updated` The timestamp of the last update for this record (in
  ISO8601 format).

### `/people/<USER_ID>/photo`

Method | Content Type       | Behaviour
:----- | :----------------- | :-----------------------------------------
`GET`  | `image/jpeg`       | Return the photo of the specific user given by `<USER_ID>` if it exists. If said user has no photo, then a 404 Not Found error will be returned.
