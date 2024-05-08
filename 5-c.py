import pandas as pd

# Row Selection
data = pd.read_csv("C:\\Users\\danda\\OneDrive\\Documents\\Desktop\\CSM A\\nba.csv", index_col="Name")
first_row = data.loc["Avery Bradley"]
second_row = data.loc["R.J. Hunter"]
print("First row:\n", first_row, "\n\nSecond row:\n", second_row)

# Row Addition
df = pd.read_csv("C:\\Users\\danda\\OneDrive\\Documents\\Desktop\\CSM A\\nba.csv", index_col="Name")
new_row = pd.DataFrame({'Team': 'Engineering', 'Number': 3, 'Position': 'PG', 'Age': 33, 'Height': '6-2', 'Weight': 189, 'College': 'AITAM', 'Salary': 99999}, index=['Aditya'])
df = pd.concat([new_row, df]).reset_index(drop=True)
print("DataFrame after adding a new row:\n", df.head())

# Row Deletion
data.drop(["Avery Bradley", "John Holland", "R.J. Hunter"], inplace=True)
print("DataFrame after deleting specified rows:\n", data)
