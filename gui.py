import tkinter as tk
from utils.torrent import torrent_start

path = "/home/aikoho/Documents/resources/torrent/MX-18.2_x64.torrent"

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_downlaod_button()
        self.create_download_input()

    def create_downlaod_button(self):
        self.download_button = tk.Button(self)
        self.download_button["text"] = "Hello World\n(click me)"
        self.download_button["command"] = self.download_button_action
        self.download_button.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def create_download_input(self):
        pass

    def download_button_action(self):
        torrent_start(path)

    def askopenfile(self):
        pass

root = tk.Tk()
app = Application(master=root)
app.mainloop()