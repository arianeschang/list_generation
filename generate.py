from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

import json


driver = webdriver.Chrome(executable_path = "chromedriver")
url = driver.command_executor._url       
session_id = driver.session_id        
driver.get("https://www.votebuilder.com/TurfList.aspx")

json_dict = {'url': url, 'session_id': session_id}
with open('browser_ids.txt', 'w') as outfile:
    json.dump(json_dict, outfile)
