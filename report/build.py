#!/usr/bin/env python
"""Report build.py"""

import xnt
import xnt.build.tex

PROPERTIES = { "doc_name" : "report", }

@xnt.target
def default():
    """Build the report"""
    build()

@xnt.target
def build():
    """Build Report"""
    return xnt.build.tex.pdflatex(PROPERTIES["doc_name"] + ".tex",
                                  bibtex=True)

@xnt.target
def clean():
    """Remove Generated Files"""
    xnt.rm("*.toc",
           "*.aux",
           "*.bbl",
           "*.out",
           "*.log",
           "*.blg")
    if "clean_pdf" in PROPERTIES:
        xnt.rm("*pdf")
