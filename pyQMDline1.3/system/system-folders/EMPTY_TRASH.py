import shutil
from system.PATH import *
os.mkdir(f'{ROOT}/system/system-folders/trash') if not os.path.exists(f'{ROOT}/system/system-folders/trash') else shutil.rmtree(
	f'{ROOT}/system/system-folders/trash') or os.mkdir(f'{ROOT}/system/system-folders/trash')
