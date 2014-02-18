--What customers are from the UK
SELECT * FROM Customers WHERE Country = 'UK';

--What is the name of the customer who has the most orders?
SELECT Customers.CustomerName, COUNT(*) FROM Customers
JOIN Orders on (Orders.CustomerID = Customers.CustomerID)
GROUP BY Customers.CustomerName
ORDER BY COUNT(*) DESC;

--What supplier has the highest average product price?
SELECT Suppliers.SupplierName, AVG(Products.Price) FROM Products
JOIN Suppliers on (Suppliers.SupplierID = Products.SupplierID)
GROUP BY Suppliers.SupplierName
ORDER BY AVG(Products.Price) DESC;

--What category has the most orders?
SELECT Categories.CategoryName, COUNT(OrderDetails.ProductID) FROM OrderDetails
	INNER JOIN Products on Products.ProductID = OrderDetails.ProductID
	INNER JOIN Categories on Categories.CategoryID = Products.CategoryID
GROUP BY Categories.CategoryID
ORDER BY COUNT(OrderDetails.ProductID) DESC;


--What employee made the most sales (by number of sales)?
--Wasn't sure how to get full details from employees but can from your example that I could just use Employees. to get all info
SELECT Employees.FirstName, COUNT(Orders.EmployeeID) FROM Orders
JOIN Employees ON (Employees.EmployeeID = Orders.EmployeeID)
GROUP BY Employees.FirstName
ORDER BY COUNT(*) DESC;	


--What employee made the most sales (by value of sales)?
--Struggled with this one until I saw the use of AS in your example...makes sense now
SELECT Employees.FirstName, SUM(Product.Price * OrderDetails.Quantity) From OrderDetails
	INNER JOIN Employees ON 
	INNER JOIN
	INNER JOIN
GROUP BY 
ORDER BY


--What employees have BS degrees? (Hint: Look at LIKE operator)
--No idea how to complete this but have your example now using LIKE '%BS%'

--What supplier has the highest average product price assuming they have at least 2 products (Hint: Look at the HAVING operator)#
--Not sure on this one but have the example to study