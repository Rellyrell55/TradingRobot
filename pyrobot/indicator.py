import operator
import numpy as np
import pandas as pd 

from typing import Any
from typing import List
from typing import Dict
from typing import Union
from typing import Optional
from typing import Tuple

from pyrobot.stock_frame import StockFrame

class Indicators():
    
    def __init__(self, price_data_frame: StockFrame) -> None:
        
        self._stock_frame: StockFrame = price_data_frame
        self._price_groups = self._stock_frame.symbol_groups
        self._current_indicators = {}
        self._indicators_signals = {}
        self._frame = self._stock_frame
        
    def set_indicator_signals(self, indicator: str, buy: float, sell: float, condition_buy: Any, condition_sell: Any) -> None:
        
        if indicator not in self._indicators_signals:
            self._current_indicators[indicator] = {}
            
        self._indicators_signals[indicator]['buy'] = buy
        self._indicators_signals[indicator]['sell'] = sell
        self._indicators_signals[indicator]['buy_operator'] = condition_buy
        self._indicators_signals[indicator]['sell_operator'] = condition_sell
            
    def get_indicator_signals(self, indicator: Optional[str]) -> Dict:
        
        if indicator and indicator in self._indicators_signals:
            return self._indicators_signals[indicator]
        else: 
            return self._indicators_signals
        
    @property
    def price_data_frame(self) -> pd.DataFrame:
        
        return self._frame
    
    @price_data_frame.setter
    def price_data_frame(self, price_data_frame: pd.DataFrame) -> None:
       
        self._frame = price_data_frame
        
    def change_in_price(self) -> pd.DataFrame:
        
        locals_data = locals()
        del locals_data['self']
        
        column_name = 'change_in_price'
        self._current_indicators[column_name] = {}
        self._current_indicators[column_name]['args'] = locals_data
        self._current_indicators[column_name]['funk'] = self.change_in_price
        
        self._frame[column_name] = self._price_groups['close'].transform(
            lambda x: x.diff()
        )
        
    
