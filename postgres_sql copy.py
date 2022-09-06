#Importing libraries
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine

#Creating a connection engine object
engine = create_engine("postgresql+psycopg2://postgres:Joyce4390@localhost:5432/student_grades.db", pool_recycle=-1)
#Checking connection
print("Engine successfully created!") 

#Loading tha csv file into postgresql from python using the pandas.to_sql() function
df = pd.read_csv('studentgrades.csv', index_col=0)
print(df)

#Saving data from the dataframe to postgres table
df.to_sql('students_grades', con=engine, if_exists='append', index=False)
print("Dataframe loaded successfully!")