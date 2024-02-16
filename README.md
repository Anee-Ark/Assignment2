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

  ## Contribution

| Contributor | Contributions            | Percentage |
|-------------|--------------------------|------------|
| Dev Mithunisvar Premraj       | Web scraping data into CSV Files and uploaded them into S3 Bucket     | 33.33%        |
| Dev         | PCA, Feature Engineering, Machine Learning | 55% |
| Dev         | PCA, Feature Engineering, Machine Learning | 55% |

