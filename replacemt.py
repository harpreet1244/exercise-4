game_list = [0,1,2]

def display(game_list):
   print(game_list)


display(game_list)

def position_check():
   choice = "wrong"
   while choice not in ['0','1','2']:

       choice = input("select the position:")
       if choice not in ['0','1',"2"]:
           print("sorry please enter the relevent posistion:")

   return int(choice)

position_check()

def replacement(game_list,position=0):

    user = input("enter the value you want to replace it with:")
    game_list[position] = user
    print(game_list)


replacement(game_list)


def keep_playing():
    choice = "wrong"
    while choice not in ["Y" , "N"]:
        choice = input("enter y or n to continue the game: ")
        if choice not in ["Y" , "N"]:
            print("please select Y OR N")
    if choice == "Y":
        return True
    else :
        return False

            


keep_playing()



def furthur():
    game_on = True
    game_list = [0,1,2]

    while game_on:

        display(game_list)
        position = position_check()
        game_list = replacement(game_list,position)
        display(game_list)
        game_on = keep_playing()


furthur()



