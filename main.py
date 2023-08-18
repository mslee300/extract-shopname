import pandas as pd
from collections import Counter

# Read the CSV file
file_name = 'input.csv'
data = pd.read_csv(file_name)

# Extract the '세부 카테고리' column and tokenize it
words = []
for cell_content in data['세부 카테고리']:
    words.extend(str(cell_content).split())

# Count the frequency of each word and create a ranking
word_counts = Counter(words)
ranking = {word: rank for rank, (word, _) in enumerate(word_counts.most_common())}

# Create a new column with the ranking of each word in the '세부 카테고리' column
data['ranking'] = data['세부 카테고리'].apply(lambda x: min(ranking[word] for word in str(x).split() if word in ranking) if any(word in ranking for word in str(x).split()) else float('inf'))

# Sort the DataFrame by the ranking
data = data.sort_values(by='ranking')

# Drop the ranking column as it's not needed in the output
data.drop(columns=['ranking'], inplace=True)

# Save the reordered DataFrame to a new CSV file
output_file_name = 'output.csv'
data.to_csv(output_file_name, index=False)

print(f"Analysis complete! The file has been reordered by the frequency of words in the '세부 카테고리' column and saved as '{output_file_name}'.")

