films={
        "Baaghi":[18,10],
        "Dil Bechraa":[18,5],
        "Abcd2":[15,8],
        "War":[18,4]
      }

while True:
    choice=input("Which movie would you like to watch? : ").strip().title()
    if choice in films:
        
    #checking the age
       age=int(input("How old are you? ").strip())
       
       if age >=films[choice][0]:
           
        #checking the availability of seats
          number_seats=films[choice][1]
          
          if number_seats>0:
             print("Enjoy the movie")
             films[choice][1]=films[choice][1] -1 
          else:
            print("Sorry! The seats are full for these movie")
       else:
         print("Sorry! you are too young to watch these movie")
    else:
      print("Sorry! these movie is not available ") 
