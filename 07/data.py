import pandas as pd 
import numpy as np
from datetime import datetime

def parse_news_data(file):
    with open(file, 'r') as File:
        data = File.read()

        articles = data.strip().split("Title:")

        rows = []
        for article in articles[1:]:
            lines = article.strip().split('\n')
            title = lines[0].strip()
            author = lines[1].split("Author")[1].strip()
            published_at = lines[2].split("Published At:")[1].strip()
            source = lines[3].split("Source:")[1].strip()
            url = lines[4].split("URL:")[1].strip()

            rows.append({
                'Title': title,
                "Author": author,
                'Published At': published_at,
                'Source': source,
                'URL': url
            })

        df = pd.DataFrame(rows)

        df['Published At'] = pd.to_datetime(df['Published At'], errors='coerce')
        return df
    
df_nasa = parse_news_data('Nasa.txt')

print("Parsed data: ")
print(df_nasa)

print("\n Missing Values")
print(df_nasa.isnull().sum())

df_nasa['Author'].fillna('Unknown', inplace=True)

df_nasa.set_index(['Author', 'Published At'], inplace=True)

print("\n Data with Hierachica Indexing : ")
print(df_nasa)

aggre_data = df_nasa.groupby('Author').agg({
    'Title': 'count',
    'Source': pd.Series.nunique
})

print("\n Aggregated Data: ")
print(aggre_data)