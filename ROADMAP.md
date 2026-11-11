# Roadmap: beginner → Data Analyst / Data Scientist

Rule of thumb: **SQL and pandas get you interviews. Projects get you offers.**

---

## 12-week plan (adjust dates, keep the order)

| Weeks | Focus | Deliverable |
|---|---|---|
| 1–2 | SQL basics: SELECT, WHERE, ORDER BY, GROUP BY, HAVING | Exercises 1–7 done |
| 3–4 | SQL joins, subqueries, CTEs, **window functions** | Exercises 8–15 done |
| 5 | Power BI: import, model, 3 visuals | 1-page sales dashboard |
| 6–7 | pandas: load, clean, groupby, merge, pivot | Notebook reproducing 5 SQL answers in pandas |
| 8 | Statistics: distributions, hypothesis tests, A/B test | Notebook analysing an A/B test |
| 9–10 | Machine learning: regression + classification (sklearn) | Model with cross-validation + metrics |
| 11 | Portfolio project 1: SQL + dashboard | Public repo + README |
| 12 | Portfolio project 2: ML end-to-end | Public repo + README |

Then repeat the project loop. **Three solid projects > ten certificates.**

## SQL checklist (tick these off)

- [ ] SELECT / WHERE / ORDER BY / LIMIT
- [ ] Aggregate functions + GROUP BY + HAVING
- [ ] INNER vs LEFT JOIN (know when LEFT matters)
- [ ] Subqueries (scalar, IN, EXISTS)
- [ ] CTEs (`WITH ...`)
- [ ] Window functions: `ROW_NUMBER`, `RANK`, `SUM() OVER`, `LAG/LEAD`
- [ ] CASE WHEN for bucketing
- [ ] Date functions: `DATE_FORMAT`, `DATE_ADD`, `DATEDIFF`
- [ ] `COALESCE`, `NULLIF`, NULL behaviour in aggregates
- [ ] Query performance basics: indexes, `EXPLAIN`

## Weekly rhythm (2 hours/day, 5 days)

- 30 min — review yesterday (no notes, rewrite a query from memory)
- 60 min — new topic
- 30 min — apply it to the `practice` database
- 10 min — commit + one-line note on what you learned

---

## GitHub: set up once, then it's automatic

Git is installed. One-time setup:

```powershell
git config --global user.name "Your Name"
git config --global user.email "you@example.com"   # use the email on your GitHub account
```

Create the repo on github.com (New repository → name `data-journey` → **no** README),
then connect this folder and push:

```powershell
cd C:\Users\MAAZ\Documents\data-journey
git remote add origin https://github.com/YOUR-USERNAME/data-journey.git
git push -u origin main
```

Daily loop:

```powershell
git add .
git commit -m "short description of what changed"
git push
```

Never commit passwords. `.gitignore` already blocks `.env` and `*password*.txt`.

## LinkedIn checklist (30 minutes, once)

- [ ] Real photo, clear headshot
- [ ] Headline: `Aspiring Data Analyst | SQL, Python, Power BI`
- [ ] Education filled in
- [ ] Skills added **as you learn them** (SQL, pandas, Power BI, statistics...)
- [ ] Follow 10 companies/people in data
- [ ] Post when your first project is done (link + 3 sentences on what you learned)

Do not claim skills you can't discuss. Update it monthly, not daily.

---

## Honest expectations

- **Data analyst** roles are more numerous and more entry-friendly.
- **Data scientist** roles usually expect statistics depth + ML + often a degree; the analyst path is the realistic bridge.
- The gap between "finished a course" and "hireable" is **projects that answer a real question**, with a README explaining the *why*.
- Interviews test SQL hardest. Practise writing queries by hand, not just reading them.
