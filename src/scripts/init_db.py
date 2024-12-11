from typing import None
import duckdb
from pathlib import Path

def initialize_database() -> None:
    """
    Initialize the DuckDB database with required tables and initial data.
    """
    # Create data directory if it doesn't exist
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)
    
    # Connect to DuckDB
    conn = duckdb.connect(str(data_dir / "warehouse.db"))
    
    try:
        # Create raw_sales table
        conn.execute("""
            CREATE TABLE IF NOT EXISTS raw_sales (
                date DATE,
                product_id INTEGER,
                quantity INTEGER,
                price DECIMAL(10,2)
            )
        """)
        
        # Insert sample data
        conn.execute("""
            INSERT INTO raw_sales VALUES
            ('2024-01-01', 1, 10, 100.00),
            ('2024-01-02', 2, 20, 200.00),
            ('2024-01-03', 3, 15, 150.00)
        """)
        
    finally:
        conn.close()

if __name__ == "__main__":
    initialize_database() 