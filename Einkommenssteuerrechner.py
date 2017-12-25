# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 11:29:59 2017

@author: Uwe
"""

import pandas as pd

def calculateTax(income):
    """
        calculates German income tax amount based on formulas from 
        https://www.finanzrechner.org/sonstige-rechner/einkommensteuerrechner/
    """
    
    if (income <= 8820):
        return 0
    else:
        if (income >= 8821 and income <= 13769):
            return (1007.27 * ((income - 8820) / 10000) + 1400) * ((income - 8820) / 10000)
        else: 
            if (income >= 13770 and income <= 54057):
                return (223.67 * ((income - 13769) / 10000) + 2397) * ((income - 13769) / 10000) + 939.57
            else:
                if (income >= 54058 and income <= 256303):
                    return (0.42 * income - 8475.44)
                else:
                    if (income >= 256304):
                        return (0.45 * income - 16164.53)
                    else:
                        return -1


def calculateTaxSplit(income):
    """ 
        returns the tax amount if "Ehegattensplitting" is used
        Logic: divide income by 2, calculate tax and multiply resulting tax by 2
        due to progression this can be significantly less
    """
    return calculateTax(income/2)*2
    
                

def calculateSoli(tax):
    return 0.055 * tax

#print("{:10.3f}".format(calculateTax(8820)), calculateSoli(calculateTax(8820)))
#print("{:10.3f}".format(calculateTax(8821)), calculateSoli(calculateTax(8821)))
#print("{:10.3f}".format(calculateTax(8822)), calculateSoli(calculateTax(8822)))
#print("{:10.3f}".format(calculateTax(15000)), calculateSoli(calculateTax(15000)))
#print("{:10.3f}".format(calculateTax(75000)), calculateSoli(calculateTax(75000)))
#print("{:10.3f}".format(calculateTax(300000)), calculateSoli(calculateTax(300000)))

#for i in range(0,101000,1000):
#    print(i,':', '{:10.2f}'.format(calculateTax(i)),':','{:10.2f}'.format(calculateTaxSplit(i)))    


df = pd.DataFrame({'Einkommen': range(0,101000,1000)})
df['Steuer'] = df['Einkommen'].apply(calculateTax)
df['SteuerSoli'] = df['Steuer'].apply(calculateSoli)
df['Steuersplit'] = df['Einkommen'].apply(calculateTaxSplit)
df['SteuersplitSoli'] = df['Steuersplit'].apply(calculateSoli)

df.to_clipboard()