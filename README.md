# book-rental

## 데이터 베이스 연결 및 설정
1. psql -U postgres -d template1;
2. CREATE ROLE track WITH LOGIN PASSWORD '1234';
3. CREATE DATABASE rental_db OWNER track;
4. secret.json 파일 \
DB_NAME -> track_db, \
DB_USER -> track, \
DB_PASSWORD -> 1234