def task_2():
    output=""
    for i in range(1,6,1):
        for j in range(0,i):
            output+="*"
        output+="\n"
    for i in range(4,0,-1):
        for j in range(0,i):
            output+="*"
        output+="\n"
    print(output)
    return

assert task_2() == '''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
