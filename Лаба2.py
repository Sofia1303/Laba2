import math

class Sphere:
    def __init__(self,r,x,y,z):
        self.r=r
        self.x=x
        self.y=y
        self.z=z
    def get_volume(self):
        return (4*math.pi*self.r**3)/3
    def get_square_(self):
        return 4*math.pi*self.r**2
    def get_radius_(self):
        return self.r
    def get_centre_(self):
        return (self.x,self.y,self.z)
    def set_radius_(self,r):
        self.r=r
    def set_center(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
    def is_point_inside(self,x,y,z):
        return ((x-self.x)**2+(y-self.y)**2+(z-self.z)**2)<self.r**2

ob = Sphere (1,2,3,4)
print('Volume is ',ob.get_volume())
print('Square is ',ob.get_square_())
print('Radius is ',ob.get_radius_())
print('Center x,y,z is ',ob.get_centre_())
ob.set_radius_(10)
print('New radius is ',ob.get_radius_())
ob.set_center(4,3,2)
print('New center x,y,z is ',ob.get_centre_())
print('This point is inside of sphere ', ob.is_point_inside(5,6,7))