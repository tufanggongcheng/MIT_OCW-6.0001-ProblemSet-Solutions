#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 10:09:58 2020

@author: syn
"""


annual_salary = float(input("Enter your annual salary: "))
total_cost = .25 * 1000000
semi_annual_raise = .07
low = 0
high = 10000
guess = 0
steps = 0
current_savings = 0

while abs(current_savings - total_cost) > 100 and guess < 9999:
    if current_savings > total_cost :
        high = guess
    else: low = guess

    guess = (low + high)/2
    steps += 1
    current_savings = 0
    for months in range(36):
        current_savings = current_savings * (1 + 0.04/12) + guess/10000 * annual_salary/12 * 1.07**(abs(months/6))
    
if guess < 9999:
    guess = int(guess)

    print("Best savings rate", guess/10000)
    print("Steps in bisection search: ", steps)
else:
    print("It is not possible to pay the down payment in three years.")
