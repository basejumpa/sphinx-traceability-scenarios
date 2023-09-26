#!/bin/bash

sphinx-build -a -b text . build/a
sphinx-build -a -b text -D config_file=config_b.json . build/b
sphinx-build -a -b text -D config_file=config_c.json . build/c
