WITH
    RANK_INFO AS (
        SELECT
            MEMBER_ID,
            RANK() OVER (
                ORDER BY
                    COUNT(REVIEW_ID) DESC
            ) AS REVIEW_RANK
        FROM
            REST_REVIEW
        GROUP BY
            MEMBER_ID
    )
SELECT
    MEMBER_NAME,
    REVIEW_TEXT,
    DATE_FORMAT(REVIEW_DATE, '%Y-%m-%d') AS REVIEW_DATE
FROM
    MEMBER_PROFILE
    NATURAL JOIN REST_REVIEW
    NATURAL JOIN RANK_INFO
WHERE
    REVIEW_RANK=1
ORDER BY
    REVIEW_DATE,
    REVIEW_TEXT;