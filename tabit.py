from typing import List
import pandas as pd

def tabit(df: pd.DataFrame, columns: List[str] = None) -> pd.DataFrame:
  


  # handle column input
  if columns is None:
    columns = list(df.columns)

  # do tabulation
  df_tabulated = df.groupby(columns).size().reset_index().rename(columns={0:'.count'})
  
  # return
  return df_tabulated
