# DB 연결정보 정의
# SQLAlchemy Engine 생성
# 세션 생성 안전한 종료 관리
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager # with문으로 DB 세션을 쓰기위한

# 데이터 베이스 url 설정
SQLALCHEMY_DATABASE_URL = "sqlite:///./products.db"

# sqlite 는 기본적으로 단일 스레드 제한
# sqlite + fastapi 조합시 다중 스레드 문제 발생
# 이를 해결하기 위한 옵션 추가 
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False} # SQLite 특정 옵션
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# yeild db가 endpoint 함수에 전달 -> endpoint 함수 종료시 finally 블록 실행
def get_db():
    db = SessionLocal()
    # return db
    try:
        yield db # 빌려주고 회수의 개념
    finally:
        db.close()
    
# 파이썬이 관리하는 방식, 데이터를 스크립트로 초기화 하거나 기타 테스트코드 적용시 사용
@contextmanager
def get_db_context():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
