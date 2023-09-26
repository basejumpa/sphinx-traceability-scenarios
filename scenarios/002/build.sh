#!/bin/bash

set -v

sphinx-build -b text -c a              . build/a1
sphinx-build -b text -c a -t feature_a . build/a2
sphinx-build -b text -c b              . build/b1
sphinx-build -b text -c b -t feature_a . build/b2

diff  -s -y build/a1/index.txt build/b1/index.txt || true
diff  -s -y build/a2/index.txt build/b2/index.txt || true
