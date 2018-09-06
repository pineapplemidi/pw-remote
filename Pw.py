from __future__ import absolute_import, print_function, unicode_literals
import Live
import io
import json
# import sys

# sys.path.append('/Library/Frameworks/Python.framework/Versions/2.7/
# lib/python2.7/site-packages/')

# from OSC import OSCClient, OSCMessage

from _Framework.ControlSurface import ControlSurface
from _Framework.SessionComponent import SessionComponent
from _Framework.ChannelStripComponent import ChannelStripComponent


class Pw(ControlSurface):

    def __init__(self, c_instance):
        super(Pw, self).__init__(c_instance)
        with self.component_guard():
            self.log('Setup Config')
            config = self._open_config()
            self._setup_session(config['width'], config['height'])
            self._setup_strip()
            self._track_clip_slots_info()

    def _open_config(self):
        with open('/users/berry/config.json') as f:
            data = json.load(f)
            self.log(json.dumps(data))
            return json.loads(json.dumps(data))

    def _track_clip_slots_info(self):
        track = self.session.tracks_to_use()[0]
        # self.log(json.dumps(dir(track.clip_slots[0].clip.name)))
        self.log(track.clip_slots[0].clip.name)

    def _setup_session(self, width, height):
        self.log('Setup Session')
        self.session = SessionComponent(width, height)
        self.session.set_offsets(0, 0)
        self.set_highlighting_session_component(self.session)

    def _setup_strip(self):
        self.log('Setup Strip')
        self.strip = ChannelStripComponent()
        self._update_strip()

    def _update_strip(self):
        self.strip.set_track(self.session.tracks_to_use()[0])

    def log(self, message):
        log_str = 'LOG: ' + message + '\n'
        with io.open(
            "/users/berry/somefile.txt",
                mode='w', encoding='utf-8') as f:
            f.write(log_str)
            f.close()
