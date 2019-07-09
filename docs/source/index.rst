=========
RegonAPI:
=========

Client for Polish GUS Regon Database (BIR)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Highlights:
  * Supports BIR v1 and BIR v1.1
  * Searching for information about business entities by: KRS, REGON and NIP
  * Fetching business entities reports
  * API messages available in English and Polish language


Usage example:

.. code-block:: python

  from RegonAPI import RegonAPI
  from pprint import pprint

  API_KEY = "abcde12345abcde12345"
  CD_PROJEKT_REGON9 = "492707333"

  api = RegonAPI(bir_version="bir1") # BIR version 1
  api.authenticate(key=API_KEY)
  res = api.dataDownloadFullReport(
    CD_PROJEKT_REGON9,
    "PublDaneRaportPrawna"
  )
  pprint(res)


Installation
^^^^^^^^^^^^


If you have installed pip then run::

    pip install RegonAPI


User guide
^^^^^^^^^^

.. toctree::
   :maxdepth: 2

   using_regonapi
   regonapi_object
   bir_versions
   obtain_key
   settings
   license
   modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
