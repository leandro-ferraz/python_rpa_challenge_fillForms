#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
main.py

Ponto de entrada da aplicação RPA.
Define parsing de argumentos, inicializa componentes e executa a lógica principal.
"""

import argparse
import logging
import sys

from rpa_automation.config import GOOGLE_URL, DOWNLOAD_DIR
from rpa_automation.core.browser import Browser
from rpa_automation.tasks.rpa_challenge_task import RPAChallengeTask

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Automação RPA Challenge — preenche formulário com dados de planilha"
    )
    parser.add_argument(
        "--url",
        default=GOOGLE_URL,
        help="URL inicial do RPA Challenge",
    )
    parser.add_argument(
        "--download-dir",
        default=DOWNLOAD_DIR,
        help="Diretório onde o Excel será baixado",
    )
    return parser.parse_args()


def setup_logging():
    """Configura o logging básico para console e/ou arquivo."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
    )


def main():
    """Função principal: inicializa browser, executa task e faz cleanup."""
    args = parse_args()
    setup_logging()
    logger = logging.getLogger(__name__)
    logger.info("Iniciando automação com URL=%s e DOWNLOAD_DIR=%s", args.url, args.download_dir)

    browser = Browser()
    try:
        task = RPAChallengeTask(browser)
        task.run()
        logger.info("Automação concluída com sucesso.")
    except Exception:
        logger.exception("Falha durante a execução da automação.")
        sys.exit(1)
    finally:
        browser.quit()


if __name__ == "__main__":
    main()
