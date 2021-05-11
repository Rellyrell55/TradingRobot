from datetime import datetime

from typing import Union
from typing import Optional
from typing import List

class Trade():

    def __init__(self):

        self.order = {}
        self.trade_id = ""

        self.side = ""
        self.side_opposite = ""
        self.enter_or_exit = ""
        self.enter_or_exit_opposite = ""

        self._order_response = {}
        self._triggered_add = False
        self._multi_leg = False