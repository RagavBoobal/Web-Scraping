#IMPORTING THE NECESSARY LIBRARIES
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

# SETTING UP THE CHROME DRIVER BY SPECIFYING THE STORAGE LINK
driver = webdriver.Chrome("E:/SOFTWARES/chromedriver_win32/chromedriver.exe")  

# SPECIFYING THE WEB APPLICATION URL THAT NEED TO BE SCRAPPED
url = "https://qcpi.questcdn.com/cdn/posting/?group=1950787&provider=1950787"

# LOADING THE WEB APPLICATION USING CHROME DRIVER
driver.get(url)

# EXTRACTING THE PAGE SOURCE AFTER EXECUTION
html = driver.page_source

# PARSING THE SOURCE WITH HTML USING BEAUTIFUL SOUP
soup = BeautifulSoup(html, "html.parser")

# FINDING THE TABLE WITH SPECIFYING THE RESPECTIVE TAG AND ID OF THE TABLE
table = soup.find("table", id="table_id")

# FINDING THE BODY TAG FOR CONTENT IN TABLE BY SPECIFYING THE RESPECTIVE TAG
tbody = table.find("tbody")

# FINDING THE ROW TAG FOR CONTENT IN TABLE BY SPECIFYING THE RESPECTIVE TAG AND NO OF ROWS WE WANT TO SCRAP
rows = tbody.find_all("tr")[:5]

# CREATING AN EMPTY LIST 
data = []

# PROCESSING THE EACH ROWS AND EXTRACTING THE DATA FROM 2nd, 3rd, 4th AND 5th COLUMNS RESPECTIVELY
for row in rows:    # ITERATING EACH ROW
    cells = row.find_all("td")[1:5] # EXTRACTING THE DATA FROM 2nd, 3rd, 4th AND 5th COLUMNS
    row_data = [cell.get_text(strip=True) for cell in cells] # GETTING THE DATA WITHOUT HTML TAGS
    data.append(row_data)   # APPENDING THE DATA TO THE LIST


# CREATING A PANDAS DATAFRAME FROM THE EXTRACTED DATA AND ALSO SPECIFYING THE COLUMN NAMES
df = pd.DataFrame(data, columns=["Quest Number", "Est. Value Notes", "Description", "Closing Date"])

# STORING THE DATAFRAME INTO AN EXCEL FILE
df.to_excel("F:/COLLEGE/INTERNSHIP AND PLACEMENT/PLACEMENT PROCESS - 2022 TO 2023/OFF CAMPUS/PRIMENUMBER TECHNOLOGIES/output.xlsx", index=False)


# CLOSING THE WEB DRIVER [CHROME BROWSER]
driver.quit()
