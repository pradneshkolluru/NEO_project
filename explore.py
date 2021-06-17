#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:34:54 2021

@author: pradneshkolluru
"""

import pandas as pd


df = pd.read_csv('/Users/pradneshkolluru/nd303-c1-advanced-python-techniques-project-starter/data/neos.csv')


print(df['name'])