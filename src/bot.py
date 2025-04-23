import logging
from config import Config
from browser import Browser
from challenge_page import Challenge_page


class Bot():
    def __init__(self, url_challenge: str = Config.URL_CHALLENGE) -> None:
        self.browser = Browser()
        self.browser.go_to(url_challenge)
        self.challenge_page = Challenge_page(self.browser)
                

    def run(self):
        logging.info("getting spreadsheet (challenge's input)")
        df_people = self.challenge_page.get_spreadsheet()
        logging.info("cleanning the column names")
        df_people = self.challenge_page.clean_column_names(df_people)
        logging.info("starting the challenge")
        self.challenge_page.start_challenge()
        logging.info('submitting the registration')
        for idx_person, dict_person in enumerate(df_people.to_dict(orient="records")):
            self.challenge_page.submit_registration( dict_person )
            logging.debug(f" - submited row [{idx_person}]")