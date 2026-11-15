# ledger

Reference version of `ledger`, the application built step by step in the labs of **Software Management & Development** (IE University, MFT & MCSDI). The labs and notes are at [ami232/ie-smd](https://github.com/ami232/ie-smd).

Personal finance ledger: balances, spending and monthly reports from a CSV file.

## Versions

Each tag is the state of the project **at the start of a session**, which is also the solution of the previous lab:

| Tag | Start of | Contents |
|---|---|---|
| `s05-start` | session 5 (Git) | the result of Lab 4: Python 3.14 project with uv, `rich` for the table, Ruff as a development dependency, a VS Code debug configuration |

If you fall behind, copy the files of the tag for your session into your own repository (on GitHub: switch to the tag, then **Code → Download ZIP**). Don't fork or clone this repository as your own: your repository must have your own history.

## Run it

```bash
uv run ledger balance
uv run ledger spending
```
## Roadmap

- Monthly report of income and spending
- A database instead of a CSV file
- A web API and a dashboard

## Author
<madsarne8-sketch>, <mads.myklebust@student.ie.edu>
