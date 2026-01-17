import pandas as pd

mydict = [
    {'branch': 'COE', 'cgpa': '9.0', 'name': 'Nikhil', 'year': '2'},
    {'branch': 'COE', 'cgpa': '9.1', 'name': 'Sanchit', 'year': '2'},
    {'branch': 'IT', 'cgpa': '9.3', 'name': 'Aditya', 'year': '2'},
    {'branch': 'SE', 'cgpa': '9.5', 'name': 'Sagar', 'year': '1'},
    {'branch': 'MCE', 'cgpa': '7.8', 'name': 'Prateek', 'year': '3'},
    {'branch': 'EP', 'cgpa': '9.1', 'name': 'Sahil', 'year': '2'}
]

# Create a DataFrame from the list of dictionaries
df = pd.DataFrame(mydict)

# Write the DataFrame to a CSV file
df.to_csv('output.csv', index=False)

data = pd.read_csv('output.csv')
print(data)