from _Framework.ChannelStripComponent import ChannelStripComponent
from _Framework.SessionComponent import SessionComponent


class Player(ChannelStripComponent):

    def __init__(self):
        self.session = self._setup_session()
        super(Player, self)
