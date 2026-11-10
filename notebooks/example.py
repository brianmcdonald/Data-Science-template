import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md("""
    # Example notebook

    A starter marimo notebook. Open it with `uv run marimo edit notebooks/example.py`.

    Notebooks are plain Python files, so they diff cleanly in Git. Once code
    matures, move it into `src/` and import it here, e.g. `from src import plots`.
    """)
    return


@app.cell
def _(mo):
    n = mo.ui.slider(1, 10, value=3, label="Rows")
    n
    return (n,)


@app.cell
def _(n):
    rows = [{"x": i, "x_squared": i**2} for i in range(1, n.value + 1)]
    rows
    return


if __name__ == "__main__":
    app.run()
