import pandas as pd

data = {
    'date': ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday',
             'Sunday'],
    'tickets_sold': [100, 120, 110, 130,
                     115, 125, 500]
}

df = pd.DataFrame(data)

mean = df['tickets_sold'].mean()
std = df['tickets_sold'].std()

df['z_score'] = (
    df['tickets_sold'] - mean
) / std

outliers = df[df['z_score'].abs() > 2]

print("Mean:", mean)
print("Standard Deviation:", std)

print("\nData with Z-Scores:")
print(df)

print("\nOutliers:")
print(outliers)