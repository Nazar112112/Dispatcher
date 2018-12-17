from math import *



class Route:
    def __init__(self, way, name, obj, side):
        self.route=self.fillWay(way, name, obj, side)
        
    def CalculateDist(self, a, b, side):
            if a==[] or b==[]:
                return side
            if a[0]!=b[0]:
                if a[1]!=b[1]:
                    return side*1.4
                else:
                    return side
            else:
                if a[1]!=b[1]:
                    return side  
                
        
        
    
       
    def addCell(self, cell, time, route):
        if cell!=[]:
            if time not in route.keys():
                route[time]=[] 
            route[time].append([cell[0], cell[1]])
            return route
    
    
        
        
    def fillWay(self, way, name, obj, side):           
        #алгоритм по принципу 0\швидкість, 0+100\швидкість
        route={}
        route['name']=name
        t=0
        T=obj.timeOfAppear
        d=0
        cCell=[]
        way.append([])
        for i in range(0, len(way)-1):
            if way[i]==[]:
                continue
            d=self.CalculateDist(cCell, way[i+1], side)
            t=d/obj.speed
            if T==int(T):
                route=self.addCell(way[i], int(T), route)
            for a in range(int(T), ceil(T+t)):
               route=self.addCell(way[i], a, route)
            cCell=way[i]
            T+=t
        for i in route.keys():
            if route[i]==[]:
                del route[i]   
        return route
    
    
    def giveByMinTime(self, way):
        a=100000000
        for i in way.keys():
            if i=='name':
                continue
            if int(i)<a:
                a=int(i)
        return a
    #
    
    def giveByMaxTime(self, way):
        a=0
        for i in way.keys():
            if i=='name':
                continue
            if int(i)>a:
                a=int(i)
        return a
    
    
    def giveByTime(self, way, time):
        for i in way.keys():
            if i==time:
                return way[i]
        if time>self.giveByMaxTime(way) or time<self.giveByMinTime(way):
            return False
        for i in range(1, time+1):
            for u in way.keys():
                if u==time-i:
                    return way[u]
                
            
        
            
        
                
            