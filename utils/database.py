from sqlite3 import *
import os
 
class database():

    def __init__(self):
        self.conn = connect("./storage/database.db")
    
    def create(self):
        sql = "CREATE TABLE snippets ( \
            uid INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, \
            title TEXT DEFAULT 'the tittle', \
            desc TEXT, content TEXT, \
            date INTEGER DEFAULT CURRENT_TIMESTAMP \
        )"

        try:
            self.conn.execute(sql)
        except OperationalError:
            pass
 

    def get_all(self):
        sql = 'SELECT * FROM snippets'
        try:
            results = self.conn.execute(sql)
            return results.fetchall()
        except OperationalError:
            raise

    def get_by_uid(self,uid):
        sql = 'SELECT * FROM snippets WHERE uid={}'.format(uid)
        try:
            results = self.conn.execute(sql)
            return results.fetchone()
        except OperationalError:
            raise

    def find_by_title(self,title):
        sql = 'SELECT * FROM snippets WHERE title like "%{}%"'.format(title)
        try:
            results = self.conn.execute(sql)
            return results.fetchall()
        except OperationalError:
            raise

    def set(self,*args):
        
        sql = 'INSERT INTO snippets VALUES (null,"{title}", "{desc}", "{content}",CURRENT_TIMESTAMP)'

        try:
            self.conn.execute(sql.format(title=args[0],desc=args[1], content=args[2]))
        except OperationalError:
            raise
        else:
            self.conn.commit()

    def update(self,*args):

        sql = ''' UPDATE snippets
                  SET title = ? ,
                      desc = ? ,
                      content = ?,
                      date = CURRENT_TIMESTAMP
                  WHERE uid = ?'''
        try:
            self.conn.execute(sql, (args[1],args[2],args[3],args[0]))
        except OperationalError:
            raise
        else:
            self.conn.commit()

    def delele_uid(self,uid):
        sql = 'DELETE FROM snippets WHERE uid = {}'.format(uid)
        try:
            self.conn.execute(sql)
        except OperationalError:
            raise
        else:
            self.conn.commit()