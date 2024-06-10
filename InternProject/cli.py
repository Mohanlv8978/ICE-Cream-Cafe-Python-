import sqlite3

def create_tables():
    # Connect to SQLite database
    conn = sqlite3.connect('ice_cream_parlor.db')
    cursor = conn.cursor()

    # Create table for seasonal flavors
    cursor.execute('''CREATE TABLE IF NOT EXISTS seasonal_flavors (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        flavor_name TEXT NOT NULL,
                        start_date TEXT NOT NULL,
                        end_date TEXT NOT NULL)''')

    # Create table for ingredient inventory
    cursor.execute('''CREATE TABLE IF NOT EXISTS ingredients (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        ingredient_name TEXT NOT NULL,
                        quantity INTEGER NOT NULL)''')

    # Create table for customer suggestions and allergy concerns
    cursor.execute('''CREATE TABLE IF NOT EXISTS customer_suggestions (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        customer_name TEXT NOT NULL,
                        suggested_flavor TEXT NOT NULL,
                        allergy_concerns TEXT)''')

    # Commit changes and close connection
    conn.commit()
    conn.close()

# Initialize the database and tables
create_tables()

# Function to add a seasonal flavor
def add_seasonal_flavor(flavor_name, start_date, end_date):
    conn = sqlite3.connect('ice_cream_parlor.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO seasonal_flavors (flavor_name, start_date, end_date)
                      VALUES (?, ?, ?)''', (flavor_name, start_date, end_date))
    conn.commit()
    conn.close()

# Function to add an ingredient
def add_ingredient(ingredient_name, quantity):
    conn = sqlite3.connect('ice_cream_parlor.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO ingredients (ingredient_name, quantity)
                      VALUES (?, ?)''', (ingredient_name, quantity))
    conn.commit()
    conn.close()

# Function to add a customer suggestion
def add_customer_suggestion(customer_name, suggested_flavor, allergy_concerns):
    conn = sqlite3.connect('ice_cream_parlor.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO customer_suggestions (customer_name, suggested_flavor, allergy_concerns)
                      VALUES (?, ?, ?)''', (customer_name, suggested_flavor, allergy_concerns))
    conn.commit()
    conn.close()
if __name__ == "__main__":
    main()
