films={"Findings Dory":[3,5],
       "Bourne":[18,5],
       "Tarzan":[15,5],
       "Ghost Busters":[12,5]
       }
while True:
    choice = raw_input("What films would you like to watch?:").strip().title()
    
    if choice in films:
        age=int(raw_input("How old are you?:").strip())
        if age >films[choice][0]:
            num_seats=films[choice][1]
            if num_seats>0:
                print 'Enjoy your film!'
                films[choice][1]=films[choice][1]-1
            else:
                print 'Sorry! We are sold out'
        else:
            print 'You are too young to watch movie'
    else:
        print ' We dont have that film'
        
                
        
        
        
           
            
