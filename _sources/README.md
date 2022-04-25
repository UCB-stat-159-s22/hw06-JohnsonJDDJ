## Fine-tuning reproduciblity of LIGO Black Hole signal tutorial, Part II

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-s22/hw06-JohnsonJDDJ/HEAD?labpath=index.ipynb)

**Note:** This repository is public so that Binder can find it. All code and data is based on the original [LIGO Center for Open Science Tutorial Repository](https://github.com/losc-tutorial/LOSC_Event_tutorial). This repository is a class exercise that restructures the original LIGO code for improved reproducibility, as a homework assignment for the [Spring 2022 installment of UC Berkeley's Stat 159/259 course, _Reproducible and Collaborative Data Science_](https://ucb-stat-159-s22.github.io). Authorship of the original analysis code rests with the LIGO collaboration.

## Makefile Commands
1. `make env` Create conda environment named `ligo`.
2. `make clean`: Clean all output files.
3. `make html`\*: Builds jupyter-book locally.
4. `make html-hub`\*: Builds jupyter-book accessible through jupyter hub.

\*: To run `make html` and `make html-hub`, you must be inside a _Python 3_ environment with _jupyter-book_ installed. The environment `ligo` runs on python 2.7, thus we cannot run `make html` and `make html-hub` under the environment `ligo`. 

## Testing `ligotools` Package

The package `pytest` is not installed by default in the `ligo` environment. To run the test on the `ligotools` package, execute the following line:

```
pip install pytest
pytest ligotools
```