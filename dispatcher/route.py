



class Route:
    def __init__(self, way):
        self.route=self.fillWay(way)
        
        
        
        
    def fillWay(self, way):
        route={}
        for i in way:
            route[i[2]]=[i[0], i[1]]
        return route