WITH
    max_sizes AS (
        SELECT
            YEAR(DIFFERENTIATION_DATE) AS 'YEAR',
            MAX(SIZE_OF_COLONY) AS MAX_SIZE
        FROM
            ECOLI_DATA
        GROUP BY
            YEAR(DIFFERENTIATION_DATE)
    )
SELECT
    YEAR(ecoli_list.DIFFERENTIATION_DATE) AS 'YEAR',
    max_sizes.MAX_SIZE-ecoli_list.SIZE_OF_COLONY AS YEAR_DEV,
    ID
FROM
    ECOLI_DATA AS ecoli_list
    INNER JOIN max_sizes ON YEAR(ecoli_list.DIFFERENTIATION_DATE)=max_sizes.YEAR
ORDER BY
    YEAR(ecoli_list.DIFFERENTIATION_DATE),
    YEAR_DEV;