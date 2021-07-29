password = 'a9825bon'
count = 3
count = int(count)
while count > 0: 
    count = count - 1  
    pwd = input('please enter password:')
    if pwd == password:
       print('you are right')
       break
    else:  
           print('wrong password')
           if count > 0:
              print('you have', count,'chance')
         

               


       
    


