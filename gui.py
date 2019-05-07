import tkinter as tk
import tkinter.filedialog
from tkinter import ttk
from utils.torrent import torrent_start
import logging

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.filepath = ""
        self.master = master
        self.pack()
        self.create_downlaod_button()
        self.create_download_input()
        self.create_input_download()
        self.create_progress_bar()

    def create_downlaod_button(self):
        self.download_button = tk.Button(self)
        self.download_button["text"] = "Start Download"
        self.download_button["command"] = self.download_button_action
        self.download_button.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def create_download_input(self):
        self.download_button = tk.Button(self)
        self.download_button["text"] = "Browse"
        self.download_button["command"] = self.askopenfile
        self.download_button.pack(side="top")

    def create_progress_bar(self):
        self.progress_bar = ttk.Progressbar(self, orient='horizontal', length=400, mode='determinate')
        self.progress_bar.pack()
        self.progress_bar['maximum'] = 100
        self.progress_bar['value'] = 30

    def create_input_download(self):
        self.download_input = tk.Entry(self, textvariable = '')

    def download_button_action(self):
        torrent_start(self.filepath)

    def askopenfile(self):
        file = tkinter.filedialog.askopenfile(initialdir = "./", title='Select file')
        pathfile git = file.name


root = tk.Tk()
root.filename = filedialog.askopenfilename(initialdir = "/", title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print (root.filename)
app = Application(master=root)
app.mainloop()
