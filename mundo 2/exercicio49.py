tabuada = int(input('qual numero voce quer ver a tabuada?'))
for count in range(10):
    print('{} x {} = {}'.format(tabuada, count+1,tabuada*(count+1)))