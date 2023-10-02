#!/bin/bash
i=0
n=2

while [ $i -lt 50 ]
do
	primo=1
	for (( j=2; j<=$n/2; j++))
	do
		if [ $((n%j)) -eq 0 ]
		then
			primo=0
			break
		fi
	done
	if [ $primo -eq 1 ]
	then
		i=$((i+1))
		echo $i $n
	fi
	n=$((n+1))
done
