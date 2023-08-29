
#https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
import math

class Points(object):
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z
        self.no= self.x,self.y,self.z

    def __sub__(self, no):
        return Points(self.x-no.x,self.y-no.y,self.z-no.z)

    def dot(self, no):
        return no.x*self.x+no.y*self.y+no.z*self.z

    def cross(self, no):
        return Points(self.z*no.y-self.y*no.z,self.z*no.x-self.x*no.z,self.x*no.y-self.y*no.x)
        
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)
    
if __name__=='__main__':
    #Coordinates function to input the different coordinates of the planes
    def Coordinates():
        points = list()
        for i in range(3):
            if i==0:
                a = int(input("input the x coordinate="))
                points.append(a)
                continue
            if i==1:
                a = int(input("input the y coordinate="))
                points.append(a)
                continue
            else:
                a = int(input("input the z coordinate="))
                points.append(a)
                continue
        return points    
     
    
    points1=Coordinates()
    print(points1)
    points2=Coordinates()
    print(points2)
    points3=Coordinates()
    print(points3)
    points4=Coordinates()
    print(points4)
    
    a=Points(*points1)
    b=Points(*points2)
    c=Points(*points3)
    d=Points(*points4)
    AB=b-a
    CD=d-c
    BC=c-b
    
    #application of cross product to get the perpendiculars of the planes
    Perpendicular1=AB.cross(BC)
    Perpendicular2=BC.cross(CD)
    
    #to find the angle between the planes
    if Perpendicular1 or Perpendicular2==0:
        print('The planes are parallel')
    else:
        Angle=math.acos(Perpendicular1.dot(Perpendicular2)/(Perpendicular1.absolute()*Perpendicular2.absolute()))
        print("%.2f"%math.degrees(Angle))
    
    
    
