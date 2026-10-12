import pandas as pd

data = {
    'song': ['Perfect', 'Faded', 'Perfect', 'Believer', 'Faded'],
    'artist': ['Ed Sheeran', 'Alan Walker', 'Ed Sheeran',
               'Imagine Dragons', 'Alan Walker']
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

df = df.drop_duplicates(keep='first')

print("\nAfter Removing Duplicates:")
print(df)