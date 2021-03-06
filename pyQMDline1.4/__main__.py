import sys

try:
	from LICENSE.POLICY import *
	from commands import *
	from imports import *
	from system.PATH import *
except Exception as e:
	print(f'failed while loading modules: {e}')
	sys.exit()

handlers = eval(open(pathlib.Path(f'{ROOT}/commands/handlers.hand'), 'r').read())

for run in pyQMD_PATH['autorun']:
	try:
		with open(pathlib.Path(run), 'r') as f:
			exec(f.read())
	except Exception as e:
		Out.err(f'[ AUTORUN-ERROR @ {run} ] {e}')

try:
	os.chdir(pyQMD_PATH['system-folder'])
except Exception as e:
	Out.err(f'''the system ({pyQMD_PATH['system-folder']}) folder wasn't able to be recognised or a key error occured.
please investigate. [ booting into root... ]
[ system error ] {e}''')

try:
	with open(pathlib.Path(f'{ROOT}/has_agreed_to_policy.bool'), 'r') as f:
		if not eval(f.read()):
			Out.success(POLICY)
			if Out.inp('[ Y/N ] >').lower() != 'y':
				sys.exit(-9)
			open(pathlib.Path(f'{ROOT}/has_agreed_to_policy.bool'), 'w').write('True')
except FileNotFoundError:
	open(pathlib.Path(f'{ROOT}/has_agreed_to_policy.bool'), 'w').write('False')
	sys.exit(-9)

while True:
	if not pyQMD_PATH['boot']:
		Out.err(f'''boot is disabled, if you want to enable boot,
please set the PATH "boot" variable to True instead of {pyQMD_PATH["boot"]}''')
		break
	try:
		try:
			current_path = os.getcwd()
			current_path = current_path[current_path.index(pyQMD_PATH['STOP']):]
		except ValueError:
			os.chdir(ROOT)
			continue
		user, host = User.get_data()
		try:
			qmd = Out.inp(f'{user}@{host} [~{os.path.sep}{current_path}] !') if type(
				eval(open(pathlib.Path(f'{ROOT}/has_agreed_to_policy.bool'), 'r').read())) == bool else sys.exit(-9)
			tmp = qmd
			qmd = qmd.split(' ')
			with open(pathlib.Path(f'{ROOT}/.pyQMD_history'), 'a') as f:
				f.write(f'{tmp}\n')
		except KeyboardInterrupt:
			print('\nKeyboardInterrupt')
			continue
		handlers[qmd[0]](*qmd[1:])
	except KeyError:
		Out.err(f'[ ERROR ] command {tmp} not found')
	except Exception as e:
		Out.err(f'[ CRITICAL-ERROR ] {e}')
