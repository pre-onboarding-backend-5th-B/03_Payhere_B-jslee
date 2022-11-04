# 03_Payhere_B-jslee
페이히어 백엔드 과제 전형

## User 
### MODEL
- User
  -  email
  -  password

### API
- Functiona
  - /api/signup: 회원가입
  - /api/login: 로그인
  - /api/logout: 로그아웃

- 제약사항
  - 토큰 인증 방식

## AccountBook
### MODEL
- AccountBook(가계부)
  - datetime
  - money
  - status(소득/지출 인지 확인)
  - is_delete(soft delete)

- Memo(메모)
  - account_book(fk)
  - content
  - datatetime
  - is_delete(soft? hard?)
### API
- CRRUD
  - `GET` /api/account-book 가계부 목록 조회
  - `POST` /api/account-book 가계부 생성
  - `POST` /api/account-book/:id/memo
  - `GET` /api/account-book/:id 가계부 상세내용 조회 + Memo
  - `PATCH/PUT` /api/account-book/:id 가계부 내용 수정
  - `PATCH/PUT` /api/account-book/:id/memo/:id 메모 수정 
  - `DELETE` /api/account-book/:id 가계부 삭제(soft delete)
  - `DELETE` /api/account-book/:id/memo/:id  메모 삭제(soft delete)
- function
  - /api/account-book/:id/retore 가계부 복구
  - /api/memo/:id/retore 메모 복구 
- 제약사항
  - 로그인한 사용자가 본인의 가계부만 접근 가능
  - 삭제한 내역을 복구할 수 있어야함