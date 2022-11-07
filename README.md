# 03_Payhere_B-jslee

페이히어 백엔드 과제 전형

# 설계

## ERD

<p align="center">
  <img src="docs/img/erd.png" width="60%" height="60%" alt="페이히어 erd"/>
</p>

## User

### MODEL

- User
    - **id(pk)**
    - name
    - email
    - password

- 제약사항
    - 토큰 인증 방식

## AccountBook

### MODEL

- AccountBook(가계부)
    - **id(pk)**
    - user(fk - OneToMany): User 과 1:N 관계
    - name: 가계부 이름

- AccountBookDiary(가계부)
    - account_book(fk - OneToMany): AccountBook 과 1:N 관계
    - money: 금액
    - status: 수입/지출 상태
    - is_delete: 삭제 여부
    - created_at: 생성 날짜
    - updated_at: 수정 날짜

- Memo(메모)
    - **id(pk)**
    - account_book_diary(fk - OneToMany): AccountBookDiary 과 1:N 관계
    - content: 메모 내용
    - created_at: 생성 날짜
    - updated_at: 수정 날짜

- 제약사항
  - 로그인한 사용자가 본인의 가계부만 접근 가능
  - 삭제한 내역을 복구할 수 있어야함
    - 로그인한 사용자가 본인의 가계부만 접근 가능
    - 삭제한 내역을 복구할 수 있어야함

## API

<details>

  <summary>
    이미지 보기
  </summary>

  <div align="center">
    <img src="docs/img/api_list.png" width="70%" height="70%" alt="페이히어 api 목록"/>
  </div>

</details>