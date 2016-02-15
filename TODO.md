# TODO:

* Allow for algorithm tables to store one-vs-one results efficiently.
    - allow for daids to be independent 
    - allow for qaids to be non-independent
    - allow for ordering to matter / not matter
    - Need to update:
        - depc.new_algo_request
        - AlgoRequest.execute
    - Careful, the descendant rowids of annot for vs one are [(1, 1), (2, 2), ...]
      this is because there is no way to say what daids you want to compare against

* Allow for custom external write functions to be specified.

* Move all version flags to config objects.
    - involves allowing differnt configs to have the same value
    - requires config namespaces

* Allow annotation of implicit edges.


* Need to remove algorithm request structure completely from the dependency
  cache. Algorithms should be specified strictuly with configs and the 
  configs should know how to address the storage of long configuration 
  options like the daid list for vsmany.


* root\_uuids should be specified as the base\_root\_uuid plus a hash of the
  attributes that matter for the requested computation.
