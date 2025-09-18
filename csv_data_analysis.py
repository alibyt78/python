import pandas as pd

# Create sample CSV
df = pd.DataFrame({
    'Name': ['Ali', 'Sara', 'Reza'],
    'Score': [85, 90, 78]
})
df.to_csv('sample.csv', index=False)

# Read and analyze
csv_df = pd.read_csv('sample.csv')
print("Average Score:", csv_df['Score'].mean())
