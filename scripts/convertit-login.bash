#!/bin/bash

ebook-convert "./recipes/${1}.recipe" .epub --username="${2}" --password="${3}" --debug-pipeline debug
