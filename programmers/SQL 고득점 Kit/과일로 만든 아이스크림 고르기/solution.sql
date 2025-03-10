-- Standard Join
SELECT
    info.FLAVOR AS FLAVOR
FROM
    ICECREAM_INFO AS info
    INNER JOIN FIRST_HALF AS shipment ON info.FLAVOR=shipment.FLAVOR
WHERE
    shipment.TOTAL_ORDER>3000
    AND info.INGREDIENT_TYPE='fruit_based'
ORDER BY
    shipment.TOTAL_ORDER DESC;

-- Implicit Join
SELECT
    info.FLAVOR AS FLAVOR
FROM
    ICECREAM_INFO AS info,
    FIRST_HALF AS shipment
WHERE
    info.FLAVOR=shipment.FLAVOR
    AND shipment.TOTAL_ORDER>3000
    AND info.INGREDIENT_TYPE='fruit_based'
ORDER BY
    shipment.TOTAL_ORDER DESC;