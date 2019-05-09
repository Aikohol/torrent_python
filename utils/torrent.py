import libtorrent as lt
import time
import sys

class Torrent(object):
    def __init__(self):
        self.ses = lt.session({'listen_interfaces': '0.0.0.0:8080'})
        self.h = {}
        self.info = {'progress': 0}

    def torrent_start(self, filepath):
        info = lt.torrent_info(filepath)
        self.h = self.ses.add_torrent({'ti': info, 'save_path': '.'})
        s = self.h.status()
        print('starting', s.name)

    def torrent_info(self):
        s = self.h.status()
        while (not s.is_seeding):
            s = self.h.status()

            print('\r%.2f%% complete (down: %.1f kB/s up: %.1f kB/s peers: %d) %s' % (
                s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000,
                s.num_peers, s.state), end=' ')
            self.info.update({'progress': s.progress * 100})
            alerts = self.ses.pop_alerts()
            for a in alerts:
                if a.category() & lt.alert.category_t.error_notification:
                    print(a)

            sys.stdout.flush()

            time.sleep(1)

        print(self.h.name(), 'complete')
