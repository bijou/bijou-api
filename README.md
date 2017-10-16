# BIJOU-API
[![Maintainability](https://api.codeclimate.com/v1/badges/8e9cc1425ceb0d97ca2d/maintainability)](https://codeclimate.com/github/bijou/bijou-api/maintainability)
[![Requirements Status](https://requires.io/github/bijou/bijou-api/requirements.svg?branch=master)](https://requires.io/github/bijou/bijou-api/requirements/?branch=master)

This is the *core* of any bijou system, it provides a GraphQL based API to
access the content and status of the server.

> This software, as well as the developer(s) working on it, does not encourage
> or directly provide the means to "pirate" or otherwise acquire the content it
> organises through illegal means.

## Categories
Bijou makes very few assumptions about your media on its own and only provides
some basic "categories" to define what type of media it thinks it is managing.
The actual heavy lifting is done by the plugins that are outlined below.

## Plugins

### Indexers
Indexers are your sources of media content that provide metadata in a format
that downloaders understand.

### Downloaders
Downloaders accept metadata about a particular entry provided by an indexer
plugin. Downloaders will also provide reports about the entries they are
currently downloading.

## Requirements

## Source
> Python 3.6 is required - no earlier versions will work!

### Building
There is a simple Makefile that abstracts the longer calls directly to python
away in tasks.

## Distributions
No requirements other than a computer capable of running the application. The
Python runtime and all included runtime files are contained in these
distributions.

## Docker
