# 데코레이터 @app.get('/hello') --- 라우터      http://localhost:8000/hello --> 서버내의 해당 함수를 실행
# @app.get('/hello')

@app.get('/hello')
def say_hello():
    return {'message' : 'Hello World'}

# 경로 파라미터 vs 쿼리 파라미터
# http://localhost:8000/hello/홍길동  경로 파라미터
@app.get('/hello/{name}')
def say_hello(name: str):
    return {'message': f'Hello {name}'}

@app.get('/greet')
def say_hello(name: str, age: int):
    return