password = 'a9825bon'
count = 3
count = int(count)
while True: 
    pwd = input('please enter password:')
    if pwd == password:
       print('you are right')
       break
    else:
           count = count - 1    
           print('you have', count,'chance')
           if count == 0:
              break
         
         

               


       
    


