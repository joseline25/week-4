#  create the data structure

#tab = [[1, 2, 3],
    #    [4, 5, 6],
#        [7, 8, 9]]
tab = [1, 2, 3, 4, 5, 6, 7, 8, 9]
dict = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'heigth': 8,
        'nine': 9
}
# display
"""def display_board():
        print('* {} '.format('*'*11))
        print('* {} | {} | {} *'.format(tab[0][0], tab[0][1], tab[0][2]))
        print('* --+ - +-- *')
        print('* {} | {} | {} *'.format(tab[1][0], tab[1][1], tab[1][2]))
        print('* --+ - +-- *')
        print('* {} | {} | {} *'.format(tab[2][0], tab[2][1], tab[2][2]))
        print('* {} '.format('*'*11))"""

def display_board1():
        print('* {} '.format('*'*11))
        print('* {} | {} | {} *'.format(dict['one'], dict['two'], dict['three']))
        print('* --+ - +-- *')
        print('* {} | {} | {} *'.format(dict['four'], dict['five'], dict['six']))
        print('* --+ - +-- *')
        print('* {} | {} | {} *'.format(dict['seven'], dict['heigth'], dict['nine']))
        print('* {} '.format('*'*11))


#display_board()
#display_board1()
# get player input



def player_input(player):


        val = int(input(' Player {} where do you want to play (choose an integer between 1 and 9 : '.format(player)))

        while tab.count(val) == 0:
                print('Enter another value')
                val = int(input('invalid position Player {} where do you want to play (choose an integer between 1 and 9 : '.format(player)))
        else:
                for i in dict:
                        if dict[i] == val:
                                dict[i] = player
                                check_win()
                                tab.remove(val)        
#player_input(player)
#display_board1()

# fonction play



def play():
        display_board1()

        #player = input('Choose between X or O : ')
        playerOne = 'X'
        playerTwo ='O'
        #playerval = 'r'
        """if player == 'X' or player =='x':
                print('You are player X. You will play with X ')
                playerval = 'X'
                playerOne = playerval
        elif player == 'O' or player == 'o':
                print('You are player O. You will play with O')
                playerval = 'O'
                playerTwo = playerval"""

        playcount = 0

        while playcount < 9:
                if playcount%2 == 0:
                        player_input(playerOne)
                        playcount = playcount + 1
                        display_board1()
                else:
                      player_input(playerTwo)
                      playcount = playcount + 1
                      display_board1()


        display_board1()
        check_win()

#Check the win

def check_win():
        if dict['one'] == dict['two'] == dict['three']:
                print('Player {} wins'.format(dict["one"]))
                return  True

        if dict['four'] == dict['five'] == dict['six']:
                print('Player {} wins'.format(dict["six"]))
                return  True

        if dict['seven'] == dict['heigth'] == dict['nine']:
                print('Player {} wins'.format(dict["nine"]))
                return  True

        if dict['one'] == dict['four'] == dict['seven']:
                print('Player {} wins'.format(dict["seven"]))
                return  True

        if dict['two'] == dict['five'] == dict['heigth']:
                print('Player {} wins'.format(dict["heigth"]))
                return  True
        if dict['three'] == dict['six'] == dict['nine']:
                print('Player {} wins'.format(dict["nine"]))
                return  True

        if dict['one'] == dict['five'] == dict['nine']:
                print('Player {} wins'.format(dict["nine"]))
                return  True
        if dict['three'] == dict['five'] == dict['seven']:
                print('Player {} wins'.format(dict["seven"]))
                return  True

play()
