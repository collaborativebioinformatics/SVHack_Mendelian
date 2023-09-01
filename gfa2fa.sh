#!/bin/bash

for f in *.gfa; do
    filename="${f%.gfa}"
    awk '/^S/{print ">"$2"_"FILENAME"\n"$3}' "$f" | fold > "$filename.fa"
done

