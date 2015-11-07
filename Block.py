"""
Author: Hongjian
Date: 11/7/2015
"""


import shapefile
from shapely.geometry import Polygon, Point, box


class Block:
    
    
    def __init__( self, shp ):
        """
        Build one Block object from the shapefile._Shape object
        """
        self.bbox = box(*shp.bbox)
        self.polygon = Polygon(shp.points)
        self.count = {'total': 0} # type: value
        
        
    
    def containPoint( self, p ):
        """
        return true if the point p happened within current Block
        """
        if self.bbox.contains(p):
            if self.polygon.contains(p):
                return True
        return False
            
    @classmethod
    def createAllCAObjects( cls ):
        cls.casf = shapefile.Reader('data/ChiCA_gps/ChiCaGPS')
        cls.cas = {}
        
        shps = cls.casf.shapes()
        for idx, shp in enumerate(shps):
            tid = cls.casf.record(idx)[4]
            trt = Block(shp)
            cls.cas[int(tid)] = trt
            
        return cls.cas
        