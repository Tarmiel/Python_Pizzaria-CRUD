import pymysql.cursors


def getConnection():
    # conexão com o banco de dados
    conexao = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='erp',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    return conexao
