# -*- coding: utf-8 -*-
import sys
#import math
import random
#from mcpi.minecraft import Minecraft


#mc = Minecraft.create()
#mc.postToChat(__file__)
bom_articles = 100
Field_size = 32

if Field_size ** 2 < bom_articles:

    #mc.postToChat("bom_articles ERROR")
    print("bom_articles ERROR")
    input(">>>  ")

    sys.exit()

bom_field = [[0 for j in range(Field_size)] for i in range(Field_size)]
bom_count_field = [[0 for j in range(Field_size)] for i in range(Field_size)]
#print(len(bom_field))
for k in range(bom_articles):
    
    random_bom_position_i = random.randint(0,Field_size - 1) 
    random_bom_position_j = random.randint(0,Field_size - 1)

    if bom_field[random_bom_position_i][random_bom_position_j] == 0 & True:     #地雷配置時に最初にクリックしたマスを避ける処理を追加する
        
        bom_field[random_bom_position_i][random_bom_position_j] = 1

        for i in range(-1,2):
            for j in range(-1,2):

                try:bom_count_field[random_bom_position_i + i][random_bom_position_j + j] += 1
                except:None

    else:
        k -= 1

    #
for i in range(Field_size):
    for j in range(Field_size):

        print(bom_field[i][j], end = " "),

    print()

print()

for i in range(Field_size):
    for j in range(Field_size):

        print(bom_count_field[i][j], end = " "),

    print()

def field_open(x,y):
    print()

