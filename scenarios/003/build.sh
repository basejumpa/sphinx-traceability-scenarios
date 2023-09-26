#!/bin/bash

set -v

sphinx-build -b text                . build/a
sphinx-build -b text -D feature_a=0 . build/b
sphinx-build -b text -D feature_a=1 . build/c

diff -s -y build/a/index.txt build/b/index.txt || true
diff -s -y build/b/index.txt build/c/index.txt || true
diff -s -y build/c/index.txt build/a/index.txt || true
