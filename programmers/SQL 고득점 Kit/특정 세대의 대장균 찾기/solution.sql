WITH RECURSIVE
    ECOLI_GENERATION AS (
        SELECT
            ID,
            PARENT_ID,
            1 AS GENERATION
        FROM
            ECOLI_DATA
        WHERE
            PARENT_ID IS NULL
        UNION ALL
        SELECT
            children.ID,
            children.PARENT_ID,
            GENERATION+1 AS GENERATION
        FROM
            ECOLI_DATA AS children
            INNER JOIN ECOLI_GENERATION ON children.PARENT_ID=ECOLI_GENERATION.ID
        WHERE
            GENERATION<3
    )
SELECT
    ID
FROM
    ECOLI_GENERATION
WHERE
    GENERATION=3
ORDER BY
    ID;