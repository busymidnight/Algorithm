-- 코드를 입력하세요



SELECT b.user_id USER_ID, b.nickname NICKNAME, sum(a.price) as TOTAL_SALES
from USED_GOODS_BOARD a inner join USED_GOODS_USER b on a.WRITER_ID = b.USER_ID
where a.status = 'DONE'
group by a.writer_id having TOTAL_SALES >= 700000
order by TOTAL_SALES;