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

# Define the aspect ranking (higher values are better)
aspect_ranking = {
    'Concentrat.': 0,
    'Stamina': 1,
    'Weight': 2,
    'Technical': 3,
    'Aggres.': 4,
    'Motivat.': 5,
    'Charisma': 6,
}

# Sort the aspects by ranking (ascending order)
sorted_aspects = sorted(aspect_ranking.keys(), key=lambda x: aspect_ranking[x])

# Track when each aspect reaches its target
concentration_met = False
stamina_met = False
weight_met = False
technical_met = False
aggression_met = False
motivation_met = False

# Training
for aspect in sorted_aspects:
    value = int(driver_aspect[aspect_ranking[aspect]])
    if aspect == 'Concentrat.':
        if value >= 219:
            concentration_met = True
        else:
            print("Yoga")
    elif aspect == 'Stamina':
            if value >= 109:
                stamina_met = True
            elif stamina_met:
                print("Fitness")
            elif aspect == 'Weight':
                if value < 81:
                    weight_met = True
                elif weight_met:
                    print("Fitness")
                elif aspect == 'Technical':
                    if value > 149:
                        technical_met = True
                elif technical_met:
                    print("Technical")
                elif aspect == 'Aggres.':
                        if value >= 49:
                            aggression_met = True
                        elif aggression_met:  # Corrected variable name here
                            print("Ninja")
                        elif aspect == 'Motivat.':
                            motivation_met = True

# If all high enough then maximize top 3
if concentration_met and stamina_met and weight_met and technical_met and aggression_met and motivation_met:
    print("Yoga")
