#!/usr/bin/env python3

#*****************************************************************************
#   Copyright 2004-2008 Steve Menard
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
#*****************************************************************************

import os
import time
from xml.dom import minidom

def output(el, prefix="") :
    if el.nodeType != el.ELEMENT_NODE :
        return

    # print("{0}<{1}".format(prefix, el.tagName), end='')

    atts = el.attributes
    for i in range(atts.length) :
        _ = atts.item(i)
        # a = atts.item(i)
        # print(' {0}="{1}"'.format(a.nodeName, a.nodeValue), end='')

    # print('>')

    nl = el.childNodes
    for i in range(nl.length) :
        output(nl.item(i), prefix + "  ")

    # print("{0}</{1}>".format(prefix, el.tagName))


# Compute the XML file path
xml_file = os.path.join(os.path.dirname(__file__), "sample", "big.xml")

t1 = time.time()
count = 30
for i in range(count):
    doc = minidom.parse(xml_file)

    el = doc.documentElement
    output(el)

t2 = time.time()
print(count, "iterations in", t2 - t1, "seconds")

