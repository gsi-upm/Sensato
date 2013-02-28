#!/bin/sh
cd ~/cnet5-solr/
java -jar start.jar&
cd /var/www/conceptnet5-master/
python conceptnet5/api.py http://localhost:5000
