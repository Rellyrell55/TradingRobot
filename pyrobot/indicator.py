import operator
import numpy as np
import pandas as pd 

from typing import List
from typing import Dict
from typing import Union
from typing import Optional
from typing import Tuple

from pyrobot.stock_frame import StockFrame

class Indicators():
    
    def __init__(self, price_data_frame: StockFrame) -> None:
        