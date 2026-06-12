import sqlite3
import pandas as pd
import re
from pathlib import Path

def create_database() -> None:
    conn: sqlite3.Connection = sqlite3.connect("database/olist.db")
    path: str = Path(f"{Path.cwd()}/data/")

    regex: str = r"(?<=olist_)\w+(?=_dataset)"

    for file in path.iterdir():
        datafile: pd.DataFrame = pd.read_csv(f'data/{file.name}')
        match: re.Match = re.search(regex, str(file))

        if match:
            match: str = match.group().replace("_", " ")
        elif file.name == "product_category_name_translation.csv":
            match: str =  "product category name translation"

        datafile.to_sql(
                f"{match}",
                conn, 
                if_exists="replace",
                index=False
            )
    
    conn.close()

def read_SQL_Query(filePath) -> pd.DataFrame:
    conn: sqlite3.Connection = sqlite3.connect("database/olist.db")
    with open(Path(filePath), "r") as file:
        query: str = file.read()

    df: pd.DataFrame = pd.read_sql(query, conn)
    conn.close()

    return df