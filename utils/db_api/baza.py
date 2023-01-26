import sqlite3

class Database:
    def __init__(self, path_to_db="baza.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data
    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([ f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def select_birnarsalar(self):
        sql="""
        SELECT * FROM myfiles_tunukafon  
        """
        return self.execute(sql, fetchall=True)

    def tunukafon_qoshish(self, Nomi:str, Rangi:str, Narxi:int):
        sql = """
        INSERT INTO tunukafonlar(Nomi, Rangi, Narxi) VALUES(?,?,?)
        """
        self.execute(sql, parameters=(Nomi, Rangi, Narxi), commit=True)


    def add_sotib_olingan_max(self, ism:str,nomi:str, tg_id:int, tur:str, rangi:str, narxi:int, miqdor:int,vaqt:str,rasm:str=None  ):
        sql = """
        INSERT INTO myfiles_Sotib_olingan_max(ism,nomi, tg_id, tur, rangi, narxi, miqdor, vaqt, rasm)
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)
        """
        self.execute(sql, parameters=(ism, nomi, tg_id, tur, rangi, narxi, miqdor, vaqt, rasm), commit=True)

    def select_maxsulot(self, **kwargs):
        sql = """SELECT * FROM myfiles_Maxsulotlar WHERE """
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchone=True)

    def select_all_tunukafonlar(self):
        sql = """
        SELECT * FROM myfiles_Maxsulotlar
        """
        return self.execute(sql, fetchall=True)

    def select_sotib_olingan_maxlar(self, **kwargs):
        sql = """SELECT * FROM myfiles_Sotib_olingan_max WHERE """
        sql, parameters = self.format_args(sql, kwargs)

        return self.execute(sql, parameters=parameters, fetchall=True)

def logger(statement):
        print(f"""
-------------------------------------------
        Executing:
        {statement}
-------------------------------------------
""")
        
