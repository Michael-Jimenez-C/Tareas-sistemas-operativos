#!/bin/bash

function primo {
	if [ $(($2)) -eq $(($1)) ]
	then
		echo "Es primo"
	else
		if [ $(($1 % $2)) -eq 0 ]
		then
			echo "No es primo"
		else
			primo $1 $(($2+1))
		fi
	fi


}

read a
primo a 2
