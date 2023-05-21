#Interactive chessboard
#input first letter of piece along with its starting position, example : to move pawn e2 input "pe2" [except for knight which is represented by n, all other pieces are selected using their first letter]
#to move the selected peice input end position as is , example: to move the above selected pawn to e4 input "e4"
"""
-----------REFERENCE---------
    pieces notation = [pawn : p , knight : n , bishop : b , rook : r , queen : q , king : k]
    
    coloumn coordinate : from left to right each coloumn is denoted by alphabets a,b,c,d,e,f,g,h respectively
    row coordinate     : from white king side to black king side numbered from 1 to 8 respectively
    
    *TO SEE BOARD , ENTER THE EXAMPLE INPUT GIVEN ABOVE
    NOTE: There is no mechanism for check or castling present.
"""
colour = False
chess_bd = []

for i  in range (0,8):
    a = []
    for j in range(0,8):    
        b = []
        a.append(b)
    chess_bd.append(a)

placingpieces = ["r","n","b","q","k","b","n","r"]
for i in range(0,8):
    chess_bd[-2][i] = ["p",False] # white
    chess_bd[-7][i] = ["p",True] # black
    chess_bd[-1][i] = [placingpieces[i],False]
    chess_bd[-8][i] = [placingpieces[i],True]
    

def move_pawn(start_x_coord,start_y_coord,end_x_coord,end_y_coord,colour):
    
    a = -1 + (2*int(colour))
    if bool(chess_bd[-(start_y_coord)][start_x_coord]) == False or (chess_bd[-(start_y_coord)][start_x_coord][0] != "p" or chess_bd[-(start_y_coord)][start_x_coord][1] != colour):
        print(chess_bd[-(start_y_coord)][start_x_coord])  
        return "INVALID INPUT(position does not have pawn)"
    
    else:
        if start_x_coord == end_x_coord:
            if bool(chess_bd[-(end_y_coord)][end_x_coord]) == True:
                return "INVALID INPUT(pawn blocked)"
            elif (-start_y_coord + a == -end_y_coord):
                chess_bd[-(start_y_coord)][start_x_coord],chess_bd[-(end_y_coord)][end_x_coord] = chess_bd[-(end_y_coord)][end_x_coord],chess_bd[-(start_y_coord)][start_x_coord]
                return "done"
            elif (-start_y_coord == int(-4.5 - a*(2.5))) and (-start_y_coord + 2*a == -end_y_coord):
                if bool(chess_bd[-start_y_coord +a][start_x_coord]) == False:
                    chess_bd[-(start_y_coord)][start_x_coord],chess_bd[-(end_y_coord)][end_x_coord] = chess_bd[-(end_y_coord)][end_x_coord],chess_bd[-(start_y_coord)][start_x_coord]
                    return "done"
                else:
                    return "INVALID INPUT(pawn blocked)(2 step)"
            else:
                return "INVALID INPUT(pawn)"
        elif ((end_x_coord == start_x_coord + 1) or (end_x_coord == start_x_coord - 1)) and (-end_y_coord == (-start_y_coord + a)):
            if bool(chess_bd[-end_y_coord][end_x_coord]) == True:
                if chess_bd[-end_y_coord][end_x_coord][1] != colour:
                    chess_bd[-(end_y_coord)][end_x_coord] = chess_bd[-(start_y_coord)][start_x_coord]
                    chess_bd[-(start_y_coord)][start_x_coord] = []
                    return "done"
                else:
                    return "INVALID INPUT(not black/white piece)(pawn)"
        else:
            return "INVALID INPUT(move not possible?(pawn))"
                    


def move_knight(start_x_coord,start_y_coord,end_x_coord,end_y_coord,colour):
    
    if bool(chess_bd[-(start_y_coord)][start_x_coord]) == False or (chess_bd[-(start_y_coord)][start_x_coord][0] != "n" or chess_bd[-(start_y_coord)][start_x_coord][1] != colour) :
        return "INVALID INPUT(no knight or its other colour/piece)"
    elif bool(chess_bd[-end_y_coord][end_x_coord]) == True and (chess_bd[-end_y_coord][end_x_coord][1] == colour):
        return "INVALID INPUT(already same colour piece at end (knight))"
    else:
        knightpos = [[-start_y_coord-3,start_x_coord+1],[-start_y_coord-3,start_x_coord-1],[-start_y_coord+3,start_x_coord+1],[-start_y_coord+3,start_x_coord-1],
            [-start_y_coord+1,start_x_coord-3],[-start_y_coord-1,start_x_coord-3],[-start_y_coord+1,start_x_coord+3],[-start_y_coord-1,start_x_coord+3]]

        if [-end_y_coord,end_x_coord] in knightpos:
            chess_bd[-end_y_coord][end_x_coord],chess_bd[-(start_y_coord)][start_x_coord] = chess_bd[-(start_y_coord)][start_x_coord],[]
            return "done"
        else:
            return "INVALID MOVE(knight)"


def move_queen(start_x_coord,start_y_coord,end_x_coord,end_y_coord,colour):  

    if bool(chess_bd[-(start_y_coord)][start_x_coord]) == False or (chess_bd[-(start_y_coord)][start_x_coord][0] != "q" or chess_bd[-(start_y_coord)][start_x_coord][1] != colour):
        return "INVALID INPUT(no queen or its other colour piece)"
    
    if (start_y_coord) == (end_y_coord):# for moving queen horizontally
        horizontalpos1 =[]
        horizontalpos2 =[]
        for i in (0,start_x_coord):# start to queen position 
            if bool(chess_bd[-(start_y_coord)][i]) == False:
                horizontalpos1.append([-(start_y_coord),i])
            elif chess_bd[-(start_y_coord)][i][1] != colour:
                horizontalpos1 = []
                horizontalpos1.append([-(start_y_coord),i])
            else:
                horizontalpos1 = []            
        
        for i in range(start_x_coord+1,8):# queen position to end
            if bool(chess_bd[-(start_y_coord)][i]) == False:
                horizontalpos2.append([-(start_y_coord),i])
            elif chess_bd[-(start_y_coord)][i][1] != colour:               
                horizontalpos2.append([-(start_y_coord),i])
                break
            else:
                break
        horizontalpos1 = horizontalpos1 + horizontalpos2
        if [-end_y_coord,end_x_coord] in horizontalpos1:
            chess_bd[-end_y_coord][end_x_coord],chess_bd[-(start_y_coord)][start_x_coord] = chess_bd[-(start_y_coord)][start_x_coord],[]
            return "done"
        else:
            return "INVALID MOVE(queen horizontal)"
    
    elif start_x_coord == end_x_coord:
        verticalpos1 = []
        verticalpos2 = []
        for i in range(-1,-start_y_coord,-1):
            if bool(chess_bd[i][start_x_coord]) == False:
                verticalpos1.append([i,start_x_coord])
            elif chess_bd[i][start_x_coord][1] != colour:
                verticalpos1 = []
                verticalpos1.append([i,start_x_coord])
            else:
                verticalpos1 = []
            
        for i in range(-start_y_coord-1,-9,-1):
            if bool(chess_bd[i][start_x_coord]) == False:
                verticalpos2.append([i,start_x_coord])
            elif chess_bd[i][start_x_coord][1] != colour:
                verticalpos2.append([i,start_x_coord])
                break
            else:
                break 
        verticalpos1 = verticalpos1 + verticalpos2
        if [-end_y_coord,end_x_coord] in verticalpos1:
            chess_bd[-end_y_coord][end_x_coord],chess_bd[-(start_y_coord)][start_x_coord] = chess_bd[-(start_y_coord)][start_x_coord],[]
            return "done"
        else:
            return "INVALID MOVE (queen vertical)"

    else:
        i = start_x_coord
        j = -start_y_coord
        diagonal = []
        c = d = 0
        if end_x_coord > start_x_coord and end_y_coord > start_y_coord : # pi/4 diagonal
            c,d = 1,-1
        elif end_x_coord < start_x_coord and end_y_coord > start_y_coord : # 3pi/4 diagonal
            c,d = -1,-1
        elif end_x_coord < start_x_coord and end_y_coord < start_y_coord : # 5pi/4 diagonal
            c,d = -1,+1
        elif end_x_coord > start_x_coord and end_y_coord < start_y_coord : # 7pi/4 diagonal
            c,d = +1,+1
        
        while True:
            try:
                if bool(chess_bd[j+d][i+c]) == False:
                    diagonal.append([j+d,i+c])
                elif chess_bd[j+d][i+c][1] != colour:
                    diagonal.append([j+d,i+c])
                    break
                else:
                    break
                
            except:
                break
            i += c 
            j += d
        if [-end_y_coord,end_x_coord] in diagonal:
            chess_bd[-end_y_coord][end_x_coord],chess_bd[-(start_y_coord)][start_x_coord] = chess_bd[-(start_y_coord)][start_x_coord],[]
            return "done"
        else:
            return "INVALID MOVE (queen diagonal)"
    
def move_bishop(start_x_coord,start_y_coord,end_x_coord,end_y_coord,colour):

    if bool(chess_bd[-(start_y_coord)][start_x_coord]) == False or (chess_bd[-(start_y_coord)][start_x_coord][0] != "b" or chess_bd[-(start_y_coord)][start_x_coord][1] != colour):
        return "INVALID INPUT(no bishop or its other colour piece)"
    elif start_x_coord != end_x_coord or start_y_coord != end_y_coord:
        i = start_x_coord
        j = -start_y_coord
        diagonal = []
        c = d = 0
        if end_x_coord > start_x_coord and end_y_coord > start_y_coord : # pi/4 diagonal
            c,d = 1,-1
        elif end_x_coord < start_x_coord and end_y_coord > start_y_coord : # 3pi/4 diagonal
            c,d = -1,-1
        elif end_x_coord < start_x_coord and end_y_coord < start_y_coord : # 5pi/4 diagonal
            c,d = -1,+1
        elif end_x_coord > start_x_coord and end_y_coord < start_y_coord : # 7pi/4 diagonal
            c,d = +1,+1
        
        while True:
            try:
                if bool(chess_bd[j+d][i+c]) == False:
                    diagonal.append([j+d,i+c])
                elif chess_bd[j+d][i+c][1] != colour:
                    diagonal.append([j+d,i+c])
                    break
                else:
                    break
                
            except:
                break
            i += c 
            j += d
        if [-end_y_coord,end_x_coord] in diagonal:
            chess_bd[-end_y_coord][end_x_coord],chess_bd[-(start_y_coord)][start_x_coord] = chess_bd[-(start_y_coord)][start_x_coord],[]
            return "done"
        else:
            return "INVALID INPUT (bishop diagonal)"
    else:
        return "INVALID INPUT(bishop)"

def move_rook(start_x_coord,start_y_coord,end_x_coord,end_y_coord,colour):

    if bool(chess_bd[-(start_y_coord)][start_x_coord]) == False or (chess_bd[-(start_y_coord)][start_x_coord][0] != "r" or chess_bd[-(start_y_coord)][start_x_coord][1] != colour):
        return "INVALID INPUT(no rook or its other colour piece)"
    if (start_y_coord) == (end_y_coord):# for moving rook horizontally
        horizontalpos1 =[]
        horizontalpos2 =[]
        for i in (0,start_x_coord):# start to rook position 
            if bool(chess_bd[-(start_y_coord)][i]) == False:
                horizontalpos1.append([-(start_y_coord),i])
            elif chess_bd[-(start_y_coord)][i][1] != colour:
                horizontalpos1 = []
                horizontalpos1.append([-(start_y_coord),i])
            else:
                horizontalpos1 = []            
        
        for i in range(start_x_coord+1,8):# rook position to end
            if bool(chess_bd[-(start_y_coord)][i]) == False:
                horizontalpos2.append([-(start_y_coord),i])
            elif chess_bd[-(start_y_coord)][i][1] != colour:               
                horizontalpos2.append([-(start_y_coord),i])
                break
            else:
                break
        horizontalpos1 = horizontalpos1 + horizontalpos2
        if [-end_y_coord,end_x_coord] in horizontalpos1:
            chess_bd[-end_y_coord][end_x_coord],chess_bd[-(start_y_coord)][start_x_coord] = chess_bd[-(start_y_coord)][start_x_coord],[]
            return "done"
        else:
            return "INVALID MOVE(rook horizontal)"
    
    elif start_x_coord == end_x_coord:
        verticalpos1 = []
        verticalpos2 = []
        for i in range(-1,-start_y_coord,-1):
            if bool(chess_bd[i][start_x_coord]) == False:
                verticalpos1.append([i,start_x_coord])
            elif chess_bd[i][start_x_coord][1] != colour:
                verticalpos1 = []
                verticalpos1.append([i,start_x_coord])
            else:
                verticalpos1 = []
            
        for i in range(-start_y_coord-1,-9,-1):
            if bool(chess_bd[i][start_x_coord]) == False:
                verticalpos2.append([i,start_x_coord])
            elif chess_bd[i][start_x_coord][1] != colour:
                verticalpos2.append([i,start_x_coord])
                break
            else:
                break 
        verticalpos1 = verticalpos1 + verticalpos2
        if [-end_y_coord,end_x_coord] in verticalpos1:
            chess_bd[-end_y_coord][end_x_coord],chess_bd[-(start_y_coord)][start_x_coord] = chess_bd[-(start_y_coord)][start_x_coord],[]
            return "done"
        else:
            return "INVALID MOVE (rook vertical)"

def move_king(start_x_coord,start_y_coord,end_x_coord,end_y_coord,colour): 

    if bool(chess_bd[-(start_y_coord)][start_x_coord]) == False or (chess_bd[-(start_y_coord)][start_x_coord][0] != "k" or chess_bd[-(start_y_coord)][start_x_coord][1] != colour):
        return "INVALID INPUT(no king or its other colour piece)"
    king_moves = [[-start_y_coord+1,start_x_coord],[-start_y_coord-1,start_x_coord],[-start_y_coord+1,start_x_coord+1],[-start_y_coord+1,start_x_coord-1],[-start_y_coord-1,start_x_coord+1],
                  [-start_y_coord-1,start_x_coord+1],[-start_y_coord,start_x_coord+1],[-start_y_coord,start_x_coord-1]]
    if [-end_y_coord,end_x_coord] in king_moves:
        chess_bd[-end_y_coord][end_x_coord],chess_bd[-(start_y_coord)][start_x_coord] = chess_bd[-(start_y_coord)][start_x_coord],[]
        return "done"
def CALL(totem,start_x_coord,start_y_coord,end_x_coord,end_y_coord,colour):
	if totem = "move_pawn":
		move_pawn(start_x_coord,start_y_coord,end_x_coord,end_y_coord,colour)
	if totem  = "move_knight":
		move_knight(start_x_coord,start_y_coord,end_x_coord,end_y_coord,colour)
	if totem = "move_bishop":
		move_bishop(start_x_coord,start_y_coord,end_x_coord,end_y_coord,colour)
	if totem = "move_rook":
		move_rook(start_x_coord,start_y_coord,end_x_coord,end_y_coord,colour)
	if totem = "move_queen":
		move_queen(start_x_coord,start_y_coord,end_x_coord,end_y_coord,colour)
	if totem = "move_king"
		move_king(start_x_coord,start_y_coord,end_x_coord,end_y_coord,colour)
def move_piece():
    pieces = {"p":move_pawn,"n":move_knight,"b":move_bishop,"r":move_rook,"q":move_queen,"k":move_king}
    x = str(input("Enter piece and startpos :"))
    x2 = str(input("endpos :"))
    
    start_x_coord = ord(x[1]) - 97
    start_y_coord = int(x[2])
    end_x_coord = ord(x2[0]) - 97   
    end_y_coord = int(x2[1])
    
    if start_x_coord not in range(0,8):
        return "INVALID INPUT(x coord)"
        
    if int(x[2]) not in range(1,9):
        return "INVALID INPUT(y coord)"
    
    if end_x_coord not in range(0,8):
        return "INVALID INPUT(x end coord)"
    
    if end_y_coord not in range(1,9):
        return "INVALID INPUT(y coord)"
    
    if x[0] in pieces:
        global colour
	    totem = pieces[x[0]]
        if CALL(totem,start_x_coord,start_y_coord,end_x_coord,end_y_coord,colour) == "done":
            colour = not(colour)
            print("-------------MOVE DONE----------")
        else:
            print("error")
    print("|"+"-"*63 +"|")
    t1 = True
    t2 = True
    for i in chess_bd:  
       
        for j in i:
            
            if bool(j) == False:
                    print("|"+(" " * 7),end ="")
               
            else:
               if j[1] == True: 
                print("|"+"\x1b[0;35;48m"+(" "*3)+j[0]+(" "*3)+"\x1b[0m",end ="")
               else:
                   print("|"+(" "*3)+j[0]+(" "*3),end ="")
            t2 = not(t2)
        t1 = not(t1)
        print("|"+"\n"+8*("|" + 7*" "),end ="")
        print("|")
        print(("|"+"-"*7)*8,end ="")
        print("|")
            
    move_piece()
            
move_piece()
