WITH
    RENTAL_HISTORY_WITH_TYPE AS (
        SELECT
            HISTORY_ID,
            CAR_TYPE,
            DATEDIFF(END_DATE, START_DATE)+1 AS DURATION,
            DAILY_FEE
        FROM
            CAR_RENTAL_COMPANY_CAR
            NATURAL JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE
            CAR_TYPE='트럭'
    )
SELECT
    HISTORY_ID,
    ROUND(
        DAILY_FEE*DURATION*(100-IFNULL(MAX(DISCOUNT_RATE), 0))/100
    ) AS FEE
FROM
    RENTAL_HISTORY_WITH_TYPE
    LEFT OUTER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN ON DURATION>=CAST(DURATION_TYPE AS SIGNED)
    AND RENTAL_HISTORY_WITH_TYPE.CAR_TYPE=CAR_RENTAL_COMPANY_DISCOUNT_PLAN.CAR_TYPE
GROUP BY
    HISTORY_ID
ORDER BY
    FEE DESC,
    HISTORY_ID DESC;