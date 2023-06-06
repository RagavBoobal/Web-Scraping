# Web-Scraping

This code file can be used to to scrap the data from web application. It Specifically scraps the data from the table which is dynamical in nature. Since it is dynamic table data, it is not possible to scrap only with using Beautiful Soup library in python. We also need selenium and chrome web driver for it.

Code Explanation : This particular code extracts the data of first five rows of 2nd, 3rd, 4th and 5th columns specifically and converts that it into a pandas dataframe and atlast stores in excel file. Where "output.xlsx" represents output data.

Below following are the requirements:
1) pip install pandas
2) pip install requests
3) pip install requests beautifulsoup4
4) pip install selenium
5) Google Chrome - https://www.google.com/chrome/?brand=YTUH
6) Chrome webdriver corresponding to the version of chrom - https://chromedriver.chromium.org/downloads
