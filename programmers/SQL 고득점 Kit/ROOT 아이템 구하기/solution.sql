SELECT
    ITEM_ID,
    ITEM_NAME
FROM
    ITEM_INFO AS info
    NATURAL JOIN ITEM_TREE AS tree
WHERE
    PARENT_ITEM_ID IS NULL
ORDER BY
    ITEM_ID;