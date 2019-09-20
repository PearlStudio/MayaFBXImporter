# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function

import os

from maya import cmds
from maya import mel


def onMayaDroppedPythonFile(*args, **kwargs):
    """for Maya2017.3+"""
    _create_shelf()


def onMayaDroppedMelFile():
    "for old Maya"
    _create_shelf()


def _create_shelf():
    script_path = os.path.dirname(__file__) + "/scripts"

    command = """
# -------------------------
# FBXImporter
# Author: @tm8r
# https://github.com/tm8r/MayaFBXImporter
# -------------------------

import os
import sys

from maya import cmds

def open_fbx_importer():
    script_path = "{0}"
    if not os.path.exists(script_path):
        cmds.error("FBX Importer install directory is not found. path={0}")
        return
    if script_path not in sys.path:
        sys.path.insert(0, script_path)
    
    import fbx_importer.view
    fbx_importer.view.FBXImporter.open()
open_fbx_importer()""".format(script_path)

    shelf = mel.eval("$gShelfTopLevel=$gShelfTopLevel")
    parent = cmds.tabLayout(shelf, query=True, selectTab=True)
    cmds.shelfButton(
        command=command,
        image="pythonFamily.png",
        annotation="FBXImporter",
        label="FBXImporter",
        imageOverlayLabel="FBXImporter",
        sourceType="Python",
        parent=parent
    )


if __name__ == "_installTm8rFBXImporter":
    onMayaDroppedMelFile()
