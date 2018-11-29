from time import *
import sqlite3 
import threading
import json
from View import *
from Db import *
from Aircraft import *
from Dispatcher import *

def fill(obj):
        a=[]
        t=int(time()-3)
        conection=sqlite3.connect('..\Db\dispatcher.db')
        cursor=conection.cursor()
        for i in range(2, 12):
                if i==2:
                    for y in obj:
                        if y.timeOfAppear==0:
                            a.append([y.name, y.startPos[0]*100, y.startPos[1]*100])
                cursor.execute('INSERT INTO maps (time, data, last_update) VALUES(?,?, ?)', (str(int(t+i)), json.dumps(a), str(time())))
                temporary=[]
                for y in obj:
                    if (i-2)>=y.timeOfAppear:
                        temporary.append([y.name, y.startPos[0]*100+(i-2-y.timeOfAppear)*y.speed[0], y.startPos[1]*100+(i-2-y.timeOfAppear)*y.speed[1]])
                a=temporary                


                # print("eror")
        print("Done!!")
        '''
        cursor.execute('SELECT * FROM maps')
        i=cursor.fetchone()
        while i is not None:
           print(str(i[0]))
           print(str(i[1])+'\n')
           i=cursor.fetchone() '''
        conection.commit()
        cursor.close()
        conection.close()


drone=Drone()
drone.create(100, 100, 10, 5, 1, [100, 0], 'a-211', [0, 0], 0, [3, 4])
dr=Drone()
dr.create(100, 100, 10, 5, 1, [-100, -50], 'a-111', [0, 1], 2, [0, 0])
helicopter=Drone()
helicopter.create(100, 100, 10, 5, 1, [0, -50], 'a-111', [1, 1], 0, [0, 0])
fill([drone, dr, helicopter])



#cursor=title.cursor()
#cursor.execute('SELECT * FROM maps')
#i=cursor.fetchone()
#while i is not None:
   # print(i[0])
  #  print(i[1]+'\n')
    #i=cursor.fetchone()
#cursor.close()
#title.close()



view=View()
#obj=[['a-111', 0, 0], ["a-112", 1000, 200]]
db=Db()
end=False
dp=Dispatcher(view)

r=dp.wayBuilder(dr)
print(r.route)
route=dp.wayBuilder(drone)
print(route.route)


while not end:  
    view.draw(db.findActualMap(0))
    view.update()
    sleep(1)

                

