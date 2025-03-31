WITH RECURSIVE
    hours AS (
        SELECT
            0 AS HOUR
        UNION
        SELECT
            HOUR+1 AS HOUR
        FROM
            hours
        WHERE
            HOUR<23
    )
SELECT
    hours.HOUR,
    IFNULL(counts.COUNT, 0)
FROM
    hours
    LEFT OUTER JOIN (
        SELECT
            HOUR(DATETIME) AS HOUR,
            COUNT(*) AS COUNT
        FROM
            ANIMAL_OUTS
        GROUP BY
            HOUR(DATETIME)
    ) AS counts ON hours.HOUR=counts.HOUR
ORDER BY
    hours.HOUR