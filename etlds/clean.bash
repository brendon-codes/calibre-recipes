#!/bin/bash

sed -r -e '/^\s*$/d' -e '/^\/\//d' < build/list.txt > build/clean.txt

