import sqlite3

class BaseHlpt:
    def __init__(self):
        self.con = sqlite3.connect("Quiz.db")
        self.cur = self.con.cursor()
    
    def create_tables(self):
        self.cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,age INTEGER)")
        
        self.cur.execute("CREATE TABLE IF NOT EXISTS grades(id INTEGER PRIMARY KEY AUTOINCREMENT,st_id INTEGER NOT NULL,sub_id INTEGER NOT NULL,mark INTEGER NOT NULL)")

        self.cur.execute("CREATE TABLE IF NOT EXISTS sub(id INTEGER PRIMARY KEY AUTOINCREMENT,sb TEXT NOT NULL)")
        
        self.con.commit()
    
    def add_student(self,*args):
        
        self.cur.execute("INSERT INTO student(name,age) VALUES(?,?)",(args[0],args[1]))

        self.con.commit()
    
    def del_student(self,id):
        self.cur.execute("DELETE FROM student WHERE id=?",(id,))

        self.con.commit()
    
    def select_students(self):
        self.cur.execute("SELECT id, name, age FROM student")
        return self.cur.fetchall()
    
    def add_mark(self,st_id,sub_id,mark):

        self.cur.execute("INSERT INTO grades(st_id,sub_id,mark) VALUES(?,?,?)",(st_id,sub_id,mark))
        
        self.con.commit()
    
    def select_student_info(self,id):
        
        self.cur.execute("SELECT student.name,sub.sb,grades.mark FROM grades JOIN student ON grades.st_id = student.id JOIN sub ON grades.sub_id = sub.id WHERE student.id=?",(id,))
        
        return self.cur.fetchall()  
    
    def add_sb(self,s):
        
        self.cur.execute("INSERT INTO sub(sb) VALUES(?)",(s,))

        self.con.commit()