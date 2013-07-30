#!/usr/bin/env python
"""Slides build.py"""

import os
import xnt
import xnt.build.tex

slides = ['2013-02-15',
          '2013-03-15',
          '2013-03-20',
          '2013-05-03',
          '2013-06-29',
          '2013-07-20',
          '2013-08-02',]

@xnt.target
def build():
    """Build Slides"""
    for slide in slides:
        xnt.tasks.xntcall(os.path.join(slide, 'build.py'),
                          targets=['build',])

@xnt.target
def default():
    """Build Slides"""
    build()
    clean()

@xnt.target
def clean():
    """Remove Generated Files"""
    for slide in slides:
        xnt.tasks.xntcall(os.path.join(slide, 'build.py'),
                          targets=['clean',])

@xnt.target
def clean_pdf():
    """Remove _all_ generated files (including PDF output)"""
    for slide in slides:
        xnt.tasks.xntcall(os.path.join(slide, 'build.py'),
                          targets=['clean_pdf',])
