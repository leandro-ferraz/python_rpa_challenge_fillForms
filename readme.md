[![Build Status](https://img.shields.io/github/actions/workflow/status/YOUR_USERNAME/YOUR_REPO/ci.yml?branch=main)](https://github.com/YOUR_USERNAME/YOUR_REPO/actions)
[![Python Version](https://img.shields.io/badge/python-%3E%3D3.12-blue)](https://www.python.org/)
[![License](https://img.shields.io/github/license/leandro-ferraz/python_rpa_challenge_fillForms)](https://github.com/leandro-ferraz/python_rpa_challenge_fillForms/blob/main/LICENSE)

# RPA Challenge Automator

Automates the download and form-filling process for the [RPA Challenge](https://www.rpachallenge.com/) using **Selenium** and **Pandas**.

---

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- 🗂️ **Download** the Excel spreadsheet automatically  
- 🔄 **Clean** and normalize column names with Pandas  
- 📤 **Submit** each record via the web form  
- 📋 Configurable **logging** and error handling  

---

## Prerequisites

- **Python** ≥ 3.12  
- **Google Chrome** (compatible with ChromeDriver)  
- Internet connection to download ChromeDriver (handled by `webdriver_manager`)  

---

## Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO

# Create and activate a virtual environment
python -m venv .venv

#activate a virtual environment
## macOS / Linux
source .venv/bin/activate
## Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

---

## Configuration

Environment variables or CLI flags can override defaults:

| Variable         | Default                          | Description                             |
|------------------|----------------------------------|-----------------------------------------|
| `URL_CHALLENGE`  | `https://www.rpachallenge.com/` | RPA Challenge URL                       |
| `LOG_LEVEL`      | `INFO`                           | Logging verbosity (DEBUG, INFO, etc.)   |

---

## Usage

```bash
python -m rpa_challenge   --url https://www.rpachallenge.com/   --download-dir ./downloads   --log-level DEBUG
```

### Available CLI options

```text
  --url            Override default challenge URL
  --download-dir   Directory to save the spreadsheet (defaults to ./downloads)
  --log-level      Logging level [DEBUG|INFO|WARNING|ERROR|CRITICAL]
```

---

## Project Structure

```
.
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── src/
    ├── rpa_challenge/
    ├── __init__.py
    ├── config.py
    ├── browser.py
    ├── challenge_page.py
    ├── bot.py
    ├── main.py
    └── __main__.py
```

---

## Contributing

1. Fork the repo  
2. Create a feature branch (`git checkout -b feature/your-feature`)  
3. Commit your changes (`git commit -m "Add feature"`)  
4. Push to the branch (`git push origin feature/your-feature`)  
5. Open a Pull Request

Please follow the code style guidelines (e.g., **Black**, **flake8**).

---

## License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for details.
