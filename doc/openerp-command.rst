.. _openerp-command:

OpenERP Command
===============

OpenERP Command provides a set of command-line tools around the OpenERP
framework: openobject-server_. All the tools are sub-commands of a single
``oe`` executable. This project is at its beginning; it is not yet ready for
public consumption.

`Disclaimer`: The OpenERP Command is still tagged as experimental (no official
support is planned currently).

.. _openobject-server: https://launchpad.net/openobject-server

Obtaining OpenERP Command
-------------------------

OpenERP Command is available through Launchpad::

  > bzr branch lp:~openerp/openerp-command/trunk openerp-command

Installing OpenERP Command
--------------------------

The provided ``setup.py`` works but doesn't list any dependency. In particular
the OpenERP server's ``openerp`` module must be importable.

You can of course run `oe` without installing it by setting a few environment
variables, e.g. in Bash::

  > export PYTHONPATH=/path/to/openerp-server/:/path/to/openerp-command/
  > export PATH=/path/to/openerp-server/:/path/to/openerp-command/:$PATH

Once done,

::

  > oe --help

should work.

Using OpenERP Command
---------------------

In contrast to the regular ``openerp-server`` script, ``oe`` defines a few
sub-commands, each with its own set of flags and options. You can get some
information for any of them with

::

  > oe <sub-command> --help

For instance::

  > oe run-tests --help

Some ``oe`` options can be provided via environment variables. For instance::

  > export OPENERP_DATABASE=trunk
  > export OPENERP_HOST=127.0.0.1
  > export OPENERP_PORT=8069

Depending on your needs, you can group all of the above in one single script;
for instance here is a, say, ``test-trunk-view-validation.sh`` file::

  COMMAND_REPO=/home/thu/repos/command/trunk/
  SERVER_REPO=/home/thu/repos/server/trunk

  export PYTHONPATH=$SERVER_REPO:$COMMAND_REPO
  export PATH=$SERVER_REPO:$COMMAND_REPO:$PATH
  export OPENERP_DATABASE=trunk
  export OPENERP_HOST=127.0.0.1
  export OPENERP_PORT=8069

  # The -d ignored is actually needed by `oe` even though `test_view_validation`
  # itself does not need it.
  oe run-tests -d ignored -m openerp.test_view_validation

Adding new sub-commands
-----------------------

``oe`` uses the ``argparse`` library to implements sub-commands. Each
sub-command lives in its own ``openerpcommand/<sub-command>.py`` file.

Bash completion
---------------

A preliminary ``oe-bash-completion`` file is provided. After sourcing it,

::

  > . oe-bash-completion

completion (using the TAB character) in Bash should be working.
