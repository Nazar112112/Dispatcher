from Route import *
from time import *


class Dispatcher:
    def __init__(self, limits, side):
        self.objectsMaps={}
        self.side=side
        self.limit=limits
        self.stables=[]



        

    def wayBuilder(self, object):
        screen=[]
        destination=object.destination
        start=object.startPos
        for i in range(0, self.limit[0]+1):
            for j in range(0, self.limit[1]+1):
                screen.append([i, j, -1])
            
        for i in screen:
            if i[0]==start[0] and i[1]==start[1]:
                i[2]=object.timeOfAppear
        #vawe started
        counter=object.timeOfAppear
        while True:
            self.numbersPlacing(counter, screen, object)
            counter+=1
            if self.isDesignationFilled(destination, screen):
                for i in screen:
                    if i[2]!=-1 and i[0]==destination[0] and i[1]==destination[1]:
                        end=i
                return Route(self.findWay(end, start, screen, object), object.name, object, self.side)
                break
            #break
       
       
    def addStables(self, stable):
        self.stables.append(stable)
        
       
       
       
       
    def numbersPlacing(self, counter, screen, obj): 
        variants=[]
        for i in screen:
            if i[2]==counter:
                variants.append([i[0], i[1]])
        for start in variants:
            for x in screen:
                newCell=False
                if x[0]==start[0]+1 and x[1]==start[1] and self.isEmpty([start[0]+1, start[1], x[2]], counter+2, obj):
                    x[2]=counter+2
                    newCell=True
                
                elif  x[0]==start[0]-1 and x[1]==start[1] and self.isEmpty([start[0]-1, start[1], x[2]],counter+2,obj):
                    x[2]=counter+2
                    newCell=True
                elif x[1]==start[1]+1 and x[0]==start[0] and self.isEmpty([start[0], start[1]+1, x[2]],counter+2,obj):
                    x[2]=counter+2
                    newCell=True
                elif  x[1]==start[1]-1 and x[0]==start[0] and self.isEmpty([start[0], start[1]-1, x[2]],counter+2, obj):
                    x[2]=counter+2
                    newCell=True
                #Треба для кожного перевірити кутові елементи  
                if x[0]==start[0]+1 and x[1]==start[1]+1 and self.isEmpty([start[0]+1, start[1]+1, x[2]],counter+3, obj):
                    x[2]=counter+3
                    newCell=True
                elif x[0]==start[0]+1 and x[1]==start[1]-1 and self.isEmpty([start[0]+1, start[1]-1, x[2]],counter+3, obj):
                    x[2]=counter+3
                    newCell=True
                elif x[0]==start[0]-1 and x[1]==start[1]+1 and self.isEmpty([start[0]-1, start[1]+1, x[2]],counter+3, obj):
                    x[2]=counter+3
                    newCell=True
                elif x[0]==start[0]-1 and x[1]==start[1]-1 and self.isEmpty([start[0]-1, start[1]-1, x[2]],counter+3, obj):
                    x[2]=counter+3 
                    newCell=True



                
                
    def isDesignationFilled(self, end, screen):
        for i in screen:
            if i[2]!=-1 and i[0]==end[0] and i[1]==end[1]:
                return True
                                                            

        
        
    def findWay(self, end, start, screen, obj):
        posibility=[]
        way=[end]
        for i in screen:
            if i[2]!=-1:
                posibility.append(i)
        a=[0, 0, 1000000000000000]
        curent=end
        while True:
            for i in posibility:
                if (i[0]==curent[0]+1 or i[0]==curent[0]-1 or i[0]==curent[0]) and (i[1]==curent[1] or i[1]==curent[1]+1 or i[1]==curent[1]-1) and i[2]<a[2]:
                    a=i
            way.append(a)
            #якщо елемент діагональний додати вільні кутові
            curent=a
            if way[len(way)-1][2]==obj.timeOfAppear:
                break
        way=way[::-1]
        route=Route(way, obj.name, obj, self.side)
        self.mapBuilder(route, obj, way)
        return way
            
            

        
        
    
    def isEmpty(self, coords, futureTime, obj):
        if len(self.objectsMaps)!=0:
            for i in range(0, int(((self.side*1.4)/obj.speed))*2+2):
                try:
                    self.objectsMaps[futureTime+i][coords[0]][coords[1]]
                    return False
                except:
                    pass
        for i in self.stables:
            if i.coords[0]==coords[0] and i.coords[1]==coords[1]:
                return False
        if coords[2]==-1:
            return True
        else:
            return False
        

        
        


    def  mapBuilder(self, route, obj, way):
        map=self.objectsMaps
        for i in range(route.giveByMinTime(route.route), route.giveByMaxTime(route.route)+1):
            for a in route.giveByTime(route.route, i):
                if i not in map.keys():
                    map[i]={}
                if a[0] not in map[i]:
                    map[i][a[0]]={}
                map[i][a[0]][a[1]]=obj.name
                   
                        
        self.objectsMaps=map

        
        

        
        
        
   