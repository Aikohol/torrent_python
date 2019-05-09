import tkinter as tk
from tkinter import ttk
import tkinter.filedialog
from utils.torrent import Torrent
import logging
import libtorrent as lt
import time
import sys
from threading import Thread
import logging

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.filepath = ""
        self.master = master
        self.pack()
        self.torrents = []
        self.labels= []
        self.create_downlaod_button()
        self.create_download_input()
        self.create_quit_button()

    def create_label_info(self):
        logging.warning("passing through")
        label = tk.Label(self)
        self.labels.append(label)
        return label

    def create_downlaod_button(self):
        self.download_button = tk.Button(self)
        self.download_button["text"] = "Start Download"
        self.download_button["command"] = self.download_button_action
        self.download_button.pack(side="top")

    def create_quit_button(self):
        for torrent in self.torrents:
            for label in self.labels:
                label.pack_forget()
                torrent.state = False
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")


    def create_download_input(self):
        self.download_button = tk.Button(self)
        self.download_button["text"] = "Browse"
        self.download_button["command"] = self.askopenfile
        self.download_button.pack(side="top")

    def download_button_action(self):
        label = self.create_label_info()
        self.labels.append(label)
        torrent = Torrent(self.filepath, label)
        self.torrents.append(torrent)
        torrent.start()

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
        for torrent in self.torrents:
            if torrent.info['progress'] > 0:
                while torrent.info['progress'] < 100:
                    self.progress_bar["maximum"] = 100
                    self.progress_bar["value"] = torrent.info['progress']
                    self.progress_bar.update()
                    print(self.progress_bar['value'])

root = tk.Tk()
app = Application(master=root)
app.mainloop()
