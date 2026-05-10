import pandas as  pd

try:
    path = r'C:\Users\hp\Downloads\Naukri Automation\naukri.xlsx'
    
    df = pd.read_excel(path, sheet_name= "Naukri")
    
    print(f' Cleaning Process Started.........')
    
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
    df.info()
    
    # Creating Year, month, Day, Month Name, day Name column
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    df['Month Name'] = df['Date'].dt.month_name()
    df['Day'] = df['Date'].dt.day
    df['Day Name'] = df['Date'].dt.day_name()
    
    # Renaming the columns
    df.rename(columns = {
        'Subuser': 'Users',
        'Resume Downloaded in Word' : 'CV Downloaded',
        'Unique CV Views or View Phone number/Call candidate': 'Unique CV View'
        
    }, inplace = True)
    
    
    # Spilting users into two columns fullname and email
    df['FullName'] = df['Users'].str.split("|").str[0].str.strip().str.title()
    df['Email'] = df['Users'].str.split("|").str[1].str.strip()
    
    # Drop column Users
    df.drop("Users",axis = 1, inplace = True) # axis = 0 = row & axis = 1 = columns
    
    # Removing all white space from column names
    df.columns = df.columns.str.strip()
    
    # Re- Shuffle the columns
    
    df = df[
        ["Date", "FullName", "Email", "Team Name", "CV Downloaded",
         "NVites", "Unique CV View", "Year", "Month",
         "Month Name", "Day", "Day Name"]
    ]
    
    # Replace special character(.) with (space)
    df["FullName"] = df["FullName"] .str.replace(".", " ", regex=False)\
        .str.replace("Ankush T", "Ankush Tedi", regex=False)\
        .str.replace("Vansh","Vansh Singh")\
        .str.strip()
    
        # Filled Missing values to "No data provided"
    df['Team Name'] = df['Team Name'].fillna("No Data Provided")
    
        # Adding total of numeric columns
    total_row = pd.DataFrame({
        "Date": ["Total"],
        "FullName": [""],
        "Email": [""],
        "Team Name": [""],
        "CV Downloaded": [df["CV Downloaded"].sum()],
        "NVites": [df["NVites"].sum()],
        "Unique CV View": [df["Unique CV View"].sum()],
        "Year": [""],
        "Month": [""],
        "Month Name": [""],
        "Day": [""],
        "Day Name": [""]
    })
    # Concat two data frame df and total_row
    df = pd.concat([df, total_row], ignore_index=True)
    
    # Save Cleaned File
    
    df.to_excel("Cleaned_Data.xlsx", sheet_name = "Cleaned_Base_Data", index = False)
    
    # print status Done
    
    print(f' All Transformation has been Done 100% ')

except FileNotFoundError:
    print("File not found. Please check the file path.")

except KeyError as e:
    print(f"Column missing in dataset: {e}")

except Exception as e:
    print(f"Unexpected error occurred: {e}")