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
def clean():
    """Clean/ remove generated files"""
    return xnt.build.tex.clean()

@xnt.target
def clean_pdf():
    """Clean/ remove generated files _including_ PDF's"""
    return xnt.build.tex.clean(remove_pdf=True)

@xnt.target
def default():
    """Build Slides"""
    build()
