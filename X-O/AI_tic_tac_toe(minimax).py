#A tic - tac -toe game (using minimax algorithm)

#import clear screen function
from special_func import clear,sleep

#setup
steps_win = 3;
number_rows = 3;
number_columns = 3;

AI_player = "X";
hu_player = "O";
#global var
list_spots_origin = [];
######################


def Start(number_rows,number_columns):
	#Print a board(AxB)
	global list_spots_origin;
	

	list_spots_origin = [];
	for i in range(0, number_rows * number_columns): 
		list_spots_origin.append(i);
		if (i % number_columns == 0 ) :
			print("\n",end="");
			print("|\t",end="");
		print(i,end="\t|\t");
	print("\n");


def GetAns():
	#Get the step that player want
	global list_spots_origin;
	x = "";
	while 1 == 1:
		x = int(input("Nhap vi tri ban muon danh dau: "));
		if x in list_spots_origin:
			print("Vi tri nay da duoc danh dau!");
		else:
			continue;
	return x;

def TakeAnsFromPlayer():
	#Take the spot that player want
	print("Player turn :",end="");
	ans = GetAns();
	return ans;

def CheckVer(kind,position):
	#Check vertically
	global list_spots_origin;
	x = position + number_columns * (steps_win - 1);
	if (x > (len(list_spots_origin) - 1)):
		return False;
	else:
		for i in range(1,steps_win):
			k = position + number_columns * i ; # k is step which we need to check 
			if (str(list_spots_origin[k]) != kind):
				return False;  
		return True;

def CheckHor(kind,position):
	#Check horizontal
	x = position + steps_win - 1;
	if (x > number_columns):
		return False;
	else:
		for i in range(1,steps_win):
			k = position + i ; # k is step which we need to check 
			if (str(list_spots_origin[k]) != kind):
				return False;  
		return True;

def CheckCrsR(kind,position):
	#Check cross right
	x = position + (number_columns + 1) * (steps_win - 1);
	if (x > (len(list_spots_origin) - 1)):
		return False;
	else:
		for i in range(1,steps_win):
			k = position + (number_columns + 1) * i ; # k is step which we need to check 
			if (str(list_spots_origin[k]) != kind):
				return False;  
		return True;

def CheckCrsL(kind,position):
	#Check cross left
	x = position + number_rows * (steps_win - 1);
	if (x > (len(list_spots_origin) - 1)):
		return False;
	else:
		for i in range(1,steps_win):
			k = position + number_rows * i ; # k is step which we need to check 
			if (str(list_spots_origin[k]) != kind):
				return False;  
		return True;

def FindAvaiSpots():
	#Search and put all available spots 'index
	list_avai_spots = [];
	for i in list_spots_origin:
		if i in range(0,number_rows * number_columns + 1):
			list_avai_spots.append(i)
	return list_avai_spots;

def CheckWin(player):
	#Check win or lose
	global list_spots_origin;
	flag = 1;
	for i in list_spots_origin:
		if (i == "X") or (i == "O"):	
	#vertical
			if (CheckVer(i,list_spots_origin.index(i)) == True):
				flag = 0;
				continue;
	#horizontal
			if (CheckHor(i,list_spots_origin.index(i)) == True):
				flag = 0;
				continue;

	#cross (right)
			if (CheckCrsR(i,list_spots_origin.index(i)) == True):
				flag = 0;
				continue;
	#cross (left)
			if (CheckCrsL(i,list_spots_origin.index(i)) == True):
				flag = 0;
				continue;
	if flag == 1 :
		return True;
	else:
		return False;

def Exit():
	#Game exit (RETRY?)
	
	x = input("Do you want to try again (Y/N):");
	x.upper();
	if x == "Y" :
		Start(number_rows,number_columns);
		Process();
	else:
		print("Goodbye!");
		sleep(2);
		#some code to wait and exit :)) 

def AnnounceWinner(player,state):
	#tell The Winner
	if state == 1 :
		print("{} is the winner".format(player));
		Exit();
	else :
		print("Tie!");
		Exit();
		

def GetMax(list_max):
	Max = 0;
	for i in list_max:
		if list_max.index(i) % 2 == 0:
			if i > Max :
				Max  = i;
				best_index = list_max.index(i) - 1;
	return best_index;

def GetMax(list_min):
	Min = 20;
	for i in list_min:
		if list_min.index(i) % 2 == 0:
			if i < Min :
				Min = i;
				best_index = list_min.index(i) - 1;
	return best_index;
	 
def minimax(new_board,player):
	#Choose the best option to win over the hu_player
	list_avai_spots = FindAvaiSpots();
	moves = [];
	best_move = 0;
	if len(list_avai_spots) > 0 :
		i = 1;
		if list_avai_spots[i] not in moves:
			index = list_avai_spots[1];
			new_board[index] = player;
			moves.append(index);
		else: 
			++i;
	flag = 1;
	# if ai wins then score 10 
	# if human wins then score -10
	# if no one wins then score 0
	if CheckWin(AI_player) == True :
		value = 10;
		flag = 0;
	else:
		if CheckWin(hu_player) == True :
			value = -10;
			flag = 0;
		else:
			if (len(list_avai_spots) == 0): 
				value = 0;
				flag = 0;
	if flag == 0:
		moves.append(value);
	else:
		moves.append(0);

	if player == AI_player:
		minimax(new_board,hu_player);
	else :
		if player == hu_player:
			minimax(new_board,AI_player);	


def ShowBoard(number_rows,number_columns):
	#Print a board(AxB)
	global list_spots_origin;
	for i in range(0, number_rows * number_columns):
		if (i % number_columns == 0 ) :
			print("\n",end="");
			print("|\t",end="");
		print(list_spots_origin[i],end="\t|\t");
	print("\n");

def Process():
	#Call functions in order
	#Change player
	
	global list_spots_origin;
	#ChangePlayer();
	clear();
	ShowBoard(number_rows,number_columns);
	
	


