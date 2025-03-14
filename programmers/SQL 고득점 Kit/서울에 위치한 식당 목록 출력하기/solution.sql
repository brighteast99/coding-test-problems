SELECT
    info.REST_ID,
    info.REST_NAME,
    info.FOOD_TYPE,
    info.FAVORITES,
    info.ADDRESS,
    ROUND(AVG(review.REVIEW_SCORE), 2) AS SCORE
FROM
    REST_INFO AS info
    INNER JOIN REST_REVIEW AS review ON info.ADDRESS LIKE '서울%'
    AND info.REST_ID=review.REST_ID
GROUP BY
    info.REST_ID
ORDER BY
    SCORE DESC,
    info.FAVORITES DESC;