CREATE DATABASE wine_shop;
SELECT * FROM wine_shop.collection;
SELECT * FROM wine_shop.customer;
SELECT * FROM wine_shop.grape_varieties;
SELECT * FROM wine_shop.manufacturer;
SELECT * FROM wine_shop.order;
SELECT * FROM wine_shop.order_wine;
SELECT * FROM wine_shop.payment;
SELECT * FROM wine_shop.supplier;
SELECT * FROM wine_shop.wine;
SELECT * FROM wine_shop.wine_grape_varieties;
SELECT * FROM wine_shop.wine_winestore;
SELECT * FROM wine_shop.winestore;
SELECT * FROM wine_shop.winestore_supplier;

-- 1 Show all customers that commands wine that have more and equal than 10 years. Order in decreasing by the number of wines.
SELECT last_name, first_name, SUM(quantity) as 'Number of wines'
FROM Customer
JOIN `Order` ON Customer.id = `Order`.customer_id
JOIN order_wine ON `Order`.id = order_id
JOIN Wine ON wine_id = Wine.id
WHERE Wine.year <= YEAR(NOW())-10
GROUP BY first_name, last_name
ORDER BY SUM(quantity) DESC;

-- 2 Shows all wines that have wine grape varieties bigger than 30%, acidity of grapes is bigger than 3.7 and group them by manufacturer.
SELECT DISTINCT manufacturer.name, wine.name, percent, acidity
FROM Wine
JOIN wine_grape_varieties ON wine_grape_varieties.wine_id = wine.id
JOIN grape_varieties ON grape_varieties.id = wine_grape_varieties.variety_id
JOIN manufacturer ON manufacturer.id = wine.manufacturer_id
WHERE percent > 30 AND acidity > 3.7
GROUP BY wine_shop.manufacturer.name, wine_shop.wine.name, percent, acidity;

-- 3 Show all wines than all bought last month and are from same manufacturer and supplier.
SELECT DISTINCT Wine.name
FROM Wine
JOIN manufacturer ON wine.manufacturer_id = manufacturer.id
JOIN wine_winestore ON wine.id = wine_winestore.wine_id
JOIN winestore ON winestore.id = wine_winestore.winestore_id
JOIN winestore_supplier ON winestore_supplier.winestore_id = winestore.id
JOIN supplier ON supplier.id = winestore_supplier.supplier_id
JOIN order_wine ON Wine.id = order_wine.wine_id
JOIN `Order` ON order_wine.order_id = `Order`.id
WHERE supplier.name = manufacturer.name
AND `Order`.order_date BETWEEN DATE_SUB(NOW(), INTERVAL 1 MONTH) AND NOW();

-- 4 Calculate how much money made each manufacturer last year
SELECT manufacturer.name, Sum(price_each * quantity) as 'Total Revenue'
FROM Manufacturer
JOIN wine ON manufacturer.id = wine.manufacturer_id
JOIN order_wine ON wine.id = order_wine.wine_id
JOIN `Order` ON order_wine.order_id = `Order`.id
WHERE `Order`.order_date BETWEEN '2022-01-01' AND '2022-12-31'
GROUP BY manufacturer.name;

-- 5 What wine is most popular in database by customers for red wine and white wine?

-- most popular red wine
SELECT wine.name, SUM(quantity) as 'Total Quantity Sold'
FROM Wine
JOIN order_wine ON wine.id = order_wine.wine_id
WHERE wine.color = 'roșu'
GROUP BY wine.name
ORDER BY SUM(quantity) DESC
LIMIT 1;

-- most popular white wine
SELECT wine.name, SUM(quantity) as 'Total Quantity Sold'
FROM Wine
JOIN order_wine ON wine.id = order_wine.wine_id
WHERE wine.color = 'alb'
GROUP BY wine.name
ORDER BY SUM(quantity) DESC
LIMIT 1;
