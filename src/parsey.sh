#!/bin/sh
old_dir=$(pwd)
#cd ../../../scrapy/scrapy-parsey-playground-2.7/lib/parsey-mcparse-face/models/syntaxnet/
cd ../../../parsey-mcparseface/parsey-mcparseface/src/models/syntaxnet/
echo Input 1: $1
echo $1 | ./syntaxnet/demo.sh
cd $old_dir

