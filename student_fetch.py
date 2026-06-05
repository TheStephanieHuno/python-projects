import pandas as pd
#  to enable it read the csv file  
df = pd.read_csv('students_demo.csv')
# load the data into the data frame and name  it df
# it is lso teh table created after reading the csv   file 

print ("====CSV FILE SUMMARY=====")
print ("Number of rows: ", len(df))
print ("Number of columns: ", len(df.columns))

for col in df.columns:
    print("-", col)

print("\nBasic Statistics:")

numeric = df.select_dtypes(include="number")

for col in numeric:
   print("Average Score:", df["Score"].mean())
   print("Highest Score:", df["Score"].max())
   print("Lowest Score:", df["Score"].min())


    

print("\nPreview:")
print(df.head())