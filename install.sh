#!/bin/bash

# reinstall czo-tools 

python3 setup.py sdist
pip3 uninstall czo-tools
pip3 install dist/czo*
