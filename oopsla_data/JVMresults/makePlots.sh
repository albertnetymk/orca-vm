#!/bin/bash

cat ring.c4 >> tmp
cat ring.cms >> tmp
cat ring.g1gc >> tmp
cat ring.parallel >> tmp
cat tmp | python jvm_scalability.py ring
rm tmp

cat trees.c4 >> tmp
cat trees.cms >> tmp
cat trees.g1gc >> tmp
cat trees.parallel >> tmp
cat tmp | python jvm_scalability.py trees
rm tmp

cat trees2.c4 >> tmp
cat trees2.cms >> tmp
cat trees2.g1gc >> tmp
cat trees2.parallel >> tmp
cat tmp
cat tmp | python jvm_scalability.py trees2
rm tmp
