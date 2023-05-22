-- 코드를 입력하세요
SELECT count(*) as USERS
from user_info u
where u.age between 20 and 29
    and u.joined between '2021-01-01' and '2021-12-31'