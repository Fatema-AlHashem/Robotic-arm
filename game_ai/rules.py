#MinMax -tic-tac-toe Algo :
#initialization :

player , opp = 'x' , 'o'
# board[3][3] mby not needed ? we will see 

def isThereAMove(board):
    for i in range(3):
      for j in range(3):
        if (board[i][j] == '_'):
          return True
    return False


def isthereAWinner(board):
  # results : tie[0],x wins[1], o wins[-1]

    #initailize to none
    result=None

    #This is a function that will look at the board and see if there is a winner. I hardcoded this function, while others went with loops and stuff like that
    # will start with cheaking the rows if there is any winnners
    if ((board[0][0] == 'x' and board[0][1] =='x' and board[0][2]== 'x') or 
        (board[1][0] == 'x' and board[1][1] =='x' and board[1][2]== 'x') or 
        (board[2][0] == 'x' and board[2][1] =='x' and board[2][2]== 'x')):
            return 1
    

    
    elif ((board[0][0] == 'o' and board[0][1] =='o' and board[0][2]== 'o') or
            (board[1][0] == 'o' and board[1][1] =='o' and board[1][2]== 'o') or
            (board[2][0] == 'o' and board[2][1] =='o' and board[2][2]== 'o')):
        return -1
    



    # this will see if there is any winner player in the columns
    if ((board[0][0]=='x' and board[1][0]=='x' and board[2][0]=='x') or
        (board[0][1]=='x' and board[1][1]=='x' and board[2][1]=='x')  or 
        (board[0][2]=='x' and board[1][2]=='x' and board[2][2]=='x')):
        return 1
    

    elif ((board[0][0]=='o' and board[1][0]=='o' and board[2][0]=='o') or 
          (board[0][1]=='o' and board[1][1]=='o' and board[2][1]=='o') or
          (board[0][2]=='o' and board[1][2]=='o' and board[2][2]=='o')):
        return -1

        # this will check for diagonal Winner, there are only two ways, I think not a lot
    if ((board[0][0]== 'x')and board[1][1]== 'x'and board[2][2]== 'x' or (board[0][2] == 'x' and board[1][1]== 'x' and board[2][0]== 'x')):
        return 1
    elif ((board[0][0]== 'o' and board[1][1] == 'o' and board[2][2]=='o') or (board[0][2] == 'o' and board[1][1]== 'o' and board[2][0]== 'o')):
        return -1

        
    #checks if tie , {no place is empty use method isThereAMove,  and no one won}
    if ( isThereAMove(board)==False and result !=1 and result !=-1 ):
        return  0