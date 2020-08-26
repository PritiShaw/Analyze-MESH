#!/bin/bash
python3 main.py
cd $1/examples
javac -cp ../classes:../lib/skrAPI.jar:../lib/commons-logging-1.1.1.jar:../lib/httpclient-cache-4.1.1.jar:../lib/httpcore-nio-4.1.jar:../lib/httpclient-4.1.1.jar:../lib/httpcore-4.1.jar:../lib/httpmime-4.1.1.jar -d ../classes GenericBatch.java
cd ..
cp $2/abstract.txt $1
./run.sh GenericBatchNew --email $3 abstract.txt >meshterms.txt
rm abstract.txt
cp $1/meshterms.txt $2
