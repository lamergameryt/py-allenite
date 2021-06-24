===========
Py-Allenite
===========

Py-Allenite is a full-fleged Python wrapper to develop applications integrating Allenite's API.

|License| |Followers|

.. |License| image:: https://img.shields.io/github/license/lamergameryt/py-allenite
.. |Followers| image:: https://img.shields.io/github/followers/lamergameryt?style=social

⏩ Quick Example
----------------

In this example, we will fetch a random meme using the API.

``main.py``

.. code-block:: python

    from allenite_api import AlleniteClient

    client = AlleniteClient()
    meme = client.get_random_meme()

    # The 0th index is the title and the 1st index is the image url.
    print(meme[0], ':', meme[1])


👩‍🏫 Installation
------------------

::

    pip install py-allenite

📈 Required Python Modules
--------------------------

The list of required python modules can be found in the ``requirements.txt`` file.

📜 Documentation
----------------

To view the documentation for this project, visit the `documentation page <https://pyallenite.readthedocs.io/en/latest/>`_.
