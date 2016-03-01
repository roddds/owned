Owned - Um Novo Jogador
==============================

This is a web-based implementation of the choose-your-own-adventure book `Owned - Um Novo Jogador
<https://www.7letras.com.br/owned-um-novo-jogador.html>`_ by Brazilian author `Simone Campos
<http://simonecampos.net>`_. This code will eventually replace the current, outdated website,
located currently at `novojogador.com.br <http://novojogador.com.br>`_.

LICENSE: BSD

Initial Setup
-------------

The steps below will get you up and running with a local development environment. For the instructions on how to get everything setup using Docker, go `here <http://cookiecutter-django.readthedocs.org/en/latest/developing-locally-docker.html>`_
. We assume you have the following installed:

* pip
* virtualenv
* PostgreSQL

First make sure to create and activate a virtualenv_, then open a terminal at the project root and install the os dependencies::

    $ sudo ./install_os_dependencies.sh install

Then install the requirements for your local development::

    $ pip install -r requirements/local.txt

.. _virtualenv: http://docs.python-guide.org/en/latest/dev/virtualenvs/

Then, create a PostgreSQL database with the following command, where `[repo_name]` is what value you entered for your project's `repo_name`::

    $ createdb [repo_name]

This project uses the excellent `django-environ`_ package with its ``DATABASE_URL`` environment variable to simplify database configuration in your Django settings. Now all you have to do is compose a definition for ``DATABASE_URL``:

.. parsed-literal::

    $ export DATABASE_URL="postgres://*<pg_user_name>*:*<pg_user_password>*\ @127.0.0.1:\ *<pg_port>*/*<pg_database_name>*"

.. _django-environ: http://django-environ.readthedocs.org

You can now run the usual Django ``migrate`` and ``runserver`` commands::

    $ python manage.py migrate
    $ python manage.py runserver

Settings
------------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.org/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Setting Up Your Data
^^^^^^^^^^^^^^^^^^^^

To load the data from the book (Paragraphs, Items, Events), use this command::

    $ python manage.py loaddata book

This should load the fixtures on the ``/owned/book/fixtures/`` directory.

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ py.test

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Live reloading and Sass CSS compilation**

If you'd like to take advantage of live reloading and Sass / Compass CSS compilation you can do so with the included Grunt task.

Make sure that nodejs_ is installed. Then in the project root run::

    $ npm install

.. _nodejs: http://nodejs.org/download/

Now you just need::

    $ grunt serve

The base app will now run as it would with the usual ``manage.py runserver`` but with live reloading and Sass compilation enabled.

To get live reloading to work you'll probably need to install an `appropriate browser extension`_

.. _appropriate browser extension: http://feedback.livereload.com/knowledgebase/articles/86242-how-do-i-install-and-use-the-browser-extensions-

Running end to end integration tests
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

N.B. The integration tests will not run on Windows.

To install the test runner::

  $ pip install hitch

To run the tests, enter the owned/tests directory and run the following commands::

  $ hitch init

Then run the stub test::

  $ hitch test stub.test

This will download and compile python, postgres and redis and install all python requirements so the first time it runs it may take a while.

Subsequent test runs will be much quicker.

The testing framework runs Django, Celery (if enabled), Postgres, HitchSMTP (a mock SMTP server), Firefox/Selenium and Redis.


Deployment
----------

We providing tools and instructions for deploying using Docker and Heroku.

Heroku
^^^^^^

.. image:: https://www.herokucdn.com/deploy/button.png
    :target: https://heroku.com/deploy

See detailed `cookiecutter-django Heroku documentation`_.

.. _`cookiecutter-django Heroku documentation`: http://cookiecutter-django.readthedocs.org/en/latest/deployment-on-heroku.html

Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.org/en/latest/deployment-with-docker.html