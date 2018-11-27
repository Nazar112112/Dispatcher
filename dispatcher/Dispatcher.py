from route import *


class Dispatcher:
    def __init__(self, view):
        self.exception=[]
        self.slots=[]
        self.view=view
        self.limit=[view.x_count, 8]
        print(self.limit)


        

    def wayBuilder(self, object):
        screen=[]
        designation=object.designation
        start=object.startPos
        for i in range(0, self.limit[0]):
            for j in range(0, self.limit[1]):
                screen.append([i, j, -1])
        for i in screen:
            if i[0]==start[0] and i[1]==start[1]:
                i[2]=0
        #vawe started
        counter=0
        while True:
            self.numbersPlacing(counter, screen)
            counter+=1
            if self.isDesignationFilled(designation, screen):
                for i in screen:
                    if i[2]!=-1 and i[0]==designation[0] and i[1]==designation[1]:
                        end=i
                
                return Route(self.findWay(end, start, screen))
                break
       
       
       
       
       
       
       
    def numbersPlacing(self, counter, screen): 
        variants=[]
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
                                                            

        
        
    def findWay(self, end, start, screen):
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
            if way[len(way)-1][2]==0:
                break
        way=way[::-1]
        return way
            
            

        
        
    
    def isEmpty(self, coords):
        if coords[2]==-1:
            return True
        else:
            return False
    

        
        


        
        
        
        

        
        
        
   