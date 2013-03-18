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
                                  bibtex=True,
                                  makeglossary=True)

@xnt.target
def clean():
    """Remove Generated Files"""
    xnt.build.tex.clean(path="./")

@xnt.target
def clean_pdf():
    """Remove _all_ generated files (including PDF output)"""
    xnt.build.tex.clean(path="./", remove_pdf=True)
