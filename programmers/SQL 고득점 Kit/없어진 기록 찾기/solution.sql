-- With join
SELECT
    outs.ANIMAL_ID,
    outs.NAME
FROM
    ANIMAL_INS AS ins
    RIGHT OUTER JOIN ANIMAL_OUTS AS outs ON ins.ANIMAL_ID=outs.ANIMAL_ID
WHERE
    ins.ANIMAL_ID IS NULL
ORDER BY
    outs.ANIMAL_ID;

-- With subquery
SELECT
    ANIMAL_ID,
    NAME
FROM
    ANIMAL_OUTS
WHERE
    ANIMAL_ID NOT IN(
        SELECT
            ANIMAL_ID
        FROM
            ANIMAL_INS
    )
ORDER BY
    ANIMAL_ID;