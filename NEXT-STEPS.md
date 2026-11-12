# Next steps — pick up here

_Last updated: 2026-11-12_

## Done ✅

- MySQL Server 8.4.9 installed, service `MySQL84` running on `127.0.0.1:3306`
- MySQL Workbench 26.10, Power BI Desktop, Git 2.56 installed
- Python (Anaconda at `E:\datascience`) queries MySQL via `mysql-connector-python`
- Practice database `practice` seeded:
  customers 800 · products 120 · orders 6000 · order_items 11300 · employees 54
- 15 SQL exercises + solutions verified working
- Starter notebook verified running end-to-end
- Git email set to `maaz.tech07@gmail.com`
- GitHub account created: **maaz-dev07**
- Repo pushed: https://github.com/maaz-dev07/data-journey (public, `main`)
- LinkedIn account created: student, Patliputra University, BSc Zoology

Root password: see `mysql-root-password.txt` on the Desktop (never commit it).

## Now: start learning ⬜

**This week — SQL exercises 1–7**

1. Open MySQL Workbench → connect `127.0.0.1:3306` as `root`
2. Query tab: `USE practice;`
3. Work through `sql/01_exercises.sql`, exercises 1–7
4. Check yourself against `sql/02_solutions.sql` only after trying

**Then the notebook**

Open `notebooks/01_connect_and_explore.ipynb` in VS Code or run `jupyter lab`
from this folder. Change one query and explain what happened.

## Daily loop

```powershell
cd C:\Users\MAAZ\Documents\data-journey
git add .
git commit -m "what you did today"
git push
```

One commit a day beats one big commit a week. This is your public proof of work.

## LinkedIn follow-ups (do this week)

- [ ] Add a photo
- [ ] Headline: `Aspiring Data Analyst | SQL, Python, Excel | BSc Zoology @ Patliputra University`
- [ ] Add education
- [ ] Add skills as you learn them (SQL now, Python when comfortable, Power BI after first dashboard)
- [ ] Follow 10 data people/companies
- [ ] Leave "Open to work" OFF until you have 1–2 projects

## Note

Your Anaconda has a modified `pymysql` that breaks on `%` in SQL. Use
`mysql+mysqlconnector://` in notebooks (already set up). The seed script is fine.
