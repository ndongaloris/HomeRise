import os

folders = [
    "data/raw",
    "data/processed",
    "notebooks",
    "src",
    "app",
    "assets/charts",
    "tests"
]

files = {
    "README.md": "# AnaliHouse\n\nPython tool for housing market analysis in Africa.",
    "requirements.txt": "pandas\nmatplotlib\nseaborn\nstreamlit",
    ".gitignore": "*.pyc\n__pycache__/\ndata/raw/\nassets/charts/",
    "src/__init__.py": "",
    "src/data_loader.py": "# Functions to load and clean data",
    "src/analysis.py": "# Filtering and aggregation logic",
    "src/visualization.py": "# Chart generation using matplotlib/seaborn",
    "app/dashboard.py": "# Streamlit app layout",
    "tests/test_analysis.py": "# Unit tests for analysis functions"
}

for folder in folders:
    os.makedirs(folder, exist_ok=True)

for path, content in files.items():
    with open(path, "w") as f:
        f.write(content)

print("✅ Repo structure generated.")
