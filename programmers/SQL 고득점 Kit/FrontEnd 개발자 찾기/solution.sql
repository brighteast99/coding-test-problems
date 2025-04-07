SELECT DISTINCT
    ID,
    EMAIL,
    FIRST_NAME,
    LAST_NAME
FROM
    DEVELOPERS
    INNER JOIN SKILLCODES ON SKILL_CODE&CODE>0
WHERE
    CATEGORY='Front End'
ORDER BY
    ID;