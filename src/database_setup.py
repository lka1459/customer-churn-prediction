import sqlite3
import pandas as pd
import re
from pathlib import Path

def create_database() -> None:
    """
    Creates the SQLite databe and populates it with the data from the CSV files.
    """
    # Ensures the existence of the "database" directory and creates a connection to the SQLite database
    Path("database").mkdir(parents=True, exist_ok=True)
    conn: sqlite3.Connection = sqlite3.connect("database/olist.db")
    path: str = Path(f"{Path.cwd()}/data/")

    # Regex pattern that extracts table names
    regex: str = r"(?<=olist_)\w+(?=_dataset)"

    # Loop that iterates through CSV files
    for file in path.iterdir():
        datafile: pd.DataFrame = pd.read_csv(f'data/{file.name}')
        match: re.Match = re.search(regex, str(file))

        # Matches the regex pattern to extract each table name
        if match:
            match: str = match.group().replace("_", " ")
        elif file.name == "product_category_name_translation.csv":
            match: str =  "product category name translation"

        # Creates a table in the database for each CSV file
        datafile.to_sql(
                f"{match}",
                conn, 
                if_exists="replace",
                index=False
            )
    
    conn.close()

def read_SQL_Query(filePath: str) -> pd.DataFrame:
    """
    Reads an SQL query and returns the result as a DataFrame.
    """
    # Connects to the SQLite database and reads the SQL query from the specified file path
    conn: sqlite3.Connection = sqlite3.connect("database/olist.db")
    with open(Path(filePath), "r") as file:
        query: str = file.read()

    # Converts the SQL query into a Dataframe
    df: pd.DataFrame = pd.read_sql(query, conn)
    conn.close()

    return df

if __name__ == "__main__":
    create_database()
    read_SQL_Query(r"sql\modeling\churn_features.sql")