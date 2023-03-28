import tkinter as tk
import hashlib

#login window
window = tk.Tk()
#label
tk.Label(window, text="name").grid(row=0)
tk.Label(window, text="password").grid(row=1)
#input save
login = tk.Entry(window)
password = tk.Entry(window, show="*")
#save to file func
def save_to_file():
	pwd = password.get()
	enc = pwd.encode()  #encrypt
	hash1 = hashlib.md5(enc).hexdigest()

	file_path = "/home/user/projects/task_manager/login.txt"
	with open("/home/user/projects/task_manager/login.txt",'w') as file:
		file.write(login.get() + " ")
		file.write(hash1 + "\n")
	file.close()

#compare login and password => login
def log_in():
	log = login.get()
	pwd = password.get()
	enc = pwd.encode()  #encrypt
	hash1 = hashlib.md5(enc).hexdigest()
	with open("/home/user/projects/task_manager/login.txt", "r") as file:
		stored_login, stored_pwd = file.read().split(" ")
	file.close()

	stored_pwd = stored_pwd.strip()
	if log == stored_login and hash1 == stored_pwd:
		print("success")
		#task manager window
		new_window = tk.Tk()
		new_window.title("task Manager")
		new_window.geometry("200x55")
		def save_task():
			task = tasks.get()
			file_path = "/home/user/projects/task_manager/tasks.txt"
			with open("/home/user/projects/task_manager/tasks.txt",'a') as file:
				file.write(tasks.get() + "\n")
			file.close()
			
		def display_file_contents():
				filename = "/home/user/projects/task_manager/tasks.txt"
				with open("/home/user/projects/task_manager/tasks.txt", "r") as file:
					contents = file.readlines()

				root = tk.Tk()
				listbox = tk.Listbox(root)
				for line in contents:
					listbox.insert(tk.END, line.strip())

				listbox.pack()
				root.mainloop()
				

		tk.Button(new_window, text="list", command=display_file_contents).grid(row=3, column=2, sticky=tk.W, pady=4)
		tasks = tk.Entry(new_window)
		tasks.grid(row=0, column=1)
		tk.Button(new_window, text="add task", command=save_task).grid(row=3, column=1, sticky=tk.W, pady=4)
		
		#closes the login windo
		window.destroy()
	else:
		print("wrong login or password")
#input textbox
login.grid(row=0, column=1)
password.grid(row=1, column=1)
#button
tk.Button(window, text="sign", command=save_to_file).grid(row=3, column=1, sticky=tk.W, pady=4)
tk.Button(window, text="login", command=log_in).grid(row=3, column=0, sticky=tk.W, pady=4)

window.mainloop()