from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from select_class_bis_link import get_link
from webdriver_manager.chrome import ChromeDriverManager
import time


def get_items_from_table(titles, tables):
    titles = [title.get_text() for title in titles]
    for table, title in zip(tables, titles):
        print(f"Title: {title}")
        rows = table.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 2:
                item_tag = cols[1].find('a')
                if item_tag:
                    item_name = item_tag.get_text(strip=True)
                    item_link = item_tag['href']
                else:
                    continue
                source_text = cols[2].get_text(strip=True) if len(cols) > 2 else "N/A"

                print(f"Item: {item_name}, Link: {item_link}, Source: {source_text}")


url = get_link()

chrome_options = Options()
chrome_options.add_argument("--headless")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get(url)

time.sleep(2)

soup = BeautifulSoup(driver.page_source, 'html.parser')

all_tables_titles = soup.find_all('h4', class_="heading-size-4")
all_tables = soup.find_all('table', class_="grid max-width")

if len(all_tables_titles) < (len(all_tables)):
    all_tables_titles = soup.find_all('h3', class_="heading-size-3")

get_items_from_table(all_tables_titles, all_tables)

driver.quit()