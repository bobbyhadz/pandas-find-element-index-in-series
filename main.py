# Pandas: Find an element's Index in Series

import pandas as pd

series = pd.Series([1, 3, 5, 7, 9, 11], index=[0, 1, 2, 3, 4, 5])

# 2    5
# dtype: int64
print(series[series == 5])

print('-' * 50)

index_of_5 = series[series == 5].index[0]
print(index_of_5)  # 👉️ 2