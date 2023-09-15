#Import Pandas and Numpys
import pandas as pd
import numpy as np

#Add table of data
data = {
    'Training': ['Fitness', 'Yoga', 'PR Training', 'Technical training', 'Sports psychologist', 'Ninja class'],
    'Concentrat.': [0, 5, -3, 0, 0, 1],
    'Aggres.': [0, -2, 0, 0, 0, 4],
    'Technical': [0, 0, 0, 5, 0, 0],
    'Stamina': [2, -2, 0, 0, 0, 0],
    'Charisma': [0, 0, 2, 0, 0, 0],
    'Motivat.': [-5, 5, 0, 0, 15, 0],
    'Weight': [-1, 0, 0, 0, 0, 0]
}

#Convert to df
df = pd.DataFrame(data)

#Ask for Inputs
driver_data = input("Input Concentration, Aggression, Technical, Stamina, Charisma, Motivation, Weight")

#Split into list
driver_aspect = driver_data.split(',')

# Create a DataFrame with the user input
user_df = pd.DataFrame([driver_aspect], columns=df.columns[1:])  # Exclude the 'Training' column

#Concentration
if int(driver_aspect[0]) < 219:
     print("Yoga")

if int(driver_aspect[0]) > 219:
    print("CON too high")