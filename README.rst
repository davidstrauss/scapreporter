=============
SCAP Reporter
=============


A utility for automated OpenSCAP reporting.


Description
===========

A utility for developer workstations that provides lightweight, automated OpenSCAP scanning and report aggregation.

Building for RPM Distribution
=============================

From the root of the project::

 sudo dnf install python3-wheel
 python3 setup.py bdist_rpm

The RPMs will appear in ``./dist/``.

Similar Projects
================

* OpenSCAP Daemon: a daemon for recurring scans, local and remote

  * https://github.com/OpenSCAP/openscap-daemon

* Foreman OpenSCAP: a plugin for The Foreman for managing OpenSCAP policy, scans, and report aggregation

  * https://github.com/theforeman/foreman_openscap

* SCAPtimony: a *deprecated* server application for report aggegation and storage

  * https://github.com/OpenSCAP/scaptimony

Note
====

This project has been set up using PyScaffold 3.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
