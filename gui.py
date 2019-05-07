import tkinter as tk
import tkinter.filedialog
from tkinter import ttk
from utils.torrent import Torrent

import logging

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.filepath = ""
        self.directorypath = ""
        self.master = master
        self.torrents = {}
        self.pack()
        self.create_downlaod_button()
        self.create_download_input()
        if self.torrents:
            self.create_progress_bar()
        # self.create_save_button()


    def create_downlaod_button(self):
        self.download_button = tk.Button(self)
        self.download_button["text"] = "Start Download"
        self.download_button["command"] = self.download_button_action
        self.download_button.pack()
        self.quit = tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack()

    def create_download_input(self):
        self.download_button = tk.Button(self)
        self.download_button["text"] = "Browse"
        self.download_button["command"] = self.askopenfile
        self.download_button.pack()

    def create_save_button(self):
        self.save_button = tk.Button(self)
        self.save_button["text"] = "Choose directory"
        self.save_button["command"] = self.askdirectory
        self.save_button.pack()

    def download_button_action(self):
        torrent = Torrent()
        torrent.load_torrent(self.filepath, self.directorypath)
        torrent.execute_torrent()
        self.torrents.update({torrent.name: torrent})

    def askopenfile(self):
        file = tkinter.filedialog.askopenfile(initialdir = "./", title='Select file')
        self.filepath = file.name

    def askdirectory(self):
        self.directorypath = tkinter.filedialog.askdirectory()

    def create_progress_bar(self):
        style = ttk.Style()
        style.configure("orange.Horizontal.TProgressbar", foreground='#ff752d', background='#ff752d')
        self.progress_bar = ttk.Progressbar(self, style='orange.Horizontal.TProgressbar', orient='horizontal',
                                            length=400, mode='determinate')
        self.progress_bar['maximum'] = 100
        logging.warning(self.torrents)
        self.progress_bar['value'] = self.torrents
        self.progress_bar.pack()


root = tk.Tk()
root.config(background='black')
app = Application(master=root)
app.config(background='#1f232e', width='500')
app.pack(side='left', fill='y')
app.pack_propagate(0)
# download = Download()
# download.config(background='#2c2f36', width='900')
# download.pack(side='left', fill='y')
# download.pack_propagate(0)
# download.mainloop()
app.mainloop()
