#https://leetcode.com/problems/replace-employee-id-with-the-unique-identifier/description/?envType=study-plan-v2&envId=top-sql-50

CREATE TABLE Employees (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE EmployeeUNI (
    id INT,
    unique_id INT,
    PRIMARY KEY (id, unique_id),
    FOREIGN KEY (id) REFERENCES Employees(id)
);

-- Employees 테이블 데이터
INSERT INTO Employees (id, name) VALUES
(1, 'Alice'),
(7, 'Bob'),
(11, 'Meir'),
(90, 'Winston'),
(3, 'Jonathan');

-- EmployeeUNI 테이블 데이터
INSERT INTO EmployeeUNI (id, unique_id) VALUES
(3, 1),
(11, 2),
(90, 3);

SELECT e.id, e.name, u.unique_id
FROM Employees e
LEFT JOIN EmployeeUNI u ON e.id = u.id;