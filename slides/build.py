#!/usr/bin/env python

import xnt
import xnt.tasks

@xnt.target
def init():
    xnt.tasks.mkdir("build")

@xnt.target
def build():
    init()
    r1 = xnt.tasks.call(["pdflatex",
                         "-output-directory",
                         "build",
                         "-draftmode",
                         "2013-02-15.tex"])
    r2 = xnt.tasks.call(["pdflatex",
                         "-output-directory",
                         "build",
                         "2013-02-15.tex"])
    return r1 | r2

@xnt.target
def clean():
    xnt.tasks.rm("build")

@xnt.target
def default():
    build()
