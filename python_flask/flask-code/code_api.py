from os import abort

from flask import Flask, request, jsonify
import cx_Oracle
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

# oracle 연결
conn = cx_Oracle.connect("jdbc", "jdbc", "localhost:1521/xe")
cur = conn.cursor()

# /codes : get 조회
@app.route("/codes", methods=['GET'])
def get_codes():
    try:
        cur.execute("SELECT COMM_CD, COMM_NM, COMM_PARENT FROM COMM_CODE")
        rows = cur.fetchall()
        print(rows)
        # 컬럼 가져오기
        columns = [col[0] for col in cur.description]
        # 딕셔너리로 변환
        results = [dict(zip(columns, row))for row in rows]
        return jsonify(results), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# /codes : post 저장
@app.route("/codes", methods=['POST'])
def post_codes():
    data = request.get_json()
    cd = data.get('COMM_CD')
    nm = data.get('COMM_NM')
    parent = data.get('COMM_PARENT')
    if not cd or not nm :
        return jsonify({'error':'missing fields'}), 400
    try:
        sql = "INSERT INTO COMM_CODE VALUES(:1, :2, :3)"
        cur.execute(sql, [cd, nm, parent])
        conn.commit()
        return jsonify({'message':'success'}), 201
    except Exception as e:
        return jsonify({'error':str(e)}), 500

# /codes<string:comm_cd> : put 수정
@app.route("/codes/<string:comm_cd>", methods=['PUT'])
def put_codes(comm_cd):
    print(comm_cd)
    print(request.get_json())
    data = request.get_json()
    nm = data.get("COMM_NM")
    if not nm or not comm_cd :
        return jsonify({'error':'missing fields'}), 400
    try:
        sql = '''
            UPDATE COMM_CODE
            SET COMM_NM = :1
            WHERE COMM_CD = :2
        '''
        cur.execute(sql, [nm, comm_cd])
        if cur.rowcount == 0:
            return jsonify({'error':f'cd:{comm_cd} not found'}), 404
        conn.commit()
        return jsonify({'message': 'update!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# /codes/<string:comm_cd> : delete 삭제
@app.route("/codes/<string:comm_cd>", methods=['DELETE'])
def delete_item(comm_cd):
    if not comm_cd :
        return jsonify({'error':'missing fields'}), 400
    try:
        sql ='''
            DELETE FROM COMM_CODE WHERE COMM_CD = :1
        '''
        cur.execute(sql, [comm_cd])
        conn.commit()
        return jsonify({'message':'delete!'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ =='__main__':
    app.run(debug=True, host="0.0.0.0")