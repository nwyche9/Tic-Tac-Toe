
# coding: utf-8

# In[2]:


from IPython.display import clear_output
def display_board(board):
    clear_output
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('------')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('------')
    print(board[1]+'|'+board[2]+'|'+board[3])
    
test=[' ']*10
display_board(test)


# In[3]:


test_board=['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)


# In[4]:


def player_input():
    marker=''
    while not (marker == 'X' or marker == 'O'):
        marker=input('Choose X or O:  ').upper()
    player1=marker
    if player1=='X':
        player2='O'
    else:
        player2='X'
    return(player1,player2)


# In[5]:


player1_marker , player2_marker=player_input()


# In[6]:


player2_marker


# In[7]:


def place_marker(board, marker, position):
    board[position]=marker
        


# In[8]:


test_board


# In[9]:


place_marker(test_board, '$', 8)
display_board(test_board)


# In[10]:


def win_check(board, mark):
    return ((board[7]==board[8]==board[9]==mark)or 
            (board[4]==board[5]==board[6]==mark)or 
            (board[1]==board[2]==board[3]==mark)or 
            (board[7]==board[4]==board[1]==mark)or 
            (board[8]==board[5]==board[2]==mark)or 
            (board[9]==board[6]==board[3]==mark)or 
            (board[7]==board[5]==board[3]==mark)or 
            (board[9]==board[5]==board[1]==mark))


# In[11]:


display_board(test_board)
win_check(test_board, 'X')


# In[12]:


import random

def choose_first():
    flip=random.randint(0,1)
    if flip ==0:
        return 'Player 1 is first'
    else: 
        return 'Player 2 is first'


# In[13]:


def space_check(board, position):
    return board[position]==' '


# In[14]:


def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True


# In[15]:


def player_choice(board):
    position=0
    while position not in range(1,10) or not space_check(board,position):
        position = int(input('Choose a position: (1-9) '))
    return position


# In[16]:


def replay():
    choice = input("Play Again? Enter Yes or No ")
    return choice=='Yes' or 'yes'


# In[ ]:


print('Welcome to Tic Tac Toe')
#use a while loop to keep the game going
while True:
    #playing the game
    the_board=[' ']*10
    player1_marker,player2_marker=player_input()
    
    turn=choose_first()
    print(turn + ' will go first!')
    
    play_game=input('Ready to play?? y or n ')
    
    if play_game=='y':
        start_game=True
    else:
        start_game=False
        
    while start_game:
        
        if turn =='Player 1':
            #show the board
            display_board(the_board)
            #choose position
            position=player_choice(the_board)
            #place marker
            place_marker(the_board,player1_marker,position)
            
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('PLAYER 1 HAS WON!!')
                start_game=False
            else:
                #check for a tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    break
                else:
                    turn = 'Player 2'
                
            
        else:
            #show on the board
            display_board(the_board)
            position=player_choice(the_board)
            place_marker(the_board,player2_marker,position)
            
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('PLAYER 2 HAS WON!!')
                start_game=False
            else:
                #check for a tie
                if full_board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    break
                else:
                    turn = 'Player 1'
                    
                    
    if not replay():
        break
    

