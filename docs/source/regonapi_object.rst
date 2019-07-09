The RegonAPI Object
===================

The :class:`RegonAPI` is the main interface object between client and REGON SOAP server.
It provides a :class:`searchData` and :class:`dataDownloadFullReport` methods allowing
searching for business entities and fetching reports.

Configuring the client
^^^^^^^^^^^^^^^^^^^^^^
To configure :class:`RegonAPI` interface, attribute ``bir_version`` needs to be set to
desired BIR version.
You can initialize the object using the following code:

.. code-block:: python

  from RegonAPI import RegonAPI

  # bir1 bir1.1 ...
  api = RegonAPI(bir_version="bir1")

To see all available BIR versions click here :doc:`bir_versions`


Authentication
^^^^^^^^^^^^^^
To authenticate client with your API Key use :class:`authenticate` method.

.. code-block:: python

  # This is an official key for testing
  API_KEY = "abcde12345abcde12345"
  api = RegonAPI(bir_version="bir1")
  api.authenticate(key=API_KEY)

Want to get key for production? Check out :doc:`obtain_key`
