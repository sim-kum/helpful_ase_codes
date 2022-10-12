## gives the average distance between the atoms Pt H 

import ase
from ase import geometry
slab = ase.io.read('CONTCAR_16')

H_indx = [atom.index for atom in slab if atom.symbol == 'H']
Pt_indx = [atom.index for atom in slab if atom.symbol == 'Pt']
dist = []
for j in H_indx:
        for i in Pt_indx:
                if 1 < slab.get_distance(j, i) < 1.9:
                        dist.append(slab.get_distance(j, i))

                else: continue
print(dist)
print(sum(dist)/len(dist))
