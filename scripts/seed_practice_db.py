"""
Seed a realistic practice database for SQL / pandas learning.

Usage (PowerShell):
    $env:MYSQL_ROOT_PASSWORD = "your-password"
    E:\\datascience\\python.exe scripts\\seed_practice_db.py

Creates schema `practice` with:
    customers, products, orders, order_items, employees
Safe to re-run: it drops and recreates the tables.
"""
import os
import random
from datetime import date, datetime, timedelta

import pymysql

HOST = "127.0.0.1"
PORT = 3306
USER = "root"
PASSWORD = os.environ.get("MYSQL_ROOT_PASSWORD")
DB = "practice"

if not PASSWORD:
    raise SystemExit("Set MYSQL_ROOT_PASSWORD env var before running this script.")

random.seed(42)

FIRST = ["Aisha", "Ben", "Carlos", "Dana", "Eli", "Fatima", "Grace", "Hiro", "Ivan",
         "Jana", "Kofi", "Lena", "Marco", "Nadia", "Omar", "Priya", "Quinn", "Rosa",
         "Sam", "Tariq", "Uma", "Victor", "Wen", "Xena", "Yusuf", "Zara", "Noah",
         "Maya", "Leo", "Sofia", "Ethan", "Chloe", "Adam", "Nina", "Raj", "Elena"]
LAST = ["Khan", "Miller", "Garcia", "Chen", "Novak", "Ali", "Okafor", "Tanaka",
        "Petrov", "Silva", "Mensah", "Fischer", "Rossi", "Haddad", "Ibrahim",
        "Sharma", "Murphy", "Lopez", "Brown", "Aziz", "Nair", "Costa", "Wang",
        "Kim", "Yilmaz", "Ahmed", "Smith", "Dubois", "Meyer", "Andersson"]

CITIES = [("Karachi", "Pakistan"), ("Lahore", "Pakistan"), ("Dubai", "UAE"),
          ("London", "UK"), ("Berlin", "Germany"), ("Paris", "France"),
          ("Toronto", "Canada"), ("New York", "USA"), ("Austin", "USA"),
          ("Sydney", "Australia"), ("Singapore", "Singapore"), ("Tokyo", "Japan"),
          ("Mumbai", "India"), ("Istanbul", "Turkey"), ("Madrid", "Spain")]

CATEGORIES = {
    "Electronics": (49, 1299),
    "Clothing": (12, 180),
    "Home": (15, 450),
    "Sports": (10, 600),
    "Books": (6, 45),
    "Beauty": (8, 120),
    "Toys": (7, 200),
    "Grocery": (2, 40),
}
ADJ = ["Pro", "Ultra", "Classic", "Eco", "Smart", "Mini", "Max", "Prime", "Flex", "Core"]
NOUNS = {
    "Electronics": ["Headphones", "Speaker", "Keyboard", "Camera", "Monitor", "Tablet",
                    "Smartwatch", "Charger", "Router", "Mouse"],
    "Clothing": ["Jacket", "Sneakers", "T-Shirt", "Jeans", "Hoodie", "Socks",
                 "Scarf", "Belt", "Cap", "Sweater"],
    "Home": ["Blender", "Lamp", "Chair", "Desk", "Mug", "Towel", "Bottle",
             "Curtain", "Rug", "Kettle"],
    "Sports": ["Yoga Mat", "Dumbbell", "Water Bottle", "Running Shoes", "Backpack",
               "Jump Rope", "Gloves", "Football", "Racket", "Helmet"],
    "Books": ["Novel", "Cookbook", "Textbook", "Biography", "Guide", "Journal",
              "Anthology", "Manual", "Almanac", "Handbook"],
    "Beauty": ["Serum", "Shampoo", "Moisturizer", "Lipstick", "Sunscreen", "Perfume",
               "Cleanser", "Face Mask", "Lotion", "Lip Balm"],
    "Toys": ["Puzzle", "Board Game", "Doll", "Building Blocks", "Action Figure",
             "RC Car", "Plush Toy", "Kite", "Train Set", "Slime Kit"],
    "Grocery": ["Coffee", "Tea", "Pasta", "Olive Oil", "Chocolate", "Honey",
                "Rice", "Cereal", "Snack Mix", "Spice Set"],
}

STATUS = ["completed"] * 78 + ["shipped"] * 10 + ["pending"] * 6 + ["cancelled"] * 4 + ["returned"] * 2
CHANNELS = ["web"] * 45 + ["mobile"] * 30 + ["store"] * 18 + ["phone"] * 7

DEPARTMENTS = {
    "Sales": (45000, 95000),
    "Marketing": (42000, 88000),
    "Engineering": (65000, 150000),
    "Support": (35000, 65000),
    "Finance": (50000, 110000),
    "Operations": (38000, 80000),
}
TITLES = {
    "Sales": ["Sales Rep", "Account Executive", "Sales Manager"],
    "Marketing": ["Marketing Analyst", "Content Lead", "Marketing Manager"],
    "Engineering": ["Data Engineer", "Software Engineer", "Engineering Manager"],
    "Support": ["Support Agent", "Support Lead", "Support Manager"],
    "Finance": ["Financial Analyst", "Controller", "Finance Manager"],
    "Operations": ["Ops Analyst", "Ops Coordinator", "Operations Manager"],
}


def random_date(start: date, end: date) -> date:
    return start + timedelta(days=random.randint(0, (end - start).days))


def main() -> None:
    conn = pymysql.connect(host=HOST, port=PORT, user=USER, password=PASSWORD,
                           charset="utf8mb4", autocommit=False)
    cur = conn.cursor()

    cur.execute(f"CREATE DATABASE IF NOT EXISTS {DB} "
                "CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci")
    cur.execute(f"USE {DB}")
    cur.execute("SET FOREIGN_KEY_CHECKS = 0")
    for t in ("order_items", "orders", "products", "customers", "employees"):
        cur.execute(f"DROP TABLE IF EXISTS {t}")
    cur.execute("SET FOREIGN_KEY_CHECKS = 1")

    cur.execute("""
        CREATE TABLE customers (
            customer_id  INT PRIMARY KEY AUTO_INCREMENT,
            first_name   VARCHAR(50)  NOT NULL,
            last_name    VARCHAR(50)  NOT NULL,
            email        VARCHAR(120) NOT NULL UNIQUE,
            city         VARCHAR(60)  NOT NULL,
            country      VARCHAR(60)  NOT NULL,
            signup_date  DATE         NOT NULL
        ) ENGINE=InnoDB
    """)
    cur.execute("""
        CREATE TABLE products (
            product_id   INT PRIMARY KEY AUTO_INCREMENT,
            product_name VARCHAR(120) NOT NULL,
            category     VARCHAR(40)  NOT NULL,
            unit_price   DECIMAL(10,2) NOT NULL,
            unit_cost    DECIMAL(10,2) NOT NULL,
            is_active    TINYINT(1)   NOT NULL DEFAULT 1
        ) ENGINE=InnoDB
    """)
    cur.execute("""
        CREATE TABLE orders (
            order_id    INT PRIMARY KEY AUTO_INCREMENT,
            customer_id INT NOT NULL,
            order_date  DATETIME NOT NULL,
            status      ENUM('completed','shipped','pending','cancelled','returned') NOT NULL,
            channel     ENUM('web','mobile','store','phone') NOT NULL,
            CONSTRAINT fk_orders_customer FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
        ) ENGINE=InnoDB
    """)
    cur.execute("""
        CREATE TABLE order_items (
            order_item_id INT PRIMARY KEY AUTO_INCREMENT,
            order_id      INT NOT NULL,
            product_id    INT NOT NULL,
            quantity      INT NOT NULL,
            unit_price    DECIMAL(10,2) NOT NULL,
            discount      DECIMAL(4,2)  NOT NULL DEFAULT 0.00,
            CONSTRAINT fk_items_order   FOREIGN KEY (order_id)   REFERENCES orders(order_id),
            CONSTRAINT fk_items_product FOREIGN KEY (product_id) REFERENCES products(product_id)
        ) ENGINE=InnoDB
    """)
    cur.execute("""
        CREATE TABLE employees (
            employee_id INT PRIMARY KEY AUTO_INCREMENT,
            first_name  VARCHAR(50) NOT NULL,
            last_name   VARCHAR(50) NOT NULL,
            department  VARCHAR(40) NOT NULL,
            job_title   VARCHAR(60) NOT NULL,
            salary      DECIMAL(10,2) NOT NULL,
            hire_date   DATE NOT NULL,
            manager_id  INT NULL,
            CONSTRAINT fk_emp_manager FOREIGN KEY (manager_id) REFERENCES employees(employee_id)
        ) ENGINE=InnoDB
    """)

    # --- customers -------------------------------------------------------
    customers = []
    used_emails = set()
    for i in range(1, 801):
        fn, ln = random.choice(FIRST), random.choice(LAST)
        city, country = random.choice(CITIES)
        base = f"{fn.lower()}.{ln.lower()}{i}"
        email = f"{base}@example.com"
        while email in used_emails:
            email = f"{base}{random.randint(1, 999)}@example.com"
        used_emails.add(email)
        customers.append((fn, ln, email, city, country,
                          random_date(date(2021, 1, 1), date(2026, 10, 1))))
    cur.executemany(
        "INSERT INTO customers (first_name,last_name,email,city,country,signup_date) "
        "VALUES (%s,%s,%s,%s,%s,%s)", customers)

    # --- products --------------------------------------------------------
    products = []
    for _ in range(120):
        cat = random.choice(list(CATEGORIES))
        lo, hi = CATEGORIES[cat]
        price = round(random.uniform(lo, hi), 2)
        cost = round(price * random.uniform(0.40, 0.75), 2)
        products.append((f"{random.choice(ADJ)} {random.choice(NOUNS[cat])} {random.randint(1, 99)}",
                         cat, price, cost, 1 if random.random() > 0.1 else 0))
    cur.executemany(
        "INSERT INTO products (product_name,category,unit_price,unit_cost,is_active) "
        "VALUES (%s,%s,%s,%s,%s)", products)

    # --- orders ----------------------------------------------------------
    orders = []
    start, end = datetime(2024, 1, 1), datetime(2026, 10, 31)
    span_days = (end - start).days
    for _ in range(6000):
        # seasonality: more orders in Nov/Dec
        d = start + timedelta(days=random.randint(0, span_days))
        if d.month in (11, 12) and random.random() < 0.45:
            d = d.replace(year=d.year if d.year < 2026 else 2025,
                          month=random.choice([11, 12]),
                          day=random.randint(1, 28))
        ts = d.replace(hour=random.randint(7, 22), minute=random.randint(0, 59),
                       second=random.randint(0, 59))
        orders.append((random.randint(1, 800), ts,
                       random.choice(STATUS), random.choice(CHANNELS)))
    cur.executemany(
        "INSERT INTO orders (customer_id,order_date,status,channel) VALUES (%s,%s,%s,%s)", orders)

    # --- order_items -----------------------------------------------------
    product_prices = {i + 1: p[2] for i, p in enumerate(products)}
    items = []
    for order_id in range(1, 6001):
        for _ in range(random.choices([1, 2, 3, 4], weights=[45, 30, 17, 8])[0]):
            pid = random.randint(1, 120)
            items.append((order_id, pid,
                          random.choices([1, 2, 3], weights=[75, 18, 7])[0],
                          product_prices[pid],
                          random.choices([0.00, 0.05, 0.10, 0.15, 0.20],
                                         weights=[60, 15, 12, 8, 5])[0]))
    cur.executemany(
        "INSERT INTO order_items (order_id,product_id,quantity,unit_price,discount) "
        "VALUES (%s,%s,%s,%s,%s)", items)

    # --- employees (3-level hierarchy) -----------------------------------
    employees = []
    for dept, (lo, hi) in DEPARTMENTS.items():
        titles = TITLES[dept]           # [staff, lead, manager]
        # manager first so the self-referencing FK is satisfied
        employees.append((random.choice(FIRST), random.choice(LAST), dept, titles[-1],
                          round(random.uniform(hi * 0.75, hi), 2),
                          random_date(date(2015, 1, 1), date(2020, 12, 31)), None))
        manager_id = len(employees)
        employees.append((random.choice(FIRST), random.choice(LAST), dept, titles[-2],
                          round(random.uniform(lo, hi * 0.7), 2),
                          random_date(date(2016, 1, 1), date(2023, 12, 31)), manager_id))
        for _ in range(7):
            employees.append((random.choice(FIRST), random.choice(LAST), dept, titles[0],
                              round(random.uniform(lo, hi * 0.55), 2),
                              random_date(date(2018, 1, 1), date(2026, 9, 1)), manager_id))
    cur.executemany(
        "INSERT INTO employees (first_name,last_name,department,job_title,salary,hire_date,manager_id) "
        "VALUES (%s,%s,%s,%s,%s,%s,%s)", employees)

    conn.commit()

    counts = {}
    for t in ("customers", "products", "orders", "order_items", "employees"):
        cur.execute(f"SELECT COUNT(*) FROM {t}")
        counts[t] = cur.fetchone()[0]
    cur.execute("""
        SELECT ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2)
        FROM order_items oi JOIN orders o ON o.order_id = oi.order_id
        WHERE o.status = 'completed'
    """)
    revenue = cur.fetchone()[0]

    conn.close()
    print("Practice database ready.")
    for k, v in counts.items():
        print(f"  {k:<12} {v:>6} rows")
    print(f"  completed revenue  {revenue:>12,.2f}")


if __name__ == "__main__":
    main()
