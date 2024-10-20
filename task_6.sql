-- Insert multiple rows into the Customers table
INSERT INTO Customers (customer_id, customer_name, email, address) VALUES
    (2, 'Blessing Malik', 'bmalik@sandtech.com', '124 Happiness Ave.'),
    (3, 'Obed Ehoneah', 'eobed@sandtech.com', '125 Happiness Ave.'),
    (4, 'Nehemial Kamolu', 'nkamolu@sandtech.com', '126 Happiness Ave.');
-- Insert multiple rows into the Customers table without specifying customer_id
INSERT INTO Customers (customer_name, email, address) VALUES
    ('Blessing Malik', 'bmalik@sandtech.com', '124 Happiness Ave.'),
    ('Obed Ehoneah', 'eobed@sandtech.com', '125 Happiness Ave.'),
    ('Nehemial Kamolu', 'nkamolu@sandtech.com', '126 Happiness Ave.');
