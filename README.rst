dtool_ibeis
===========

|ReadTheDocs| |Pypi| |Downloads| |Codecov| |CircleCI| |Travis| |Appveyor| 

Data tools for ibeis.

Currently in proof of concept mode. 

Contains the SQLDatabaseController powering the IBEIS API

Contains a preliminary dependency cache


# Goals of this project

* Allow for small pieces code and algorithms to be easilly integrated into a
  large scale cache / pipeline structure. 

* Each computation function should be fairly self contained, stateless, and
  re-usable by other projects that do not wish to conform to the rules set by
  this structure.


.. |CircleCI| image:: https://circleci.com/gh/Erotemic/dtool.svg?style=svg
    :target: https://circleci.com/gh/Erotemic/dtool
.. |Travis| image:: https://img.shields.io/travis/Erotemic/dtool/master.svg?label=Travis%20CI
   :target: https://travis-ci.org/Erotemic/dtool?branch=master
.. |Appveyor| image:: https://ci.appveyor.com/api/projects/status/github/Erotemic/dtool?branch=master&svg=True
   :target: https://ci.appveyor.com/project/Erotemic/dtool/branch/master
.. |Codecov| image:: https://codecov.io/github/Erotemic/dtool/badge.svg?branch=master&service=github
   :target: https://codecov.io/github/Erotemic/dtool?branch=master
.. |Pypi| image:: https://img.shields.io/pypi/v/dtool_ibeis.svg
   :target: https://pypi.python.org/pypi/dtool_ibeis
.. |Downloads| image:: https://img.shields.io/pypi/dm/dtool_ibeis.svg
   :target: https://pypistats.org/packages/dtool_ibeis
.. |ReadTheDocs| image:: https://readthedocs.org/projects/dtool_ibeis/badge/?version=latest
    :target: http://dtool_ibeis.readthedocs.io/en/latest/
