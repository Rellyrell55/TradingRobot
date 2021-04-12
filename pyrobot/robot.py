import pandas as pd

from td.client import TDClient
from td.utils import milliseconds_since_epoch

from datetime import datetime
from datetime import time
from datetime import timezone

from typing import List
from typing import Dict
from typing import Union

class PyRobot():
    
    def __init__(self, client_id: str, rediect_uri: str, credentials_path: srt = None, trading_account: str = None) -> None:
        
        self.trading_account: str = trading_account
        self.client_id: str = client_id
        self.rediect_uri: str = rediect_uri
        self.credentials_path: str = credentials_path
        self.session: TDClient = self._create_session()
        self.trades: dict = {}
        self.historical_prices: dict = {}
        self.stock_frame: None