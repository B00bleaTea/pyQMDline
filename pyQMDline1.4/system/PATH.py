import os
import pathlib

ROOT = os.path.abspath('.')
pyQMD_PATH = {"STOP": "pyQMDline",
              "boot": True,

              "system-folder": pathlib.Path(f"{ROOT}/system"),

              "media": pathlib.Path(f"{ROOT}/system/system-folders/media"),
              "documents": pathlib.Path(f"{ROOT}/system/system-folders/documents"),
              "trash": pathlib.Path(f"{ROOT}/system/system-folders/trash"),

              "autorun": [f'{ROOT}/LICENSE/__license__.py',
                          f'{ROOT}/system/system-folders/EMPTY_TRASH.py'],

              "theme-file": pathlib.Path(f"{ROOT}/THEME.pqtheme"),

              "version": "1.4",
              "phase": "beta"}

# this in the PATH of your download of pyQMDline
# if you don't know what you're doing it's possible that you'll break it
# AKA. don't touch anything if you're not experienced enough
