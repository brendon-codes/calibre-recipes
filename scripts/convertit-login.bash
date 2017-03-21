#!/bin/bash

ebook-convert "./recipes/${1}.recipe" .epub -vv --username="${2}" --password="${3}" --debug-pipeline debug
