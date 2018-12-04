



class Route:
    def __init__(self, way, name):
        self.route=self.fillWay(way, name)
        
        
        
        
    def fillWay(self, way, name):
        route={}
        route['name']=name
        for i in way:
            route[i[2]]=[i[0], i[1]]
        return route
    
    
    def giveByMinTime(self, way):
        a=[0, 0, 100000000]
        for i in way:
            if i[2]<a[2]:
                a=i
        return a[2]
    #
    
    def giveByMaxTime(self, way):
        a=[0,0,0]
        for i in way:
            if i[2]>a[2]:
                a=i
        return a[2]
    
    
    def giveByTime(self, way, time):
        for i in way:
            if i[2]==time:
                return [i[0], i[1]]
        if time>self.giveByMaxTime(way) or time<self.giveByMinTime(way):
            return False
        for i in range(1, time+1):
            for u in way:
                if u[2]==time-i:
                    return [u[0], u[1]]
                
            
        
            
        
                
            