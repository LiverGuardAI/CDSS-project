import mysql.connector

# 라이브러리 pip install mysql-connector-python 필요

def db_connect():
    """DB 연결 객체 반환 함수"""
    conn = mysql.connector.connect(
        host="34.55.49.77",
        port=3306,
        user="acorn",
        password="acorn1234",  # 👈 직접 입력
        database="LiverGuard"         # 실제 DB명으로 변경
    )
    return conn
