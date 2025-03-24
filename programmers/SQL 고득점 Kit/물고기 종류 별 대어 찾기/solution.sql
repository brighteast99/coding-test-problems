WITH
    max_length_info AS (
        SELECT
            ID,
            FISH_NAME,
            LENGTH,
            MAX(LENGTH) OVER (
                PARTITION BY
                    FISH_TYPE
            ) AS MAX_LENGTH
        FROM
            FISH_INFO AS info
            NATURAL JOIN FISH_NAME_INFO AS name_info
    )
SELECT
    ID,
    FISH_NAME,
    LENGTH
FROM
    max_length_info
WHERE
    LENGTH=MAX_LENGTH
ORDER BY
    ID;