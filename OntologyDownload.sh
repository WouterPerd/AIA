#!/bin/bash

file="URL.txt" #file name

IFS=' ' #setting space as delimiter

while read -r line
do
	read -a ARRAY <<< "$line" #reads line as an array as tokens separated by IFS
	curl -L -H \"Accept: text/turtle\" ${ARRAY[1]} >> ${ARRAY[0]}.ttl #Creates the ontology files
	unset ARRAY
done <$file
