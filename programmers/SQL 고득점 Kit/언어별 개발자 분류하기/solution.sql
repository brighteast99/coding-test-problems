WITH
    SKILL_INFO AS (
        SELECT
            SUM(SKILLCODES.CATEGORY='Front End') AS FRONT_END,
            SUM(SKILLCODES.NAME='Python') AS HAS_PYTHON,
            SUM(SKILLCODES.NAME='C#') AS HAS_CSHARP,
            DEVELOPERS.ID,
            DEVELOPERS.EMAIL
        FROM
            DEVELOPERS
            INNER JOIN SKILLCODES ON DEVELOPERS.SKILL_CODE&SKILLCODES.CODE
        GROUP BY
            DEVELOPERS.ID,
            DEVELOPERS.EMAIL
        HAVING
            FRONT_END
            OR HAS_CSHARP
    )
SELECT
    CASE
        WHEN (
            FRONT_END
            AND HAS_PYTHON
        ) THEN 'A'
        WHEN HAS_CSHARP THEN 'B'
        ELSE 'C'
    END AS GRADE,
    ID,
    EMAIL
FROM
    SKILL_INFO
ORDER BY
    GRADE,
    ID;