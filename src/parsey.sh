#!/bin/sh
old_dir=$(pwd)
#cd ../../../scrapy/scrapy-parsey-playground-2.7/lib/parsey-mcparse-face/models/syntaxnet/
cd /home/egaebel/Programs/scrapy/scrapy-parsey-playground-2.7/lib/parsey-mcparse-face/models/syntaxnet/
echo Input 1: $1
echo $1 | ./syntaxnet/demo.sh
cd $old_dir

