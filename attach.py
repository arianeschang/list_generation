from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
import json
import time
import configs

def attach_to_session(executor_url, session_id):
    original_execute = WebDriver.execute
    def new_command_execute(self, command, params=None):
        if command == "newSession":
            # Mock the response
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return original_execute(self, command, params)
    # Patch the function before creating the driver object
    WebDriver.execute = new_command_execute
    driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    driver.session_id = session_id
    # Replace the patched function with original function
    WebDriver.execute = original_execute
    return driver

def submit_data(driver):
    element = driver.find_element_by_id("ctl00_ContentPlaceHolderVANPage_VanDetailsItemReportFormatInfo_VANInputItemDetailsItemReportFormatInfo_ReportFormatInfo")
    element.send_keys(configs.REPORT_FORMAT)


    element = driver.find_element_by_id("ctl00_ContentPlaceHolderVANPage_VanDetailsItemvdiScriptID_VANInputItemDetailsItemActiveScriptID_ActiveScriptID")
    element.send_keys(configs.SCRIPT)


    element = driver.find_element_by_id("ctl00_ContentPlaceHolderVANPage_VanDetailsItemVANDetailsItemScriptSource_ScriptSource_VANInputItemDetailsItemScriptSource_ScriptSource")
    element.send_keys(configs.CONTACTED_HOW)

    element = driver.find_element_by_id("ctl00_ContentPlaceHolderVANPage_VanDetailsItemMiniVANCampaign_VANInputItemDetailsItemMiniVANCampaign_MiniVANCampaign")
    element.send_keys(configs.MINIVAN_CAMPAIGN)

    element = driver.find_element_by_id("ctl00_ContentPlaceHolderVANPage_VANDetailsItemExcludeVoted_VANInputItemDetailsItemExcludeVoted_ExcludeVoted_0")
    element.click()

    element = driver.find_element_by_id("ctl00_ContentPlaceHolderVANPage_ButtonSortOptionsSubmit")
    element.click()


def main():

    with open('browser_ids.txt', 'r') as f:
        browser = json.loads(f.read())

    driver = attach_to_session(browser['url'], browser['session_id'])

    keep_going = True

    while keep_going is True:
        url = driver.current_url
        print(url)
        if url.startswith('https://www.votebuilder.com/ScriptSortOptions.aspx'):
            submit_data(driver)
            time.sleep(2)
        else:
            keep_going = False


if __name__ == "__main__":
    main()


