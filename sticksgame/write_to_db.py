import sqlalchemy
import tenacity


@tenacity.retry(wait = tenacity.wait.wait_fixed(0.03) + tenacity.wait.wait_random(0.01, 0.03), stop = tenacity.stop.stop_after_delay(2))
def write_to_db(df, db_name, table_name, **kwargs):
  """
  write table to SQLite database

  Args:
      df (pd.DataFrame): 
      db_name ([type]): [description]
      table_name (str): Name of the table to store info in. 
  """

  for key, value in kwargs.items(): 
    df[key] = value


  # write to database
  db = sqlalchemy.create_engine("sqlite:///" + db_name)
  df.to_sql(table_name, con=db, if_exists="append")

