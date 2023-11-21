import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('Hello Wilders, welcome to my application!')

st.write("voici la df entière")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_car = pd.read_csv(link)

# Here we use "magic commands":
df_car

st.write("voici la heatmap des correlations pour toutes les régions confundus")
import seaborn as sns
viz_correlation = sns.heatmap(df_car.select_dtypes(include=np.number).corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)
plt.close()

st.write("voici la df par région")
options = list(df_car['continent'].unique())
choix_region = st.selectbox('choisisser la region: ', options)
df_region = df_car[(df_car['continent']==choix_region)]


df_region
st.write("voici la df par région", choix_region)
sns.boxplot(x = df_region['cubicinches']).figure
plt.close()
