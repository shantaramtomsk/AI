import pandas as pd

# Создание DataFrame

data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}

df = pd.DataFrame(data)

# Операции с данными

df['Age'] = df['Age'] + 1  # Увеличение возраста на 1 год
print(df)