

def playerMove():
    # this will give mw thw idia if this if the players turn or else if it the turn of the oppponints for the palyer
    return



def bestMove(board):
  BestScore=float('-inf')
  #Looping throgh the whole board to find an empty spot for the maximizing [x] to test best move
  for i in range(3):
      for j in range(3):
          if (board[i][j]==''):
              board[i][j]=ai
              # float(-inf) is alpha , float(inf) is beta
              score=minimax(board,0 ,float(-inf),float(inf),false)
              #undoing the board
              board[i][j]=''
              if(score >BestScore):
                 BestScore= score
                 move={i,j}






  #after it loops through all possible solutions , i.e plays whole game , to see which placemnt of x is most optimal
  board[move.i][move.j]=ai
  currentPlayer=human




def minimax(board ,depth,isMaximizing,isthereAWinner):
  result=isthereAWinner()
  #Basically if isthereAWinner enters any of the if statments and returns 1,-1 or 0 then result wont be none anymore.
  if result is not None:
     return result




  if (isMaximizing):
      BestScore=float(-inf)
      for i in range(3):
          for j in range(3):
              if (board[i][j]==''):
                  board[i][j]=ai
                  score=minimax(board,depth+1,alpha,beta,False)
                  board[i][j]=''
                  BestScore=max(score,BestScore)
                  alpha=max(alpha,score)
                  if (alpha>=beta):
                      break








          return BestScore




  else:
        BestScore=float('inf')
        for i in range (3):
            for j in range (3):
                if (board[i][j]==''):
                    board[i][j]=human
                    score=minimax(board,depth+1,alpha,beta,True)
                    board[i][j]=''
                    BestScore=min(score,BestScore)
                    beta=min(beta,score)
                    if (alpha>=beta):
                        break







            return BestScore