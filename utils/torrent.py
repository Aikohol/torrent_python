import libtorrent as lt
import time
import sys
from threading import Thread
import logging


class Torrent(object):
    def __init__(self):
        self.is_downloading = True
        self.ses = {}
        self.h = {}
        self.name = ""
        self.progress = 0
    def load_torrent(self, filepath, directory):
        self.ses = lt.session({'listen_interfaces': '0.0.0.0:8080'})

        info = lt.torrent_info(filepath)
        self.h = self.ses.add_torrent({'ti': info, 'save_path': directory + '/'})
        self.name = filepath


    def execute_torrent(self):
        s = self.h.status()
        print('starting', s.name)
        logging.warning(s)
        while (not s.is_seeding and self.is_downloading):
            s = self.h.status()

            print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % (
                s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000,
                s.num_peers, s.state), end=' ')
            self.progress = s.progress
            alerts = self.ses.pop_alerts()
            for a in alerts:
                if a.category() & lt.alert.category_t.error_notification:
                    print(a)

            sys.stdout.flush()

            time.sleep(1)

        print(self.h.name(), 'complete')

