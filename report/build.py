#!/usr/bin/env python

import xnt
import os

properties = { "doc_name" : "report",
               "build.dir": "build", }

@xnt.target
def default():
    build()

@xnt.target
def init():
    xnt.mkdir(properties["build.dir"])

@xnt.target
def build():
    init()
    return build_doc(properties["doc_name"])

@xnt.target
def clean():
    xnt.rm("build")

@xnt.target
def cp():
    xnt.cp(os.path.join(properties["build.dir"],
                   properties["doc_name"]) + ".pdf",
           os.path.join(os.getcwd(),
                        properties["doc_name"]) + ".pdf")

def build_doc(doc_name):
    def pdflatex(draftmode=False):
        cmd = ["pdflatex",
               "-output-directory",
               properties["build.dir"],
               doc_name]
        if draftmode:
            cmd.append("-draftmode")
        return xnt.call(cmd)
    def bibtex():
        xnt.cp("references.bib", properties["build.dir"])
        cwd = os.getcwd()
        os.chdir(properties["build.dir"])
        r = xnt.call(["bibtex", doc_name])
        os.chdir(cwd)
        return r
    r1 = pdflatex(True)
    r2 = bibtex()
    r3 = pdflatex(True)
    r4 = pdflatex()
    return r1 | r2 | r3 | r4
