import pandas as pd
import time

"""
Lets test if by providing the isin method with a set its faster than providing it with a list


the set is around 19% faster than a list with 8 values, its worth to use it

dicts on the other hand perform badly.
"""

chicago_data: pd.DataFrame = pd.read_csv("chicago.csv")

def replace_dollar_sign(str_:str)->str:
  

   str_ = str_.replace("$","")

   decimal_index = str_.find(".")

   return str_[:decimal_index]

chicago_data = chicago_data.dropna(subset=["Employee Annual Salary"])
chicago_data["Employee Annual Salary"] = chicago_data["Employee Annual Salary"].apply(replace_dollar_sign).astype(int)

inclusion_list = [100320,70764,90744,88596,70380,91062,96414,84450]
inclusion_set = set([100320,70764,90744,88596,70380,91062,96414,84450])
inclusion_dict = {100320:0, 70764:1}

start_list = time.time()

chicago_data["Employee Annual Salary"].isin(inclusion_list)

end_list = time.time()
print("list operation took", end_list - start_list)


start_set = time.time()

chicago_data["Employee Annual Salary"].isin(inclusion_set)

end_set = time.time()
print("set operation took", end_set - start_set)


start_dict = time.time()

chicago_data["Employee Annual Salary"].isin(inclusion_dict)

end_dict = time.time()
print("dict operation took", end_dict - start_dict)

print(type(inclusion_dict))