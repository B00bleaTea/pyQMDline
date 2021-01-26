from .qmd_imports import *

try:
	with open('./system/PATH.path', 'r') as PATH:
		pyQMD_PATH = eval(PATH.read())
except Exception as e:
	Out.err(f'[ CRITICAL ] failed while trying to load the PATH')


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
		dirname = ''
		for piece in args:
			dirname += f" {piece}"
		os.chdir(dirname[1:])

	@classmethod
	def list_dir(cls, *args):
		for dir in os.listdir():
			Out.out(f"NAME: {dir} \t IS_FILE: {os.path.isfile(os.path.realpath(dir))}")

	@classmethod
	def make_file(cls, *args):
		if not os.path.exists(args[0]):
			name = ''
			for piece in args:
				name += f' {piece}'
			open(name[1:], 'w').close()
		else:
			Out.err('this file already exists')

	@classmethod
	def make_dir(cls, *args):
		if not os.path.exists(args[0]):
			name = ''
			for piece in args:
				name += f' {piece}'
			os.mkdir(name[1:])
		else:
			Out.err('this directory already exists')

	@classmethod
	def remv(cls, *args):
		if Out.inp('are you sure [Y/N] >').lower() == 'y':
			name = ''
			for piece in args:
				name += f" {piece}"
			name = name[1:]
			try:
				try:
					os.remove(name)
				except:
					shutil.rmtree(name)
			except:
				Out.err(f'[ ERROR ] unexistant path or unable to remove {name}')

	@classmethod
	def show_content(cls, *args):
		name = ''
		for piece in args:
			name += f" {piece}"
		name = name[1:]
		with open(name, 'r') as f:
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
				f.write(prev + future[1:] + "\n")

	@classmethod
	def overwrite_content(cls, *args):
		if Out.inp('are you sure you want to overwrite this file >').lower() == 'y':
			future = ''
			for piece in args[1:]:
				future += f" {piece}"
			with open(args[0], 'w') as f:
				f.write(future[1:] + "\n")

	@classmethod
	def trash(cls, *args):
		if '-c' in args:
			if Out.inp('are you sure >').lower() == 'y':
				os.mkdir('./system-folders/trash') if not os.path.exists(
					'./system-folders/trash') else shutil.rmtree('./system-folders/trash') or os.mkdir(
					'./system-folders/trash')
				Out.out('trash bin has been cleaned out')
		if '-l' in args:
			for trashed in os.listdir('./system-folders/trash'):
				Out.out(f'{trashed}')
		if '-c' not in args and '-l' not in args:
			name = ''
			for piece in args:
				name += f" {piece}"
			name = name[1:]
			shutil.move(name, pyQMD_PATH['trash'])

	@classmethod
	def move(cls, *args):
		path_name = ''
		for piece in args[1:]:
			path_name += f" {piece}"
		path_name = path_name[1:]
		shutil.move(args[0], path_name)


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
		if '-e' not in args:
			with open(os.path.realpath('../commands/pyQMDline.man'), 'r') as f:
				Out.out(f.read())
		else:
			with open(os.path.realpath('../commands/pyQMDexamples.man'), 'r') as f:
				Out.out(f.read())

	@classmethod
	def youtube_downloader(cls, *args):
		Out.out('processing...')
		yt = pytube.YouTube(args[0])

		Out.out('pick a stream\n')
		for stream in yt.streams:
			Out.out(f'''
		\t\t{stream}
		\t\t====================
		\t\titag: {stream.itag}
		\t\tmime type: {stream.mime_type}
		\t\tquality: {stream.resolution or stream.abr or None}
		''')

		stream = int(Out.inp('itag >'))
		stream = yt.streams.get_by_itag(stream)
		Out.out(f'downloading video " {stream.title} "')
		stream.download(output_path=pyQMD_PATH['media'])
		Out.success(f'finished downloading " {stream.title} ", check your media folder')

	@classmethod
	def fake_clear(cls, *args):
		print('\n' * 1500)

	@classmethod
	def date(cls, *args):
		Out.out(time.ctime(time.time()))

	@classmethod
	def printf(cls, *args):
		string = ''
		for piece in args:
			string += f" {piece}"
		string = string[1:]
		eval(f'Out.out({string})')


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

	@classmethod
	def get_ip(cls, *args):
		info = requests.get('https://ipapi.co/json/').json()
		Out.out(f'your {info["version"]} IP address is {info["ip"]}')


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

	@classmethod
	def pyql(cls, *args):
		handlers = eval(open('../commands/handlers.hand', 'r').read())
		name, extention = os.path.splitext(args[0])
		line = 0
		if extention.lower() != '.pyql':
			Out.err(f'[ FILE-FORMAT ERROR ] please supply a *.pyql file instead of *{extention} file')
			return
		with open(args[0], 'r') as f:
			for command in f.readlines():
				line += 1
				try:
					qmd = command.strip('\n').split(" ")
					handlers[qmd[0]](*qmd[1:])
				except Exception as e:
					command = command.strip('\n')
					Out.err(f'[ PYQL-ERROR @ {command} ] LINE {line} - {e}')
					break


class Process:
	@classmethod
	def processes(cls, *args):
		processes, count = [], 0
		for proc in psutil.process_iter():
			count += 1
			processes.append((proc.name(), proc.pid))
		Out.out(tabulate(processes, headers=['NAME', 'PID']))
		Out.out(f'TOTAL PROCESSES RUNNING: {count}')

	@classmethod
	def find_by_name(cls, *args):
		name_ = ''
		for piece in args:
			name_ += f' {piece}'
		name_ = name_[1:]
		processes, pids, valid = [], [], []
		for proc in psutil.process_iter():
			processes.append(proc.name())
			pids.append(proc.pid)
		for name in processes:
			if name == name_:
				try:
					indx = processes.index(name_)
				except:
					Out.err('[ PID ] process not found')
				valid.append((processes[indx], pids[indx]))
				processes.pop(indx)
				pids.pop(indx)
		Out.out(tabulate(valid, headers=['NAME', 'PID']))

	@classmethod
	def find_by_pid(cls, *args):
		processes, pids = [], []
		for proc in psutil.process_iter():
			processes.append(proc.name())
			pids.append(proc.pid)
		Out.out(
			tabulate([(processes[pids.index(int(args[0]))], pids[pids.index(int(args[0]))])], headers=['NAME', 'PID']))

	@classmethod
	def kill_pid(cls, *args):
		try:
			p = psutil.Process(int(args[0]))
			p.kill()
		except Exception as e:
			Out.err(f"[ PRC ] can't kill this process {args[0]}, {e}")
			return
		Out.success(f'successfully killed the process {args[0]}')
