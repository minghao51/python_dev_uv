{{
    config(
        materialized='table'
    )
}}

WITH daily_sales AS (
    SELECT
        date,
        SUM(quantity * price) as daily_revenue,
        COUNT(DISTINCT product_id) as unique_products,
        SUM(quantity) as total_quantity
    FROM {{ ref('raw_sales') }}
    GROUP BY date
)

SELECT
    date,
    daily_revenue,
    unique_products,
    total_quantity,
    daily_revenue / NULLIF(total_quantity, 0) as average_price_per_unit
FROM daily_sales 