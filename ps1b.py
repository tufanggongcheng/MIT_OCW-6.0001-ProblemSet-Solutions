#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 09:59:39 2020

@author: syn
"""


annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

months = 0
current_savings = 0
while current_savings < 0.25 * total_cost:
    months += 1
    current_savings += 0.04 * current_savings/12
    current_savings += annual_salary/12 * portion_saved
    if months%6 == 0:
        annual_salary += semi_annual_raise * annual_salary
print("Number of months: ", months)
