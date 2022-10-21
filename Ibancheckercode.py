#!/usr/bin/env python
# coding: utf-8

# In[1]:


Ibans = ["DE02120300000000202051", "DE02600501010002034340","DE02370501980001802065","DE02700100800030876808"]


for Iban in Ibans:
    Iban_rearranged = Iban[4:] + Iban[0:4]
 
    if "DE" in Iban_rearranged:
        full_numbered_Iban = Iban_rearranged.replace("DE", "1314")    
        if (int(full_numbered_Iban) % 97) == 1:
            print("Iban is valid".format(Iban))
        else:
            print("Iban is not valid".format(Iban))
    

