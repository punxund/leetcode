# https://leetcode.com/problems/recyclable-and-low-fat-products/description/?envType=study-plan-v2&envId=top-sql-50

CREATE TABLE Products (
  product_id INT PRIMARY KEY,
  low_fats ENUM('Y', 'N'),
  recyclable ENUM('Y', 'N')
);

INSERT INTO Products VALUES
(0, 'Y', 'N'),
(1, 'Y', 'Y'),
(2, 'N', 'Y'),
(3, 'Y', 'Y'),
(4, 'N', 'N');

SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';