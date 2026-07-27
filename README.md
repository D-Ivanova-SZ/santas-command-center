
```markdown
# 🎅 Santa's Command Center

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

A festive, modular Python console application that helps Santa Claus manage his Christmas operations by pulling real-time data from external APIs and displaying it with a polished terminal UI. Integrated three external REST APIs, robust error handling and a rich, color-coded terminal interface.
## 📖 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Screenshots](#-screenshots)
- [Installation](#️-installation)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [APIs Used](#-apis-used)
- [Technologies](#-technologies)
- [License](#-license)

## 🎯 Overview

Santa's Command Center is an interactive console application built as a hands-on exercise in working with external REST APIs, structured error handling, and terminal UI design using the `rich` library. The app follows a modular architecture that separates concerns between HTTP communication, business logic, and presentation.

## ✨ Features

- **Real-time API Integration** — fetches live weather, jokes, and cocktail recipe data
- **Rich Terminal UI** — color-coded tables, panels, and formatted output via `rich`
- **Robust Error Handling** — network failures and malformed data never crash the app
- **Interactive Search** — repeatable cocktail search without restarting the module
- **Modular Architecture** — clean separation between `core/`, `modules/`, and `app.py`

## 📸 Screenshots

[Greeting Card](screenshots/greeting.png)
[Main Menu](screenshots/menu.png)
[Weather Module](screenshots/weather.png)
[Joke Module](screenshots/joke.png)
[Cocktail Module](screenshots/cocktail.png)

## ⚙️ Installation

### Prerequisites
- Python 3.7 or higher
- Internet connection (for API requests)

### Setup

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/santas-command-center.git
cd santas-command-center

# Create a virtual environment
python -m venv venv

# Activate it
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## 🚀 Usage

```bash
python app.py
```

| Option | Module | Description |
|--------|--------|--------------|
| `1` | Weather Station | Checks Lapland flight conditions |
| `2` | Elf Morale Booster | Fetches a random joke |
| `3` | Santa's Fuel | Searches cocktail recipes |
| `Q` | Quit | Exits the application |

## 📁 Project Structure

```
santas-command-center/
│
├── app.py                 # Main application and menu
├── requirements.txt       # Project dependencies
├── README.md
├── LICENSE
│
├── core/
│   └── api.py              # HTTP request helper
│
└── modules/
    ├── weather.py           # Weather station module
    ├── spirit.py            # Elf morale booster module
    └── fuel.py               # Cocktail search module
```

## 🔌 APIs Used

- [Open-Meteo API](https://open-meteo.com/) — weather data (no key required)
- [Official Joke API](https://official-joke-api.appspot.com/) — random jokes (no key required)
- [TheCocktailDB](https://www.thecocktaildb.com/) — cocktail recipes (no key required)

## 🛠️ Technologies

- **Python 3** — core language
- **[requests](https://requests.readthedocs.io/)** — HTTP client for API calls
- **[rich](https://rich.readthedocs.io/)** — terminal formatting and styling

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

**Author:** Daniela Ivanova (https://github.com/D-Ivanova-SZ)
```