import shutil
import pathlib
from system.PATH import *

os.mkdir(pathlib.Path(f'{ROOT}/system/system-folders/trash')) if not os.path.exists(
    pathlib.Path(f'{ROOT}/system/system-folders/trash')) else shutil.rmtree(
    pathlib.Path(f'{ROOT}/system/system-folders/trash')) or os.mkdir(
    pathlib.Path(f'{ROOT}/system/system-folders/trash'))
