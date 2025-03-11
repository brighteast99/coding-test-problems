-- With subquery
SELECT
    info.ITEM_ID,
    info.ITEM_NAME,
    info.RARITY
FROM
    ITEM_INFO AS info
    INNER JOIN ITEM_TREE AS tree ON info.ITEM_ID=tree.ITEM_ID
WHERE
    tree.PARENT_ITEM_ID IN (
        SELECT
            ITEM_ID
        FROM
            ITEM_INFO
        WHERE
            RARITY='RARE'
    )
ORDER BY
    info.ITEM_ID DESC;

-- With 3 table join
SELECT
    info.ITEM_ID,
    info.ITEM_NAME,
    info.RARITY
FROM
    ITEM_INFO AS info
    INNER JOIN ITEM_TREE AS tree ON info.ITEM_ID=tree.ITEM_ID
    INNER JOIN ITEM_INFO AS parent_info ON tree.PARENT_ITEM_ID=parent_info.ITEM_ID
WHERE
    parent_info.RARITY='RARE'
ORDER BY
    info.ITEM_ID DESC;