'''
Name: scene-preview.py
Version: 1.0.0
Author: gfxhacks.com
Desc: Captures and saves a scene preview based on the active viewport, at the current frame. Uses playblast feature.
'''

import maya.cmds as cmds
import os
import time

# set screenshot dimensions
width = 960
height = 540

# get active viewport panel
panel = cmds.getPanel( withFocus=True )

# throw error if active panel is not a viewport
if "modelPanel" not in cmds.getPanel(typeOf=panel):
	cmds.confirmDialog( title='Error!', message='Please select a viewport panel first.', button=['Ok'], defaultButton='Ok', dismissString='No' )
	raise RuntimeError('Error: Please select a viewport panel, then try again.')

# get current frame number
curFrame = int(cmds.currentTime( query=True ))

# get name of current file
scName = cmds.file( query=True, sn=True, shn=True )

# get path of current file
scPath = cmds.file( query=True, sn=True )

# set new path where previews will be saved to
path = scPath + "-prv/"

# get name of current camera
cam = cmds.modelEditor( panel, query=True, camera=True )

# get current timestamp
ts = int( time.time() )

# construct full path
fullPath = "{}{}-{}-f{}-{}.jpg".format( path, scName, cam, curFrame, ts )

# Create path if it doesn't exist
if not os.path.exists( path ):
    os.makedirs(path)

# run playblast for current viewport
cmds.playblast( fr=curFrame, v=False, fmt="image", c="jpg", orn=False, cf=fullPath, wh=[width,height], p=100 )

# log path to console for reference
print('Snapshot saved as: ' + fullPath )

# show popup message in viewport
cmds.inViewMessage( amg='<span style="color:#82C99A;">Snapshot saved</span> for <hl>' + cam + '</hl> in <hl>' + scName + '<hl> at frame <hl>' + str(curFrame) + '</hl>', pos='topRight', fade=True, fst=3000 )
