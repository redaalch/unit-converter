# Unit Converter

A Python unit converter for temperature and length, built for Assignment 2: GitHub Collaboration & Automation.

Project status: Temperature and length conversions completed.

## Team and feature plan

Chosen theme: Unit Converter. Group size: 2 members.

| Member | GitHub username | Assigned feature | Feature branch |
| --- | --- | --- | --- |
| Reda Alalach | [redaalch](https://github.com/redaalch) | Temperature conversions: Celsius, Fahrenheit, Kelvin | `feature/temperature` |
| Nour El Houda Garaoui | [Nour-2101](https://github.com/Nour-2101) | Length conversions: meters, kilometers, miles | `feature/length` |

Each member will make at least two meaningful commits on their feature branch and add at least three meaningful unit tests. The complete suite will cover normal conversions, boundary values, and invalid inputs.

Each member will open a Pull Request into `main` and review the other member's Pull Request, leaving a meaningful line comment before approval. The group will complete a Request changes cycle and resolve a controlled conflict in the project status line above.

## Project structure

```text
unit-converter/
├── README.md
├── .gitignore
├── requirements.txt
├── unit_converter/       # Python conversion modules
├── tests/                # pytest test files
└── docs/                 # GitHub Pages project page
```

## Local setup

Use Python 3.12. Each member should clone the shared repository into their own local copy:

```bash
git clone https://github.com/redaalch/unit-converter.git
cd unit-converter
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, activate the virtual environment with `.venv\Scripts\activate`.

The temperature and length converters are implemented in `unit_converter/`. Run the complete test suite from the repository root:

```bash
python -m pytest -q
```

## Usage

From the repository root, start Python with `python`, then run:

```python
from unit_converter.temperature import convert_temperature
from unit_converter.length import convert_length

print(round(convert_temperature(0, "C", "F"), 2))  # 32.0
print(convert_length(1, "mi", "m"))  # 1609.344
```

Use `exit()` to return to the terminal.

## Collaboration workflow

Start each feature from the latest `main`:

```bash
git switch main
git pull origin main
git switch -c feature/temperature
```

Member B uses `feature/length` instead. Push the feature branch and open a Pull Request after making and checking the changes. Future feature changes go through Pull Requests.

## Project page

The project page is in `docs/index.html`. It documents both converters, the team, local setup, usage, and tests.

GitHub Pages URL: [https://redaalch.github.io/unit-converter/](https://redaalch.github.io/unit-converter/).

Publishing setup: merge the project-page Pull Request, then select `main` and `/docs` under **Settings → Pages → Deploy from a branch**. The site becomes available after the first successful Pages build.

## Group report

The report covers both converters, 35 pytest cases, peer reviews, the controlled README conflict, CI, and the GitHub Pages deployment.

- [Final group report (PDF)](reports/Assignment_2_Report_Reda_Nour.pdf)
- [Editable group report (Word)](reports/Assignment_2_Report_Reda_Nour.docx)
