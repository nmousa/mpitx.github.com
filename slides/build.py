#!/usr/bin/env python
"""Slides build.py"""

import xnt
import xnt.build.tex

PROPERTIES = { "doc_name": "2013-02-15.tex", }

@xnt.target
def build():
    """Build Slides"""
    return xnt.build.tex.pdflatex(PROPERTIES["doc_name"])

@xnt.target
def clean():
    """Clean up generated files"""
    xnt.rm("*.toc",
           "*.aux",
           "*.log",
           "*.out")
    if "clean_pdf" in PROPERTIES:
        xnt.rm("*.pdf")

@xnt.target
def default():
    """Build Slides"""
    build()
