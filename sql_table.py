import sqlite3

# Создание и подключение к БД
connection = sqlite3.connect('electronics_store.db')
cursor = connection.cursor()

# Включаем поддержку внешних ключей
cursor.execute("PRAGMA foreign_keys = ON")

# 1. Удаление старых таблиц (если они есть)
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



users = [
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


cursor.execute("""
INSERT INTO customers (name,email_address,phone_number,city,registered_at) VALUES (?,?,?,?,?)
""",users)

connection.commit()