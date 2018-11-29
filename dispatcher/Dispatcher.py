from Route import *
from time import *


class Dispatcher:
    def __init__(self, view):
        self.objectsMaps=[]
        self.view=view
        self.limit=[view.x_count, 8]



        

    def wayBuilder(self, object):
        screen=[]
        destination=object.destination
        start=object.startPos
        for i in range(0, self.limit[0]):
            for j in range(0, self.limit[1]):
                screen.append([i, j, -1])
        for i in screen:
            if i[0]==start[0] and i[1]==start[1]:
                i[2]=object.timeOfAppear
        #vawe started
        counter=object.timeOfAppear
        while True:
            self.numbersPlacing(counter, screen)
            counter+=1
            if self.isDesignationFilled(destination, screen):
                for i in screen:
                    if i[2]!=-1 and i[0]==destination[0] and i[1]==destination[1]:
                        end=i
                
                return Route(self.findWay(end, start, screen, object))
                break
       
       
       
       
       
       
       
    def numbersPlacing(self, counter, screen): 
        variants=[]
        #print(screen)
        for i in screen:
            if i[2]==counter:
                variants.append([i[0], i[1]])
        for start in variants:
            for x in screen:
                if x[0]==start[0]+1 and x[1]==start[1] and self.isEmpty([start[0]+1, start[1], x[2]]):
                    x[2]=counter+2
                
                elif  x[0]==start[0]-1 and x[1]==start[1] and self.isEmpty([start[0]-1, start[1], x[2]]):
                    x[2]=counter+2
                
                elif x[1]==start[1]+1 and x[0]==start[0] and self.isEmpty([start[0], start[1]+1, x[2]]):
                    x[2]=counter+2
                
                elif  x[1]==start[1]-1 and x[0]==start[0] and self.isEmpty([start[0], start[1]-1, x[2]]):
                    x[2]=counter+2
                
                if x[0]==start[0]+1 and x[1]==start[1]+1 and self.isEmpty([start[0]+1, start[1]+1, x[2]]):
                    x[2]=counter+3
                
                elif x[0]==start[0]+1 and x[1]==start[1]-1 and self.isEmpty([start[0]+1, start[1]-1, x[2]]):
                    x[2]=counter+3
                
                elif x[0]==start[0]-1 and x[1]==start[1]+1 and self.isEmpty([start[0]-1, start[1]+1, x[2]]):
                    x[2]=counter+3
                
                elif x[0]==start[0]-1 and x[1]==start[1]-1 and self.isEmpty([start[0]-1, start[1]-1, x[2]]):
                    x[2]=counter+3
                

                
                
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
            curent=a
            if way[len(way)-1][2]==obj.timeOfAppear:
                break
        way=way[::-1]
        route=Route(way)
        self.mapBuilder(route, obj, way)
        return way
            
            

        
        
    
    def isEmpty(self, coords):
        if len(self.objectsMaps)!=0:
            for i in self.objectsMaps:
                try:
                    if i[coords[2]][0]==coords[0] and i[coords[2]][1]==coords[1]:
                        return False

                except:
                    pass
        if coords[2]==-1:
            return True
        else:
            return False
        

        
        


    def  mapBuilder(self, route, obj, way):
        map={}
        for i in range(route.giveByMinTime(way), route.giveByMaxTime(way)+1):
            map[i]=route.giveByTime(way, i)
        print(map)
        self.objectsMaps.append(map)
            
        
        
        

        
        
        
   