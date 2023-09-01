SELECT
    product_id,
    warehouse_id,
    quantity
FROM inventory
WHERE (product_id, warehouse_id, date) IN (
    SELECT
        product_id,
        warehouse_id,
        MAX(date) AS latest_date
    FROM inventory
    GROUP BY product_id, warehouse_id
);