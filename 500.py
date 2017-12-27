# -*- coding: utf-8 -*-
__author__ = 'todoroki'

import re

punt = re.compile(r"(?P<punt>[\.:;!\?]) (?P<head>[A-Z])")

if __name__ == "__main__":
    f = open('nlp.txt', 'r')
    for line in f:
        print(punt.sub(r"\g<punt>\n\g<head>", line))
    f.close()
