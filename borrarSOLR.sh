#!/bin/sh
curl http://localhost:8983/solr/update -H "Content-type: text/xml" --data-binary '<delete><query>*:*</query></delete>'
curl http://localhost:8983/solr/update -H "Content-type: text/xml" --data-binary '<commit />'
 curl http://localhost:8983/solr/update -H "Content-type: text/xml" --data-binary '<optimize />'


