'''
問34 一筆書きシェルピンスキーガスケット

@author: NSatoh
'''


import turtlesvg as ttl
t = ttl.MyTurtle()

t.speed(10)

def var_sierpinski(length, n):
    if n > 0:
        for i in range(3):
            t.fd(length)
            t.left(120)
            var_sierpinski(length * 0.5, n-1)

# まずは次の行はコメントアウトしたままにせよ．
# t.tracer(0)

# 適当な引数を与えてvar_sierpinskiを実行せよ．
