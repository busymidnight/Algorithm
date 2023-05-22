-- 코드를 입력하세요
SELECT ug.BOARD_ID, ug.WRITER_ID,ug.TITLE,ug.PRICE, 
    CASE 
        WHEN ug.STATUS = 'SALE'
        THEN '판매중'
        WHEN ug.STATUS = 'RESERVED'
        THEN '예약중'
        WHEN ug.STATUS = 'DONE'
        THEN '거래완료'
    END as STATUS
from USED_GOODS_BOARD ug
where ug.CREATED_DATE = '2022-10-05'
order by ug.BOARD_ID desc