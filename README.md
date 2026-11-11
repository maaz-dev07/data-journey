# data-journey

My path from beginner to **Data Analyst / Data Scientist**, built in public.

## What's here

```
data-journey/
├── notebooks/          Jupyter notebooks (analysis, pandas, ML later)
│   └── 01_connect_and_explore.ipynb
├── sql/                SQL practice exercises + solutions
│   ├── 01_exercises.sql
│   └── 02_solutions.sql
├── scripts/
│   └── seed_practice_db.py   recreates the practice database
└── ROADMAP.md          12-week plan + checklists
```

## Environment

| Tool | Purpose |
|---|---|
| MySQL 8.4 + Workbench | SQL practice (database `practice`) |
| Anaconda / Python 3.12 (`E:\datascience`) | pandas, Jupyter, scikit-learn |
| Power BI Desktop | dashboards |
| VS Code + Git | editing + version control |

## Start here

1. Open MySQL Workbench → connect to `127.0.0.1:3306` as `root`
2. In the query tab: `USE practice;` then `SHOW TABLES;`
3. Work through `sql/01_exercises.sql` (answers in `02_solutions.sql`)
4. Open the notebook: `jupyter lab` from this folder, or open
   `notebooks/01_connect_and_explore.ipynb` in VS Code

## Rebuild the practice database

```powershell
$env:MYSQL_ROOT_PASSWORD = "your-root-password"
E:\datascience\python.exe scripts\seed_practice_db.py
```

The password is read from an environment variable on purpose — **never commit passwords**.
