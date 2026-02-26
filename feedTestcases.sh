#!/bin/bash

while IFS= read -r line || [[ -n "$line" ]]
do
  echo "Processing: $line"
  echo "$line" | python3 "cipherToPlaintext.py" >> "output.txt"
done < "testcases.txt"