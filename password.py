password = input('please enter password:')
count = 3
count = int(count)

while True: 
    if password == 'a9825bon':
       print('you are right')
       break
    elif password != 'a9825bon':
           count = count - 1    
           print('you have', count,'chance')
           password = input('plesase enter again: ')
           if count == 0:
              break

               


       
    


