import pymysql
from config import host, user, password, db_name

try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Successfully connected...")
    print("#" * 20)

    try:
        with connection.cursor() as cursor:
            create_table_collection = "CREATE TABLE IF NOT EXISTS `Collection` (`id` int NOT NULL AUTO_INCREMENT, name varchar(64) NOT NULL, `season` varchar(64) NOT NULL, PRIMARY KEY (`id`))"

            create_table_customer = "CREATE TABLE IF NOT EXISTS `Customer`(`id` int NOT NULL AUTO_INCREMENT," \
            "`last_name` varchar(64) NOT NULL," \
            "`first_name` varchar(64) NOT NULL," \
            "`email` varchar(256) NOT NULL," \
            "`phone` varchar(64) NOT NULL," \
            "`birth_date` date NOT NULL," \
            "`password` varchar(64) NOT NULL," \
            "`surname` varchar(64) NOT NULL," \
            "`full_address` varchar(256) NOT NULL, PRIMARY KEY (`id`));" \

            create_table_grape_varieties = "CREATE TABLE IF NOT EXISTS `Grape_varieties`(`id` int NOT NULL AUTO_INCREMENT," \
            "`name` varchar(64) NOT NULL," \
            "`acidity` float NOT NULL, PRIMARY KEY (`id`));" \

            create_table_manufacturer = "CREATE TABLE IF NOT EXISTS `Manufacturer`(`id` int NOT NULL AUTO_INCREMENT," \
            "`name` varchar(64) NOT NULL," \
            "`srl` varchar(64) NOT NULL," \
            "`country` varchar(64) NOT NULL, PRIMARY KEY (`id`));" \

            create_table_order = "CREATE TABLE IF NOT EXISTS `Order`(`id` int NOT NULL AUTO_INCREMENT," \
            "`customer_id` int NOT NULL," \
            "`total_quantity` int NOT NULL," \
            "`order_date` datetime NOT NULL," \
            "`required_date` datetime NOT NULL," \
            "`shipped_date` datetime NOT NULL," \
            "`status` int NOT NULL," \
            "`comments` varchar(256) NOT NULL, PRIMARY KEY (`id`)," \
            "KEY `FK_2` (`customer_id`)," \
            "CONSTRAINT `FK_12_1` FOREIGN KEY `FK_2` (`customer_id`) REFERENCES `Customer` (`id`));" \

            create_table_order_wine = "CREATE TABLE IF NOT EXISTS `order_wine`(`wine_id` int NOT NULL," \
            "`order_id` int NOT NULL," \
            "`quantity` int NOT NULL," \
            "`price_each` float NOT NULL, PRIMARY KEY (`wine_id`, `order_id`)," \
            "KEY `FK_1` (`wine_id`)," \
            "CONSTRAINT `FK_11_3` FOREIGN KEY `FK_1` (`wine_id`) REFERENCES `Wine` (`id`)," \
            "KEY `FK_3` (`order_id`)," \
            "CONSTRAINT `FK_12` FOREIGN KEY `FK_3` (`order_id`) REFERENCES `Order` (`id`));" \

            create_table_payment = "CREATE TABLE IF NOT EXISTS `Payment`(`id` int NOT NULL AUTO_INCREMENT," \
            "`payment_date` datetime NOT NULL," \
            "`customer_id` int NOT NULL," \
            "`amount` float NOT NULL, PRIMARY KEY (`id`)," \
            "KEY `FK_3` (`customer_id`)," \
            "CONSTRAINT `FK_13` FOREIGN KEY `FK_3` (`customer_id`) REFERENCES `Customer` (`id`));" \

            create_table_supplier = "CREATE TABLE IF NOT EXISTS `Supplier`(`id` int NOT NULL AUTO_INCREMENT," \
            "`name` varchar(64) NOT NULL," \
            "`phone_number` varchar(64) NOT NULL, PRIMARY KEY (`id`));" \

            create_table_wine = "CREATE TABLE IF NOT EXISTS `Wine`(`id` int NOT NULL AUTO_INCREMENT," \
            "`name` varchar(64) NOT NULL," \
            "`collection_id` int NOT NULL," \
            "`manufacturer_id` int NOT NULL," \
            "`abv` float NOT NULL," \
            "`color` varchar(45) NOT NULL," \
            "`type` varchar(45) NOT NULL," \
            "`category` varchar(45) NOT NULL," \
            "`year` int NOT NULL," \
            "`price` float NOT NULL," \
            "`volume` float NOT NULL, PRIMARY KEY (`id`)," \
            "KEY `FK_3` (`manufacturer_id`)," \
            "CONSTRAINT `FK_16` FOREIGN KEY `FK_3` (`manufacturer_id`) REFERENCES `Manufacturer` (`id`)," \
            "KEY `FK_5` (`collection_id`)," \
            "CONSTRAINT `FK_20` FOREIGN KEY `FK_5` (`collection_id`) REFERENCES `Collection` (`id`));" \

            create_table_wine_grape_varieties = "CREATE TABLE IF NOT EXISTS `wine_grape_varieties`(`wine_id` int NOT NULL," \
            "`variety_id` int NOT NULL," \
            "`percent` float NOT NULL, PRIMARY KEY (`wine_id`, `variety_id`)," \
            "KEY `FK_2_1` (`wine_id`)," \
            "CONSTRAINT `FK_20_1` FOREIGN KEY `FK_2_1` (`wine_id`) REFERENCES `Wine` (`id`)," \
            "KEY `FK_3` (`variety_id`)," \
            "CONSTRAINT `FK_20_2` FOREIGN KEY `FK_3` (`variety_id`) REFERENCES `Grape_varieties` (`id`));" \

            create_table_wine_winestore = "CREATE TABLE IF NOT EXISTS `wine_winestore`(`winestore_id` int NOT NULL," \
            "`wine_id` int NOT NULL," \
            "`qty_in_stock` int NOT NULL, PRIMARY KEY (`winestore_id`, `wine_id`)," \
            "KEY `FK_1` (`winestore_id`)," \
            "CONSTRAINT `FK_12_2` FOREIGN KEY `FK_1` (`winestore_id`) REFERENCES `WineStore` (`id`)," \
            "KEY `FK_3` (`wine_id`)," \
            "CONSTRAINT `FK_13_1` FOREIGN KEY `FK_3` (`wine_id`) REFERENCES `Wine` (`id`));" \

            create_table_wine_store = "CREATE TABLE IF NOT EXISTS `WineStore`(`id` int NOT NULL AUTO_INCREMENT," \
            "`name` varchar(64) NOT NULL," \
            "`country` varchar(64) NOT NULL," \
            "`address` varchar(64) NOT NULL," \
            "`city` varchar(64) NOT NULL, PRIMARY KEY (`id`));" \

            create_table_winestore_supplier = "CREATE TABLE IF NOT EXISTS `winestore_supplier`(`supplier_id` int NOT NULL," \
            "`winestore_id` int NOT NULL, PRIMARY KEY (`supplier_id`, `winestore_id`)," \
            "KEY `FK_3` (`winestore_id`)," \
            "CONSTRAINT `FK_12_3` FOREIGN KEY `FK_3` (`winestore_id`) REFERENCES `WineStore` (`id`)," \
            "KEY `FK_3_1` (`supplier_id`)," \
            "CONSTRAINT `FK_11_1` FOREIGN KEY `FK_3_1` (`supplier_id`) REFERENCES `Supplier` (`id`));" \

            cursor.execute(create_table_collection)
            cursor.execute(create_table_customer)
            cursor.execute(create_table_grape_varieties)
            cursor.execute(create_table_wine_store)

            cursor.execute(create_table_manufacturer)
            cursor.execute(create_table_wine)
            cursor.execute(create_table_order)
            cursor.execute(create_table_payment)
            cursor.execute(create_table_supplier)

            cursor.execute(create_table_order_wine)
            cursor.execute(create_table_wine_grape_varieties)
            cursor.execute(create_table_wine_winestore)
            cursor.execute(create_table_winestore_supplier)

            print("Table created successfully")

            collection_sql = "INSERT INTO wine_shop.collection (name, season) VALUES (%s, %s)"
            collection_val = [
                ("Carlevana Alb de Mereni", "toamna"),
                ('Carlevana Black Raven', 'primavara'),
                ('Carlevana Merlotage', 'vara'),
                ('Carlevana Pastoral', 'iarna'),
                ('Carlevana Villa Danastris', 'toamna'),
                ('Codru', 'primavara'),
                ('Cricova Cabernet', 'iarna'),
                ('Cricova Cahor', 'toamna'),
                ('Cricova Codru', 'vara'),
                ('Port Mereni', 'toamna')
            ]

            customer_sql = "INSERT INTO wine_shop.customer (last_name, first_name, email, phone, birth_date, password, surname, full_address) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            customer_val = [
                ('Selwyn', 'Karl', 'kselwyn@gmail.com', '0685478952', '1995-12-01', 'encrypted', 'kselwyn', '305 - 14th Ave. S. Suite 3B'),
                ('Rastus', 'Elizabeth', 'erastus@gmail.com', '06884152', '1988-09-18', 'encrypted', 'erastus', 'Keskuskatu 45'),
                ('Winona', 'Becky', 'bwinona@gmail.com', '06812511152', '1973-04-21', 'encrypted', 'bwinona', 'Independentei 15/2 blocul 10'),
                ('Anderson', 'Greta', 'ganderson@gmail.com', '06744552', '1970-11-11', 'encrypted', 'ganderson', 'Dacia 12/1 blocul 19'),
                ('Waverly', 'John', 'jwavely@gmail.com', '06854545452', '1999-08-14', 'encrypted', 'jwavely', 'Filtrowa 21')
            ]

            grape_varieties_sql = "INSERT INTO wine_shop.grape_varieties (name, acidity) VALUES (%s, %s)"
            grape_varieties_val = [
                ('Cabernet Sauvignon', '3.78'),
                ('Merlot', '4.01'),
                ('Chardonnay', '3.4'),
                ('Sauvignon Blanc', '3.6'),
                ('Riesling de Rhein', '3.0'),
                ('Pinot Noir', '3.7'),
                ('Rkatsiteli', '3.32'),
                ('Malbec', '3.75'),
                ('Riesling de Rhein', '3.1')
            ]

            wine_store_sql = "INSERT INTO wine_shop.WineStore (name, country, address, city) VALUES (%s, %s, %s, %s)"
            wine_store_val = [
                ('Vinoteca', 'Moldova', 'str.Pușkin 15', 'Chisinau'),
                ('ALCOMARKET', 'Moldova', 'bd. Moscova 1/1', 'Chisinau'),
                ('FOX Wines', 'Romania', 'Strada Grigore Ionescu 58', 'Bucuresti'),
                ('HORA Wine', 'Romania', 'Șoseaua Arcu 4', 'Iași'),
                ('ALCOMARKET', 'Moldova', 'str. Mihai Viteazul 12/1', 'Chisinau')
            ]

            manufacturer_sql = "INSERT INTO wine_shop.manufacturer (name, srl, country) VALUES (%s, %s, %s)"
            manufacturer_val = [
                ('Purcari', 'ÎM Vinăria Purcari SRL', 'Moldova'),
                ('FAUTOR', 'S.R.L. FAUTOR', 'Moldova'),
                ('Et Cetera', 'SRL ET CETERA WINE', 'Moldova'),
                ('Cojusna', 'S.R.L. VOITIS DISTILLERY', 'Moldova'),
                ('Dionysos-Mereni', 'I.M. DIONYSOS-MERENI S.A.', 'Moldova'),
                ('Gogu Winery', 'Dorimax SRL.', 'Moldova'),
                ('Gitana Winery', 'S.C. VINĂRIA ŢIGANCA S.R.L.', 'Moldova')
            ]

            wine_sql = "INSERT INTO wine_shop.wine (name, collection_id, manufacturer_id, abv, color, type, category, year, price, volume) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            wine_val = [
                ('EXCLUSIV ROȘU DE PURCARI', '1', '1', '13.5', 'roșu', 'sec', 'Vinuri Rosii', '2012', '2000', '0.75'),
                ('FAUTOR ILLUSTRO CHARDONNAY', '2', '2', '12.8', 'alb', 'sec', 'Vinuri Albe', '2016', '357', '0.75'),
                ('NANGHTY BOYS MAGNUM', '3', '3', '16', 'roșu', 'sec', 'Vinuri Rosii', '2016', '2500', '1.5'),
                ('COJUSNA AURIU', '4', '4', '16', 'alb', 'dulce', 'Vinuri de Colectie', '1978', '500', '0.7'),
                ('COJUSNA CABERNET', '5', '4', '14', 'roșu', 'sec', 'Vinuri de Colectie', '1987', '375', '0.7'),
                ('PORT MERENI', '6', '5', '15', 'roșu', 'dulce', 'Vinuri dulci', '2004', '317', '0.75'),
                ('GOGU MALBEC ROSE', '7', '6', '13', 'roz', 'sec', 'Vinuri roze', '2022', '180', '0.75'),
                ('TIGANCA MANASTIREA ROHBACH CRU MAGNUM', '8', '7', '13.5', 'alb', 'sec', 'Vinuri Albe', '2015', '988', '1.5')
            ]

            order_sql = "INSERT INTO wine_shop.order (customer_id, total_quantity, order_date, required_date, shipped_date, status, comments) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            order_val = [
                ('1', '13', '2022-01-23', '2023-01-25', '2022-01-25', '3', 'a se livra in a doua jumatate a zilei'),
                ('3', '90', '2023-01-23', '2023-02-15', '2023-02-15', '1', 'achitare card'),
                ('2', '3', '2023-01-23', '2023-01-27', '2023-01-27', '2', '-'),
                ('4', '1', '2022-11-03', '2022-11-05', '2022-11-05', '3', 'livrat cu succes'),
                ('5', '40', '2023-01-13', '2023-01-15', '2023-01-15', '2', 'rog comanda sa fie lasata la receptie'),
                ('1', '70', '2022-04-30', '2022-04-30', '2021-04-30', '3', 'null'),
                ('2', '6', '2023-01-25', '2023-01-25', '2023-01-25', '1', 'rog un apel preventiv'),
                ('3', '17', '2023-01-03', '2023-01-30', '2023-01-30', '1', '.'),
                ('3', '3', '2022-04-06', '2023-04-06', '2023-04-06', '3', '.')
            ]

            payment_sql = "INSERT INTO wine_shop.payment (payment_date, customer_id, amount) VALUES (%s, %s, %s)"
            payment_val = [
                ('2023-01-25', '1', '2505'),
                ('2023-02-15', '3', '35245'),
                ('2023-01-27', '2', '342'),
                ('2022-11-05', '4', '35'),
                ('2023-01-15', '5', '7546'),
                ('2021-04-30', '1', '15489'),
                ('2023-01-25', '2', '145'),
                ('2023-01-30', '3', '3456')
            ]

            supplier_sql = "INSERT INTO wine_shop.supplier (name, phone_number) VALUES (%s, %s)"
            supplier_val = [
                ('Purcari', '06842505'),
                ('Metro', '025835245'),
                ('Et Cetera', '0236342'),
                ('Alcomarket', '04845435'),
                ('Gogu', '079827546'),
                ('Novak', '054815489'),
                ('Vinaria de vale', '047145'),
                ('Gitana Winery', '07953456')
            ]

            order_wine_sql = "INSERT INTO wine_shop.order_wine (wine_id, order_id, quantity, price_each) VALUES (%s, %s, %s, %s)"
            order_wine_val = [
                ('1', '3', '4', '252'),
                ('2', '5', '9', '454'),
                ('3', '2', '2', '584'),
                ('4', '6', '98', '58'),
                ('5', '5', '9', '81'),
                ('4', '5', '1', '230'),
                ('1', '1', '1', '100'),
                ('7', '1', '45', '150')
            ]

            wine_grape_varieties_sql = "INSERT INTO wine_shop.wine_grape_varieties (wine_id, variety_id, percent) VALUES (%s, %s, %s)"
            wine_grape_varieties_val = [
                ('1', '1', '50'),
                ('1', '2', '35'),
                ('1', '8', '15'),

                ('2', '3', '60'),
                ('2', '4', '25'),
                ('2', '5', '15'),

                ('3', '6', '100'),
                ('4', '7', '100'),
                ('5', '1', '100'),
                ('6', '1', '100'),
                ('7', '8', '100'),
                ('8', '9', '100')
            ]

            wine_winestore_sql = "INSERT INTO wine_shop.wine_winestore (winestore_id, wine_id, qty_in_stock) VALUES (%s, %s, %s)"
            wine_winestore_val = [
                ('1', '1', '50'),
                ('1', '2', '35'),
                ('1', '4', '155'),
                ('1', '5', '165'),
                ('1', '6', '118'),
                ('1', '8', '178'),

                ('2', '3', '258'),
                ('2', '4', '89'),
                ('2', '5', '14'),

                ('3', '6', '100'),
                ('3', '7', '100'),
                ('3', '8', '100'),

                ('4', '3', '11'),

                ('5', '1', '216'),
                ('5', '2', '15'),
                ('5', '3', '25'),
                ('5', '4', '2'),
                ('5', '5', '574'),
                ('5', '6', '48'),
                ('5', '7', '37'),
                ('5', '8', '118')
            ]

            winestore_supplier_sql = "INSERT INTO wine_shop.winestore_supplier (supplier_id, winestore_id) VALUES (%s, %s)"
            winestore_supplier_val = [
                ('1', '1'),
                ('1', '2'),
                ('1', '3'),
                ('1', '4'),
                ('1', '5'),

                ('2', '1'),
                ('2', '5'),

                ('3', '1'),
                ('3', '3'),
                ('3', '2'),

                ('4', '4'),
                ('4', '5'),
                ('4', '1'),
                ('4', '2'),

                ('5', '3'),
                ('5', '4'),

                ('6', '5'),

                ('7', '1'),
                ('7', '2'),

                ('8', '3'),
                ('8', '4'),
                ('8', '5')
            ]

            cursor.executemany(collection_sql, collection_val)
            cursor.executemany(customer_sql, customer_val)
            cursor.executemany(grape_varieties_sql, grape_varieties_val)
            cursor.executemany(wine_store_sql, wine_store_val)
            cursor.executemany(manufacturer_sql, manufacturer_val)
            cursor.executemany(wine_sql, wine_val)
            cursor.executemany(order_sql, order_val)
            cursor.executemany(payment_sql, payment_val)
            cursor.executemany(supplier_sql, supplier_val)
            cursor.executemany(order_wine_sql, order_wine_val)
            cursor.executemany(wine_grape_varieties_sql, wine_grape_varieties_val)
            cursor.executemany(wine_winestore_sql, wine_winestore_val)
            cursor.executemany(winestore_supplier_sql, winestore_supplier_val)

            print("Inserted successfully")
            connection.commit()
    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)
