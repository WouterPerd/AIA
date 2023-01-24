#!/bin/bash

java validate sdg.ttl urls > URL.txt

file="URL.txt" #file name

IFS=' ' #setting space as delimiter

while read -r line
do
	read -a ARRAY <<< "$line" #reads line as an array as tokens separated by IFS
	if [ -f ${ARRAY[0]}.ttl ] #checks for duplicates
	then
		echo "DUPLICATE"
	else
		curl -L -H "Accept: text/turtle" ${ARRAY[1]} >> ${ARRAY[0]}.ttl #Creates the ontology files
		java validate ${ARRAY[0]}.ttl output > ${ARRAY[0]}.txt
	fi
	unset ARRAY
done <$file
