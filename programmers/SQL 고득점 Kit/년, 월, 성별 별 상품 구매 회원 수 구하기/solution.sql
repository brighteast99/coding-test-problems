SELECT
    YEAR(SALES_DATE),
    MONTH(SALES_DATE),
    GENDER,
    COUNT(DISTINCT USER_ID)
FROM
    USER_INFO
    NATURAL JOIN ONLINE_SALE
WHERE
    GENDER IS NOT NULL
GROUP BY
    YEAR(SALES_DATE),
    MONTH(SALES_DATE),
    GENDER
ORDER BY
    YEAR(SALES_DATE),
    MONTH(SALES_DATE),
    GENDER