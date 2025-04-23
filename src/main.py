import argparse
import logging
import sys

from config import Config
from bot import Bot

def parse_args():
    parser = argparse.ArgumentParser(description="Executor do RPA Challenge")
    parser.add_argument("--url", default=Config.URL_CHALLENGE, help="URL do desafio")
    parser.add_argument("--log-level", default="INFO", choices=["DEBUG","INFO","WARNING","ERROR","CRITICAL"])
    return parser.parse_args()

def setup_logging(level: int):
    logging.basicConfig(format="%(asctime)s %(levelname)s %(message)s", level=level)

def main():
    args = parse_args()
    log_level = logging.getLevelNamesMapping().get(args.log_level)
    setup_logging(log_level)

    try:
        bot = Bot()
        logging.info("Starting the execution")

        bot.run()
        logging.info("Sucessfull")
    except Exception:
        logging.exception("Fail during the execution")
        sys.exit(1)
    finally:
        logging.info("Finish")

if __name__ == "__main__":
    main()
