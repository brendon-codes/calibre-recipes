#!/usr/bin/env python3

import sys
import json
from pprint import pprint


def clean(lin):
    a = lin.strip()
    parts = a.split(".")
    red = filter(lambda r: r != "*", parts)
    b = ".".join(red)
    return b


def main():
    items = list(map(clean, sys.stdin))
    tree = json.dumps(items, indent=None, sort_keys=True)
    froze = "".join(["DOMAINS = frozenset(\n", tree, "\n)"])
    print(froze)
    return True


if __name__ == "__main__":
    main()
    sys.exit(0)
