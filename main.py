import pandas as pd  # Importing pandas for data manipulation
from sqlalchemy import create_engine  # Importing SQLAlchemy to handle database connections
from sqlalchemy import text  # Importing SQLAlchemy's text module for executing raw SQL queries



# Load CSV files
df1 = pd.read_csv("Country_Mapping_Table.csv")  # Load country mapping data into a DataFrame
df2 = pd.read_csv("Country_Table.csv")  # Load country details into a DataFrame
df3 = pd.read_csv("Genre_Mapping_Table.csv")  # Load genre mapping data into a DataFrame
df4 = pd.read_csv("Genre_Table.csv")  # Load data into a DataFrame
df5 = pd.read_csv("Main_Table.csv", encoding="ISO-8859-1")  # Load data into a DataFrame

# Displaying the summary of first DataFrame
print(df1.info())
print(df1.describe())
print(df1.head())

# Renaming the columns:
df1.columns = ["Sl_No","IMDB_ID", "Country_ID"]
df2.columns = ["Country_Code", "Country_ID"]
df3.columns = ["Sl_No","IMDB_ID", "Genre_ID"]
df4.columns = ["Genre", "Genre_ID"]
df5.columns = ["Title","Type", "Release_Year", "IMDB_ID", "IMDB_Avg_Rating", "IMDB_Num_of_Votes"]

# Data Cleaning:
df1.isnull().sum()
# df1.drop("Sl_No",axis=1, inplace = True)

df1.duplicated().sum()
df1.reset_index().duplicated().sum()

df1.drop_duplicates(inplace = True)
df1.duplicated().sum()

df1.dropna(inplace = True)
df1.isnull().sum()
df1.loc[: ,"IMDB_ID"] = df1["IMDB_ID"].str.strip()

# Second Table:
print(df2.info())
print(df2.describe())
print(df2.head())
df2["Country_Code"].unique()

df2.isnull().sum()
df2.dropna(inplace = True)
df2.isnull().sum()

df2.duplicated().sum()
df2.drop_duplicates(inplace = True)

df2.loc[: ,"Country_Code"] = df2["Country_Code"].str.strip()

# Third Table:
print(df3.info())
print(df3.describe())
print(df3.head())

# df3.drop("Sl_No",axis = 1,inplace = True)

df3.isnull().sum()
df3.dropna(inplace = True)

df3.duplicated().sum()
df3.drop_duplicates(inplace = True)

# Fourth Table:
print(df4.info())
print(df4.describe())
print(df4.head())

df4.isnull().sum()

df4.duplicated().sum()

df4.loc[: ,"Genre"] = df4["Genre"].str.strip()

# Fifth Table:
print(df5.info())
print(df5.describe())
print(df5.head())

df5.isnull().sum()
df5.dropna(inplace = True)

df5.duplicated().sum()
df5.loc[: ,"Title"] = df5["Title"].str.strip()

df5["Release_Year"] = df5["Release_Year"].astype(int)

df5["IMDB_Num_of_Votes"] = df5["IMDB_Num_of_Votes"].astype(int)

# Define the SQLAlchemy engine
engine = create_engine('mysql+mysqlconnector://root:mysqlpraj$0205@localhost:3306/ByteBlossom_048')  # Create an SQLAlchemy engine for database operations

# Upload each DataFrame to a MySQL table
df1.to_sql('country_mapping', con=engine, if_exists='replace', index=False)
df2.to_sql('country', con=engine, if_exists='replace', index=False)
df3.to_sql('genre_mapping', con=engine, if_exists='replace', index=False)
df4.to_sql('genre', con=engine, if_exists='replace', index=False)
df5.to_sql('movie_data', con=engine, if_exists='replace', index=False)


# Verification query
with engine.connect() as connection:
result = connection.execute(text("SELECT COUNT(*) FROM country_mapping"))  # Using raw SQL queries for database interactions
    count = result.scalar()  # Use .scalar() to get a single value from the result
    print(count)

# Close the engine
engine.dispose()





































