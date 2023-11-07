from math import*
def sphere_volume(r):
        x=(4/3)*pi*r**3
        print('%.2f'%(x))
def sphere_surface(r):
        x=4*pi*r**2
        print('%.2f'%(x))
def cylinder_volume(r,h):
        x=pi*h*r**2
        print('%.2f'%(x))
def cylinder_surface(r,h):
        x=2*pi*r*h
        print('%.2f'%(x))
def cone_volume(r,h):
        x=(1/3)*pi*h*r**2
        print('%.2f'%(x))
def cone_surface(r,h):
        x=pi*r*(r+sqrt(h**2+r**2))
        print('%.2f'%(x))
r=int(input('r'))
h=int(input('h'))
sphere_volume(r)
sphere_surface(r)
cylinder_surface(r,h)
cylinder_volume(r,h)
cone_surface(r,h)
cone_volume(r,h)
