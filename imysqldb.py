import MySQLdb

class IMySQLdb:

    def __init__(self,host="127.0.0.1",user='root',password='1111',db='bitnami_redmine',port=3306,charset='utf8'):
        self.conn = MySQLdb.connect(host,user,password,db,port)
        self.conn.select_db(db)
        self.cursor = self.conn.cursor()
        self.run_sql('set names utf8')
        
        self.current_record = None
        
        
    def run_sql(self,sql):
        self.cursor.execute(sql)
    
    def get_next(self):
        self.current_record = self.cursor.fetchone()
        return self.current_record
        
    def get_current(self):
        return self.current_record
        
    def get_all(self):
        return self.cursor.fetchall()
        
    def close(self):
        self.conn.commt()
        self.cursor.close()
        self.conn.close()
 
 
if __name__ == "__main__":
    i_mysqldb = IMySQLdb()
