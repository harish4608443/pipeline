def delays(count):
    i=count
    low=12
    medium=18
    high=24
    #super_high=40
    delay=0
    print("Number of pedestrians= "+ str(i))
    if i < low:
        if i<1:
            print('green light delay = 0 sec')
        elif i<6:
            delay=i*1.5
            print('green light delay = '+str(delay)+' sec')
        elif i<9:
            delay=5*1.5
            print('green light delay = '+str(delay)+' sec')
        else:
            delay=7*1.5
            print('green light delay = '+str(delay)+' sec')
    elif i < medium:
        if i<15:
            delay=i*1.5
            print('green light delay = '+str(delay)+' sec')
        else:
            delay=i*1.5
            print('green light delay = '+str(delay)+' sec')
    elif i < high:
        if i<21:
            delay=i*1.5
            print('green light delay = '+str(delay)+' sec')
        else:
            delay=60
            print('green light delay = '+str(delay)+' sec')
    return(delay)
# 123123123123222222111
