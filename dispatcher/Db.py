from  sqlite3 import *
import json
import time


class Db:
        def __init__(self):
                self.conection=connect('..\Db\dispatcher.db')
                self.cursor=self.conection.cursor()


        def findActualMap(self, i):
                self.cursor.execute('SELECT * FROM maps WHERE time <'+str(int(time.time()+i))+' ORDER BY time  DESC LIMIT 1')
                a=json.loads(self.cursor.fetchone()[2])
                return a



                
        def close_(self):
                self.cursor.close()
                self.conection.commit()
                
                
                
        def saveMap(self, Time, map):
            self.cursor.execute('INSERT INTO maps (time, data, last_update) VALUES(?,?, ?)', ((str(Time)), json.dumps(map), str(int(time.time()))))
           
                


