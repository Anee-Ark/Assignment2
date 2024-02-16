# Assignment 2
![image](https://user-images.githubusercontent.com/108534539/218347565-ebebee5e-3de3-427a-8370-cef5e44c3591.png)
## Web Scraping Project with Selenium

This repository contains a Jupyter Notebook script for automating web scraping tasks using Selenium. The script navigates through the CFA Institute's website, collecting URLs of refresher readings, extracting key information from each, and saving the data in a structured CSV format.

### Prerequisites

Before running the script, ensure you have the following installed:
- Python
- Selenium
- Chrome WebDriver (or a driver for your preferred browser)

You can install Selenium using pip:

```bash
pip install selenium '''

### Description
The script operates in several key steps:

Initialization: Importing necessary Selenium modules and initializing a Chrome WebDriver for browser automation.
Web Scraping: The script navigates through the CFA Institute's website, handling pagination, extracting URLs of the readings, and dealing with issues such as timeouts and missing elements.
Data Extraction and CSV Creation: It processes the collected URLs to extract information like the publication year, introduction, learning outcomes, and summary. This information is then organized and saved into a CSV file.
