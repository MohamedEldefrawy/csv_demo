import hashlib

import pandas as pd


# Skip odd rows
def logic(index):
    if index % 2 != 0:
        return True
    return False


# Read CSV file
data = pd.read_csv("annual-enterprise-survey-2020-financial-year-provisional-csv.csv", skiprows=lambda x: logic(x))


# concate result in one line
result = ""
for row in data.Industry_code_NZSIOC:
    result += str(row)

# hash result
hashed_object = hashlib.md5(result.encode())

print(hashed_object.hexdigest())
