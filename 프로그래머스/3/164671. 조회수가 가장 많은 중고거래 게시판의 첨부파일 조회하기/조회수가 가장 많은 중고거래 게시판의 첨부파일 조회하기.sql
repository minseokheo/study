-- 코드를 입력하세요
SELECT CONCAT('/home/grep/src/', A.BOARD_ID, '/', B.FILE_ID, B.FILE_NAME, B.FILE_EXT) AS 'FILE_PATH'
FROM USED_GOODS_BOARD AS A, USED_GOODS_FILE AS B
WHERE A.BOARD_ID = B.BOARD_ID AND A.VIEWS = 
                                    (SELECT MAX(VIEWS)
                                    FROM USED_GOODS_BOARD)
ORDER BY 1 DESC