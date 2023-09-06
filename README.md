# book-rental

## 데이터 베이스 연결 및 설정
1. psql -U postgres -d template1;
2. CREATE ROLE track WITH LOGIN PASSWORD '1234';
3. CREATE DATABASE rental_db OWNER track;
4. secret.json 파일 \
DB_NAME -> track_db, \
DB_USER -> track, \
DB_PASSWORD -> 1234

## fixture 데이터 
- 데이터 내보내기 <br>
`python -Xutf8 manage.py dumpdata books.category books.book --indent 2 >  books_data.json`
- 데이터 가져오기 <br>
`python -Xutf8 manage.py loaddata books_data.json`