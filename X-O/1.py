#A tic - tac -toe game (origin)

#import clear screen function
from special_func import clear,sleep

#setup
steps_win = 4;
key = "O"; # later will be "X". "X" is for the first player
#global var
list_ans = [];
######################
number_rows = 10;
number_columns = 10;


def Start(number_rows,number_columns):
	#Print a board(AxB)
	global list_ans;
	global key;
	key = "O"; # later will be "X". "X" is for the first player
	list_ans = [];
	for i in range(0, number_rows * number_columns): 
		list_ans.append(i);
		if (i % number_columns == 0 ) :
			print("\n",end="");
			print("|\t",end="");
		print(i,end="\t|\t");
	print("\n");

def GetAns():
	#Get the step that player want
	global list_ans;
	x = "";
	while x not in list_ans:
		x = int(input("Nhap vi tri ban muon danh dau: "));
	return x;


def ChangePlayer():
	#Change from player 1 to player 2
	global key, list_ans;
	if key == 'O':
		key = 'X';
		print("player 1: ");
		x = GetAns();
		list_ans[x] = key;

	else:
		key = 'O';
		print("player 2: ");
		x = GetAns();
		list_ans[x] = key;
	
def CheckVer(kind,position):
	#Check vertically
	global list_ans;
	x = position + number_columns * (steps_win - 1);
	if (x > (len(list_ans) - 1)):
		return False;
	else:
		for i in range(1,steps_win):
			k = position + number_columns * i ; # k is step which we need to check 
			if (str(list_ans[k]) != kind):
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
			if (str(list_ans[k]) != kind):
				return False;  
		return True;

def CheckCrsR(kind,position):
	#Check cross right
	x = position + (number_columns + 1) * (steps_win - 1);
	if (x > (len(list_ans) - 1)):
		return False;
	else:
		for i in range(1,steps_win):
			k = position + (number_columns + 1) * i ; # k is step which we need to check 
			if (str(list_ans[k]) != kind):
				return False;  
		return True;

def CheckCrsL(kind,position):
	#Check cross left
	x = position + number_rows * (steps_win - 1);
	if (x > (len(list_ans) - 1)):
		return False;
	else:
		for i in range(1,steps_win):
			k = position + number_rows * i ; # k is step which we need to check 
			if (str(list_ans[k]) != kind):
				return False;  
		return True;

def CheckWin(player):
	#Check win or lose
	global list_ans;
	flag = 1;
	for i in list_ans:
		if (i == "x") or (i == "o"):	
	#vertical
			if (CheckVer(i,list_ans.index(i)) == True):
				flag = 0;
				continue;
	#horizontal
			if (CheckHor(i,list_ans.index(i)) == True):
				flag = 0;
				continue;

	#cross (right)
			if (CheckCrsR(i,list_ans.index(i)) == True):
				flag = 0;
				continue;
	#cross (left)
			if (CheckCrsL(i,list_ans.index(i)) == True):
				flag = 0;
				continue;


	if flag == 0 :
		print("{} is the winner".format(player));
		return True;
	else: 
		return False;

def ShowBoard(number_rows,number_columns):
	#Print a board(AxB)
	global list_ans;
	for i in range(0, number_rows * number_columns):
		if (i % number_columns == 0 ) :
			print("\n",end="");
			print("|\t",end="");
		print(list_ans[i],end="\t|\t");
	print("\n");


def Process():
	#Call functions in order
	#Change player
	
	global key, list_ans;
	ChangePlayer();
	clear();
	ShowBoard(number_rows,number_columns);
	
	
	if (CheckWin(key) == True):
		x = input("Do you want to try again (Y/N):");
		x.upper();
		if x == "Y" :
			Start(number_rows,number_columns);
			Process();
		else:
			print("Goodbye!");
			sleep(2);
			#some code to wait and exit :)) 
	else:
		Process();




########################################
Start(number_rows,number_columns);
#clear();
Process();

