#!/bin/bash
clear
mkdir raiz
cd raiz
mkdir -p a b c d e
cd a
mkdir -p f/j/q/w/y
cd f/j
mkdir p
cd ..
mkdir k
cd k
mkdir -p r x z
cd ../../..
cd b
mkdir g
cd ../c
mkdir -p h/r
cd h
mkdir -p m/s
cd m
mkdir t
cd ../../../e
mkdir -p v/ac/ad
cd v
mkdir ab
cd ../..
clear

cd c/h
touch prueba{1..2}.txt
touch aswdf.xls gardsa.csv agddgs.json dlfa.c
cp *.* ./../../e/v/ab
cp *.txt ./m/t
cp ???d*.* ./m/s

cd ./m/t
chmod u=x,g=r,o=rwx prueba1.txt
chmod 201 prueba2.txt

clear

ls -l
