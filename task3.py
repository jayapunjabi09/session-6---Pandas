import pandas as pd

data = {
    'order_id': [1, 2, 3, 4, 5, 6, 7, 8],
    'order_amount': [200, 250, 300, 350,
                     400, 450, 500, 5000]
}

df = pd.DataFrame(data)

Q1 = df['order_amount'].quantile(0.25)
Q3 = df['order_amount'].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[
    (df['order_amount'] < lower) |
    (df['order_amount'] > upper)
]

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)

print("\nOutliers:")
print(outliers)