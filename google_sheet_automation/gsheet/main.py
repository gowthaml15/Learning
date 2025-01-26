import pygsheets
import pandas as pd 
import sqlite3
from database_connection.sqlite_db import SQLite


def main():
    # set-up configuration 
    gc = pygsheets.authorize(service_account_file = 'client_secret.json')

    # default sheet name
    sheet_name = 'testing_automation'

    #Check if the sheet is already present or create one
    sh = gc.open(sheet_name)
    try:
        print("Already present")
        spreadsheet = gc.open(sheet_name)
    except pygsheets.SpreadsheetNotFound:
        print("---")
        spreadsheet = gc.create(sheet_name)
    
    # Check for a specific worksheet (sheet) name and create it if not present
    worksheet_name = "test"
    try:
        worksheet = spreadsheet.worksheet_by_title(worksheet_name)
        print(f"Worksheet '{worksheet_name}' already exists.")
    except pygsheets.WorksheetNotFound:
        worksheet = spreadsheet.add_worksheet(worksheet_name)
        print(f"Worksheet '{worksheet_name}' created.")
    
    # Get the data and load it as a pandas
    sheet_df = worksheet.get_as_df()
    
    # Connect to SQLite database (creates a new file if it doesn't exist)
    query = "SELECT * FROM users"
    sql = SQLite("user_info.db",query)

    # Query the database and load data into a Pandas DataFrame
    database_df = sql.get_query_output()

    # Custom logic to concat and check whether there is any duplicate data
    combined_df = pd.concat([sheet_df,database_df])

    unique_df = combined_df.drop_duplicates(subset=['user_id','name','age'],keep='first')

    # Push the data to sheets
    worksheet.set_dataframe(unique_df, (1, 1))  # Start from cell A1
    print("Data successfully written to Google Sheet!")
    


if __name__=='__main__':
    main()