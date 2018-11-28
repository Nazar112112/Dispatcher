#


class Aircraft:
    def __init__(self, name):
        self.maxHorisontal=0
        self.maxVertical=0
        self.maxSpeedUpHorisontal=0
        self.maxSpeedUpVertical=0
        self.priority=0
        self.name=name
        self.speed=[]
        
        
        
        
    def move(self, map, time):
        data=[]
        if map !=[]:
            for i in map:
                print(i[0], self.name)
                if i[0]==self.name:
                    data.append(self.name)
                    data.append(i[1]+self.speed[0]*time)
                    data.append(i[2]+self.speed[1]*time)
                    break
        else:
            data.append(self.name)
            data.append(self.speed[0]*time)
            data.append(self.speed[1]*time)
            
        return data
                
                    
        

        
        
    def create(self, maxHorisontal, maxVertical, maxSpeedUpHorisontal, maxSpeedUpVertical, priority, speed, name, startPos, timeOfAppear, destination):
        self.maxHorisontal=maxHorisontal
        self.maxVertical=maxVertical
        self.maxSpeedUpHorisontal=maxSpeedUpHorisontal
        self.maxSpeedUpVertical=maxSpeedUpVertical
        self.priority=priority
        self.speed=speed
        self.name=name
        self.startPos=startPos
        self.timeOfAppear=timeOfAppear
        self.destination=destination
    
    
    
class Drone(Aircraft):
    def __init__(self):
        pass
        
class Helicopter(Aircraft):
    def __init__(self):
        pass
        
class Airplane(Aircraft):
    def __init__(self):
        pass






        