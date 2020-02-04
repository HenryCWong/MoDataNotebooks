# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:35:55 2019

@author: cywon
"""
#given a pool of numbers create an 11 digit ID

def numOfIds(pool):
    if len(pool) < 11:
        return(0)
    possible = int(len(pool)/11) #round down number of possible based on characters
    numOfEights = findNumOfEights(pool)
    print(numOfEights)

    return(min([possible,numOfEights]))

    # Write your code here

def findNumOfEights(pool):
    eights = 0
    for i in pool:
        if i == "8":
            eights += 1
    return(eights)
    
print(numOfIds("888888555555555555555"))