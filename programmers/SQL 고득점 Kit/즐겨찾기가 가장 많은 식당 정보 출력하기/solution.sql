SELECT
    FOOD_TYPE,
    REST_ID,
    REST_NAME,
    FAVORITES
FROM
    (
        SELECT
            *,
            RANK() OVER (
                PARTITION BY
                    FOOD_TYPE
                ORDER BY
                    FAVORITES DESC
            ) AS RANKING
        FROM
            REST_INFO
    ) AS POPULAR_REST
WHERE
    RANKING=1
ORDER BY
    FOOD_TYPE DESC;