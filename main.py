#John Parkhurst
#9/7/20
#CSc 310 Professor Mandal
#This is COnways game of life

#Quick Rule Guide
#Live cell with 1 live neighbor dies
#Live cell with 2 or 3 live neighbors just continues
#live cells with more than 3 live neighbors dies as if
#by overpopulations
#Any dead cell with exactly 3 live neighbors become a live
#cell
import tkinter as tk
def check(board,x,y):
    num = 0
    position = [board[x-1][y-1],board[x][y-1],board[x+1][y-1],board[x-1][y],board[x+1][y],board[x-1][y+1],board[x][y+1],board[x+1][y+1]]
    print(position)
    return board
#Gen is generations also known as the amount of
#times we want the board to run
#size is the board 1d size so a 3x3 would be size 3
#board is the 2 dimensional array we edit
def conway(gen,size,board,text):
    if gen == 0:
        update(text, board, size)
        return board
    for x in range(size):
        for y in range(size):
            #WE NEED TO MAKE A GAME SAVE HERE THEN EDIT THE BOARD SO IT DOESNT MESS up
             board =check(board,x,y)

    return conway(gen-1,size,board,text)
def update(text,board,size):
    text.delete(1.0,tk.END)
    for x in range(size):
        text.insert(1.0,str(board[x])+'\n')
    return
def display(board):
    root = tk.Tk()
    root.geometry("800x600")
    root.resizable(width=False,height=False)
    backFrame = tk.Frame(root,bg ='#00107B')
    backFrame.place(relx=0,rely=0,relwidth=1,relheight=1)
    frame = tk.Frame(root,bg='#5ADCFF')
    frame.place(relx=.05,rely=.05,relwidth=.9,relheight=.9)
    but = tk.Button(root,bd = 5, bg ="yellow",text="Start",command=lambda:conway(5,5,board,field))
    but.place(relx=.5, rely=0.80, relwidth=0.1, relheight=.05, anchor='n')
    field = tk.Text(frame,bg='green',bd=5)
    field.place(relwidth=.75,relheight=.5,relx=.125,rely=.2)
    root.mainloop()
    return
if __name__ == "__main__":
    size =5
    board = [[ ' ','*','*', ' ', ' '],[' ','*',' ',' ',' '] ,['*','*' ,'*' ,' ','*'],[' ' ,' ' ,' ' ,' ' ,'*'],[' ','*',' ', '*','*']]
    display(board)
    #final = conway(0,size,board)