-- 코드를 입력하세요
SELECT m.MEMBER_ID, m.MEMBER_NAME, m.GENDER, DATE_FORMAT(m.date_of_birth,'%Y-%m-%d') AS DATE_OF_BIRTH
from MEMBER_PROFILE m
where m.date_of_birth like '%-03-%' and m.gender = 'W' and m.TLNO IS NOT NULL
order by m.Member_ID asc;
