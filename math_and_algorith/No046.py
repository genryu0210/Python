# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 16:33:53 2022

@author: 406429
"""
R,C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

c = []
while True :    
    try :
        c = list(map(str,input().split()))
        replace_list = [cc.replace("#","-1 ") for cc in c]
        replace_list = [cc.replace(".", "0 ") for cc in replace_list]
    except :
        break
maze = []
for i in range(R) :
    maze.append(replace_list[i].split())

#ここまででdが迷路の経路になってくれた
#ここから迷路の探索

#左に探索
if int(maze[sy + 0][sx + -1]) == 0 :
    int(maze[sy + 0][sx + -1]) += 1
#上に探索
if int(maze[sy + 1][sx + 0]) == 0 :
    maze[sy + 1][sx + 0] = 1
#右に探索
if int(maze[sy + 0][sx + 1]) == 0 :
    maze[sy + 0][sx + 1] = 1
#下に探索
if int(maze[sy + -1][sx + 0]) == 0 :
    maze[sy + -1][sx + 0] = 1
    