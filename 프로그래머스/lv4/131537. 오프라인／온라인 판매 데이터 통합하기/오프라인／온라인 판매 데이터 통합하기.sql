-- 코드를 입력하세요
SELECT DATE_FORMAT(SALES_DATE,'%Y-%m-%d') as SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
from ONLINE_SALE
where SALES_DATE between '2022-03-01' and '2022-03-31'
union all
SELECT DATE_FORMAT(SALES_DATE,'%Y-%m-%d') as SALES_DATE, PRODUCT_ID, NULL as USER_ID ,SALES_AMOUNT
from OFFLINE_SALE
where SALES_DATE between '2022-03-01' and '2022-03-31'

order by 1,2,3 asc;