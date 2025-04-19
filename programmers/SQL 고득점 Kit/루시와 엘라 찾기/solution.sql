SELECT
    ANIMAL_ID,
    NAME,
    SEX_UPON_INTAKE
FROM
    ANIMAL_INS
WHERE
    NAME IN ("Lucy", "Ella", "Pickle", "Sabrina", "Mitty")
ORDER BY
    ANIMAL_ID;