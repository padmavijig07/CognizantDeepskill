-- ==========================
-- CREATE TABLES
-- ==========================

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    customer_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE,
    city VARCHAR(50)
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10,2)
);

CREATE TABLE orders (
    order_id SERIAL PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);

CREATE TABLE order_details (
    order_detail_id SERIAL PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id)
        REFERENCES orders(order_id),
    FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);

-- ==========================
-- INSERT DATA
-- ==========================

INSERT INTO customers (customer_name, email, city) VALUES
('Arjun', 'arjun@gmail.com', 'Chennai'),
('Priya', 'priya@gmail.com', 'Bangalore'),
('Rohan', 'rohan@gmail.com', 'Hyderabad'),
('Sneha', 'sneha@gmail.com', 'Chennai');

INSERT INTO products (product_name, category, price) VALUES
('Laptop', 'Electronics', 65000),
('Mouse', 'Electronics', 800),
('Keyboard', 'Electronics', 1500),
('Office Chair', 'Furniture', 7000);

INSERT INTO orders (customer_id, order_date) VALUES
(1, '2026-01-10'),
(2, '2026-01-12'),
(1, '2026-01-15'),
(3, '2026-01-18');

INSERT INTO order_details (order_id, product_id, quantity) VALUES
(1, 1, 1),
(1, 2, 2),
(2, 3, 1),
(3, 4, 1),
(4, 2, 3);

-- ==========================
-- COUNT RECORDS
-- ==========================

SELECT COUNT(*) FROM customers;
SELECT COUNT(*) FROM products;
SELECT COUNT(*) FROM orders;
SELECT COUNT(*) FROM order_details;

-- ==========================
-- CRUD OPERATIONS
-- ==========================

-- CREATE
INSERT INTO customers (customer_name, email, city)
VALUES ('Kavya', 'kavya@gmail.com', 'Coimbatore');

-- READ
SELECT * FROM customers;

-- UPDATE
UPDATE products
SET price = 68000
WHERE product_id = 1;

-- DELETE
DELETE FROM customers
WHERE customer_id = 5;

-- ==========================
-- JOINS
-- ==========================

-- Customer and Order Details
SELECT
    c.customer_name,
    o.order_date
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id;

-- Customer, Product and Quantity
SELECT
    c.customer_name,
    p.product_name,
    od.quantity
FROM customers c
INNER JOIN orders o
ON c.customer_id = o.customer_id
INNER JOIN order_details od
ON o.order_id = od.order_id
INNER JOIN products p
ON od.product_id = p.product_id;

-- Customers with No Orders
SELECT
    c.customer_name
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;

-- Products and Total Quantity Sold
SELECT
    p.product_name,
    SUM(od.quantity) AS total_quantity
FROM products p
LEFT JOIN order_details od
ON p.product_id = od.product_id
GROUP BY p.product_name;

-- ==========================
-- ALTER TABLE
-- ==========================

-- Add a column
ALTER TABLE customers
ADD COLUMN phone_number VARCHAR(15);

-- Add a default column
ALTER TABLE products
ADD COLUMN stock INT DEFAULT 100;

-- Add a CHECK constraint
ALTER TABLE order_details
ADD CONSTRAINT chk_quantity
CHECK (quantity > 0);

-- Rename a column
ALTER TABLE customers
RENAME COLUMN customer_name TO full_name;

-- Drop a column
ALTER TABLE customers
DROP COLUMN phone_number;