SELECT
    CATEGORY,
    PRICE,
    PRODUCT_NAME
FROM
    (
        SELECT
            CATEGORY,
            PRICE,
            PRODUCT_NAME,
            RANK() OVER (
                PARTITION BY
                    CATEGORY
                ORDER BY
                    PRICE DESC
            ) AS RANKING
        FROM
            FOOD_PRODUCT
        WHERE
            CATEGORY IN ('과자', '국', '김치', '식용유')
    ) AS PRICE_RANK
WHERE
    RANKING=1
ORDER BY
    PRICE DESC;