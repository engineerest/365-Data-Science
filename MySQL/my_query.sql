

CREATE TABLE IF NOT EXISTS customers
(
	customer_id INT AUTO_INCREMENT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email_address VARCHAR(255),
    number_of_complaints INT,
    PRIMARY KEY (customer_id),
    UNIQUE KEY (email_address)
);

ALTER TABLE customers
ADD UNIQUE KEY (email_address);



CREATE TABLE IF NOT EXISTS customers
(
	customer_id INT AUTO_INCREMENT,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    email_address VARCHAR(255),
    number_of_complaints INT,
    PRIMARY KEY (customer_id)
);

# ALTER TABLE customers
# ADD COLUMN gender ENUM('M', 'F') AFTER last_name;


ALTER TABLE customers
CHANGE COLUMN number_of_complaints number_of_complaints INT DEFAULT 0;


INSERT INTO customers (first_name, last_name, gender, email_address, number_of_complaints) VALUES ('John', 'Mackinley', 'M', 'join.mckinley@465datascience.com', 0);

INSERT INTO customers (first_name, last_name, gender) VALUES ('Peter', 'Figaro', 'M');
SELECT * FROM customers;

ALTER TABLE customers
ALTER COLUMN number_of_complaints DROP DEFAULT;



CREATE TABLE  IF NOT EXISTS items
(
	item_code VARCHAR(255),
    item VARCHAR(255),
    unit_price NUMERIC(10, 2)
);


CREATE TABLE IF NOT EXISTS sales.sales
(
	purchase_number INT AUTO_INCREMENT,
    date_of_purchase DATE,
    customer_id INT,
    item_code VARCHAR(10),
PRIMARY KEY (purchase_number),
FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS sales.companies
(
    company_id VARCHAR(255),
	company_name VARCHAR(255),
    headquaters_phone_number VARCHAR(255),
    PRIMARY KEY (company_id)
);


ALTER TABLE companies
MODIFY company_name VARCHAR(255) NULL;

ALTER TABLE companies
CHANGE COLUMN company_name company_name VARCHAR(255) NOT NULL;

INSERT INTO companies (headquaters_phone_number, company_name) VALUES ('+1 (202) 555-0196', 'Company A');

SELECT * FROM companies;

ALTER TABLE sales
ADD FOREIGN KEY (customer_id) REFERENCES customers(customer_id) ON DELETE CASCADE;

