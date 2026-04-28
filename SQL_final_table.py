import sqlite3

# Создание и подключение к БД
connection = sqlite3.connect('electronics_store.db')
cursor = connection.cursor()

# Включаем поддержку внешних ключей
cursor.execute("PRAGMA foreign_keys = ON")

# 1. Удаление старых таблиц
cursor.execute("DROP TABLE IF EXISTS orders")
cursor.execute("DROP TABLE IF EXISTS products")
cursor.execute("DROP TABLE IF EXISTS customers")

# 2. Создание таблицы клиентов (Customers)
cursor.execute("""
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email_address TEXT UNIQUE NOT NULL,
    phone_number TEXT,
    city TEXT DEFAULT 'Москва',
    registered_at TEXT DEFAULT CURRENT_TIMESTAMP
)
""")

# 3. Создание таблицы товаров (Products)
cursor.execute("""
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    item_name TEXT NOT NULL,
    brand_name TEXT NOT NULL,
    category TEXT,
    price_usd REAL NOT NULL,
    stock_quantity INTEGER DEFAULT 0,
    is_available BOOLEAN DEFAULT 1
)
""")

# 4. Создание таблицы заказов (Orders)
cursor.execute("""
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    client_id INTEGER NOT NULL,
    item_id INTEGER NOT NULL,
    order_date TEXT NOT NULL,
    delivery_date TEXT,
    total_amount REAL,
    order_status TEXT CHECK(order_status IN ('new', 'shipped', 'delivered', 'cancelled')),
    FOREIGN KEY (client_id) REFERENCES customers(customer_id) ON DELETE CASCADE,
    FOREIGN KEY (item_id) REFERENCES products(product_id) ON DELETE SET NULL
)
""")

# 5. Заполнение таблицы customers (15 записей)
customers = [
    ("Иван Петров", "ivan.petrov@mail.ru", "+7-900-123-45-67", "Москва", "2024-01-15"),
    ("Мария Смирнова", "maria.smirnova@yandex.ru", "+7-911-234-56-78", "Санкт-Петербург", "2024-02-20"),
    ("Алексей Козлов", "alex.kozlov@gmail.com", "+7-925-345-67-89", "Казань", "2024-03-10"),
    ("Елена Морозова", "elena.morozova@mail.ru", "+7-903-456-78-90", "Новосибирск", "2024-03-25"),
    ("Дмитрий Волков", "dmitry.volkov@yandex.ru", "+7-918-567-89-01", "Екатеринбург", "2024-04-05"),
    ("Ольга Лебедева", "olga.lebedeva@gmail.com", "+7-926-678-90-12", "Москва", "2024-04-18"),
    ("Сергей Соколов", "sergey.sokolov@mail.ru", "+7-909-789-01-23", "Нижний Новгород", "2024-05-02"),
    ("Анна Кузнецова", "anna.kuznetsova@yandex.ru", "+7-917-890-12-34", "Самара", "2024-05-20"),
    ("Максим Попов", "maxim.popov@gmail.com", "+7-904-901-23-45", "Челябинск", "2024-06-08"),
    ("Наталья Васильева", "natalya.vasilieva@mail.ru", "+7-921-012-34-56", "Санкт-Петербург", "2024-06-25"),
    ("Андрей Михайлов", "andrey.mikhailov@yandex.ru", "+7-912-123-45-67", "Пермь", "2024-07-10"),
    ("Екатерина Новикова", "ekaterina.novikova@gmail.com", "+7-906-234-56-78", "Краснодар", "2024-07-28"),
    ("Павел Федоров", "pavel.fedorov@mail.ru", "+7-915-345-67-89", "Воронеж", "2024-08-15"),
    ("Юлия Романова", "yulia.romanova@yandex.ru", "+7-908-456-78-90", "Ростов-на-Дону", "2024-09-01"),
    ("Николай Григорьев", "nikolay.grigoriev@gmail.com", "+7-922-567-89-01", "Уфа", "2024-09-20")
]

cursor.executemany("""
    INSERT INTO customers (name, email_address, phone_number, city, registered_at) 
    VALUES (?, ?, ?, ?, ?)
""", customers)

# 6. Заполнение таблицы products (15 записей)
products = [
    ("iPhone 15 Pro", "Apple", "Смартфоны", 999.99, 50, 1),
    ("Samsung Galaxy S24", "Samsung", "Смартфоны", 899.99, 45, 1),
    ("MacBook Pro 16", "Apple", "Ноутбуки", 2499.99, 20, 1),
    ("Dell XPS 15", "Dell", "Ноутбуки", 1799.99, 30, 1),
    ("Sony WH-1000XM5", "Sony", "Наушники", 349.99, 100, 1),
    ("AirPods Pro 2", "Apple", "Наушники", 249.99, 80, 1),
    ("iPad Air 5", "Apple", "Планшеты", 599.99, 40, 1),
    ("Samsung Galaxy Tab S9", "Samsung", "Планшеты", 549.99, 35, 1),
    ("Apple Watch Series 9", "Apple", "Часы", 399.99, 60, 1),
    ("Xiaomi Mi Band 8", "Xiaomi", "Часы", 49.99, 200, 1),
    ("Canon EOS R6", "Canon", "Камеры", 2499.99, 15, 1),
    ("GoPro Hero 12", "GoPro", "Камеры", 399.99, 25, 1),
    ("LG OLED C3 55", "LG", "Телевизоры", 1499.99, 10, 1),
    ("PlayStation 5", "Sony", "Игровые консоли", 499.99, 30, 1),
    ("Nintendo Switch OLED", "Nintendo", "Игровые консоли", 349.99, 40, 1)
]

cursor.executemany("""
    INSERT INTO products (item_name, brand_name, category, price_usd, stock_quantity, is_available) 
    VALUES (?, ?, ?, ?, ?, ?)
""", products)

# 7. Заполнение таблицы orders (15 записей)
orders = [
    (1, 1, "2024-01-20", "2024-01-25", 999.99, "delivered"),
    (2, 2, "2024-02-25", "2024-03-01", 899.99, "delivered"),
    (3, 3, "2024-03-15", "2024-03-20", 2499.99, "delivered"),
    (4, 5, "2024-04-01", "2024-04-05", 349.99, "delivered"),
    (5, 6, "2024-04-20", "2024-04-25", 249.99, "delivered"),
    (6, 7, "2024-05-05", "2024-05-10", 599.99, "shipped"),
    (7, 8, "2024-05-25", "2024-05-30", 399.99, "shipped"),
    (8, 9, "2024-06-10", "2024-06-15", 49.99, "delivered"),
    (9, 10, "2024-06-28", "2024-07-03", 1799.99, "delivered"),
    (10, 11, "2024-07-15", "2024-07-20", 549.99, "shipped"),
    (11, 12, "2024-08-01", "2024-08-05", 2499.99, "new"),
    (12, 13, "2024-08-20", "2024-08-25", 399.99, "new"),
    (13, 14, "2024-09-05", "2024-09-10", 1499.99, "shipped"),
    (14, 15, "2024-09-25", "2024-09-30", 499.99, "new"),
    (15, 4, "2024-10-01", "2024-08-23", 999.99, "cancelled")
]

cursor.executemany("""
    INSERT INTO orders (client_id, item_id, order_date, delivery_date, total_amount, order_status) 
    VALUES (?, ?, ?, ?, ?, ?)
""", orders)

connection.commit()
connection.close()

