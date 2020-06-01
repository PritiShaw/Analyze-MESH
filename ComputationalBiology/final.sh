#!/bin/bash
python3 main.py
cd /home/priti/Documents/Development/GSoC20/SKR_Web_API_V2_3/examples
javac -cp ../classes:../lib/skrAPI.jar:../lib/commons-logging-1.1.1.jar:../lib/httpclient-cache-4.1.1.jar:../lib/httpcore-nio-4.1.jar:../lib/httpclient-4.1.1.jar:../lib/httpcore-4.1.jar:../lib/httpmime-4.1.1.jar -d ../classes GenericBatch.java
cd ..
cp /home/priti/Documents/Development/GSoC20/ISSUE1ExtractingMeSHTermsforArticles/ComputationalBiology/abstract.txt /home/priti/Documents/Development/GSoC20/SKR_Web_API_V2_3
./run.sh GenericBatchNew --email pritishaw0103@gmail.com abstract.txt >meshterms.txt
rm abstract.txt
cp /home/priti/Documents/Development/GSoC20/SKR_Web_API_V2_3/meshterms.txt /home/priti/Documents/Development/GSoC20/ISSUE1ExtractingMeSHTermsforArticles/ComputationalBiology
