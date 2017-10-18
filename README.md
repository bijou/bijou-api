# BIJOU-SERVER
[![Build Status](https://travis-ci.org/bijou/bijou-server.svg?branch=master)](https://travis-ci.org/bijou/bijou-server)
[![Maintainability](https://api.codeclimate.com/v1/badges/f67d1d9948216b3b25aa/maintainability)](https://codeclimate.com/github/bijou/bijou-server/maintainability)
[![Requirements Status](https://requires.io/github/bijou/bijou-server/requirements.svg?branch=master)](https://requires.io/github/bijou/bijou-server/requirements/?branch=master)

This is the *core* of any bijou system, it provides a GraphQL based API to
access the content and status of the server.

> This software, as well as the developer(s) working on it, does not encourage
> or directly provide the means to "pirate" or otherwise acquire the content it
> organises through illegal means.

## Types
Bijou makes very few assumptions about your media on its own and only provides
some basic "types" to describe the media objects that it manages.
The actual heavy lifting is done by the plugins that are outlined below.

### Movie
For your cinematic experiences, the "movie" type is used to define a media
object that has a **title** and a **year** as the bare minimum amount of
metadata.

### Television
The silver screen is organised first with a _show_ which requires, at a
minimum, a **title** and a **year**.

The invidiual episodes belonging to a _show_ require either a **season number**
or to be marked as _special_ along with the **episode number** and an optional
**title**

### Anime

### Standup

## Plugins

### Layouts
These plugins describe the way that your files are laid out and organised.
The ones supplied by bijou are recommended however any configuration is
possible - the bijou layouts mimic the filesystem found in other similar
applications such as Radarr and Sonarr.

### Indexers
Indexers are your sources of media content that provide metadata in a format
that downloaders understand.

### Downloaders
Downloaders accept metadata about a particular entry provided by an indexer
plugin. Downloaders will also provide reports about the entries they are
currently downloading.

### Informants
Informants are used to gather metadata about the "types" specified above.

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
