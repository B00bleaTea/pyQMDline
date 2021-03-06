from commands import *
from imports import *

handlers = {
	"exit": Utilities.exit,
	"help": Utilities.help,
	"echo": Utilities.std_output,
	"cwd": Utilities.current_working_dir,
	"URL": Utilities.open_url,

	"chpass": User.change_pass,
	"chuser": User.change_user,
	"chhost": User.change_host,
	"neofetch": User.info,

	"cd": FilePaths.change_dir,
	"ls": FilePaths.list_dir,

	"file": FilePaths.make_file,
	"dir": FilePaths.make_dir,
	"rm": FilePaths.remv,
	"dump": FilePaths.show_content,
	"WRITE": FilePaths.add_content,
	"OVERWRITE": FilePaths.overwrite_content,

	"POST": Requests.POST,
	"GET": Requests.GET,

	"py": Compile.python,
	"shell": Compile.shell
}

with open('./system/PATH.path', 'r') as PATH:
	pyQMD_PATH = eval(PATH.read())

for run in pyQMD_PATH['autorun']:
	try:
		with open(run, 'r') as f:
			eval(f.read())
	except Exception as e:
		Out.err(f'[ AUTORUN-ERROR @ {run} ] {e}')

try:
	os.chdir(pyQMD_PATH['system-folder'])
except Exception as e:
	Out.err(f'''the system ({pyQMD_PATH['system-folder']}) folder wasn't able to be recognised or a key error occured.
please investigate. [ booting into root... ]
[ system error ] {e}''')

while True:
	if not pyQMD_PATH['boot']:
		Out.err(f'''boot is disabled, if you want to enable boot,
please set the PATH "boot" variable to True instead of {pyQMD_PATH["boot"]}''')
		break
	try:
		try:
			current_path = os.getcwd()
			current_path = current_path[current_path.index(pyQMD_PATH['STOP']):]
		except:
			os.chdir(pyQMD_PATH['QMD'])
			continue
		user, host = User.get_data()
		qmd = Out.inp(f'{user} @ {host} [ {current_path} ] >>').split(' ')
		handlers[qmd[0]](*qmd[1:])
	except Exception as e:
		Out.err(f'[ ERROR ] {e}')
