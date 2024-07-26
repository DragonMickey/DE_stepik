def read_sales_data(file_path):
    """Принимает путь к файлу и возвращает список продаж. Продажи в свою очередь являются словарями с ключами
    product_name, quantity, price, date."""
    sales_data = []
    with open(file_path, 'r') as file:
        for line in file:
            lst = line.strip().split(',')
            product_name = lst[0]
            quantity = int(lst[1])
            price = int(lst[2])
            date = lst[3][1:]
            dictionary = {
                'product_name': product_name,
                'quantity': quantity,
                'price': price,
                'date': date
            }
            sales_data.append(dictionary)
    return sales_data


def total_sales_per_product(sales_data):
    """Принимает список продаж и возвращает словарь, где ключ - название продукта, а значение - общая сумма продаж
    этого продукта."""
    total_sales = {}
    for product in sales_data:
        product_name = product['product_name']
        quantity = product['quantity']
        price = product['price']
        if product_name in total_sales:
            total_sales[product_name] += quantity * price
        else:
            total_sales[product_name] = quantity * price
    return total_sales


def sales_over_time(sales_data):
    """Принимает список продаж и возвращает словарь, где ключ - дата, а значение общая сумма продаж за эту дату."""
    date_sales = {}
    for product in sales_data:
        date = product['date']
        quantity = product['quantity']
        price = product['price']
        if date in date_sales:
            date_sales[date] += quantity * price
        else:
            date_sales[date] = quantity * price
    return date_sales


sales = read_sales_data('data.txt')
total_sales_per_product = total_sales_per_product(sales)
sales_over_time = sales_over_time(sales)
print('Продукт с наибольшей выручкой:', max(total_sales_per_product, key=total_sales_per_product.get))
print('День с наибольшей суммой продаж:', max(sales_over_time, key=sales_over_time.get))
