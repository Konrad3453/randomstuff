import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()


with open(file_path, "r") as f:
    words = f.read()
    word = words.split()
    words_no_eptylines = words.replace("\n","")
    

def countlines():
    countline = 0
    for character in words:
        if character == "\n":
            countline += 1
    return int(countline)


number_of_words= f"Number of words in this file is:  {str(len(word))}"
number_of_chars = f"Number of characters in this file is:  {str(len(words_no_eptylines))}"
number_of_lines = f"Number of lines in this file is:  {countlines()}"
file_pather = f"Path:  {file_path}"


window = tk.Toplevel()
window.title(f"File Statistics")
window.geometry("350x100")
label1 = tk.Label(window, text=number_of_words)
label2 = tk.Label(window, text=number_of_chars)
label3 = tk.Label(window, text=number_of_lines)
label4 = tk.Label(window, text=file_pather)
label1.pack()
label2.pack()
label3.pack()
label4.pack()
window.mainloop()