-- Standard Join
SELECT
    board.TITLE,
    board.BOARD_ID,
    reply.REPLY_ID,
    reply.WRITER_ID,
    reply.CONTENTS,
    DATE_FORMAT (reply.CREATED_DATE, "%Y-%m-%d") AS CREATED_DATE
FROM
    USED_GOODS_BOARD AS board
    INNER JOIN USED_GOODS_REPLY AS reply ON board.BOARD_ID=reply.BOARD_ID
WHERE
    YEAR (board.CREATED_DATE)=2022
    AND MONTH (board.CREATED_DATE)=10
ORDER BY
    reply.CREATED_DATE,
    board.TITLE;

-- Implicit Join
SELECT
    board.TITLE,
    board.BOARD_ID,
    reply.REPLY_ID,
    reply.WRITER_ID,
    reply.CONTENTS,
    DATE_FORMAT (reply.CREATED_DATE, "%Y-%m-%d") AS CREATED_DATE
FROM
    USED_GOODS_BOARD AS board,
    USED_GOODS_REPLY AS reply
WHERE
    board.BOARD_ID=reply.BOARD_ID
    AND YEAR (board.CREATED_DATE)=2022
    AND MONTH (board.CREATED_DATE)=10
ORDER BY
    reply.CREATED_DATE,
    board.TITLE;