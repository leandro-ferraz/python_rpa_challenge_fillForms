from config import Config
from browser import Browser
from challenge_page import Challenge_page


class Bot():
    def __init__(self) -> None:
        self.browser = Browser()
        self.browser.go_to(Config.URL_CHALLENGE)
        self.challenge_page = Challenge_page(self.browser)
                

    def run(self):
        df_people = self.challenge_page.get_spreadsheet()
        df_people = self.challenge_page.clean_column_names(df_people)
        self.challenge_page.start_challenge()
        self.challenge_page.submit_registration(df_people)


"""

    def open_website(self):
        URL = r'https://www.rpachallenge.com/'
        self.browser.go_to(URL)

    def download_spreadsheet(self):
        xpath_download_button = '//a[contains(normalize-space(.), "Download Excel")]'
        self.challenge_page.find().click()

    def fill_web_form(self):
        pass
"""

bot = Bot()
bot.run()