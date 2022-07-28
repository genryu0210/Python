# -*- coding: utf-8 -*-
"""
Created on Tue Jul  5 09:35:36 2022

@author: 406429

"""
file3 = open('Output3.txt', 'w')


spell = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","J","K","L","M","N","P","R","S","T","W","X","Y","Z"]

flag = True
for i in range(len(spell)) :
    for j in range(len(spell)) :
        serch_str = "SPI06" + spell[i] + spell[j]
        print(serch_str)
        file3.write(serch_str + "\n")
        if serch_str == "SPI06JX" :
            flag = False
            break
    if flag == False :
        break
file3.close()

