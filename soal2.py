# nomor 1
import numpy as np
def xyz():
    a=np.array([[1,-2,1],[3,1,-2],[7,-6,-1]]) #x  - 2y +  z; 3x +  y - 2z; 7x - 6y -  z
    b=np.array([6,4,10])
    hasil=np.linalg.solve(a,b) 
    return hasil
print('Nilai x =',xyz()[0],'\nNilai y =', round(xyz()[1],1),'\nNilai z =',round(xyz()[2],1))

# nomot 2
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
plt.figure('3D Plotting',figsize=(12,6))
i=plt.subplot(131, projection='3d')

## Gambar 1 x-2y+z=6
# x dan y = 0
a=np.array([[1]]) #harus dua dimensi variablenya
b=np.array([6])
z1=np.linalg.solve(a,b)
# y dan z = 0
c=np.array([[1]]) #harus dua dimensi variablenya
b=np.array([6])
x1=np.linalg.solve(c,b)
# x dan z = 0
d=np.array([[-2]]) #harus dua dimensi variablenya
b=np.array([6])
y1=np.linalg.solve(d,b)
titikx1=np.array([x1[0],0,0])
titiky1=np.array([0,y1[0],0])
titikz1=np.array([0,0,z1[0]])
i.scatter(titikx1,titiky1,titikz1,color='blue',marker='o',s=20)
#i.plot_surface(titikx1, titiky1, titikz1, color='green')
i.set_xlabel('Nilai X')
i.set_ylabel('Nilai Y')
i.set_zlabel('Nilai Z')
i.text2D(0.05, 0.95, "x-2y+z=6", transform=i.transAxes)
verts = [list(zip(titikx1,titiky1,titikz1))]
i.add_collection3d(Poly3DCollection(verts,facecolor='red',alpha=0.2))

## Gambar 2 3x+y-2z=4
j=plt.subplot(132, projection='3d')
# x dan y = 0
a2=np.array([[-2]]) #harus dua dimensi variablenya
b2=np.array([4])
z2=np.linalg.solve(a2,b2)
# y dan z = 0
c2=np.array([[3]]) #harus dua dimensi variablenya
b2=np.array([4])
x2=np.linalg.solve(c2,b2)
# x dan z = 0
d2=np.array([[1]]) #harus dua dimensi variablenya
b2=np.array([4])
y2=np.linalg.solve(d2,b2)
titikx2=np.array([x2[0],0,0])
titiky2=np.array([0,y2[0],0])
titikz2=np.array([0,0,z2[0]])
j.scatter(titikx2,titiky2,titikz2,color='red',marker='o',s=20)
j.set_xlabel('Nilai X')
j.set_ylabel('Nilai Y')
j.set_zlabel('Nilai Z')
verts = [list(zip(titikx2,titiky2,titikz2))]
j.text2D(0.05, 0.95, "3x+y-2z=4", transform=j.transAxes)
j.add_collection3d(Poly3DCollection(verts,facecolor='green',alpha=0.2))

## Gambar 3 7x-6y-1z=10
k=plt.subplot(133, projection='3d')
# x dan y = 0
a3=np.array([[-1]]) #harus dua dimensi variablenya
b3=np.array([10])
z3=np.linalg.solve(a3,b3)
# y dan z = 0
c3=np.array([[7]]) #harus dua dimensi variablenya
b3=np.array([10])
x3=np.linalg.solve(c3,b3)
# x dan z = 0
d3=np.array([[-6]]) #harus dua dimensi variablenya
b3=np.array([10])
y3=np.linalg.solve(d3,b3)
titikx3=np.array([x3[0],0,0])
titiky3=np.array([0,y3[0],0])
titikz3=np.array([0,0,z3[0]])
k.scatter(titikx3,titiky3,titikz3,color='green',marker='o',s=20)
k.set_xlabel('Nilai X')
k.set_ylabel('Nilai Y')
k.set_zlabel('Nilai Z')
verts = [list(zip(titikx3,titiky3,titikz3))]
k.text2D(0.05, 0.95, "7x-6y-1z=10", transform=k.transAxes)
k.add_collection3d(Poly3DCollection(verts,facecolor='purple',alpha=0.2))
plt.grid(True)
plt.show()

