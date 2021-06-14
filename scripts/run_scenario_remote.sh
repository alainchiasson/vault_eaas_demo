#!/usr/bin/env bash

export VAULT_TOKEN=root  # Special case for demo only ( to be changed)

echo "generating datafiles ..."

date > f01.txt
sleep 1
date > f02.txt
sleep 1
date > f03.txt

echo "ecrypting files ... "
for x in f??.txt; do encrypt.sh $x > ${x%%.txt}.enc; done

echo " preparing second set of data files ...."

sleep 1
date > r01.txt
sleep 1
date > r02.txt
sleep 1
date > r03.txt

echo "rotating encryption key"
rotate_key.sh 

echo "encrypt new set of data"
for x in r??.txt; do encrypt.sh $x > ${x%%.txt}.enc; done

echo "display currnt encrypted data and decrypted -> Notice key versions..."
for x in *.enc; do echo "$(cat $x) -> $(decrypt.sh $x)"; done

echo "\n Return to continue..."
read junk

echo "Rewrap secrets with new key... "
for x in *.enc; do rewrap_secret.sh $x > ${x%%.enc}.en2 ; done

echo "redisplay encrypted data and decrypted -> Notice key versions..."
for x in *.en2; do echo "$(cat $x) -> $(decrypt.sh $x)"; done
