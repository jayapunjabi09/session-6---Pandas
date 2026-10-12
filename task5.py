import pandas as pd

data = {
    'transaction_id': [1, 2, 3, 4, 5, 6, 7],
    'amount': [100, 150, 200, 250, 300, 350, 5000]
}

df = pd.DataFrame(data)

def find_outliers(df, column):
    mean = df[column].mean()
    std = df[column].std()

    z_score = (df[column] - mean) / std

    return df[z_score.abs() > 2]

result = find_outliers(df, 'amount')

print("Outlier Transactions:")
print(result)