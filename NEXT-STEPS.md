# Next steps — pick up here

_Last updated: 2026-11-11 (end of setup day)_

## Done ✅

- MySQL Server 8.4.9 installed, service `MySQL84` running on `127.0.0.1:3306`
- MySQL Workbench 26.10, Power BI Desktop, Git 2.56 installed
- Python (Anaconda at `E:\datascience`) can query MySQL via `mysql-connector-python`
- Practice database `practice` seeded:
  customers 800 · products 120 · orders 6000 · order_items 11300 · employees 54
- This repo initialised, 2 commits on `main`
- 15 SQL exercises + solutions verified working
- Starter notebook verified running end-to-end

Root password: see `mysql-root-password.txt` on the Desktop.

## Pending — do these first ⬜

1. **Set your real Git email** (currently the placeholder `maaz@example.com`):
   ```powershell
   git config --global user.email "you@example.com"
   ```

2. **Create a GitHub account** at github.com (verify the email).

3. **Create the repo and push** — on github.com: New repository → `data-journey`
   → Public → no README. Then in a NEW terminal:
   ```powershell
   cd C:\Users\MAAZ\Documents\data-journey
   git remote add origin https://github.com/YOUR-USERNAME/data-journey.git
   git push -u origin main
   ```
   A browser window will open for sign-in — that is Git Credential Manager, approve it.

4. **Create a LinkedIn account** — photo, headline
   `Aspiring Data Analyst | SQL, Python`, education, follow 10 data people.
   Checklist is in `ROADMAP.md`.

## First learning task

Open MySQL Workbench → connect `127.0.0.1:3306` as `root` → `USE practice;`
then work through `sql/01_exercises.sql`, exercises **1–7**.

Commit daily:
```powershell
git add .
git commit -m "what you did today"
git push
```

## Note

Your Anaconda has a modified `pymysql` that breaks on `%` in SQL. Use
`mysql+mysqlconnector://` in notebooks (already set up). The seed script is fine.
