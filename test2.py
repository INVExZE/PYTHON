class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category


class Electronics(Product):
    def __init__(self, name, price, warranty_period):
        super().__init__(name, price, 'Electronics')
        self.warranty_period = warranty_period


class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price, 'Clothing')
        self.size = size


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)

    def view_cart(self):
        return [product.name for product in self.cart]

    def empty_cart(self):
        self.cart = []


class Order:
    order_count = 0

    def __init__(self, customer, products):
        Order.order_count += 1
        self.order_id = Order.order_count
        self.customer = customer
        self.products = products
        self.total = sum(product.price for product in products)

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

# Creating a customer
customer = Customer('John Doe', 'john@example.com')

# Adding products to the customer's cart
customer.add_to_cart(phone)
customer.add_to_cart(shirt)

# Viewing the cart
print("Cart contents:", customer.view_cart())

# Placing an order
order = Order(customer, [phone, shirt])

# Viewing order details
print("Order ID:", order.order_id)
print("Customer:", order.customer.name)
print("Products:", [product.name for product in order.products])
print("Total:", order.total)

# Calculating discount
discounted_total = Order.calculate_discount(order.total, 10)
print("Total after discount:", discounted_total)

# Summary of orders
print("Total orders placed:", Order.get_order_count())
