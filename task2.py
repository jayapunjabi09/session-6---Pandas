import pandas as pd

data = {
    'product_id': [101, 102, 101, 103, 102, 104],
    'user_id': [1, 2, 1, 3, 2, 4],
    'rating': [5, 4, 5, 3, 4, 5],
    'review_text': ['Good', 'Nice', 'Good',
                    'Average', 'Nice', 'Excellent']
}

df = pd.DataFrame(data)

duplicates = df.duplicated(
    subset=['product_id', 'user_id'],
    keep=False
)

print("Duplicate Reviews:")
print(df[duplicates])

print("\nNumber of Duplicate Reviews:")
print(duplicates.sum())