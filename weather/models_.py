import fdb
import os # получение данных из .env
from dotenv import load_dotenv # подключение .env
load_dotenv() # подключение .env
db_path = os.getenv('DB_PATH')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_charset = os.getenv('DB_CHARSET')

print(db_path)

try:
     dataset = fdb.connect(
         dsn=db_path,
         user=db_user,
         password=db_password,
         charset=db_charset)
     cursor = dataset.cursor()
     print("Успешное соединение")
except fdb.Error as e:
    print(f"Ошибка подключения {e}")


#красивый вывод на разных строках
# get_all_products = cursor.execute('SELECT ID, NAME_PRODUCT, DATE_SELL, PRICE, AMOUNT FROM PRODUCTS ORDER BY NAME_PRODUCT').fetchallmap()
# print(get_all_products)
# for row in get_all_products:
#     id = row ['id']
#     product_name = row ['name_product']
#     date_sell = row ['date_sell'].strftime('%d.%m.%Y')
#     summa = float(row ['price'])*float(row ['amount'])

#     print('Идентификатор: ', id,'\n'+'Наименование: ', product_name,'\n'+'Дата продажи: ', date_sell,'\n'+'Выручка: ', summa,'\n'+'---------------------'+'\n')

#добавляю кофе
# cursor.execute('''
# INSERT INTO PRODUCTS_CATEGORIES (NAME_CATEGORY)
#               VALUES ('Кофе')
# ''')
# dataset.commit()
# insert_products = cursor.execute('SELECT * FROM PRODUCTS_CATEGORIES').fetchall()
# print(insert_products)


#кикнула кофе
# cursor.execute('''
# DELETE FROM PRODUCTS_CATEGORIES
#               WHERE NAME_CATEGORY='Кофе'
# ''')
# dataset.commit()
# delete_products = cursor.execute('SELECT * FROM PRODUCTS_CATEGORIES').fetchall()
# print(delete_products)


#сделала анти-скидку на картошку
# cursor.execute('''
# UPDATE PRODUCTS
# SET PRICE = PRICE*1.7
#                WHERE NAME_PRODUCT='Картошка'
# ''')
# dataset.commit()
# n_price = cursor.execute('SELECT * FROM PRODUCTS').fetchallmap()
# for row in n_price:
#     product_name = row ['name_product']
#     price = row ['price']

#     print('Наименование: ', product_name, '\n', 'Цена: ', price, '\n', '---------------------', '\n',)


#Выведите информацию о всех продажах заданного продукта построчно 
# get_all_products = cursor.execute('''SELECT NAME_PRODUCT, DATE_SELL FROM PRODUCTS WHERE NAME_PRODUCT='Апельсины' ''').fetchallmap()
# for row in get_all_products:
#     product_name = row ['name_product']
#     date_sell = row ['date_sell'].strftime('%d.%m.%Y')

#     print('Наименование: ', product_name, '\n', 'Дата продажи: ', date_sell, '\n', '---------------------', '\n',)


#Выведите количество продуктов с указанием категории, к которой они относятся (функция COUNT)
# categories = cursor.execute('''SELECT COUNT (*), ID_CATEGORY FROM PRODUCTS GROUP BY ID_CATEGORY ''').fetchall()
# for category in categories:
#     id=category[1]
#     category_name = cursor.execute(f'''SELECT NAME_CATEGORY FROM PRODUCTS_CATEGORIES WHERE ID = {id}''').fetchallmap()
#     print(category_name[0]['NAME_CATEGORY'], '---', category[0], ',')
