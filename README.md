# BIJOU-API
This is the *core* of any bijou system, it provides a GraphQL based API to
access the content and status of the server.

<aside class="notice">
This software, as well as the developer(s) working on it, does not encourage or
directly provide the means to "pirate" or otherwise acquire the content it
organises through illegal means.
</aside>

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
<aside class="warning">
Python 3.6 is required - no earlier versions will work!
</aside>

## Distributions
No requirements other than a computer capable of running the application. The
Python runtime and all included runtime files are contained in these
distributions.

## Docker
