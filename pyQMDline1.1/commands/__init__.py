from .qmd_imports import *

try:
	with open('./system/PATH.path', 'r') as PATH:
		pyQMD_PATH = eval(PATH.read())
except:
	pass


def change_json_key(file: open, key: str, value: str):
	with open(file, 'r') as f:
		data = json.loads(f.read())
		data[key] = value
		json.dump(data, open(file, 'w'))


def check_pass(password: str):
	with open(User.profile_data, 'r') as f:
		data = json.loads(f.read())
		if password == data['password']:
			return True
		return False


with open(os.path.realpath('./commands/pyQMDline.man'), 'r') as f:
	man_page = f.read()


class User:
	profile_data = os.path.realpath('./profile/profile.json')

	@classmethod
	def get_data(cls, *args):
		with open(User.profile_data, 'r') as f:
			data = json.loads(f.read())
			return data['user'], data['host']

	@classmethod
	def change_pass(cls, *args):
		with open(User.profile_data, 'r') as f:
			if check_pass(Out.inp('current password >')):
				change_json_key(User.profile_data, 'password', args[0])
				return 0
			Out.err('[ PASS ] failed to change the password')
			return -1

	@classmethod
	def change_user(cls, *args):
		with open(User.profile_data, 'r') as f:
			if check_pass(Out.inp('current password >')):
				change_json_key(User.profile_data, 'user', args[0])
				return 0
			Out.err('[ USER ] failed to change the user')
			return -1

	@classmethod
	def change_host(cls, *args):
		with open(User.profile_data, 'r') as f:
			if check_pass(Out.inp('current password >')):
				change_json_key(User.profile_data, 'host', args[0])
				return 0
			Out.err('[ HOST ] failed to change the host machine name')
			return -1

	@classmethod
	def info(cls, *args):
		user, host = User.get_data()
		Out.out(f'''
	OS: {platform.system()} @ pyQMDline
	HOST: {platform.system()} @ {host}
	USER: {platform.node()} @ {user}
''')

	@classmethod
	def pyqmd_version(cls, *args):
		Out.out(f'pyQMDline version {pyQMD_PATH["version"]}')


class FilePaths:
	@classmethod
	def change_dir(cls, *args):
		os.chdir(args[0])

	@classmethod
	def list_dir(cls, *args):
		for dir in os.listdir():
			Out.out(f"NAME: {dir} \t IS_FILE: {os.path.isfile(os.path.realpath(dir))}")

	@classmethod
	def make_file(cls, *args):
		if not os.path.exists(args[0]):
			open(args[0], 'w').close()
		else:
			Out.err('this file already exists')

	@classmethod
	def make_dir(cls, *args):
		if not os.path.exists(args[0]):
			os.mkdir(args[0])
		else:
			Out.err('this directory already exists')

	@classmethod
	def remv(cls, *args):
		if Out.inp('are you sure [Y/N] >').lower() == 'y':
			try:
				try:
					os.remove(args[0])
				except:
					shutil.rmtree(args[0])
			except:
				Out.err(f'[ ERROR ] unexistant path or unable to remove {args[0]}')

	@classmethod
	def show_content(cls, *args):
		with open(args[0], 'r') as f:
			Out.out(f'========= content of {args[0]} =========\n')
			Out.out(f.read())

	@classmethod
	def add_content(cls, *args):
		with open(args[0], 'r') as f:
			prev = f.read()
			future = ''
			for piece in args[1:]:
				future += f" {piece}"
			with open(args[0], 'w') as f:
				f.write(prev + future[1:])

	@classmethod
	def overwrite_content(cls, *args):
		if Out.inp('are you sure you want to overwrite this file >').lower() == 'y':
			future = ''
			for piece in args[1:]:
				future += f" {piece}"
			with open(args[0], 'w') as f:
				f.write(future[1:])


class Utilities:
	@classmethod
	def exit(cls, *args):
		if args and '-f' in args:
			sys.exit(130)
		elif Out.inp('are you sure >').lower() == 'y':
			sys.exit(0)

	@classmethod
	def open_url(cls, *args):
		webbrowser.open(args[0])

	@classmethod
	def std_output(cls, *args):
		future = ''
		for fut in args:
			future += f' {fut}'
		Out.out(future[1:])

	@classmethod
	def current_working_dir(cls, *args):
		Out.out(os.getcwd())

	@classmethod
	def help(cls, *args):
		Out.out(man_page)


class Requests:
	@classmethod
	def POST(cls, *args):
		r = eval(f'requests.post("{args[0]}", "{args[1]}").{args[2]}') if 'json' not in args else eval(
			f'requests.post("{args[0]}", "{args[1]}").{args[2]}()')
		Out.out(r)

	@classmethod
	def GET(cls, *args):
		r = eval(f'requests.get("{args[0]}", "{args[1]}").{args[2]}') if 'json' not in args else eval(
			f'requests.get("{args[0]}", "{args[1]}").{args[2]}()')
		Out.out(r)


class Compile:
	@classmethod
	def python(cls, *args):
		code = ''
		for code_ in args:
			code += f' {code_}'
		print(Fore.MAGENTA, end='')
		eval(code)
		print(Style.RESET_ALL, end='')

	@classmethod
	def shell(cls, *args):
		cmd = subprocess.check_output(args)
		Out.out(cmd.decode())
