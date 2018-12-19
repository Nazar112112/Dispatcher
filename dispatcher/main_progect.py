from time import *
import sqlite3 
from threading import *
import threading
import json
from View import *
from Db import *
from Object import *
from Dispatcher import *



side=100

drones=[]

drone=Drone()
drone.create(100, 100, 10, 5, 1, 100, 'a-211', [2, 0], 0, [4, 0])
drones.append(drone)

dr=Drone()
dr.create(100, 100, 10, 5, 1, 200, 'a-212', [2, 5], 3, [13, 5])
drones.append(dr)

dr2=Drone()
dr2.create(100, 100, 10, 5, 1, 50, 'a-215', [13, 3], 1, [0, 0])
drones.append(dr2)
dr3=Drone()

dr3.create(100, 100, 10, 5, 1, 123, 'a-213', [0, 0], 5, [13, 8])
drones.append(dr3)

stable=[]
limits=[13, 8]

bld=Stable()
bld.fill([9, 0])
bld2=Stable()
bld2.fill([3, 0])
bld1=Stable()
bld1.fill([3,1])
bld3=Stable()
bld3.fill([1, 0])
bld4=Stable()
bld4.fill([13, 0])

view=View(side, limits)
#obj=[['a-111', 0, 0], ["a-112", 1000, 200]]
db=Db()
end=False
dp=Dispatcher(limits, side)
dp.addStables(bld)
dp.addStables(bld2)
dp.addStables(bld1)
dp.addStables(bld3)
stable.append(bld)
stable.append(bld1)
stable.append(bld2)
stable.append(bld3)
stable.append(bld4)




#db.writeToDB([route, rt])
routes=[]
for i in drones:
    routes.append(dp.wayBuilder(i)) 
CurrentTime=(int(time()))

for i in  dp.objectsMaps.keys():
    db.saveMap(i+CurrentTime, dp.objectsMaps[i])
    
    

tim=time()
while not end: 
    if int(time()-tim):
        view.draw(db.findActualMap(0), stable)
        tim=time()
    view.update()
    

                

