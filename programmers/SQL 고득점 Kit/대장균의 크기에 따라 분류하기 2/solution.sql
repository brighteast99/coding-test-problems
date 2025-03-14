SELECT
    ID,
    CASE
        WHEN percentile<=0.25 THEN 'CRITICAL'
        WHEN percentile<=0.5 THEN 'HIGH'
        WHEN percentile<=0.75 THEN 'MEDIUM'
        ELSE 'LOW'
    END AS COLONY_NAME
FROM
    (
        SELECT
            ID,
            PERCENT_RANK() OVER (
                ORDER BY
                    SIZE_OF_COLONY DESC
            ) AS percentile
        FROM
            ECOLI_DATA
    ) AS RANK_DATA
ORDER BY
    ID;