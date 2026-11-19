# Architecture
Approved boundary: the API submits commands; only the worker owns report persistence.
This isolates persistence retries from request handling. A legacy API direct-write path still needs migration; it is not an approved exception.
