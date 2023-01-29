dtool_ibeis
===========

|Pypi| |Downloads| |Codecov| |GithubActions| 

Data tools for `IBEIS <https://github.com/Erotemic/ibeis>`_.

Currently in proof of concept mode (and wont be developed further).

Contains the SQLDatabaseController powering the IBEIS API

Contains a preliminary dependency cache


# Goals of this project

* Allow for small pieces code and algorithms to be easilly integrated into a
  large scale cache / pipeline structure. 

* Each computation function should be fairly self contained, stateless, and
  re-usable by other projects that do not wish to conform to the rules set by
  this structure.


Repos relevant to the ibeis project:

* https://github.com/Erotemic/plottool_ibeis

* https://github.com/Erotemic/guitool_ibeis

* https://github.com/Erotemic/dtool_ibeis

* https://github.com/Erotemic/vtool_ibeis

* https://github.com/Erotemic/vtool_ibeis_ext

* https://github.com/Erotemic/pyflann_ibeis

* https://github.com/Erotemic/pyhesaff

* https://github.com/Erotemic/utool

* https://github.com/Erotemic/ibeis


.. |CircleCI| image:: https://circleci.com/gh/Erotemic/dtool_ibeis.svg?style=svg
    :target: https://circleci.com/gh/Erotemic/dtool_ibeis
.. |Travis| image:: https://img.shields.io/travis/Erotemic/dtool_ibeis/main.svg?label=Travis%20CI
   :target: https://travis-ci.org/Erotemic/dtool_ibeis?branch=main
.. |Appveyor| image:: https://ci.appveyor.com/api/projects/status/github/Erotemic/dtool_ibeis?branch=main&svg=True
   :target: https://ci.appveyor.com/project/Erotemic/dtool_ibeis/branch/main
.. |Codecov| image:: https://codecov.io/github/Erotemic/dtool_ibeis/badge.svg?branch=main&service=github
   :target: https://codecov.io/github/Erotemic/dtool_ibeis?branch=main
.. |Pypi| image:: https://img.shields.io/pypi/v/dtool_ibeis.svg
   :target: https://pypi.python.org/pypi/dtool_ibeis
.. |Downloads| image:: https://img.shields.io/pypi/dm/dtool_ibeis.svg
   :target: https://pypistats.org/packages/dtool_ibeis
.. |ReadTheDocs| image:: https://readthedocs.org/projects/dtool_ibeis/badge/?version=latest
    :target: http://dtool_ibeis.readthedocs.io/en/latest/
.. |GithubActions| image:: https://github.com/Erotemic/dtool_ibeis/actions/workflows/tests.yml/badge.svg?branch=main
    :target: https://github.com/Erotemic/dtool_ibeis/actions?query=branch%3Amain
