import heapq

# ---------------------- Product Class ----------------------
class Product:
    def __init__(self, product_id, name, price, quantity, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        self.price_history = []

    def update_price(self, new_price):
        self.price_history.append((self.price, new_price))
        self.price = new_price

    def __repr__(self):
        return f"{self.name} (ID: {self.product_id}) - ${self.price}, Qty: {self.quantity}, Category: {self.category}"


# ---------------------- Inventory (Hash Table) ----------------------
class Inventory:
    def __init__(self):
        self.products = {}  # Hash Table (Dictionary)

    def add_product(self, product):
        self.products[product.product_id] = product

    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]

    def get_product(self, product_id):
        return self.products.get(product_id, None)

    def update_price(self, product_id, new_price):
        if product_id in self.products:
            self.products[product_id].update_price(new_price)

    def update_quantity(self, product_id, new_quantity):
        if product_id in self.products:
            self.products[product_id].quantity = new_quantity


# ---------------------- Priority Queue (Heap) ----------------------
class PriorityQueue:
    def __init__(self):
        self.heap = []

    def add_product(self, product, priority):
        heapq.heappush(self.heap, (priority, product))

    def pop_product(self):
        return heapq.heappop(self.heap)[1] if self.heap else None

    def search_product(self, product_id):
        for priority, product in self.heap:
            if product.product_id == product_id:
                return product
        return None


# ---------------------- Binary Search Tree (BST) ----------------------
class BSTNode:
    def __init__(self, product):
        self.product = product
        self.left = None
        self.right = None

class ProductBST:
    def __init__(self):
        self.root = None

    def insert(self, product):
        if not self.root:
            self.root = BSTNode(product)
        else:
            self._insert(self.root, product)

    def _insert(self, node, product):
        if product.price < node.product.price:
            if node.left:
                self._insert(node.left, product)
            else:
                node.left = BSTNode(product)
        else:
            if node.right:
                self._insert(node.right, product)
            else:
                node.right = BSTNode(product)

    def search(self, price):
        return self._search(self.root, price)

    def _search(self, node, price):
        if not node:
            return None
        if node.product.price == price:
            return node.product
        elif price < node.product.price:
            return self._search(node.left, price)
        else:
            return self._search(node.right, price)

    def inorder_traversal(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.product)
            self._inorder(node.right, result)


# ---------------------- Linked List (Price History Tracking) ----------------------
class PriceHistoryNode:
    def __init__(self, old_price, new_price):
        self.old_price = old_price
        self.new_price = new_price
        self.next = None

class PriceHistory:
    def __init__(self):
        self.head = None

    def add_price_change(self, old_price, new_price):
        new_node = PriceHistoryNode(old_price, new_price)
        new_node.next = self.head
        self.head = new_node

    def display_history(self):
        temp = self.head
        while temp:
            print(f"Price changed from ${temp.old_price} to ${temp.new_price}")
            temp = temp.next


# ---------------------- TESTING & DEMONSTRATION ----------------------

print("\n--- Inventory Management System Testing ---\n")

# Initialize Inventory
inventory = Inventory()

# Create Products
p1 = Product(101, "Laptop", 1200, 5, "Electronics")
p2 = Product(102, "Phone", 800, 10, "Electronics")
p3 = Product(103, "Headphones", 150, 20, "Accessories")

# Test 1: Insert and Retrieve Products
inventory.add_product(p1)
inventory.add_product(p2)
print("Product Retrieved:", inventory.get_product(102))  

# Test 2: Updating Product Price and Quantity
inventory.update_price(102, 750)
inventory.update_quantity(102, 5)
print("Updated Product:", inventory.get_product(102)) 

# Test 3: Removing a Product
inventory.remove_product(103)
print("After Deletion:", inventory.get_product(103))

# Test 4: Priority Queue Operations
pq = PriorityQueue()
pq.add_product(p1, 2)  # Lower priority
pq.add_product(p2, 1)  # Higher priority
print("Highest Priority Product:", pq.pop_product())

# Test 5: BST Operations
bst = ProductBST()
bst.insert(p1)
bst.insert(p2)
print("BST Search Result:", bst.search(800))

# Test 6: Price History Tracking
ph = PriceHistory()
ph.add_price_change(100, 120)
ph.add_price_change(120, 140)
ph.display_history()