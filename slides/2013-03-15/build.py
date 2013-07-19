#!/usr/bin/env python
"""Slides build.py"""

import xnt
import xnt.build.tex

PROPERTIES = { "doc_name": "2013-03-15.tex", }

@xnt.target
def build():
    """Build Slides"""
    return xnt.build.tex.pdflatex(PROPERTIES["doc_name"])

@xnt.target
def default():
    """Build Slides"""
    build()

@xnt.target
def clean():
    """Remove Generated Files"""
    xnt.build.tex.clean(path="./")

@xnt.target
def clean_pdf():
    """Remove _all_ generated files (including PDF output)"""
    xnt.build.tex.clean(path="./", remove_pdf=True)
