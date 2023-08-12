import pandas as pd
import matplotlib.pyplot as plt

# Generate hypothetical Uber trip data
data = {
    'trip_id': [1, 2, 3, 4, 5],
    'pickup_time': ['2023-08-11 18:30:00', '2023-08-11 19:15:00', '2023-08-11 20:00:00', '2023-08-11 21:30:00', '2023-08-11 22:45:00'],
    'age': [25, 30, 22, 40, 28],
    'gender': ['Male', 'Female', 'Male', 'Female', 'Male']
}

df = pd.DataFrame(data)

# Convert pickup_time to datetime
df['pickup_time'] = pd.to_datetime(df['pickup_time'])

# Analyze demographic data
age_bins = [18, 25, 35, 45, 55, 65]
age_labels = ['18-24', '25-34', '35-44', '45-54', '55-64']

df['age_group'] = pd.cut(df['age'], bins=age_bins, labels=age_labels, right=False)

# Plot age distribution
age_group_counts = df['age_group'].value_counts().sort_index()
age_group_counts.plot(kind='bar', xlabel='Age Group', ylabel='Number of Trips', title='Age Distribution of Tall Ship Visitors')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Plot gender distribution
gender_counts = df['gender'].value_counts()
gender_counts.plot(kind='bar', xlabel='Gender', ylabel='Number of Trips', title='Gender Distribution of Tall Ship Visitors')
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

