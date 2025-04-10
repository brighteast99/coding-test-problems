SELECT
    FLAVOR
FROM
    (
        SELECT
            *
        FROM
            FIRST_HALF
        UNION ALL
        SELECT
            *
        FROM
            JULY
    ) AS TOTAL_ORDERS
GROUP BY
    FLAVOR
ORDER BY
    SUM(TOTAL_ORDER) DESC
LIMIT
    3;