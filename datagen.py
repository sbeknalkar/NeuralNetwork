# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 21:10:03 2018

@author: sumed
"""

from skyfield.api import load

ts = load.timescale()

class _Date:
    """ Get day, month and year
    Will be used while making """
    def __init__(self, dt, mnth, yr):
        self.dt = dt
        self.mnth = mnth
        self.yr = yr
        

    def leap_year(self):
        if (self.yr % 4 == 0):
            return True
        else:
            return False
        

class _Planet:
    """ Loading planet data from .bsp file"""
    def __init__(self, numplan):
        numplan = int(numplan)
        self.numplan = numplan
        planets = load('de421.bsp')
        #self.planetstr = self.getplanetstr()
        self.planet = planets[self.getplanetstr()]
        
        
    def getplanetstr(self):
        planetstr = ['mercury','venus','earth','mars',
                     'jupiter','saturn','uranus','neptune','moon', 'sun',
                     'jupiter barycenter', 'neptune barycenter', 
                     'pluto barycenter']
        if (self.numplan > 0 and self.numplan < 14):
            return planetstr[self.numplan - 1]
        else:
            return planetstr[4] # Return mars for now
    
    def setnumplan(self, nplanet):
        self.numplan = nplanet
    
    def getplanetobj(self):
        return self.planet
    
class _Time(_Date):
    """ Returns an array of time using the utc format"""
    
    def __init__(self, yr):
        self.yr = yr
        self.tc = []
        self.monthsort()
        
    def monthsort(self):
        ndays = 0
        for self.mnth in range(1,13):
            if (self.mnth == 4 or self.mnth == 6 or self.mnth == 9 or self.mnth == 11):
                ndays = 30
                self.gettc(ndays)
            elif (self.mnth == 1 or self.mnth == 3 or self.mnth == 5 or self.mnth == 7
                or self.mnth == 8 or self.mnth == 10 or self.mnth ==12):
                ndays = 31
                self.gettc(ndays)
            elif (self.mnth == 2 and self.leap_year()):
                ndays = 29
                self.gettc(ndays)
            elif (self.mnth ==2 and self.leap_year() == False):
                ndays = 28
                self.gettc(ndays)
    
    def gettc(self, ndays):
        for dates in range(1,ndays+1):
            self.tc.append(ts.utc(self.yr, self.mnth, dates))
    
    def gettcobj(self):
        return self.tc
            

'''class FoodForTheBeast():
    """ This is where we calculate the data for the neural network """
    
    def __init__(self, nplanet1, nplanet2, yr1, y2):
        self.nettc =[]
        
        
    def getnettc(self):
'''

def FoodForTheBeast(nplanet1, nplanet2, yr1, yr2):
    yr1 = int(yr1)
    yr2 = int(yr2)
    yr2_1 = yr2 - yr1
    
    tc = []
    
    nplanet1 = int(nplanet1)
    nplanet2 = int(nplanet2)
    
    planet1 = _Planet(nplanet1).getplanetobj()
    planet2 = _Planet(nplanet2).getplanetobj()

    distanc = []
    datec = []
    
    i = 0
    
    for yrs in range(1, yr2_1 + 2):
        tc = _Time(yr1 + yrs).gettcobj()

        for tcount in range(1,len(tc) + 1):
            astroc = planet1.at(tc[tcount-1]).observe(planet2)
            ra1, dec1, dist1 = astroc.radec()
            i=i+1
            distanc.append(dist1.au)
            datec.append(i)
       
    print (len(distanc), len(datec))
    return distanc, datec

        
    
    
    

    
            
        
            
            
        
    

        
    
        
