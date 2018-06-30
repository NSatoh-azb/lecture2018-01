# -*- coding: utf-8 -*-
"""
テトリスのブロックデータたち

ブロック内の数字はblock_colorsの色に対応する。
（0 = 黒（背景色）, 1 = 青， 2 = 黄色，...） 

ブロックの回転した形状は自動で計算させる関数などを作る方が良いが，
今回は簡易的な実装のため回転後の形状を全部手動で登録する．
"""

# ブロックの色のデータ： （R, G, B) それぞれ 0～255
block_colors = [(0,   0,   0), #　黒 = 背景ブロックの色
                (0,   0,   255), (0,   255, 0),   (0,   255, 255), 
                (255, 0,   0),   (255, 0,   255), (255, 255, 0),
                (0,   0,   165), (0,   165, 0),   (0,   165, 165),
                (0,   165, 255), (165, 0,   0),   (165, 0,   165), 
                (165, 0,   255), (165, 165, 0),   (165, 165, 255),
                (165, 255, 0),   (165, 255, 255), (255, 0,   165),
                (255, 165, 165), (255, 165, 255), (255, 255, 165),
                (128, 128, 128) # グレー = 壁の色
               ]


block_data = []

block_data.append([
    [[1, 1, 1],
     [1, 0, 0],
     [0, 0, 0]],
     
    [[0, 1, 1],
     [0, 0, 1],
     [0, 0, 1]],
     
    [[0, 0, 0],
     [0, 0, 1],
     [1, 1, 1]],
     
    [[1, 0, 0],
     [1, 0, 0],
     [1, 1, 0]]  
])

block_data.append([
    [[2, 2, 2, 2],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0]],
     
    [[0, 0, 0, 2],
     [0, 0, 0, 2],
     [0, 0, 0, 2],
     [0, 0, 0, 2]],

    [[0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [2, 2, 2, 2]],

    [[2, 0, 0, 0],
     [2, 0, 0, 0],
     [2, 0, 0, 0],
     [2, 0, 0, 0]]
])

