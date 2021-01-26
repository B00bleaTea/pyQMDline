import sys
try:
	from commands import *
	from imports import *
except Exception as e:
	print(f'failed while loading modules: {e}')
	sys.exit()

handlers = eval(open('./commands/handlers.hand', 'r').read())

with open('./system/PATH.path', 'r') as PATH:
	pyQMD_PATH = eval(PATH.read())

for run in pyQMD_PATH['autorun']:
	try:
		with open(run, 'r') as f:
			eval(f.read())
	except:
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
		qmd = Out.inp(f'{user} @ {host} [ ~/{current_path} ] >>').split(' ')
		handlers[qmd[0]](*qmd[1:])
	except Exception as e:
		Out.err(f'[ ERROR ] {e}')
