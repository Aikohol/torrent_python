import tkinter as tk
from tkinter import ttk
import tkinter.filedialog
from utils.torrent import Torrent
import asyncio
import logging

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.filepath = ""
        self.master = master
        self.pack()
        self.torrents = {}
        self.torrent = Torrent()
        self.create_downlaod_button()
        self.create_download_input()
        self.create_progress_bar()
        asyncio.run(self.run_progressBar())

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

    def download_button_action(self):
        self.torrent.torrent_start(self.filepath)
        self.torrent.torrent_info()


    def askopenfile(self):
        file = tkinter.filedialog.askopenfile(initialdir = "./", title='Select file', filetypes = (("torrent files",".torrent"),("all files",".*")))
        self.filepath = file.name

    def create_progress_bar(self):
        style = ttk.Style()
        style.configure("orange.Horizontal.TProgressbar", foreground='#ff752d', background='#ff752d')
        self.progress_bar = ttk.Progressbar(self, style='orange.Horizontal.TProgressbar', orient='horizontal',
                                            length=400, mode='determinate')
        self.progress_bar.pack()

    def run_progressBar(self):
        if self.torrent.info['progress'] > 0:
            while self.torrent.info['progress'] < 100:
                self.progress_bar["maximum"] = 100
                self.progress_bar["value"] = self.torrent.info['progress']
                self.progress_bar.update()
                print(self.progress_bar['value'])
        yield


root = tk.Tk()
app = Application(master=root)
app.mainloop()
