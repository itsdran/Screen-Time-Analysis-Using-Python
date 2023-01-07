#Imports the necessary Python libraries and the dataset:

import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

data = pd.read_csv("Screentime-App-Details.csv")
print(data.head())

#Checks if dataset has any null values or not
#data.isnull().sum()

#Prints descriptive statistics of the data
#print(data.describe())

#Analyzes the screentime of user; graphs the amount of usage of the apps:
"""figure = px.bar(data_frame=data, 
                x = "Date", 
                y = "Usage", 
                color="App", 
                title="Usage")
figure.show()"""

#Analyzes the number of notifications received from the apps:
"""figure = px.bar(data_frame=data, 
                x = "Date", 
                y = "Notifications", 
                color="App", 
                title="Notifications")
figure.show()"""

#Analyzes the number of times apps were opened:
"""figure = px.bar(data_frame=data, 
                x = "Date", 
                y = "Times opened", 
                color="App",
                title="Times Opened")
figure.show()"""

#Graphs the relationship between the number of notifications and the amount of usage:
figure = px.scatter(data_frame = data, 
                    x="Notifications",
                    y="Usage", 
                    size="Notifications", 
                    trendline="ols", 
                    title = "Relationship Between Number of Notifications and Usage")
figure.show()
