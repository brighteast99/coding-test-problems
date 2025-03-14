SELECT
    parent.ID,
    COUNT(child.ID) AS CHILD_COUNT
FROM
    ECOLI_DATA AS parent
    LEFT OUTER JOIN ECOLI_DATA AS child ON child.PARENT_ID=parent.ID
GROUP BY
    parent.ID;