# TODO:

* Allow for algorithm tables to store one-vs-one results efficiently.
    - allow for daids to be independent 
    - allow for qaids to be non-independent
    - allow for ordering to matter / not matter
    - Need to update:
        - depc.new_algo_request
        - AlgoRequest.execute

* Allow for custom external write functions to be specified.

* Move all version flags to config objects.
    - involves allowing differnt configs to have the same value
    - requires config namespaces

* Allow annotation of implicit edges.
