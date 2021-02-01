import sys

try:
	from .qmd_imports import *
	from system.PATH import *
except Exception as e:
	print(f'failed to load modules in commands, {e}')
	sys.exit()


# random functions and/or variables
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


def get_size(bytes_, suffix="B"):
	factor = 1024
	for unit in ["", "K", "M", "G", "T", "P"]:
		if bytes_ < factor:
			return f"{bytes_:.2f}{unit}{suffix}"
		bytes_ /= factor


partitions = psutil.disk_partitions()
disk_io = psutil.disk_io_counters()
disk_info = []

for partition in partitions:
	try:
		partition_usage = psutil.disk_usage(partition.mountpoint)
		disk_info.append((partition.device, partition.mountpoint, partition.fstype,
						get_size(partition_usage.total), get_size(partition_usage.used),
						get_size(partition_usage.free), f'{partition_usage.percent}%',
						get_size(disk_io.read_bytes), get_size(disk_io.write_bytes)))
	except PermissionError:
		continue


# caching the disk info

# all user management commands
class User:
	profile_data = os.path.realpath(f'{ROOT}/profile/profile.json')

	@classmethod
	def get_data(cls, *args):
		with open(User.profile_data, 'r') as f:
			data = json.loads(f.read())
			return data['user'], data['host']

	@classmethod
	def change_pass(cls, *args):
		with open(User.profile_data, 'r') as _:
			if check_pass(Out.inp('current password >')):
				if args[0].strip():
					change_json_key(User.profile_data, 'password', args[0].strip())
					return 0
			Out.err('[ PASS ] failed to change the password')
			return -1

	@classmethod
	def change_user(cls, *args):
		with open(User.profile_data, 'r') as _:
			if check_pass(Out.inp('current password >')):
				if args[0].strip():
					change_json_key(User.profile_data, 'user', args[0].strip())
					return 0
			Out.err('[ USER ] failed to change the user')
			return -1

	@classmethod
	def change_host(cls, *args):
		with open(User.profile_data, 'r') as _:
			if check_pass(Out.inp('current password >')):
				if args[0].strip():
					change_json_key(User.profile_data, 'host', args[0].strip())
					return 0
			Out.err('[ HOST ] failed to change the host machine name')
			return -1

	@classmethod
	def pyqmd_version(cls, *args):
		Out.out(f'pyQMDline version {pyQMD_PATH["version"]} {pyQMD_PATH["phase"]}')


# pyQMDline file and directory manager commands
class FilePaths:
	@classmethod
	def change_dir(cls, *args):
		dirname = ''
		for piece in args:
			dirname += f" {piece}"
		os.chdir(dirname[1:])

	@classmethod
	def list_dir(cls, *args):
		tabular_data = []
		for file_path in os.listdir():
			tabular_data.append((file_path, os.path.isfile(os.path.realpath(file_path))))
		Out.out(tabulate(tabular_data, headers=['NAME', 'IS_FILE']))

	@classmethod
	def make_file(cls, *args):
		if not os.path.exists(args[0]):
			name = ''
			for piece in args:
				name += f' {piece}'
			name = name[1:]
			open(name, 'w').close()
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
			Out.out(f'========= content of {name} =========\n')
			Out.out(f.read())

	@classmethod
	def add_content(cls, *args):
		filename = args[args.index('-F'):args.index('-C')][1:]
		content = args[args.index('-C'):][1:]

		name = ''
		content_ = ''
		for piece in filename:
			name += f" {piece}"
		name = name[1:]
		for c_piece in content:
			content_ += f" {c_piece}"
		content_ = content_[1:]

		with open(name, 'r') as f:
			prev = f.read()
			with open(name, 'w') as f1:
				f1.write(prev + content_ + '\n')

	@classmethod
	def overwrite_content(cls, *args):
		if Out.inp('are you sure you want to overwrite this file >').lower() == 'y':
			filename = args[args.index('-F'):args.index('-C')][1:]
			content = args[args.index('-C'):][1:]

			name = ''
			content_ = ''
			for piece in filename:
				name += f" {piece}"
			name = name[1:]
			for c_piece in content:
				content_ += f" {c_piece}"
			content_ = content_[1:]

			with open(name, 'w') as f1:
				f1.write(content_ + '\n')

	@classmethod
	def trash(cls, *args):
		if '-c' in args:
			if Out.inp('are you sure >').lower() == 'y':
				os.mkdir(f'{pyQMD_PATH["trash"]}') if not os.path.exists(
					f'{pyQMD_PATH["trash"]}') else shutil.rmtree(f'{pyQMD_PATH["trash"]}') or os.mkdir(
					f'{pyQMD_PATH["trash"]}')
				Out.success('trash bin has been cleaned out')
		if '-l' in args:
			for trashed in os.listdir(f'{pyQMD_PATH["trash"]}'):
				Out.out(f'{trashed}')
		if '-r' in args:
			name = ''
			tmp = []
			for item in args:
				tmp.append(item)
			tmp.remove('-r')
			for piece in tmp:
				name += f' {piece}'
			name = name[1:]
			if name.strip():
				shutil.move(f"{pyQMD_PATH['trash']}/{name}", os.getcwd())
				return
			Out.err('please supply a real folder or file')
		if '-c' not in args and '-l' not in args and '-r' not in args:
			name = ''
			for piece in args:
				name += f" {piece}"
			name = name[1:]
			shutil.move(name, pyQMD_PATH['trash'])

	@classmethod
	def move(cls, *args):
		filename = args[args.index('-F'):args.index('-D')][1:]
		directoty = args[args.index('-D'):][1:]

		name = ''
		path_name = ''
		for piece in filename:
			name += f" {piece}"
		name = name[1:]
		for d_piece in directoty:
			path_name += f" {d_piece}"
		path_name = path_name[1:]

		shutil.move(name, path_name)


# usual pyQMDline utilities
class Utilities:
	@classmethod
	def info(cls, *args):
		uname = platform.uname()

		boot_time = psutil.boot_time()
		boot_time = datetime.datetime.fromtimestamp(boot_time)
		cpu_freq = psutil.cpu_freq()

		svmem = psutil.virtual_memory()
		swap = psutil.swap_memory()

		gpus = GPUtil.getGPUs()
		list_gpus = []
		for gpu in gpus:
			gpu_id = gpu.id

			gpu_name = gpu.name
			gpu_load = f"{gpu.load * 100}%"
			gpu_free_memory = f"{gpu.memoryFree}MB"

			gpu_used_memory = f"{gpu.memoryUsed}MB"
			gpu_total_memory = f"{gpu.memoryTotal}MB"

			gpu_temperature = f"{gpu.temperature} °C"
			gpu_uuid = gpu.uuid
			list_gpus.append((
				gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
				gpu_total_memory, gpu_temperature, gpu_uuid
			))
		# get required data ^
		Out.out(f'''
-==== SYSTEM INFORMATION ====-
System: {uname.system}
None Name: {uname.node}
Release: {uname.release}
Version: {uname.version}
Machine: {uname.machine}

Boot Time: {boot_time.year}-{boot_time.month}-{boot_time.day} {boot_time.hour}:{boot_time.minute}:{boot_time.second}


-==== CPU INFORMATION ====-
Physical cores: {psutil.cpu_count(logical=False)}
Total Cores: {psutil.cpu_count(logical=True)}

Max Frequency: {cpu_freq.max:.2f}Mhz
Min Frequency: {cpu_freq.min:.2f}Mhz
Current Frequency: {cpu_freq.current:.2f}Mhz

Total CPU Usage: {psutil.cpu_percent()}%
CPU Usage Per Core: \n{tabulate([(core, f'{percentage}%') 
								for core, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1), start=1)],
								headers=['CORE', 'PERCENT'], tablefmt="github")}


-==== MEMORY INFORMATION ====-
Total: {get_size(svmem.total)}
Available: {get_size(svmem.available)}
Used: {get_size(svmem.used)}
Percentage: {svmem.percent}%

-=== SWAP ===-
Total: {get_size(swap.total)}
Free: {get_size(swap.free)}
Used: {get_size(swap.used)}
Percentage: {swap.percent}%


-==== GPU INFORMATION ====-
{tabulate(list_gpus, headers=["Id", "Name", "Load", "Free Memory", "Used Memory", "Total Memory", "Temperature", "UUID"]
		,tablefmt="fancy_grid")}

======================================================================
[ you can also run: [ diskscan and/or netscan ] for more information ]''')

	@classmethod
	def get_net_info(cls, *args):
		if_addrs = psutil.net_if_addrs()
		for interface_name, interface_addresses in if_addrs.items():
			for address in interface_addresses:
				Out.out(f"=== Interface: {interface_name} ===")
				if str(address.family) == 'AddressFamily.AF_INET':
					Out.out(f"  IP Address: {address.address}")
					Out.out(f"  Netmask: {address.netmask}")
					Out.out(f"  Broadcast IP: {address.broadcast}")
				elif str(address.family) == 'AddressFamily.AF_PACKET':
					Out.out(f"  MAC Address: {address.address}")
					Out.out(f"  Netmask: {address.netmask}")
					Out.out(f"  Broadcast MAC: {address.broadcast}")
		net_io = psutil.net_io_counters()
		Out.out(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
		Out.out(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")
		Out.out('''
======================================================================
[ you can also run: [ qfetch and/or diskscan ] for more information ]''')

	@classmethod
	def get_disk_info(cls, *args):
		Out.out(tabulate(disk_info, headers=['Device', 'Mountpoint', 'File System Type', 'Total Size', 'Used', 'Free',
											'Used ( % )', 'Total Read', 'Total Write'], tablefmt='fancy_grid'))
		Out.out('''
======================================================================
[ you can also run: [ qfetch and/or netscan ] for more information ]''')

	@classmethod
	def exit(cls, *args):
		if '-f' in args:
			sys.exit(130)
		elif Out.inp('are you sure >').lower() == 'y':
			sys.exit(0)

	@classmethod
	def open_url(cls, *args):
		# i don't think there's urls with spaces?
		if args[0].strip():
			webbrowser.open(args[0])
			return
		Out.success('please enter a valid URL')

	@classmethod
	def std_output(cls, *args):
		future = ''
		for fut in args:
			future += f' {fut}'
		future = future[1:]
		Out.out(future)

	@classmethod
	def current_working_dir(cls, *args):
		Out.out(os.getcwd())

	@classmethod
	def help(cls, *args):
		if '-e' in args:
			with open(os.path.realpath(f'{ROOT}/commands/pyQMDexamples.man'), 'r') as f:
				Out.out(f.read())
			return
		with open(os.path.realpath(f'{ROOT}/commands/pyQMDline.man'), 'r') as f:
			Out.out(f.read())

	@classmethod
	def clear(cls, *args):
		print("\033[H\033[J", end='') if '-F' not in args else print('\n' * 500)

	@classmethod
	def date(cls, *args):
		Out.out(time.ctime(time.time()))

	@classmethod
	def printf(cls, *args):
		string = ''
		for piece in args:
			string += f" {piece}"
		string = string[1:]
		eval(f'out(f"{string}")', {}, {"out": Out.out})

	@classmethod
	def set_theme(cls, *args):
		name = ''
		for piece in args:
			name += f" {piece}"
		name = name[1:]
		if os.path.splitext(name)[1] != '.pqtheme':
			Out.err('please supply a *.pqtheme file to change your theme')
			return
		with open(name, 'r') as f:
			theme = f.read()
		open(pyQMD_PATH["theme-file"], 'w').write(theme)
		Out.out('Restart pyQMDline for your theme to apply')


# the request class
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
		# send a request to the info API
		info = requests.get('https://ip.me/').text
		Out.out(f'your IP address is: {info.strip()}')
		del info


# compiler class
class Compile:
	@classmethod
	def python(cls, *args):
		code = ''
		for code_ in args:
			code += f' {code_}'
		code = code[1:]
		print(Fore.MAGENTA, end='')
		# yea, eval is dangerous, but thinking of a better solution
		eval(code, {}, {})
		print(Style.RESET_ALL, end='')

	@classmethod
	def shell(cls, *args):
		cmd = subprocess.check_output(args)
		Out.out(cmd.decode())

	@classmethod
	def pyql(cls, *args):
		# yes, yes, yes - evil eval, i'll think of a better solution
		handlers = eval(open(f'{ROOT}/commands/handlers.hand', 'r').read())
		name, extention = os.path.splitext(args[0])
		line = 0
		if extention.lower() != '.pyql':
			Out.err(f'[ FILE-FORMAT ERROR ] please supply a *.pyql file instead of *{extention} file')
			return
		with open(args[0], 'r') as f:
			for command in f.readlines():
				# basically simulating the user input
				line += 1
				try:
					qmd = command.strip('\n').split(" ")
					handlers[qmd[0]](*qmd[1:])
				except Exception as e:
					command = command.strip('\n')
					if command.strip() != '':
						Out.err(f'[ PYQL-ERROR @ {command} ] LINE {line} - {e}')
						break


# the process manager class
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

	# ??happy?? 500 lines of code

	@classmethod
	def kill_pid(cls, *args):
		try:
			p = psutil.Process(int(args[0]))
			p.kill()
		except Exception as e:
			Out.err(f"[ PRC ] can't kill this process {args[0]}, {e}")
			return
		Out.success(f'successfully killed the process {args[0]}')


# fun commands
class Random:
	@classmethod
	def popup(cls, *args):
		content = ''
		for piece in args:
			content += f" {piece}"
		content = content[1:]
		easygui.msgbox(content)

	@classmethod
	def rid_tsil(cls, *args):
		atad_ralubat = []

		for meti in os.listdir():
			pmt = []
			emen = ''
			pmt_emen = meti

			for rettel in meti:
				pmt.append(rettel)
			pmt.reverse()
			for rettel_ in pmt:
				emen += rettel_

			atad_ralubat.append((emen, "eurT" if os.path.isfile(os.path.abspath(pmt_emen)) else "eslaF"))
		Out.out(tabulate(atad_ralubat, headers=["EMEN", "ELIF_SI"]))
