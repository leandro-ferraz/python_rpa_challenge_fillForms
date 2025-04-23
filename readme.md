[![Build Status](https://img.shields.io/github/actions/workflow/status/leandro-ferraz/python_rpa_challenge_fillforms/ci.yml?branch=main)](https://github.com/leandro-ferraz/python_rpa_challenge_fillforms/actions)
[![Python Version](https://img.shields.io/badge/python-%3E%3D3.12-blue)](https://www.python.org/)
[![License](https://img.shields.io/github/license/leandro-ferraz/python_rpa_challenge_fillforms)](https://github.com/leandro-ferraz/python_rpa_challenge_fillforms/blob/main/LICENSE)

# RPA Challenge Automator

Automates the download and form-filling process for the [RPA Challenge](https://www.rpachallenge.com/) using **Selenium**, **Pandas**, and is packaged in a **Docker** container for easy deployment.

In this challenge, form fields can shift positions between sessions and use dynamic selectors, and there is an input spreadsheet with a column header that isn’t handled in the default dataset, requiring robust locator strategies and flexible data mapping.

---

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Docker Usage](#docker-usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

---

## Features

- 🗂️ **Download** the Excel spreadsheet automatically
- 🔄 **Clean** and normalize column names with Pandas
- 📤 **Submit** each record via the web form
- 🐳 **Containerized** with Docker for consistent environments
- 📋 Configurable **logging** and error handling

---

## Prerequisites

- **Python** ≥ 3.12 (for local install)
- **Docker** (for containerized run)
- **Google Chrome** (compatible with ChromeDriver)
- Internet connection to download ChromeDriver (handled by `webdriver_manager`)

---

## Installation

Clone the repository and set up a Python virtual environment:

```bash
# Clone the repo
git clone https://github.com/leandro-ferraz/python_rpa_challenge_fillforms.git
cd python_rpa_challenge_fillforms

# Create and activate a virtual environment
python -m venv .venv

# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Install Python dependencies
pip install -r requirements.txt
```

---

## Configuration

Environment variables or CLI flags can override defaults:

| Variable        | Default                         | Description                           |
| --------------- | ------------------------------- | ------------------------------------- |
| `URL_CHALLENGE` | `https://www.rpachallenge.com/` | RPA Challenge URL                     |
| `LOG_LEVEL`     | `INFO`                          | Logging verbosity (DEBUG, INFO, etc.) |

---

## Usage

Run the automator directly with Python:

```bash
python -m src --url https://www.rpachallenge.com/ --log-level DEBUG
```

### Available CLI options

```text
  --url            Override default challenge URL  
  --download-dir   Directory to save the spreadsheet  
  --log-level      Logging level [DEBUG|INFO|WARNING|ERROR|CRITICAL]  
```

---

## Docker Usage

Build and run the application inside a Docker container (no local Python/Chrome needed):

1. **Build the Docker image**
   ```bash
   docker build -t rpa-challenge .
   ```
2. **Create a download dir (if isn't created)
   ```bash
   mkdir -p downloads
   ```

2. **Run the container**
   ```bash
   docker run --rm \
     -v "$(pwd)/downloads:/app/downloads" \
     rpa-challenge \
     --url https://www.rpachallenge.com/ \
     --log-level DEBUG
   ```

- `--rm` removes the container after it finishes.  
- `-v "$(pwd)/downloads:/app/downloads"` mounts your local `downloads` folder to the container.  
- `--log-level` choose one => [DEBUG|INFO|WARNING|ERROR|CRITICAL] 
- Flags passed after the image name go to the Python script entrypoint.

If you don’t need to persist the download locally, simply:

```bash
docker run rpa-challenge
```

---

## Project Structure

```
.
├── Dockerfile                 # Docker configuration for container build
├── .gitignore
├── LICENSE
├── README.md
├── requirements.txt
└── src/
    ├── __init__.py
    ├── config.py              # Default settings and overrides
    ├── browser.py             # Selenium wrapper with custom options
    ├── challenge_page.py      # Page-specific automation logic
    ├── bot.py                 # Run tasks
    ├── main.py                # CLI parsing and entrypoint
    └── __main__.py            # Enables python -m src
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
