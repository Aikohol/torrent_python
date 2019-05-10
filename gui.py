import tkinter as tk
from tkinter import ttk
import tkinter.filedialog
from utils.torrent import Torrent
import logging

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.filepath = ""
        self.directorypath = ""
        self.master = master
        self.pack(fill='both')
        self.torrents = []
        self.labels= []
        self.bars = []
        self.create_save_button()
        self.create_download_input()
        self.create_downlaod_button()
        self.create_quit_button()

    def create_label_info(self):
        label = tk.Label(self)
        label['bg'] = '#3e3e3e'
        self.labels.append(label)
        return label

    def create_downlaod_button(self):
        self.download_button = tk.Button(self)
        self.download_button["text"] = "Start Download"
        self.download_button["bg"] = '#3aac92'
        self.download_button["width"] = '20'
        self.download_button["command"] = self.download_button_action
        self.download_button.grid(row=2, column=1)

    def create_quit_button(self):
        for torrent in self.torrents:
            for label in self.labels:
                label.pack_forget()
                torrent.state = False
        self.quit = tk.Button(self, bg="#c3767c", text="QUIT",
                              fg="white", width='20',
                              command=self.master.destroy)
        self.quit.grid(row=3, column=1)


    def create_download_input(self):
        self.download_button = tk.Button(self)
        self.download_button["text"] = "Add Torrent..."
        self.download_button["bg"] = '#3aac92'
        self.download_button["width"] = '20'
        self.download_button["command"] = self.askopenfile
        self.download_button.grid(row=1, column=1)

    def download_button_action(self):
        if self.filepath != "":
            label = self.create_label_info()
            self.labels.append(label)
            bar = self.create_progress_bar()
            self.bars.append(bar)
            torrent = Torrent(self.filepath, bar, label, self.directorypath)
            self.torrents.append(torrent)
            torrent.start()

    def askopenfile(self):
        file = tkinter.filedialog.askopenfile(initialdir = "./", title='Select file', filetypes = (("torrent files",".torrent"),("all files",".*")))
        if file:
            self.filepath = file.name

    def create_save_button(self):
        self.save_button = tk.Button(self)
        self.save_button["text"] = "Save as..."
        self.save_button["bg"] = '#3aac92'
        self.save_button["width"] = '20'
        self.save_button["command"] = self.askdirectory
        self.save_button.grid(row=0, column=1)

    def askdirectory(self):
        self.directorypath = tkinter.filedialog.askdirectory()

    def create_progress_bar(self):
        style = ttk.Style()
        style.configure("orange.Horizontal.TProgressbar", foreground='#c3767c', background='#c3767c')
        progress_bar = ttk.Progressbar(self, style='orange.Horizontal.TProgressbar', orient='horizontal',
                                            length=300, maximum=100, mode='determinate')
        return progress_bar

    def run_progressBar(self):
        for torrent in self.torrents:
            if torrent.info['progress'] > 0:
                while torrent.info['progress'] < 100:
                    self.progress_bar["maximum"] = 100
                    self.progress_bar["value"] = torrent.info['progress']
                    self.progress_bar.update()
                    print(self.progress_bar['value'])

root = tk.Tk()
root.title('Torrent')
root.configure(background='#3e3e3e')
app = Application(master=root)
app.configure(background='#3e3e3e')
app.columnconfigure(2,minsize=750, pad=15)
app.columnconfigure(1, pad=15)
app.propagate(0)
app.mainloop()
