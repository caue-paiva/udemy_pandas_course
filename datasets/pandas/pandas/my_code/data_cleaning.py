import pandas as pd
import os
from typing import Any

DATASET_PATH: str = os.path.join("worldstats.csv")

str__ = " gggg"

def parse_col_names(df: pd.DataFrame)-> pd.DataFrame:
   """
   makes the column names all underscore, removes whitespaces before and after the name and 
   replaces whitespaces between the words in each name with _
   
   OBS: Returns a DF View
   """
   def lower_case_and_underline(col_name:str)->str:
      return col_name.lower().removeprefix(" ").removesuffix(" ").replace(" ", "_")

   df.columns = [lower_case_and_underline(x) for x in  df.columns] 
   return df

def group_repeated_keys(se: pd.Series)-> pd.Series:
   unique_keys:dict[Any,Any] = {}

   for index, label in enumerate(se.index):
      #creates a dict key and assigns it a zero val if it doesnt exist
      unique_keys.setdefault(label, 0)
      #adds the value associated with that key to the dict val
      unique_keys[label] +=  series.iloc[index]
   
   #creates a new series with the unique vals
   return pd.Series(unique_keys)

def fillna_placehold_dtype(df :pd.DataFrame)->pd.DataFrame:
   """
   fills DF missing/NaN values with the correct dtype placeholder for that column
   
   """

   #dict mapping each dtype to its placeholder val
   dtype_std_val_map: dict[str,Any] = {
      "object" : "unknown",
      #"datetime64[ns]": , see what kind of placeholder val would fit here
      "float64" : 0.0,
      "int64": 0
   }   

   #creates a series mapping each column to a correct placeholder based on dtype
   dtype_column_map:pd.Series = df.dtypes.map(dtype_std_val_map)

   return df.fillna(dtype_column_map)
  

raw_df: pd.DataFrame = pd.read_csv(DATASET_PATH,index_col="country")
series:pd.Series = raw_df["GDP"].squeeze()

series_grouped = group_repeated_keys(series)


print(series_grouped)

#parsed_df = parse_col_names(raw_df).copy()
#parsed_df = parsed_df.dropna(axis=0)
#print(parsed_df)
