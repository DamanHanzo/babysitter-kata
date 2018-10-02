# Babysitter

This repository contains a program, named Babysitter, that is a solution to Babysitter Kata.

## Assumptions

We are assuming that the starting bed-time is 9 pm or 21 hours.

## Usage 

BabySitter class constructor accpets 2 mandatory arguments and one optional arguemnt:
 - ```startTime```: Time when sitter starts his/her shift
 - ```endTime```: Time when sitter's shift ends
 - ```bedTime(optional)```: Bed time. If this argument is not supplied then 21 hours will be used as a default bed time. 
 
 Create babysitter object: ```sitter = BabySitter(startTime, endTime, bedTime)```
 
 Calculate total wages earned: ```sitter.total_wages_earned()```
