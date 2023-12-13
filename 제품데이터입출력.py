import sqlite3

class ProductManager:
    def __init__(self, db_file='products.db'):
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                product_id INTEGER PRIMARY KEY,
                product_name TEXT NOT NULL,
                quantity INTEGER NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.conn.commit()

    def insert_product(self, product_name, quantity, price):
        self.cursor.execute('''
            INSERT INTO products (product_name, quantity, price)
            VALUES (?, ?, ?)
        ''', (product_name, quantity, price))
        self.conn.commit()

    def update_product(self, product_id, product_name, quantity, price):
        self.cursor.execute('''
            UPDATE products
            SET product_name=?, quantity=?, price=?
            WHERE product_id=?
        ''', (product_name, quantity, price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        self.cursor.execute('''
            DELETE FROM products
            WHERE product_id=?
        ''', (product_id,))
        self.conn.commit()

    def select_all_products(self):
        self.cursor.execute('''
            SELECT * FROM products
        ''')
        return self.cursor.fetchall()

# 샘플 데이터 추가
def add_sample_data(product_manager):
    sample_data = [
        ('Laptop', 5, 1200.0),
        ('Mouse', 50, 20.0),
        ('Keyboard', 30, 40.0),
        ('Monitor', 10, 300.0),
        ('Headphones', 20, 50.0),
        ('Printer', 8, 150.0),
        ('Desk', 15, 200.0),
        ('Chair', 25, 80.0),
        ('Tablet', 12, 350.0),
        ('Smartphone', 40, 600.0)
    ]
    for data in sample_data:
        product_manager.insert_product(*data)

if __name__ == '__main__':
    # ProductManager 객체 생성
    product_manager = ProductManager()

    # 샘플 데이터 추가
    add_sample_data(product_manager)

    # 모든 제품 조회
    all_products = product_manager.select_all_products()
    print("All Products:")
    for product in all_products:
        print(product)

    # 제품 수정
    product_manager.update_product(1, 'Updated Laptop', 8, 1500.0)

    # 제품 삭제
    product_manager.delete_product(3)

    # 수정 및 삭제 후 다시 모든 제품 조회
    updated_products = product_manager.select_all_products()
    print("\nUpdated Products:")
    for product in updated_products:
        print(product)

    # 연결 종료
    product_manager.conn.close()
