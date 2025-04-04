-- With join
SELECT
    ins.NAME,
    ins.DATETIME
FROM
    ANIMAL_INS AS ins
    LEFT OUTER JOIN ANIMAL_OUTS AS outs ON ins.ANIMAL_ID=outs.ANIMAL_ID
WHERE
    outs.ANIMAL_ID IS NULL
ORDER BY
    ins.DATETIME
LIMIT
    3;

-- With subquery
SELECT
    NAME,
    DATETIME
FROM
    ANIMAL_INS
WHERE
    ANIMAL_ID NOT IN(
        SELECT
            ANIMAL_ID
        FROM
            ANIMAL_OUTS
    )
ORDER BY
    DATETIME
LIMIT
    3;