# Data-Science-template
A starter template for data science work using [uv](https://docs.astral.sh/uv/), [marimo](https://marimo.io/) and [Quarto](https://quarto.org/).
Created by Brian Mc Donald

*Replace this file with a README specific to your project*

## Getting started

### One-time setup (per machine)

1. Install [uv](https://docs.astral.sh/uv/getting-started/installation/) to manage Python, packages and tools. On macOS/Linux `curl -LsSf https://astral.sh/uv/install.sh | sh` and on Windows PowerShell: `powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"`
2. Install Quarto, marimo and [marimo-studio](https://marimo-team.github.io/marimo-studio/) as uv tools, so they are available everywhere on your machine:

   ```bash
   uv tool install quarto-cli
   uv tool install marimo-studio --with-executables-from marimo
   ```

   The second command puts `marimo` and `marimo-studio` in one shared environment. marimo-studio pins an exact marimo version, so installing them together keeps the two compatible. If the commands are not found afterwards, run `uv tool update-shell` and restart your terminal.

### Per project

1. Run `uv init --bare` to create a new uv project. It creates a `pyproject.toml`; the `uv.lock` file and `.venv` directory appear when you add the first package.
2. Run `uv add <packagename>` to add packages. Example: `uv add polars matplotlib requests marimo jupyter`, and `uv add --dev ruff` for development-only tools.
   - `marimo` is needed in the project so that notebooks can see the project's packages. Use `uv add marimo-studio` instead if you want Studio views in the project.
   - `jupyter` is needed for Quarto to execute Python cells.
3. Do exploration in marimo notebooks: `uv run marimo edit notebooks/example.py`. Notebooks are plain Python files, so they work well with version control, and they can also be run as scripts (`uv run python notebooks/example.py`) or as apps (`uv run marimo run notebooks/example.py`).
4. When code is maturing, move it to files in src. The examples can be changed as needed. To import it in notebooks (`from src import plots`), add this to `pyproject.toml`:

   ```toml
   [tool.marimo.runtime]
   pythonpath = ["."]
   ```

5. Create quarto files for the analysis and formats you want, calling the code from src - dashboards, websites, pptx, pdf.
6. Run `uv run quarto render` in the quarto directory to render the quarto files and check that the outputs appear in the reports directory. `uv run` makes Quarto use the project's Python environment.
7. If you wish to publish a directory as a static site, you can use this [Github Action](https://github.com/peaceiris/actions-gh-pages) to copy a directory to a gh-pages branch, which you can then configure using Github Pages.

Anyone cloning an existing project only needs `uv sync` to recreate the environment from `uv.lock`.

## Tips
- Run `uv run ruff format` to format all files in a directory to keep your code clean. The Ruff VSCode extension is convenient.
- Use .gitignore to exclude certain files and directories from version control. Definitely exclude .DS_Store, .venv, .env and `__marimo__`. Consider excluding data and reports. Do commit `pyproject.toml` and `uv.lock`.
- Use `uv run <command>` to run anything inside the project environment without activating it. Example: `uv run python src/data_get.py`
- Use `uv remove <packagename>` to remove a package, and `uv tree` to see what depends on what.
- Use `uv python install 3.13` and `uv python pin 3.13` to choose the Python version for a project.

## Running tools without installing them (optional)
`uvx` (short for `uv tool run`) runs a tool in a temporary, cached environment. It is handy for one-off use, for trying a tool before installing it, or on a machine where you have not done the one-time setup.

```bash
uvx ruff format                                        # format code without adding ruff to the project
uvx marimo edit --sandbox scratch.py                   # throwaway notebook; packages are recorded in the file itself
uvx --with marimo-studio marimo edit notebook.py --sandbox   # the same, with Studio
uvx marimo-studio view create dashboard --target notebook.py
uvx --from quarto-cli quarto render                    # --from is needed when the command name differs from the package name
uvx marimo@latest --version                            # force the newest release
```

`uvx` tools do not see the packages in your project. For project work use `uv run`, or the `--sandbox` flag so that marimo installs the packages a notebook declares.

## Keeping things up to date

| What | Command |
| --- | --- |
| uv itself | `uv self update` |
| All uv tools (Quarto, marimo, marimo-studio) | `uv tool upgrade --all` |
| One uv tool | `uv tool upgrade quarto-cli` |
| All project packages | `uv lock --upgrade` then `uv sync` |
| One project package | `uv lock --upgrade-package polars` then `uv sync` or `uv sync --upgrade`|
| Tools cached by uvx | `uvx <tool>@latest` |

- `uv tool list` shows the installed tools and their versions.
- `uv lock --upgrade` stays inside the version ranges in `pyproject.toml`. To go past a range, edit it or re-add the package, e.g. `uv add "polars>=2"`.
- marimo-studio decides which marimo version the shared tool environment gets, so marimo there may sit slightly behind the newest release.

## Structure

```
├── README.md          <- Replace with a README for your project
├── pyproject.toml     <- Created by `uv init`; lists the project's packages
├── uv.lock            <- Created by uv; exact package versions, commit it
├── data
│   ├── external       <- Data from third party sources
│   ├── interim        <- Intermediate data that has been transformed
│   ├── processed      <- Final data sets for analysis and modelling
│   └── raw            <- The original, immutable data
├── docs               <- Project documentation
├── models             <- Trained models, predictions and summaries
├── notebooks          <- marimo notebooks (.py) for exploration
│   └── example.py
├── quarto             <- Quarto source files, rendered into reports
│   ├── _quarto.yml
│   └── example1.qmd
├── references         <- Data dictionaries, manuals and other material
├── reports            <- Rendered outputs
│   └── figures
└── src                <- Mature, reusable code
    ├── data_get.py
    ├── data_process.py
    ├── features.py
    ├── model.py
    └── plots.py
```

## Optional: Pixi
[Pixi](https://pixi.sh/latest/) is an alternative to uv that can also install conda packages. It is worth considering when a project needs non-Python dependencies that are awkward to get from PyPI, such as GDAL, R or compiled geospatial libraries.

- Install on macOS/Linux with `curl -fsSL https://pixi.sh/install.sh | bash` and on Windows PowerShell with `iwr -useb https://pixi.sh/install.ps1 | iex`
- `pixi init .` creates a project, and `pixi init --format pyproject` uses `pyproject.toml` so it sits alongside the uv setup.
- `pixi add <packagename>` adds conda packages and `pixi add --pypi <packagename>` adds PyPI packages.
- `pixi run <command>` runs inside the environment, and `pixi task add fetch python src/data_get.py` saves a command as a task to run with `pixi run fetch`.
- `pixi update` or `pixi upgrade` update package versions, and `pixi self-update` updates Pixi.
- marimo can use Pixi for sandboxed notebooks: `marimo edit --sandbox=pixi notebook.py`
- Add `.pixi` to .gitignore (already included in this template).
