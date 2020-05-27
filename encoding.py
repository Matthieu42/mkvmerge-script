import os;
import sys;
filePathSrc="D:\Séries\Subtitle"
for root, dirs, files in os.walk(filePathSrc):
    for fn in files:
      if fn[-4:] != '.jar' and fn[-5:] != '.ear' and fn[-4:] != '.gif' and fn[-4:] != '.jpg' and fn[-5:] != '.jpeg' and fn[-4:] != '.xls' and fn[-4:] != '.GIF' and fn[-4:] != '.JPG' and fn[-5:] != '.JPEG' and fn[-4:] != '.XLS' and fn[-4:] != '.PNG' and fn[-4:] != '.png' and fn[-4:] != '.cab' and fn[-4:] != '.CAB' and fn[-4:] != '.ico':
        notepad.open(root + "\\" + fn)
        console.write(root + "\\" + fn + "\r\n")
        #Does not work --> notepad.runMenuCommand("Encoding", "Character sets", "Chinese", "GB2312 (Simplified)")
        notepad.menuCommand(MENUCOMMAND.FORMAT_ANSI)
        # notepad.runMenuCommand("Encoding", "Convert to UTF-8-BOM")
        notepad.menuCommand(MENUCOMMAND.FORMAT_CONV2_UTF_8)
        # Reference: https://github.com/bruderstein/PythonScript/blob/master/PythonScript/src/NotepadPython.cpp
        notepad.save()
        notepad.close()