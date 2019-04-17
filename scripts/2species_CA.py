#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 11:25:05 2018

@author: jl
"""

#####--------------------SIMPLE AUTOMATA

import random 
import numpy as np 
import matplotlib.pyplot as plt
import copy
import os
import datetime
import timeit

start = timeit.default_timer()
datafile_path =os.getcwd()
now = datetime.datetime.now()

class animal(object):    
    ##
    def __init__(self,ide,posx,posy,stat='Alive'):
        self.ide=ide
        self.posx=posx
        self.posy=posy
        self.stat=stat
    
    def position(self):
        return [self.posx,self.posy]
    
    def play(self,world,R):
    ###---------------main method that calls the actions that each specie can do    
        ##------defining limitis 
        counter=0
        lim_min=0
        lim_max=len(world)
        ##-------choose  a neighbour cell---------------------
        newx=self.posx+random.randint(-self.max_move,self.max_move)
        newy=self.posy+random.randint(-self.max_move,self.max_move)

        ###----------------if it's within the limits of the world------------
        if newx>lim_min and newx<lim_max and newy>lim_min and newy<lim_max:
    
        ##----------act in consequence according to the kind of specie and neighbour-- 
        
            if self.typ=='prey':
                if world[newx,newy]==0  and random.random()>0.7:
                    self.reproduce(newx,newy,world,R)
                    #self.move(newx,newy,world)
            
            elif self.typ=='predator_1':
                if world[newx,newy]==0:
                    self.move(newx,newy,world)
                elif world[newx,newy]==1 and random.random()<0.32:
                    self.eat(newx,newy,world,R)
                elif world[newx,newy]==2 and random.random()>0.9:
                    self.die(world,R)
                            
            elif self.typ=='predator_2':
                if world[newx,newy]==0:
                    self.move(newx,newy,world)
                elif world[newx,newy]==2 and random.random()<0.15:
                    self.eat(newx,newy,world,R)
                elif world[newx,newy]==3 and random.random()>0.9:
                    self.die(world,R)
                    
            #print(self.typ,world[newx,newy])
            
    def move(self,newx,newy,world):
        world[self.posx,self.posy]=0

        self.posx=newx
        self.posy=newy

        if self.typ=='prey':
            num=1
        elif self.typ=='predator_1':
            num=2
        elif self.typ=='predator_2':
            num=3

        world[newx,newy]=num
        return(self.position())   
    
    def reproduce(self,newx,newy,W,R):
        
        if self.typ=='prey':
            n=Prey(self.ide+'s',newx,newy)
            W[newx,newy]=1
            R.append(n)
        elif self.typ=='predator_1':
            n=Predator_1(self.ide+'s',self.posx,self.posy)
            W[self.posx,self.posy]=2
            R.append(n)
        elif self.typ=='predator_2':
            n=Predator_2(self.ide+'s',self.posx,self.posy)
            W[self.posx,self.posy]=3
            R.append(n)
    
    def eat(self,newx,newy,W,R):
            tipo=self.typ
            det=self.find(newx,newy,R)
            R[det].typ=self.typ
            if self.typ=='predator_1':
                num=2
            elif self.typ=='predator_2':
                num=3
            
            W[newx,newy]=num
            
    def die(self,W,R):
        W[self.posx,self.posy]=0
        dele=self.find(self.posx,self.posy,R)
        R.remove(R[dele])
            
    def find(self,fx,fy,lista):
        for index, item in enumerate(lista):
            if item.posx == fx and item.posy==fy:
                break
        else:
            index = -1
        
        return index
#        for item in lista:
#            if fx==item.posx and fy==item.posy:
#                return item

     

class Prey(animal):
    def __init__(self,ide,posx,posy,typ='prey'):
        self.typ=typ   
        self.ide=ide
        self.posx=posx
        self.posy=posy
        self.max_move=1
        self.stat='Alive'


class Predator_1(animal):   
    def __init__(self,ide,posx,posy,typ='predator_1'):
        self.typ=typ
        self.ide=ide
        self.posx=posx
        self.posy=posy
        self.max_move=1
        self.stat='Alive'


class Predator_2(animal):
    def __init__(self,ide,posx,posy,typ='predator_2'):
        self.typ=typ
        self.ide=ide
        self.posx=posx
        self.posy=posy
        self.max_move=1
        self.stat='Alive'

    
def stats(Arr):
    pop1=0
    pop2=0
    pop3=0
    for i in range(0,len(Arr)):
        
        if Arr[i].typ=='prey':
            pop1=pop1+1
            
        if Arr[i].typ=='predator_1':
            pop2=pop2+1
            
        if Arr[i].typ=='predator_2':
            pop3=pop3+1
        
    return(pop1,pop2,pop3)


#def ecosystem(tmax,sz,spec1_i,spec2_i,spec3_i,vis='true',plo='false')

###-----------initial conditions for the "wolrd "--------------------
tmax=500
szx=szy=10
sz=150
##-------------------INITIAL POPULATIONS-------------------------
###-----specie 3 eats specie 2, specie 2 eats specie 1
spec1_i=100 #grass
spec2_i=100 #rabbit
spec3_i=100 #foxes
vis='false'
plo='false'
times=1
TT=0
while TT<times:
    save_dir=datafile_path+'/'+str(sz)+'x'+str(sz)+'_s1:'+str(spec1_i)+'_s2:'+str(spec2_i)+'_s3:'+str(spec3_i)+'_'+str(TT)
    print(save_dir)
    ###-------------------initializing the "World"---------------------
    W=np.zeros((sz,sz),np.uint8) 
    W_n=np.zeros((sz,sz),np.uint8)
    A=[] # The list that contains all the individuals. 
    nA=[] # a copy of the list
    
    
    c_1=c_2=c_3=0
    #while c_1<spec1_i and c_2<spec2_i and c_3<spec3_i:
    while c_1+c_2+c_3<spec1_i+spec2_i+spec3_i and len(A)<sz*sz:
        ra=np.random.randint(1,5)  
        x=np.random.randint(1,len(W)-1)
        y=np.random.randint(1,len(W)-1)
        if W[x,y]==0:
            
            if ra==1 and c_1<spec1_i:
                s1=Prey('prey_'+str(c_1),x,y)
                W[x,y]='1'
                A.append(s1)    
                c_1=c_1+1
            
            elif ra==2 and c_2<spec2_i:
                s2=Predator_1('predator1_'+str(c_1),x,y)
                W[x,y]='2'
                A.append(s2)    
                c_2=c_2+1
        
            elif ra==3 and c_3<spec3_i:       
                s3=Predator_2('predator2_'+str(c_1),x,y)
                W[x,y]='3'
                A.append(s3)    
                c_3=c_3+1
        
        T=[]
        S1=[]
        S2=[]
        S3=[]
        t=0
    while t<tmax:
            nA=copy.deepcopy(A)   
            W_n=copy.deepcopy(W)
            ####------------The actions (Using Monte Carlo updates)----------------
            ###------choose a random animal and move it------------------------
            #A[np.random.randint(0,len(A)-1)].play(W,A)
            
            
            ####-----------The actions (updating the whole latice every step)------
            for x in A:
                x.play(W,A)
            #    if x.stat=='predator_2':
            #        print(x.stat)
                #if x.stat=='dd':
                    #A.pop(A[x])
                    #print('done')
            
            ###-------------delete the onew who didn't maket to the next one
            
            
            ###------------Obtaining Statistics from the System----------------- 
            L=stats(A)
            T.append(t)    
            S1.append(L[0]/(1)*1.)
            S2.append(L[1]/(1)*1.)
            S3.append(L[2]/(1)*1.)
            if vis=='true':
                print(TT,t)
                #print(TT)
            t=t+1
            #W=copy.deepcopy(W_n)    
            
            ####--------------visualize the system IRT-------------------    
            if plo=='true':
                plt.figure(1)
                plt.clf()
                plt.axis([0, sz, 0, sz])
                plt.ion()
                
                for i in range(0,len(A)-1):   
                    if A[i].typ=='prey':
                        plt.plot(A[i].posx,A[i].posy,'go')
                    elif A[i].typ=='predator_1':
                        plt.plot(A[i].posx,A[i].posy,'b*')
                    elif A[i].typ=='predator_2':
                        plt.plot(A[i].posx,A[i].posy,'r*')
                
                plt.pause(0.00000001)
            
            #####--------------------takae some some screenshots--------------------------
            #    if t==tmax/2:
            #        SS1=[]
            #        SS1=copy.deepcopy(A)   
            #    if t==tmax*3/4:
            #        SS2=[]
            #        SS2=copy.deepcopy(A)
            #    if t==tmax*1/4:
            #        SS3=[]
            #        SS3=copy.deepcopy(A)
            #    
            #    #A=copy.deepcopy(nA)   
            #        
            ####------------------ visualize the evolution of populations vs time---------
    total=sz*sz
    dat=np.column_stack((T,S1,S2,S3))  
    np.savetxt(save_dir, dat , fmt='%.18g', delimiter=' ', newline=os.linesep)
    print(TT)
    TT=TT+1

 
plt.figure(2)
plt.plot(T,S1,'g-+',label='Prey')
plt.plot(T,S2,'b',label='Predator 1')
plt.plot(T,S3,'r',label='Predator 2')
plt.legend(bbox_to_anchor=(.75, .95), loc=2, borderaxespad=0.)
plt.xlabel(['Simulation Steps'])
plt.ylabel(['Population'])

plt.show()

#plt.figure(3)
#plt.plot(np.log(T),S1,'g',np.log(T),S2,'b',np.log(T),S3,'r')
#plt.xlabel(['Simulation Steps'])
#plt.ylabel(['Population'])
#plt.show()

#plt.figure(4)
#
#plt.figure(4)
#for r1 in SS1:   
#    if r1.typ=='prey':
#        plt.plot(r1.posx,r1.posy,'go')
#    elif r1.typ=='predator_1':
#        plt.plot(r1.posx,r1.posy,'b*')
#    elif r1.typ=='predator_2':
#        plt.plot(r1.posx,r1.posy,'r*')
#plt.show()
#
#plt.figure(5)
#for r1 in SS2:   
#    if r1.typ=='prey':
#        plt.plot(r1.posx,r1.posy,'go')
#    elif r1.typ=='predator_1':
#        plt.plot(r1.posx,r1.posy,'b*')
#    elif r1.typ=='predator_2':
#        plt.plot(r1.posx,r1.posy,'r*')
#plt.show()
#
#plt.figure(6)
#for r1 in SS3:   
#    if r1.typ=='prey':
#        plt.plot(r1.posx,r1.posy,'go')
#    elif r1.typ=='predator_1':
#        plt.plot(r1.posx,r1.posy,'b*')
#    elif r1.typ=='predator_2':
#        plt.plot(r1.posx,r1.posy,'r*')
#plt.show()

stop = timeit.default_timer()
print stop - start 