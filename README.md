# Data-Science-template
A starter template for data science work using Pixi.
Created by Brian Mc Donald

*Replace this file with a README specific to your project*

## Getting started

1. Install [Quarto](https://quarto.org/docs/get-started/), the tool/format for publishing to different formats
2. Install [Pixi](https://pixi.sh/latest/) to manage packages. On MacOS `curl -fsSL https://pixi.sh/install.sh | bash` and on Windows Powershell: `iwr -useb https://pixi.sh/install.ps1 | iex`
3. Run `Pixi init .` to create a new Pixi project. It creates a pixi.toml and pixi.lock file.
3. Run pixi add <packagename> to add pacakges. Example: pixi add python ruff polars matploltib requests 
4. Do exploration in notebooks - ipynb's will keep cell output, which is good for exploratory analysis but is messy for version control.
5. When code is maturing, move it to files in src. The examples can be changed as needed.
6. Create quarto files for the analysis and formats you want, calling the code from src - dashboards, websites, pptx pdf.
7. Run `quarto render` in the quarto directory to render the quarto files and check that the outputs appear in the Reports directory.
8. If you wish to publish a directory as a static site, you can use thi [Github Action](https://github.com/peaceiris/actions-gh-pages) to copy a directory to a gh-pages branch, which you can then configure using Github Pages.

# Tips
- Run `ruff format` to format all files in a directory to keep your code clean. The Ruff VSCode extension is convenient.
- Use .gitignore to exclude certain files and directories from version control. Definitely exclude .DS_Store, .pixi, .env. Consider excluding data, reports and notebooks.
- Use Pixi tasks to simplify running commands or scripts. Example `pixi task add cow cowpy "Hello User"` or `pixi task add fetch python data_get.py --option all`, then running `pixi run cow` or `pixi run fetch`
- Use `pixi update` or `pixi upgrade` to update package versions


## Structure

├── LICENSE            <- Open-source license if one is chosen
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── quarto
│   ├── example1.qmd   <- Quarto markdown file for a dashboard, website, pdf etc. 
│   ├── _quarto.yml    <- Quarto project configuration.
│
├── pixi.toml     <- Project configuration file with package metadata 
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
│
└── src   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes the module a Python module
    │
    ├── .env                    <- Stored credentials . Manually add. Included in  .gitignore so it's excluded from vc.
    │
    ├── data_get.py             <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── model.py                <- Code to create and run models       
    │
    └── plots.py                <- Code to create visualizations  