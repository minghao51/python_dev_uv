from typing import List, Dict
from dagster import asset, AssetExecutionContext
import pandas as pd
import duckdb

@asset
def raw_sales_data(context: AssetExecutionContext) -> pd.DataFrame:
    """
    Load raw sales data from a CSV file.
    
    Args:
        context: The asset execution context.
        
    Returns:
        pd.DataFrame: Raw sales data.
    """
    # Example data creation
    data = {
        'date': ['2024-01-01', '2024-01-02', '2024-01-03'],
        'product_id': [1, 2, 3],
        'quantity': [10, 20, 15],
        'price': [100.0, 200.0, 150.0]
    }
    df = pd.DataFrame(data)
    context.log.info(f"Loaded {len(df)} rows of raw sales data")
    return df

@asset
def processed_sales_data(
    context: AssetExecutionContext,
    raw_sales_data: pd.DataFrame
) -> Dict[str, List]:
    """
    Process raw sales data and calculate daily metrics.
    
    Args:
        context: The asset execution context.
        raw_sales_data: Raw sales data DataFrame.
        
    Returns:
        Dict[str, List]: Processed sales metrics.
    """
    # Calculate daily revenue
    raw_sales_data['revenue'] = raw_sales_data['quantity'] * raw_sales_data['price']
    daily_revenue = raw_sales_data.groupby('date')['revenue'].sum().to_dict()
    
    context.log.info(f"Processed sales data for {len(daily_revenue)} days")
    return {
        'dates': list(daily_revenue.keys()),
        'revenues': list(daily_revenue.values())
    } 