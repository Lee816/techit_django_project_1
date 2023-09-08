[첫 번째 미션](https://likelion.notion.site/a39c371947944c3596655245392dc905)

# 테스트 방법

1. 가상환경 설치 및 접속
2. `pip instal`

## POSTGRESQL 사용시 연결법
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

