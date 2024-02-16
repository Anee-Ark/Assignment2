# Assignment 2
![Architecture Diagram](https://github.com/BigDataIA-Spring2024-Sec1-Team1/demo-repository/blob/main/architecture_diagram.png)
## Part 1: Web Scraping with Selenium and Beautiful Soup

This repository contains a Jupyter Notebook script for automating web scraping tasks using Selenium. The script navigates through the CFA Institute's website, collecting URLs of refresher readings, extracting key information from each, and saving the data in a structured CSV format.

### Prerequisites

Before running the script, ensure you have the following installed:
- Python
- Selenium
- Chrome WebDriver (or a driver for your preferred browser)

You can install Selenium using pip:
```
pip install selenium
```

## Description

- Initialization: Importing necessary Selenium modules and initializing a Chrome WebDriver for browser automation.
- Web Scraping: The script navigates through the CFA Institute's website, handling pagination, extracting URLs of the readings, and dealing with issues such as timeouts and missing elements.
- Data Extraction and CSV Creation: It processes the collected URLs to extract information like the publication year, introduction, learning outcomes, and summary. This information is then organized and saved into a CSV file.

## Part 2: Extracting Data through PyPDF and Grobid 

### Prerequisites

Before running the script, ensure you have the following installed:
- Python
- Docker
- Grobid

You can install PyPdf using pip:

```
pip install PyPDF2
```
## Description


## Part 3: Move the CSV file (output of part 1) to Snowflake using SQLAlchemy

### Prerequisites
Before running the script, ensure you have the following: 
- Python
- Snowflake
- SQLAlchemy

 You can install SQLAlchemy using pip:

```
pip install SQLAlchemy
```

## Description

- Snowflake Connection Setup: Connect to Snowflake and set up the connection parameters.

-Data Preparation and Upload: Loads CSV data into a pandas DataFrame, handles missing values, and insert the data into a Snowflake table.

-Cleanup and Finalization: Commit the changes made to the Snowflake database and closes the connection.

## Part 4: Move the CSV file, txt files extracted from PyPdf and Grobid to S3 bucket. Move the structured metadata of Grobid output to Snowflake

### Prerequisites

Before running the script, ensure you have the following: 
- S3 Bucket
- Snowflake
- SQLAlchemy
- Python
- Boto3

You can install Boto3 using pip:

```
pip install boto3
```

## Description

- Configure your AWS credentials to allow programmatic access to your S3 bucket.
- Write a Python function that takes the paths to the CSV file, Grobid extracted text files, and PyPDF extracted text files as input parameters.
- Inside the function, establish a connection to your AWS S3 bucket using boto3.client('s3').


  ## Contribution

| Contributor | Contributions            | Percentage |
|-------------|--------------------------|------------|
| Dev Mithunisvar Premraj       | Web scraping data into CSV File and uploaded them into S3 Bucket     | 33.33%        |
| Aneesh Koka        | Extracted data from pdf using PyPDF and Grobid | 33.33% |
| Rishabh Shah         | Moved the csv file to Snowflake, created a AWS account and did the documentation | 33.33% |

