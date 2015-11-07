"""

Pre-process Chicago taxi data for visualization.

Author: Hongjian
Date: 11/7/2015

The raw file is in the ../../../dataset/ChicagoTaxi/2013-dec.txt

We map those trips to CA

"""

from shapely.geometry import Polygon, Point, box
from Block import Block

fraw = '../../dataset/ChicagoTaxi/2013-dec.txt'


if __name__ == '__main__':
    
    cas = Block.createAllCAObjects()
    with open(fraw, 'r') as fin, open('data/taxi.txt', 'w') as fout:
        header = fin.readline()
        
        for line in fin:
            try:
                ls = line.split("\t")
                
                trp = []
                trp.append( ls[2] )     # travel time
                trp.append(ls[7])       # meter on time
                
                pickup = ls[9].replace('"', '')
                pc = pickup.split(",")
                p = Point( float(pc[1]), float(pc[0]) )
                
                flag = False
                for t, ca in cas.items():
                    if ca.containPoint(p):
                        trp.append(str(t))   # meter on CA id
                        flag = True
                        break
                if not flag:
                    trp.append('-1')
                        
                        
                
                trp.append(pickup)      # meter on position
                trp.append(ls[8])       # meter off time
                
                dropoff = ls[11].replace('"', '')
                dc = dropoff.split(",")
                d = Point( float(dc[1]), float(dc[0]) )
                
                flag = False
                for t, ca in cas.items():
                    if ca.containPoint(d):
                        trp.append(str(t))   # meter off CA id
                        flag = True
                        break
                if not flag:
                    trp.append('-1')
                        
                trp.append(dropoff)     # meter off position
                
                fout.write(','.join(trp) + '\n')
            except IndexError:
                continue