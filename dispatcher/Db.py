import sqlite3
import json
from time import *


class Db:
        def __init__(self):
                self.conection=sqlite3.connect('..\Db\dispatcher.db')
                self.cursor=self.conection.cursor()


        def findActualMap(self, i):
                self.cursor.execute('SELECT * FROM maps WHERE time <'+str(int(time()+i))+' ORDER BY time  DESC LIMIT 1')
                a=json.loads(self.cursor.fetchone()[2])
                return a



                
        def close_(self):
                self.cursor.close()
                self.conection.close()



