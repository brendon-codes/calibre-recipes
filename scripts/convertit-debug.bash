#!/bin/bash

ebook-convert "./recipes/${1}.recipe" .epub --debug-pipeline debug --test
