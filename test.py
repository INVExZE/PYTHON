class Product:
    def __init__(self, name, price, category):
        self.__name = name
        self.__price = price
        self.__category = category

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_category(self):
        return self.__category

    def set_price(self, price):
        self.__price = price


class Electronics(Product):
    def __init__(self, name, price, warranty_period):
        super().__init__(name, price, 'Electronics')
        self.__warranty_period = warranty_period

    def get_warranty_period(self):
        return self.__warranty_period


class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price, 'Clothing')
        self.__size = size

    def get_size(self):
        return self.__size
    
class Shoes(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price, 'Clothing')
        self.__size = size

    def get_size(self):
        return self.__size


class Customer:
    def __init__(self, name, email):
        self.__name = name
        self.__email = email
        self.__cart = []

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def add_to_cart(self, product):
        self.__cart.append(product)

    def view_cart(self):
        return [product.get_name() for product in self.__cart]

    def empty_cart(self):
        self.__cart = []


class Order:
    order_count = 0

    def __init__(self, customer, products):
        Order.order_count += 1
        self.__order_id = Order.order_count
        self.__customer = customer
        self.__products = products
        self.__total = sum(product.get_price() for product in products)

    def get_order_id(self):
        return self.__order_id

    def get_customer(self):
        return self.__customer

    def get_products(self):
        return self.__products

    def get_total(self):
        return self.__total

    @staticmethod
    def calculate_discount(total, discount_percent):
        return total * (1 - discount_percent / 100)

    @classmethod
    def get_order_count(cls):
        return cls.order_count


# Example usage
# Creating products
phone = Electronics('Smartphone', 699.99, '2 years')
shirt = Clothing('T-Shirt', 19.99, 'M')
shoe = Shoes('Shoes', 299.99, '40')

# Creating a customer
customer = Customer('Ankit Kumar', 'ankit@gmail.com')

# Adding products to the customer's cart
customer.add_to_cart(phone)
customer.add_to_cart(shirt)
customer.add_to_cart(shoe)

# Viewing the cart
print("-------------------------------------------------------------------")
print("\nCart contents:", customer.view_cart())

# Placing an order
order = Order(customer, [phone, shirt, shoe])

# Viewing order details
print("Order ID:", order.get_order_id())
print("Customer:", order.get_customer().get_name())
print("Products:", [product.get_name() for product in order.get_products()])
print("\nTotal:", order.get_total())

# Calculating discount
discounted_total = Order.calculate_discount(order.get_total(), 10)
print('Total after discount: ', discounted_total)

# Summary of orders
print("\nTotal orders placed:", Order.get_order_count())
print("-------------------------------------------------------------------")
