SELECT a.book_id BOOK_ID, b.author_name AUTHOR_NAME, date_format(a.published_date, '%Y-%m-%d') PUBLISHED_DATE
from book a inner join author b on a.author_id = b.author_id
where a.category = '경제'
order by a.published_date asc;