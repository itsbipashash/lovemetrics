import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Parse chat
pattern = r'(\d{2}/\d{2}/\d{4}),\s(\d{2}:\d{2})\s-\s([^:]+):\s(.+)'
messages = []

with open('chat.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for line in lines:
    match = re.match(pattern, line.strip())
    if match:
        date, time, author, message = match.groups()
        messages.append({
            'date': date,
            'time': time,
            'author': author.strip(),
            'message': message.strip()
        })

df = pd.DataFrame(messages)
df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
df['hour'] = df['time'].str[:2].astype(int)
df['month'] = df['date'].dt.to_period('M')
df['word_count'] = df['message'].apply(lambda x: len(x.split()))

print("Total messages:", len(df))
print(df['author'].value_counts())

# Chart 1 - Peak hours
plt.figure(figsize=(12,5))
df.groupby('hour')['message'].count().plot(kind='bar', color='pink')
plt.title('What time do you both talk most? 🌙')
plt.xlabel('Hour of Day')
plt.ylabel('Messages')
plt.tight_layout()
plt.savefig('peak_hours.png')
print("✅ Chart saved as peak_hours.png!")

# Chart 2 - Messages per month
plt.figure(figsize=(12,5))
df.groupby('month')['message'].count().plot(kind='bar', color='purple')
plt.title('Most active months 💕')
plt.xlabel('Month')
plt.ylabel('Messages')
plt.tight_layout()
plt.savefig('monthly_activity.png')
print("✅ Chart saved as monthly_activity.png!")

# Chart 3 - Who texts more (pie chart)
plt.figure(figsize=(6,6))
df['author'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['pink','purple'])
plt.title('Who texts more? 💬')
plt.tight_layout()
plt.savefig('who_texts_more.png')
print("✅ Chart saved as who_texts_more.png!")