SELECT DISTINCT
    DEVELOPERS.ID,
    DEVELOPERS.EMAIL,
    DEVELOPERS.FIRST_NAME,
    DEVELOPERS.LAST_NAME
FROM
    DEVELOPERS,
    (
        SELECT
            CODE
        FROM
            SKILLCODES
        WHERE
            NAME IN ('Python', 'C#')
    ) AS target_skills
WHERE
    DEVELOPERS.SKILL_CODE&target_skills.CODE
ORDER BY
    DEVELOPERS.ID;