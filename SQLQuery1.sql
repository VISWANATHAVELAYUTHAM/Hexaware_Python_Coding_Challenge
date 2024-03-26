-- Create Product table
CREATE TABLE Product (
    productId INT PRIMARY KEY,
    productName NVARCHAR(255),
    description NVARCHAR(255),
    price FLOAT,
    quantityInStock INT,
    type NVARCHAR(50)
);

-- Create Electronics table (Subclass of Product)
CREATE TABLE Electronics (
    productId INT PRIMARY KEY,
    brand NVARCHAR(255),
    warrantyPeriod INT,
    FOREIGN KEY (productId) REFERENCES Product(productId)
);

-- Create Clothing table (Subclass of Product)
CREATE TABLE Clothing (
    productId INT PRIMARY KEY,
    size NVARCHAR(50),
    color NVARCHAR(50),
    FOREIGN KEY (productId) REFERENCES Product(productId)
);

-- Create User table
CREATE TABLE [User] (
    userId INT PRIMARY KEY,
    username NVARCHAR(50),
    [password] NVARCHAR(50), -- Avoid using "password" as column name, as it's a reserved keyword
    role NVARCHAR(10)
);

-- Create Order table
CREATE TABLE [Order] (
    orderId INT PRIMARY KEY,
    userId INT,
    productId INT,
    FOREIGN KEY (userId) REFERENCES [User](userId),
    FOREIGN KEY (productId) REFERENCES Product(productId)
);