game = 1
win=0
draw=0
lose=0
gamecount=0
while game==1:
     gamecount+=1
     Data = [" "," "," "," "," "," "," "," "," "," "]
     print("Let's Play a game of tic tac toe")
     print('''The Rules are simple - You must enter the square you want to mark, it should be vacant''')
     print("You are O ")
     print("")
     round = 1
     turn=0
     while round==1:
          if gamecount%2!=0:
               valid = 0     
               while valid==0:
                    UserPlay = int(input("Enter the square you want to mark "))
                    if UserPlay<10 and UserPlay>0:
                         if Data[UserPlay]==" ":
                              valid = 1
                         else:
                              print("WRONG INPUT")
                    else:
                         valid = 0
                         print("Wrong Input")
               Data[UserPlay] = "O"
               turn+=1
               print("")
          for i in range(1,10):
               round = 1
               if i in (1,4,7):
                    if Data[i]=="X" and Data[i+1]=="X"and Data[i+2]=="X":
                         print("YOU HAVE LOST THE GAME!!")
                         lose+=1
                         round = 2 
                    elif Data[i]=="O" and Data[i+1]=="O"and Data[i+2]=="O":
                         print("YOU HAVE WON THE GAME!!")
                         win+=1
                         round = 2      
               if i in (1,2,3):
                    if Data[i]=="X" and Data[i+3]=="X"and Data[i+6]=="X":
                         print("YOU HAVE LOST THE GAME!!")
                         lose+=1
                         round = 2
     
                    elif Data[i]=="O" and Data[i+3]=="O"and Data[i+6]=="O":
                         print("YOU HAVE WON THE GAME!!")
                         win+=1
                         round = 2
               if i==1:
                    if Data[i]=="X" and Data[i+4]=="X"and Data[i+8]=="X":
                         print("YOU HAVE LOST THE GAME!!")
                         lose+=1
                         round = 2 
                    elif Data[i]=="O" and Data[i+4]=="O"and Data[i+8]=="O":
                         print("YOU HAVE WON THE GAME!!")
                         win+=1
                         round = 2
               if i==3:
                    if Data[i]=="X" and Data[i+2]=="X"and Data[i+4]=="X":
                         print("YOU HAVE LOST THE GAME!!")
                         lose+=1
                         round = 2  
                    elif Data[i]=="O" and Data[i+2]=="O"and Data[i+4]=="O":
                         print("YOU HAVE WON THE GAME!!")
                         win+=1
                         round = 2
          if turn==9 and round==1:
                    print("ITS A DRAW!!")
                    draw+=1
                    round = 2
          print("")         
          Botplay = 0
          for i in range(0,10):
               if i in (1,4,7):
                    if Data[i]=="X" and Data[i+1]=="X"and Data[i+2]==" ":
                         Botplay = i+2 
                    elif Data[i]=="X" and Data[i+1]==" "and Data[i+2]=="X":
                         Botplay = i+1 
                    elif Data[i]==" " and Data[i+1]=="X"and Data[i+2]=="X":
                         Botplay = i
                    elif Data[i]=="O" and Data[i+1]=="O"and Data[i+2]==" ":
                         Botplay = i+2 
                    elif Data[i]=="O" and Data[i+1]==" "and Data[i+2]=="O":
                         Botplay = i+1 
                    elif Data[i]==" " and Data[i+1]=="O"and Data[i+2]=="O":
                         Botplay = i      
               if i in (1,2,3):
                    if Data[i]=="X" and Data[i+3]=="X"and Data[i+6]==" ":
                         Botplay = i+6
                    elif Data[i]=="X" and Data[i+3]==" "and Data[i+6]=="X":
                         Botplay = i+3 
                    elif Data[i]==" " and Data[i+3]=="X"and Data[i+6]=="X":
                         Botplay = i 
                    elif Data[i]=="O" and Data[i+3]=="O"and Data[i+6]==" ":
                         Botplay = i+6 
                    elif Data[i]=="O" and Data[i+3]==" "and Data[i+6]=="O":
                         Botplay = i+3 
                    elif Data[i]==" " and Data[i+3]=="O"and Data[i+6]=="O":
                         Botplay = i
               if i==1:
                    if Data[i]=="X" and Data[i+4]=="X"and Data[i+8]==" ":
                         Botplay = i+8 
                    elif Data[i]=="X" and Data[i+4]==" "and Data[i+8]=="X":
                         Botplay = i+4 
                    elif Data[i]==" " and Data[i+4]=="X"and Data[i+8]=="X":
                         Botplay = i  
                    elif Data[i]=="O" and Data[i+4]=="O"and Data[i+8]==" ":
                         Botplay = i+8 
                    elif Data[i]=="O" and Data[i+4]==" "and Data[i+8]=="O":
                         Botplay = i+4 
                    elif Data[i]==" " and Data[i+4]=="O"and Data[i+8]=="O":
                         Botplay = i
               if i==3:
                    if Data[i]=="X" and Data[i+2]=="X"and Data[i+4]==" ":
                         Botplay = i+4 
                    elif Data[i]=="X" and Data[i+2]==" "and Data[i+4]=="X":
                         Botplay = i+2 
                    elif Data[i]==" " and Data[i+2]=="X"and Data[i+4]=="X":
                         Botplay = i
                    elif Data[i]=="O" and Data[i+2]=="O"and Data[i+4]==" ":
                         Botplay = i+4 
                    elif Data[i]=="O" and Data[i+2]==" "and Data[i+4]=="O":
                         Botplay = i+2 
                    elif Data[i]==" " and Data[i+2]=="O"and Data[i+4]=="O":
                         Botplay = i
          if Botplay==0:
               final_score = 4
               point = [0,0,0,0,0,0,0,0,0,0]
               for i in range(1,10):
                    XData = list(Data)
                    if XData[i]==" ":
                         XData[i]="X"
                         move_score = 0
                         for j in range(1,10):
                              OData = list(XData)
                              if OData[j]==" ":
                                   OData[j]="O"
                                   O_threat = 0
                                   X_threat = 0
                                   NewData = list(OData)
                                   for k in range(1,10):
                                        if k in (1,4,7):
                                             if NewData[k]=="O" and NewData[k+1]=="O"and NewData[k+2]==" ":
                                                  O_threat+=1 
                                             elif NewData[k]=="O" and NewData[k+1]==" "and NewData[k+2]=="O":
                                                  O_threat+=1 
                                             elif NewData[k]==" " and NewData[k+1]=="O"and NewData[k+2]=="O":
                                                  O_threat+=1
                                             elif NewData[k]=="X" and NewData[k+1]=="X"and NewData[k+2]==" ":
                                                  X_threat+=1 
                                             elif NewData[k]=="X" and NewData[k+1]==" "and NewData[k+2]=="X":
                                                  X_threat+=1 
                                             elif NewData[k]==" " and NewData[k+1]=="X"and NewData[k+2]=="X":
                                                  X_threat+=1      
                                        if k in (1,2,3):
                                             if NewData[k]=="O" and NewData[k+3]=="O"and NewData[k+6]==" ":
                                                  O_threat+=1
                                             elif NewData[k]=="O" and NewData[k+3]==" "and NewData[k+6]=="O":
                                                  O_threat+=1 
                                             elif NewData[k]==" " and NewData[k+3]=="O"and NewData[k+6]=="O":
                                                  O_threat+=1 
                                             elif NewData[k]=="X" and NewData[k+3]=="X"and NewData[k+6]==" ":
                                                  X_threat+=1 
                                             elif NewData[k]=="X" and NewData[k+3]==" "and NewData[k+6]=="X":
                                                  X_threat+=1 
                                             elif NewData[k]==" " and NewData[k+3]=="X"and NewData[k+6]=="X":
                                                  X_threat+=1
                                        if k==1:
                                             if NewData[k]=="O" and NewData[k+4]=="O"and NewData[k+8]==" ":
                                                  O_threat+=1 
                                             elif NewData[k]=="O" and NewData[k+4]==" "and NewData[k+8]=="O":
                                                  O_threat+=1 
                                             elif NewData[k]==" " and NewData[k+4]=="O"and NewData[k+8]=="O":
                                                  O_threat+=1  
                                             elif NewData[k]=="X" and NewData[k+4]=="X"and NewData[k+8]==" ":
                                                  X_threat+=1 
                                             elif NewData[k]=="X" and NewData[k+4]==" "and NewData[k+8]=="X":
                                                  X_threat+=1 
                                             elif NewData[k]==" " and NewData[k+4]=="X"and NewData[k+8]=="X":
                                                  X_threat+=1
                                        if k==3:
                                             if NewData[k]=="O" and NewData[k+2]=="O"and NewData[k+4]==" ":
                                                  O_threat+=1 
                                             elif NewData[k]=="O" and NewData[k+2]==" "and NewData[k+4]=="O":
                                                  O_threat+=1 
                                             elif NewData[k]==" " and NewData[k+2]=="O"and NewData[k+4]=="O":
                                                  O_threat+=1
                                             elif NewData[k]=="X" and NewData[k+2]=="X"and NewData[k+4]==" ":
                                                  X_threat+=1 
                                             elif NewData[k]=="X" and NewData[k+2]==" "and NewData[k+4]=="X":
                                                  X_threat+=1 
                                             elif NewData[k]==" " and NewData[k+2]=="X"and NewData[k+4]=="X":
                                                  X_threat+=1
                                        
                                   if X_threat>0:
                                        varient = 1
                                   elif O_threat==0:
                                        varient = 2
                                   elif O_threat==1:
                                        varient= 2
                                   elif O_threat==2:
                                        varient= 4
                                   if varient>move_score:
                                        move_score = varient
                         if move_score==0:
                             move_score=1
                         if move_score<=final_score:
                              final_score=move_score
                              point[i]=final_score
               for i in range(1,10):
                    if i==5:
                         if point[i]==final_score:
                              Botplay=i
                    elif point[i]!=0 and Botplay!=5:
                         Botplay=i
          if round==1:
               Data[Botplay]="X"
               turn+=1
          
          print("                SCORE")
          print("        Win-",win,"draw-", draw,"Lose-",lose,sep=" ")

          print('''
               |     |
            ''',Data[1],'''  |  ''',Data[2],'''  |  ''',Data[3],'''
          _____|_____|_____
               |     |
            ''',Data[4],'''  |  ''',Data[5],'''  |  ''',Data[6],'''
          _____|_____|_____
               |     |     
            ''',Data[7],'''  |  ''',Data[8],'''  |  ''',Data[9],'''
               |     |

          ''',sep="")

          if round==1:
               round = 1
               for i in range(1,10):
                    if i in (1,4,7):
                         if Data[i]=="X" and Data[i+1]=="X"and Data[i+2]=="X":
                              print("YOU HAVE LOST THE GAME!!")
                              lose+=1
                              round = 2 
                         elif Data[i]=="O" and Data[i+1]=="O"and Data[i+2]=="O":
                              print("YOU HAVE WON THE GAME!!")
                              win+=1
                              round = 2      
                    if i in (1,2,3):
                         if Data[i]=="X" and Data[i+3]=="X"and Data[i+6]=="X":
                              print("YOU HAVE LOST THE GAME!!")
                              lose+=1
                              round = 2
          
                         elif Data[i]=="O" and Data[i+3]=="O"and Data[i+6]=="O":
                              print("YOU HAVE WON THE GAME!!")
                              win+=1
                              round = 2
                    if i==1:
                         if Data[i]=="X" and Data[i+4]=="X"and Data[i+8]=="X":
                              print("YOU HAVE LOST THE GAME!!")
                              lose+=1
                              round = 2 
                         elif Data[i]=="O" and Data[i+4]=="O"and Data[i+8]=="O":
                              print("YOU HAVE WON THE GAME!!")
                              win+=1
                              round = 2
                    if i==3:
                         if Data[i]=="X" and Data[i+2]=="X"and Data[i+4]=="X":
                              print("YOU HAVE LOST THE GAME!!")
                              lose+=1
                              round = 2  
                         elif Data[i]=="O" and Data[i+2]=="O"and Data[i+4]=="O":
                              print("YOU HAVE WON THE GAME!!")
                              win+=1
                              round = 2
               if turn==9 and round==1:
                         print("ITS A DRAW!!")
                         draw+=1
                         round = 2
               print("")
          
          if gamecount%2==0 and round==1:
               valid = 0     
               while valid==0:
                    UserPlay = int(input("Enter the square you want to mark "))
                    if UserPlay<10 and UserPlay>0:
                         if Data[UserPlay]==" ":
                              valid = 1
                         else:
                              print("WRONG INPUT")
                    else:
                         valid = 0
                         print("Wrong Input")
               Data[UserPlay] = "O"
               turn+= 1
               print("") 
                      
     game = int(input("WOULD YOU LIKE TO PLAY ANOTHER GAME!!, PRESS 1 TO PLAY ANOTHER GAME or press 2 to exit"))
     print("")
