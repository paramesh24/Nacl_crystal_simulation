import numpy as np
natoms =200
system_size=60
lattice_parm=5.6
m_T=np.array([[1,0,0],
              [0,1,0],
              [0,0,1]])*lattice_parm#([[1,0,0],[0,1,0],[0,0,1]])*lattice_parm #([[0,1/2,1/2],[1/2,0,1/2],[1/2,1/2,0]])*lattice_parm
atoms=np.array([[0,0,0], #fcc #cl
               [0.5,0.5,0],
               [0.5,0,0.5],
               [0,0.5,0.5],
               [0.5,0.5,0.5],#na
               [0.5,0,0],
               [0,0.5,0],
               [0,0,0.5]])*lattice_parm

position=[]
types=[]
char=[]
xlo=2
ylo=2
zlo=2
xhi=10
yhi=10
zhi=10
n=0
for i in range(xlo,xhi):
    for j in range(ylo,yhi):
        for k in range(zlo,zhi):
              v=np.array([i,j,k])
              cor=np.inner(m_T,v)
              t=1
              for atom in atoms:
                 position.append(cor+atom)
                 if t<=4:
                    types.append(2)
                    char.append(-1)
                 else:
                    types.append(1) 
                    char.append(1)
                 n+=1
                 t+=1
                 
with open('nacl.data','w') as fdata:
    fdata.write("#Random atom data\n\n")
    fdata.write("{} atoms\n\n".format(n))                         
    fdata.write("{} atom types\n\n".format(2))  
    #Box dimension
    fdata.write("{} {} xlo xhi\n".format(0.0 ,system_size ))  
    fdata.write("{} {} ylo yhi\n".format(0.0 ,system_size ))  
    fdata.write("{} {} zlo zhi\n\n".format(0.0 ,system_size ))  
    fdata.write("Atoms\n\n")
    for i in range(0,n):
        fdata.write("{}  1  {}  {}  {}   {}   {}\n".format(i+1,types[i],char[i],position[i][0],position[i][1],position[i][2]))  
