class Product:
    product_count = 0  # Class variable to track total products
    
    def _init_(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock
        Product.product_count += 1
    
    def sell(self, quantity):
        """Reduces stock by quantity if enough stock is available."""
        if quantity <= 0:
            print("Quantity must be positive.")
            return False
        if quantity > self.stock:
            print(f"Not enough stock. Only {self.stock} units of {self.name} available.")
            return False
        
        self.stock -= quantity
        return True
    
    def restock(self, quantity):
        """Increases stock by the given quantity."""
        if quantity <= 0:
            print("Restock quantity must be positive.")
            return
        self.stock += quantity
        print(f"Restocked {quantity} x {self.name}. New stock: {self.stock}")
    
    #property
    def stock_value(self):
        """Returns the total value of the stock: price x stock"""
        return self.price * self.stock
    
    def _str_(self):
        return f"{self.name} | KES {self.price:.2f} | Stock: {self.stock} | Value: KES {self.stock_value:.2f}"


class Customer:
    def _init_(self, name, email):
        self.name = name
        self.email = email
        self.purchase_history = []  # List of Order objects
    
    def add_order(self, order):
        """Adds an order to the customer's purchase history."""
        self.purchase_history.append(order)
    
    def total_spent(self):
        """Calculates total amount spent by the customer."""
        return sum(order.total_price() for order in self.purchase_history)
    
    def _str_(self):
        return f"Customer: {self.name} | {self.email} | Orders: {len(self.purchase_history)} | Total Spent: KES {self.total_spent():.2f}"


class VIPCustomer(Customer):
    """Inherits from Customer and adds discount functionality."""
    
    def _init_(self, name, email, discount_rate):
        super()._init_(name, email)  # Initialize parent class attributes
        self.discount_rate = discount_rate  # e.g., 0.1 for 10%
    
    def total_spent(self):
        """Calculates total spent with discount applied."""
        gross_total = super().total_spent()  # Get total before discount
        discount_amount = gross_total * self.discount_rate
        return gross_total - discount_amount
    
    