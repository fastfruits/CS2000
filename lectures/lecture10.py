"""Lecture 10 Notes"""

import pandas as pd
import numpy as np
import array
from typing import Any

v1 = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print(v1)
print(f"Shape: {v1.shape}")
print(v1.tolist)

range_step = np.arange(0, 10, 2)

a = np.arange(6)
a.reshape(2, 3)
print(f"Reshaped to 2x3 \n{a}")

transposed = a.transpose()
print(f"Transposed \n{transposed}")

flatten = a.flatten()
print(f"Flattened: \n{flatten}")

nums: np.ndarray[Any, np.dtype[np.int64]] = np.random.randint(10, 20, size=(4, 5))
print(nums)

df = pd.DataFrame(
    {'Person': ['Elephant', 'Cat'],
     'Age': [13, 10]})

print(df)

names = df['Person']
print(f"Person: {names}")

name_list = list(df['Person'])
print(f"As list: {name_list}")

first_name = df['Person'][0]
print(first_name)

new_rows = pd.DataFrame({
    'Person': ['Sally', 'Patty'],
    'Age': [13, 5]
})

expanded_db = pd.concat([df, new_rows], ignore_index=True)
print(expanded_db)
