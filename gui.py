import tkinter as tk
import tkinter.filedialog
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
        torrent_start(self.filepath)

    def askopenfile(self):
        file = tkinter.filedialog.askopenfile(initialdir = "./", title='Select file', filetypes = (("torrent files",".torrent"),("all files",".*")))
        self.filepath = file.name


root = tk.Tk()
app = Application(master=root)
app.mainloop()
