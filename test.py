# def get_full_name(first_name:str,last_name:str):
#     all_names = first_name + last_name
#     return all_names
# print (get_full_name("Joyce" ,"Ndichu"))

from typing import List


def process_items(items: List[str]):
    for item in items:
        print(item)
print(process_items["Joyce","Ndichu"])