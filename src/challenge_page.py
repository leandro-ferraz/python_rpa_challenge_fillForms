import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement 

from src.browser import Browser #import just for ilustrate a specific typehint (find method)


class Challenge_page:
    def __init__(self, browser: Browser):
        self.browser = browser

    def get_spreadsheet(self) -> pd.DataFrame:
        xpath_button_download = '//a[contains(normalize-space(.), "Download Excel")]'
        download_button = self.browser.find(By.XPATH, xpath_button_download)
        url_spreadsheet = download_button.get_attribute("href")
        return pd.read_excel(url_spreadsheet)
    
    def start_challenge(self):
        xpath_button_start = '//button[normalize-space(.)="Start"]'
        self.browser.find(By.XPATH, xpath_button_start).click()
        
    def submit_registration(self, dict_person: dict):
        xpath_company_name = '//div[label[normalize-space(.)="Company Name"]]//input'
        xpath_email = '//div[label[normalize-space(.)="Email"]]//input'
        xpath_last_name = '//div[label[normalize-space(.)="Last Name"]]//input'
        xpath_first_name = '//div[label[normalize-space(.)="First Name"]]//input'
        xpath_role_in_company = '//div[label[normalize-space(.)="Role in Company"]]//input'
        xpath_address = '//div[label[normalize-space(.)="Address"]]//input'
        xpath_phone_number = '//div[label[normalize-space(.)="Phone Number"]]//input'
        xpath_button_submit = '//input[@type="submit" and @value="Submit"]'

        self.browser.find(By.XPATH, xpath_company_name).send_keys(dict_person['company name'])
        self.browser.find(By.XPATH, xpath_email).send_keys(dict_person['email'])
        self.browser.find(By.XPATH, xpath_last_name).send_keys(dict_person['last name'])
        self.browser.find(By.XPATH, xpath_first_name).send_keys(dict_person['first name'])
        self.browser.find(By.XPATH, xpath_role_in_company).send_keys(dict_person['role in company'])
        self.browser.find(By.XPATH, xpath_address).send_keys(dict_person['address'])
        self.browser.find(By.XPATH, xpath_phone_number).send_keys(dict_person['phone number'])
        self.browser.find(By.XPATH, xpath_button_submit).click()

    @staticmethod
    def clean_column_names(df_people: pd.DataFrame) -> pd.DataFrame:
        df_people.columns = df_people.columns.str.strip().str.lower()
        return df_people