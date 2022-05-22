import hashlib

import pandas as pd


def logic(index):
    if index % 2 != 0:
        return True
    return False


# Test case
# data = pd.read_csv("testcase.csv", skiprows=lambda x: logic(x))

# Actual Data
data = pd.read_csv("annual-enterprise-survey-2020-financial-year-provisional-csv.csv", skiprows=lambda x: logic(x))


# print(data.Number)
# print(data.Industry_code_NZSIOC)

result = ""
for row in data.Industry_code_NZSIOC:
    result += str(row)

hashed_object = hashlib.md5(result.encode())
# print(result)
print(hashed_object.hexdigest())
