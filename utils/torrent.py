import libtorrent as lt
import time
import sys
from threading import Thread, active_count
import logging

class Torrent(Thread):
    def __init__(self, filepath,bar, label, directorypath):
        super(Torrent, self).__init__()
        self.ses = lt.session({'listen_interfaces': '0.0.0.0:8080'})
        self.filepath = filepath
        if directorypath:
            self.directorypath = directorypath
        else:
            self.directorypath = '.'
        self.h = {}
        self.progress = 0
        self.text = ""
        self.state = True
        logging.warning("label")
        logging.warning(label)
        self.label = label
        self.bar = bar

    def run(self):
        info = lt.torrent_info(self.filepath)
        self.h = self.ses.add_torrent({'ti': info, 'save_path': self.directorypath + '/'})
        s = self.h.status()
        print('starting', s.name)

        s = self.h.status()
        self.label.grid(row=active_count() - 1, column=2)
        self.bar.grid(row=active_count() - 1, column=3)
        
        while (not s.is_seeding and self.state):
            s = self.h.status()

            print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % (
                s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000,
                s.num_peers, s.state), end=' ')

            self.text = '\r'+ s.name+": " +'%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % (
                s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000,
                s.num_peers, s.state)
            self.progress = s.progress * 100
            alerts = self.ses.pop_alerts()
            for a in alerts:
                if a.category() & lt.alert.category_t.error_notification:
                    print(a)
            if self.state:
                self.label["text"] = self.text
                self.bar["value"] = self.progress
                self.bar.update()
            sys.stdout.flush()

            time.sleep(1)

        print(self.h.name(), 'complete')
    # def torrent_start(self, filepath):
    #     info = lt.torrent_info(filepath)
    #     self.h = self.ses.add_torrent({'ti': info, 'save_path': '.'})
    #     s = self.h.status()
    #     print('starting', s.name)
    #
    # def torrent_info(self):
    #     s = self.h.status()
    #     while (not s.is_seeding):
    #         s = self.h.status()
    #
    #         print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % (
    #             s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000,
    #             s.num_peers, s.state), end=' ')
    #         self.info.update({'progress': s.progress * 100})
    #         alerts = self.ses.pop_alerts()
    #         for a in alerts:
    #             if a.category() & lt.alert.category_t.error_notification:
    #                 print(a)
    #
    #         sys.stdout.flush()
    #
    #         time.sleep(1)
    #
    #     print(self.h.name(), 'complete')
