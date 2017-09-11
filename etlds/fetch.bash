#!/bin/bash

URL="https://publicsuffix.org/list/public_suffix_list.dat"

curl -X GET "${URL}" -o "./build/list.txt"

