This is just a minimally reproducible example of using pytest-qt to test
a simple widget. These are the two ways I've tried running the tests.

pytest directly
---------------

.. code:: bash

    $ python -m venv .venv
    $ source .venv/bin/activate.fish
    (.venv)$ pip install pyqt5 pytest pytest-qt
    (.venv)$ python setup.py develop
    (.venv)$ python -m pytest

This results in a successful test run.

tox
---

.. code:: bash

    $ tox

This results in an ``InvocationError`` with no further explanation.
