import json
# import traceback
# import ccxt
from datetime import datetime, timedelta
import time
# import pytz
from datetime import timedelta
# from tqdm.auto import tqdm
import matplotlib.pyplot as plt
# from itertools import accumulate
import matplotlib
import pandas as pd
import numpy as np
import requests 
# import ast


# Pull Fear and Greed daily Data (Returned much quicker on repeat, check and test headers)
endpoint = 'https://api.alternative.me/fng/?limit=3000&format=json&date_format=us'
fg_data =  requests.get(endpoint).json()


# Individual value for fear and greed
endpoint_individual = 'https://api.alternative.me/fng/?&format=json&date_format=us'
fg_data_individual = requests.get(endpoint_individual).json()
fg_data_individual['data'][0]


value_classification = fg_data_individual['data'][0]['value_classification']


if value_classification == "Fear" or "Greed" or "Extreme Greed":
    print(f"DON'T BUY")
    
elif value_classification == "Extreme Fear":
    print(f"BUY") 
    



