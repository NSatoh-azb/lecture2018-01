'''
一筆書きシェルピンスキーガスケットのk角形版．

@author: NSatoh
'''

import turtlesvg as ttl
t = ttl.MyTurtle()
t.speed(10)

def var_sierpinski_k(length, k, n, r=0.5):
    if n > 0:
        for i in range(k):
            t.fd(length)
            t.left(360/k)
            var_sierpinski_k(length * r, 
                               k, n-1, r)

t.bgcolor('black')
t.pencolor('white')


# タートルが最後まで動くのに結構時間がかかるが，
# 動くところを見たければ次の行はコメントアウトせよ．
t.tracer(0)

# 7角形の例
var_sierpinski_k(100, 7, 4, r=0.5)
