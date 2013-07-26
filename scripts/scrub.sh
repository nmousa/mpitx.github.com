#!/bin/sh

for f in $@
do
    awk '/user/ { printf "(%s %s %s %s %s)\n", FILENAME, $1, $2, $3, $4}' ${f}|
    sed -n -e 's/user//' \
           -e 's/system//' \
           -e 's/elapsed//' \
           -e 's/%CPU//p'
done > temp

awk '/[0-9]{1,2}:[0-9]{2}:[0-9]{2}/ {fi = index($4, ":"); si = fi + 3; h = 3600 * substr($4, 1, fi); m = 60 * substr($4, fi + 1, 2); s = substr($4, si + 1, 2); $4 = h + m + s; print }' < temp

awk '/[0-9]{1,2}:[0-9]{2}\.[0-9]{2}/ {fi = index($4, ":"); m = 60 * substr($4, 1, fi); s = substr($4, fi+1, length($f) - fi); $4 = m + s; print }' < temp

rm temp
