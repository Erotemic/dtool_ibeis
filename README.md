# dtool README FILE

Data tools. 

Currently in proof of concept mode. 

Contains the SQLDatabaseController powering the IBEIS API

Contains a preliminary dependency cache


# Goals of this project

* Allow for small pieces code and algorithms to be easilly integrated into a
  large scale cache / pipeline structure. 

* Each computation function should be fairly self contained, stateless, and
  re-usable by other projects that do not wish to conform to the rules set by
  this structure.
