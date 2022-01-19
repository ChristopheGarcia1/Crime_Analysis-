#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Running a heierarchecal clustering model on cleaned crime data (not expanded)
# along with food scarcity data


# In[ ]:


import pandas as pd
import hvplot.pandas

from sklearn.decomposition import PCA
from sklearn.cluster import AgglomerativeClustering, KMeans
from sklearn.preprocessing import StandardScaler,OneHotEncoder

import plotly.figure_factory as ff
import plotly.express as px


# In[ ]:


# Loading data
file_path = "Crime_Analysis-/src/resources/crime_data_cleaned.csv"
data = pd.read_csv(file_path)

data.head(10)


# In[ ]:


# Gathering crime data for only the THEFT and BURGLARY related crimes
temp = data['crime_type_x'].unique().tolist()
temp_b = []
for crime in temp:
    if 'THEFT' in crime:
        temp_b.append(crime)
    if 'BURGLARY' in crime:
        temp_b.append(crime)
temp_b


# In[ ]:


data_is_theft = data.isin({'crime_type_x': temp_b})
data = data.loc[data_is_theft['crime_type_x'] == True]
data.reset_index(drop=True, inplace=True)
data


# In[ ]:


data_trimmed = data[['crime_type_x', 'latitude', 'longitude', 'time_occ', 'family_violence', 'wind_speed', 'weather_main', 'temp', 'humidity', 'Avg. Income/H/hold', 'food_deprived_50', 'food_deprived_25', 'food_deprived_10']]
# Transform the string data column
def change_string(member):
    if member == 'Yes' or member == 'Y':
        return 1
    else:
        return 0
    
data_trimmed['food_deprived_50'] = data_trimmed['food_deprived_50'].apply(change_string)
data_trimmed['food_deprived_25'] = data_trimmed['food_deprived_25'].apply(change_string)
data_trimmed['food_deprived_10'] = data_trimmed['food_deprived_10'].apply(change_string)
data_trimmed['family_violence'] = data_trimmed['family_violence'].apply(change_string)


# Generate our categorical variable lists
categorical = data_trimmed.dtypes[data_trimmed.dtypes == "object"].index.tolist()
categorical

# Create a OneHotEncoder instance
enc = OneHotEncoder(sparse=False)

# Fit and transform the OneHotEncoder using the categorical variable list
data_encoded = pd.DataFrame(enc.fit_transform(data_trimmed[categorical]))

# Add the encoded variable names to the dataframe
data_encoded.columns = enc.get_feature_names(categorical)

data_trimmed = data_trimmed.merge(data_encoded,left_index=True, right_index=True)
data_trimmed = data_trimmed.drop(categorical,1)


# In[ ]:


# Looking for the best K
inertia = []
k = list(range(1, 10))

for i in k:
    km = KMeans(n_clusters=i, random_state=0)
    km.fit(data_trimmed)
    inertia.append(km.inertia_)
    
# Define a DataFrame to plot the Elbow Curve using hvPlot
elbow_data = {"k": k, "inertia": inertia}
df_elbow = pd.DataFrame(elbow_data)
elbow_plot = df_elbow.hvplot.line(x="k", y="inertia", title="Elbow Curve", xticks=k)
elbow_plot


# In[ ]:


# Initialize the K-means model
model = KMeans(n_clusters=4, random_state=0)

# Fit the model
model.fit(data_trimmed)

# Predict clusters
predictions = model.predict(data_trimmed)
data_trimmed["class"] = model.labels_

# Standardize data with StandardScalar
data_scaled = StandardScaler().fit_transform(data_trimmed)

# Initialize PCA model
pca = PCA(n_components=3)

# Get two principal components for the iris data.
pca_data = pca.fit_transform(data_scaled)

data_pca = pd.DataFrame(
    data= pca_data, columns= ['principal component 1', 'principal component 2', 'principal component 3']
)

# Add the predicted class columns
data_pca["class"] = model.labels_

data_pca = data_pca.merge(data[['crime_type_x', 'time_occ', 'latitude', 'longitude', 'wind_speed', 'weather_main', 'family_violence', 'zip_code', 'temp', 'Avg. Income/H/hold', 'food_deprived_50', 'food_deprived_25', 'food_deprived_10']],left_index=True, right_index=True)

fig = px.scatter_3d(
    data_pca,
    x="principal component 1",
    y="principal component 2",
    z="principal component 3",
    hover_data=["crime_type_x", "zip_code", 'time_occ', 'temp', 'weather_main', 'Avg. Income/H/hold', 'food_deprived_50', 'food_deprived_25', 'Avg. Income/H/hold', 'latitude', 'longitude'],
    color="class",
    width=1200)
fig.update_layout(legend=dict(x=0,y=1))
fig.show()


# In[ ]:


fig.write_html("file_theft.html")


# In[ ]:




