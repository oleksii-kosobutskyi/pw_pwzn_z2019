def task_1():
    output=""
    for i in range(1,10):
        for j in range(0,i):
            output+=str(i)
        output+="\n"
    print(output)
    return

assert task_1() == '''
1
22
333
4444
55555
666666
7777777
88888888
999999999
'''
