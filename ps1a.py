#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 22:02:07 2020

@author: syn
"""


annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
months = 0
current_savings = 0
while current_savings < 0.25 * total_cost:
    months += 1
    current_savings += 0.04 * current_savings/12
    current_savings += annual_salary/12 * portion_saved
print("Number of months: ", months)

    