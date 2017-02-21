#!/bin/bash

ebook-convert "./recipes/${1}.recipe" .epub -vv --debug-pipeline debug
