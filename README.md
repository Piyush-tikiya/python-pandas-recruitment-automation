# ***Automated-Recruitment-Data-Pipeline***

### ***Project Overview***
```
- This project automates the daily cleaning and transformatiIon of recruitment reports downloaded from Naukri in Excel format using Python and Pandas.
- The pipeline processes raw recruitment data, performs multiple cleaning and transformation steps, and generates a structured, analysis-ready Excel output file for reporting and dashboarding purposes.
- The automation reduces repetitive manual Excel work and ensures consistent, accurate, and reusable data processing for recruitment operations.
```
### ***Problem Statement***
```
Recruitment teams often receive daily Excel reports containing raw and inconsistent candidate activity data. Manual cleaning of these files consumes significant time and introduces risks of human error.

Common challenges included:

- Inconsistent column naming
- Date columns stored as object datatype
- Combined full name and email in a single column
- Missing values in team information
- Formatting inconsistencies in names
- Daily repetitive manual cleaning tasks
- Difficulty preparing data for reporting and dashboards

The objective of this project was to automate the complete cleaning workflow and generate a standardized reporting-ready dataset automatically.

```
### ***Tools Used***
```

| Tool                   | Purpose                          |
| ---------------------- | -------------------------------- |
| Python                 | Core programming language        |
| Pandas                 | Data cleaning and transformation |
| Excel                  | Input and output reporting files |
| Jupyter Notebook       | Development and testing          |
| VS Code                | Script creation                  |
| Windows Task Scheduler | Daily automation execution       |

```

### ***Features***
```
- Automated Excel file reading using Pandas
- Date conversion and date-based feature generation
- Column standardization and renaming
- Full name and email extraction from combined fields
- String cleaning and formatting
- Missing value handling
- Numeric summary row generation
- Reordering of final columns
- Automated cleaned Excel export
- Error handling using try-except
- Reusable Python automation script
- Ready for Power BI and reporting workflows
- Daily scheduled execution support using Windows Task Scheduler
```
### ***Workflow***
```
      Raw Naukri Excel File
              ↓
      Load Excel File using Pandas
              ↓
      Convert Date Columns
              ↓
      Create Year / Month / Day Features
              ↓
      Rename and Standardize Columns
              ↓
      Split Full Name and Email
              ↓
      Clean String Values
              ↓
      Handle Missing Values
              ↓
      Generate Total Summary Row
              ↓
      Reorder Final Dataset
              ↓
      Export Cleaned Excel File
              ↓
      Automate Execution using Task Scheduler

```
### ***Folder Structure***
```
      automated-recruitment-data-pipeline
      │
      ├── data
      │   ├── raw
      │   │   └── naukri.xlsx
      │   │
      │   └── cleaned
      │       └── Cleaned_Data.xlsx
      │
      ├── scripts
      │   └── daily_cleaning.py
      │
      ├── screenshots
      │
      ├── README.md
      │
      ├── requirements.txt
      │
      └── .gitignore
```
### ***How to Run***
#### ***Step 1 — Clone Repository***
```
git clone <repository-link>
```
#### ***Step 2 — Install Required Libraries***
```
pip install pandas openpyxl
```
#### ***Step 3 — Place Raw Excel File***
```
data/raw/
```
#### ***Step 4 — Run Python Script***
```
python daily_cleaning.py
```
#### ***Step 5 — Output Generated***
```
Cleaned_Data.xlsx
```

### ***Screenshots***

```
screenshots/
├── raw_data.png
├── python_script.png
├── cleaned_output.png
├── task_scheduler.png
```

