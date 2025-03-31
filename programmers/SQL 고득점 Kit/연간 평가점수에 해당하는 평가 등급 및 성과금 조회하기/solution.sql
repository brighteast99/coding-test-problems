WITH
    GRADE_INFO AS (
        SELECT
            EMP_NO,
            CASE
                WHEN AVG(SCORE)>=96 THEN 'S'
                WHEN AVG(SCORE)>=90 THEN 'A'
                WHEN AVG(SCORE)>=80 THEN 'B'
                ELSE 'C'
            END AS GRADE,
            CASE
                WHEN AVG(SCORE)>=96 THEN 0.2
                WHEN AVG(SCORE)>=90 THEN 0.15
                WHEN AVG(SCORE)>=80 THEN 0.1
                ELSE 0
            END AS BONUS_RATE
        FROM
            HR_GRADE
        GROUP BY
            EMP_NO
    )
SELECT
    EMP_NO,
    EMP_NAME,
    GRADE,
    SAL*BONUS_RATE AS BONUS
FROM
    HR_EMPLOYEES
    NATURAL JOIN GRADE_INFO
ORDER BY
    EMP_NO;