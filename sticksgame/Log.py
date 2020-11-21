import sqlalchemy
import pandas as pd



class Log:
  """
  Class to collect key value entries (aka dict) into a list. 
  """

  d   = None
  log = None

  def __init__(self, **kwargs):
    self.d = dict(kwargs)
    self.log = []

  def append(self, log: dict):
    self.log.append({**self.d, **log})

  def to_df(self, **kwargs) -> pd.DataFrame:
    # prepare data as data.frame
    df = pd.DataFrame(self.log)

    # return data.frame
    return df

      
  

