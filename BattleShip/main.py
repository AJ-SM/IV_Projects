import os
from random import choice
from time import sleep,time
import numpy as np

# declaring all the variables and constants used
player1 = "player1"
player2 = "player2"
game_size = 5
gamearea_of = {player1: "", player2: ""}
game_mode = ""
ship_position_of = {player1: "", player2: ""}
ship_names_short = {"destroyer": "D", "cruiser": "C", "battleship": "B"}
ship_names_index = {1: "destroyer", 2: "cruiser", 3: "battleship"}
ship_sizes = {"D": 2, "C": 3, "B": 4}
initial_no_of_ships = {"destroyer": 1, "cruiser": 1, "battleship": 1}
number_of_ships = {player1: "", player2: ""}
ship_alignment = {"vertical": "v", "horizontal": "h"}
ship_alignment_index = {1: "vertical", 2: "horizontal"}
valid_coordinates = {}
occupied_coordinates = {}
current_player = ""
opposite_player = ""
my_flag = ""
hit_count = {}
hitted_ship_position_of = {player1: [], player2: []}
chosen_ship = ""
chosen_alignment = ""
visual_of_area_of = {player1: {}, player2: {}}
possible_hit = {player1: [], player2: []}
attacked_at = {player1: [], player2: []}
remaining_position = {player1: [], player2: []}
game_start_time=''
# current_time=''

#    this is for setting the game for start of each new game


def set_game():
    global gamearea_of, ship_position_of, current_player, opposite_player, player1, player2, visual_of_area_of, remaining_position,game_start_time
    arr = np.array([[i, j] for i in range(game_size) for j in range(game_size)])
    gamearea_of[player1] = arr.reshape(game_size, game_size, 2).copy()
    gamearea_of[player2] = arr.reshape(game_size, game_size, 2).copy()
    ship_position_of[player1] = {}
    ship_position_of[player2] = {}
    valid_coordinates[player1] = gamearea_of[player1] + 1
    valid_coordinates[player2] = gamearea_of[player2] + 1
    current_player = player1
    opposite_player = player2
    visual_of_area_of = {player1: {}, player2: {}}
    remaining_position = {player1: [], player2: []}
    game_start_time=time()
    reset_game()


#     this is to reset the game
def reset_game():
    global ship_position_of, valid_coordinates, gamearea_of, occupied_coordinates, number_of_ships, hit_count, initial_no_of_ships, hitted_ship_position_of, visual_of_area_of, player2, player1, possible_hit, attacked_at, remaining_position
    for i in range(game_size):
        for j in range(game_size):
            ship_position_of[player1][position(player1, i, j)] = " - "
            ship_position_of[player2][position(player2, i, j)] = " - "
            visual_of_area_of[player1][position(player1, i, j)] = " - "
            visual_of_area_of[player2][position(player1, i, j)] = " - "
            remaining_position[player1].append([i + 1, j + 1])
            remaining_position[player2].append([i + 1, j + 1])
    occupied_coordinates[player1] = []
    occupied_coordinates[player2] = []
    number_of_ships = {
        player1: initial_no_of_ships.copy(),
        player2: initial_no_of_ships.copy(),
    }
    hit_count = {player1: 0, player2: 0}
    hitted_ship_position_of = {player1: [], player2: []}
    possible_hit = {player1: [], player2: []}
    attacked_at = {player1: [], player2: []}


# this is for the ship alignment display to help players choose coordinates to place thir ships accordingly
def display_ship_alignment_of(player):
    global game_size, ship_position_of, player1, player2
    if player == player1:
        print("\t\t-------------------------------")
        print(f"\t\t{player1}'s ship alignment")
        for i in range(game_size):
            print("\t\t\t", end="")
            for j in range(game_size):
                print(ship_position_of.get(player1)[position(player1, i, j)], end=" ")
            print()
        print("\t\t-------------------------------")
    else:
        print("\t\t-------------------------------")
        print(f"\t\t{player2}'s ship alignment")
        for i in range(game_size):
            print("\t\t\t", end="")
            for j in range(game_size):
                print(ship_position_of.get(player2)[position(player2, i, j)], end=" ")
            print()
        print("\t\t-------------------------------")


# this is display of game when running hit miss part ,created to have a better display of sea of both current and oppposite player (only shows the hitted(X) and missed(O) and remaining area as(-) )
def display_visual_for(player):
    global player2, player1, game_size, visual_of_area_of
    if player == player1:
        # print('-------------------------------')
        print(f"\t\tSea of {player2}")
        for i in range(game_size):
            print("\t\t\t", end="")
            for j in range(game_size):
                print(visual_of_area_of.get(player2)[position(player1, i, j)], end=" ")
            print()
        print("\t\t-------------------------------")
    else:
        # print('-------------------------------')
        print(f"\t\tSea of {player1}")
        for i in range(game_size):
            print("\t\t\t", end="")
            for j in range(game_size):
                print(visual_of_area_of.get(player1)[position(player2, i, j)], end=" ")
            print()
        print("\t\t-------------------------------\n")


# this is to display the coordinate system for convenience of player


def display_coordinates():
    global game_size, gamearea_of, player1, player2
    # print('-------------------------------')
    print("\t\t- coordinate system -")
    for i in range(game_size):
        print("\t\t", end="")
        for j in range(game_size):
            print(gamearea_of.get(player1)[i, j] + 1, end=" ")
        print()
    print("\t\t-------------------------------")


# some commonly used functinos


def position(player, i, j):
    return str(gamearea_of.get(player)[i, j])


# to clear the screen
def clrscr():
    os.system("cls")


# to display the number of availale ships in garage
def display_garage_info():
    print(
        f"My Garage (overall:{sum(number_of_ships[current_player].values())}) \n\t: ",
        end="",
    )
    for n, i in enumerate(number_of_ships[current_player].items()):
        if n != len(number_of_ships[current_player].items()) - 1:
            print(f"{i[0]}:{i[1]}", end=", ")
        else:
            print(f"{i[0]}:{i[1]}", end=".\n")


# to dispay the ship sizes for convenience of selecting the ship
def display_ship_sizes():
    global ship_names_short, ship_sizes
    i1, i2 = list(ship_names_short.keys()), list(ship_sizes.values())
    print("\nShip Sizes: ", end=" ")
    for n, f in enumerate(i1):
        if n != len(i1) - 1:
            print(f"{f}:{i2[n]}", end=", ")
        else:
            print(f"{f}:{i2[n]}", end=" (cells).")


# to display who is current player
def display_current_player():
    print(f"Now Playing: {current_player.capitalize()}\n")


# to change the current player that is altering the player
def change_current_player():
    global current_player, opposite_player
    if current_player == player1:
        current_player = player2
        opposite_player = player1
    else:
        current_player = player1
        opposite_player = player2


# check whether the list(it is of the coordinates ex [1,4]) provided is element of parent numpy array
def is_list_an_element(parent, child):
    return np.any(
        np.all(parent.reshape(-1, parent.shape[-1]) == np.array(child), axis=1)
    )


# to convert the input taken in string for the coordinates of ship placement to list
def index_to_coords(index):
    return list(map(int, index.split()))


# to check if there is availability of location for the given coordinates with ship size and ship alignment
def is_loc_available(coords, ship_size, ship_align):
    global valid_coordinates, current_player

    validity_of_loc = is_list_an_element(valid_coordinates[current_player], coords)
    ship_area = []
    x, y = coords
    if ship_align == "v":
        for i in range(ship_size):
            ship_area.append([x + i, y])
    else:
        for i in range(ship_size):
            ship_area.append([x, y + i])

    vacancy_of_loc = True
    for elem in ship_area:
        if not is_list_an_element(valid_coordinates[current_player], elem) or (
            elem in occupied_coordinates[current_player]
        ):
            vacancy_of_loc = False
            break
    yield validity_of_loc and vacancy_of_loc
    yield ship_area


def game_instructions():
    print("\t\t--- HII There ! This is BAttleShip by -LogicTitans ---")
    print("\nSome Instructions for you to quicky understand the game:\n")
    print(f"1)You have following ships:-{ship_names_short}\n")
    sleep(0.5)
    print(f"2)Ships are of sizes:-{ship_sizes}\n")
    sleep(0.5)
    print(f"3)Initial No. of ships:-{initial_no_of_ships}\n")
    sleep(0.55)
    print(f"6)you can place ship as:-{ship_alignment}\n")
    sleep(0.5)
    print(
        f"4)use index to enter your choice.\n\teg.{ship_names_index},{ship_alignment_index}\n"
    )
    sleep(0.5)


def display_all_about_ship_input():
    clrscr()
    print(f"Game Mode: {game_mode}\t", end="")
    display_current_player()
    display_garage_info()
    display_ship_sizes()
    print("\nShip Index: ", ship_names_index)


# for taking ship type input
def ship_Type_input():
    global my_flag, ship_names_index, number_of_ships, chosen_ship, ship_names_short, ship_sizes

    while True:
        chosen_ship = ""
        if (
            sum(number_of_ships[current_player].values()) == 0
            and sum(number_of_ships[opposite_player].values()) == 0
        ):
            clrscr()
            print(f"{current_player.capitalize()} has placed all ships.")
            sleep(1)
            change_current_player()
            return "all Placed"

        if sum(number_of_ships[current_player].values()) == 0:
            clrscr()
            print(f"{current_player.capitalize()} has placed all ships.")
            sleep(1)
            change_current_player()
            clrscr()
            print(f"NOW PLAYING : {current_player.capitalize()}")
            sleep(1)

        # this if block checks if computer is playing and returns the ship type
        if game_mode == 2 and current_player == player2:
            chosen_ship = choice(list(ship_names_index.values()))
            if number_of_ships[current_player][chosen_ship] != 0:
                number_of_ships[current_player][chosen_ship] -= 1
                return ship_names_short[chosen_ship]
        else:
            display_all_about_ship_input()
            index = input("\n\nEnter ship (index) :-")
            if index in list(map(str, ship_names_index)):
                chosen_ship = ship_names_index.get(int(index))
                if number_of_ships[current_player][chosen_ship] != 0:
                    number_of_ships[current_player][chosen_ship] -= 1
                    return ship_names_short[chosen_ship]
                else:
                    display_all_about_ship_input()
                    print("\n\nEnter ship Name (index) :-ahh!😒 Not in Garage.")
                    sleep(0.75)
            else:
                display_all_about_ship_input()
                print("\n\nEnter ship Name (index) :-ahh!😒 Not Valid Index.")
                sleep(0.75)


# for taking ship alignment input
def ship_alignment_input():
    global my_flag, ship_alignment_index, chosen_alignment
    chosen_alignment = ""
    # this if block assigns the ship alignment for chosen ship of computer
    if game_mode == 2 and current_player == player2:
        chosen_alignment = choice(list(ship_alignment_index.values()))

    else:
        while True:
            clrscr()
            display_current_player()
            print(f"Chosen Ship: {chosen_ship}\n")
            print(f"Ship Alignment Index :- {ship_alignment_index}\n")
            index = input("Enter ship Alignment (index) :-")
            if index in list(map(str, ship_alignment_index)):
                break
            else:
                clrscr()
                display_current_player()
                print(f"Chosen Ship: {chosen_ship}\n")
                print(f"Ship Alignment Index :- {ship_alignment_index}\n")
                print("ahh!😒 You didn't choose Valid Index")
                sleep(0.75)
        chosen_alignment = ship_alignment_index.get(int(index))

    return ship_alignment.get(chosen_alignment)


# to take the input of coordinates to place the ship
def ship_coordinates_input(ship_type, ship_align):
    global my_flag, valid_coordinates, current_player, occupied_coordinates
    ship_size = ship_sizes.get(ship_type)
    while True:
        if game_mode == 2 and current_player == player2:
            a = np.reshape(valid_coordinates[current_player], (-1, 2)).tolist()
            coords = choice(a)
        else:
            while True:
                clrscr()
                display_current_player()
                print(
                    f"Ship:- {chosen_ship.capitalize()} | Alignment:- {chosen_alignment.capitalize()} | Size:- {ship_sizes[ship_names_short[chosen_ship]]}"
                )
                display_coordinates()
                display_ship_alignment_of(current_player)
                index = input("\nEnter Coordinates to place the ship :-")
                if len(index.split()) == 2 and all(
                    char.isdigit() for char in index.split()
                ):
                    coords = index_to_coords(index)
                    break
                else:
                    clrscr()
                    display_current_player()
                    print(
                        f"Ship:- {chosen_ship.capitalize()} | Alignment:- {chosen_alignment.capitalize()} | Size:- {ship_sizes[ship_names_short[chosen_ship]]}"
                    )
                    display_coordinates()
                    display_ship_alignment_of(current_player)
                    print(
                        "\nEnter Coordinates to place the ship :-Not valid!!! Try again🔁"
                    )
                    sleep(0.75)

        loc_avail, ship_area = is_loc_available(coords, ship_size, ship_align)
        if loc_avail:
            for i in ship_area:
                occupied_coordinates[current_player].append(i)
                ship_position_of[current_player][
                    str(np.array(i) - 1)
                ] = f" {ship_type} "

            break
        elif game_mode == 2 and current_player == player2:
            pass
        else:
            clrscr()
            display_current_player()
            print(
                f"Ship:- {chosen_ship.capitalize()} | Alignment:- {chosen_alignment.capitalize()} | Size:- {ship_sizes[ship_names_short[chosen_ship]]}"
            )
            display_coordinates()
            display_ship_alignment_of(current_player)
            print("\nEnter Coordinates to place the ship :-Not valid!!! Try again 🔁.")
            sleep(0.5)
    return coords


# call all the function which are required for the all kind of ship inputs
def ship_input():
    global ship_names_short
    while True:
        a = ship_Type_input()
        if a in ship_names_short.values():
            ship_coordinates_input(a, ship_alignment_input())
        else:
            clrscr()
            print("All ships of Both players are Placed!! Now Hit on others ship.💪")
            sleep(1)
            break


# function to displays hit miss user interface
def display_of_hitMiss():
    clrscr()
    print(
        f"\t\t{player1.capitalize()}: {hit_count[player1]} \t {player2.capitalize()}: {hit_count[player2]}\n"
    )
    display_coordinates()
    display_visual_for(player1)
    display_visual_for(player2)
    print()
    display_current_player()


# to add possible hit coordinates
def add_to_possible_hit(possible_hit, list_of_list):
    for elem in list_of_list:
        if is_list_an_element(valid_coordinates[current_player], elem):
            possible_hit.append(elem)


def run_hit_miss():
    while True:
        if (
            len(occupied_coordinates[current_player]) in hit_count.values()
        ):  # breaks the hit miss part if all occupied positions are hitted
            break

        validity_of_hit = False
        while not validity_of_hit:

            if (
                game_mode == 2 and current_player == player2
            ):  # checks if computer is playing
                count = 0
                for i in possible_hit[current_player]:
                    if i in attacked_at[current_player]:
                        count += 1
                if count == len(
                    possible_hit[current_player]
                ):  # if all possible hits are already attacked choose a random hit coordinates
                    hit_at = choice(remaining_position[opposite_player])
                else:
                    while True:
                        a = choice(
                            possible_hit[current_player]
                        )  # takes random from possible hit positions
                        if is_list_an_element(valid_coordinates[current_player], a):
                            hit_at = a
                            break
                validity_of_hit = True

            else:
                display_of_hitMiss()
                index = input("\nEnter coordinates to HIT the ship :-")
                if len(index.split()) == 2 and all(
                    char.isdigit() for char in index.split()
                ):
                    hit_at = index_to_coords(index)
                    validity_of_hit = is_list_an_element(
                        valid_coordinates[current_player], hit_at
                    )
                else:
                    print("Ahh!!! Not Valid, Try agian🔁")
                    sleep(0.75)
                    continue

            if validity_of_hit:
                if hit_at in occupied_coordinates[opposite_player]:
                    if hit_at not in hitted_ship_position_of[opposite_player]:
                        hitted_ship_position_of[opposite_player].append(hit_at)
                        visual_of_area_of[opposite_player][
                            str(np.array(hit_at) - 1)
                        ] = " X "
                        ship_position_of[opposite_player][
                            str(np.array(hit_at) - 1)
                        ] = " X "
                        hit_count[current_player] += 1
                        attacked_at[current_player].append(hit_at)
                        if hit_at in remaining_position[opposite_player]:
                            remaining_position[opposite_player].remove(hit_at)
                        x, y = hit_at
                        add_to_possible_hit(
                            possible_hit[current_player],
                            [[x - 1, y], [x + 1, y], [x, y - 1], [x, y + 1]],
                        )
                        if game_mode == 2 and current_player == player2:
                            display_of_hitMiss()
                            print(
                                "Enter Coordinates to HIT the ship :-Hitted ship!"
                            )
                            sleep(1)
                        else:
                            display_of_hitMiss()
                            print(
                                "Enter Coordinates to HIT the ship :-Hurray!!🥳 It is HIT."
                            )
                            sleep(0.75)
                    else:
                        if game_mode == 2 and current_player == player2:
                            display_of_hitMiss()
                            print(
                                "Enter Coordinates to HIT the ship :-Thinking of position."
                            )
                            sleep(0.1)
                        else:
                            display_of_hitMiss()
                            print("Enter Coordinates to HIT the ship :-ahh!!😒 Already Attacked!!")
                            sleep(0.75)
                        validity_of_hit = False
                        continue

                else:
                    if hit_at not in hitted_ship_position_of[opposite_player]:
                        hitted_ship_position_of[opposite_player].append(hit_at)
                        visual_of_area_of[opposite_player][
                            str(np.array(hit_at) - 1)
                        ] = " O "
                        ship_position_of[opposite_player][
                            str(np.array(hit_at) - 1)
                        ] = " O "
                        attacked_at[current_player].append(hit_at)
                        if hit_at in remaining_position[opposite_player]:
                            remaining_position[opposite_player].remove(hit_at)

                        if game_mode == 2 and current_player == player2:
                            display_of_hitMiss()
                            print(
                                "Enter Coordinates to HIT the ship :-Thinking of position."
                            )
                            sleep(0.1)
                        else:
                            display_of_hitMiss()
                            print(
                                "Enter Coordinates to HIT the ship :-ahhh!!😒 It is Miss."
                            )
                            sleep(0.75)
                    else:
                        if game_mode == 2 and current_player == player2:
                            display_of_hitMiss()
                            print(
                                "Enter Coordinates to HIT the ship :-Thinking of position."
                            )
                            sleep(0.1)
                        else:
                            display_of_hitMiss()
                            print(
                                "Enter Coordinates to HIT the ship :-ahhh!!😒 Already attacked."
                            )
                            sleep(0.75)
                        validity_of_hit = False
               
            else:
                display_of_hitMiss()
                print("Enter Coordinates to HIT the ship :-ahhh!!😒 Not in sea.")
                sleep(0.75)

        change_current_player()


# to declare winner
def declare_winner():
    global occupied_coordinates, hit_count
    if len(occupied_coordinates[player1]) == hit_count[player1]:
        clrscr()
        print(f"{player1} wins!!")
        print(f'Game Time : {round(time()-game_start_time)/60,2}min')
    else:
        clrscr()
        print(f"{player2} wins!!")
        print(f'Game Time : {round(time()-game_start_time)/60,2}min')


# to ask game mode (per)son vs person / person vs computer)
def ask_game_mode():
    global game_mode
    game_mode = 0
    while not game_mode:
        clrscr()
        a = input("Select Game Mode:-\n1)Person VS Person \n2)Person VS Computer. \t:-")
        if a.isdigit() and a in ["1", "2"]:
            game_mode = int(a)
        else:
            print("\nEnter a valid index of Game Mode.")


# to ask players their names
def ask_player_names():
    global player1, player2
    if game_mode == 2:
        player2 = "computer"
        player1 = input("\nEnter Player1 Name:-")
    else:
        player1 = input("\nEnter Player1 Name:-")
        player2 = input("\nEnter Player2 Name:-")


def start_game():
    ask_game_mode()
    ask_player_names()
    set_game()
    clrscr()
    print(f"NOW PLAYING : {current_player.capitalize()}")
    sleep(1)
    ship_input()
    run_hit_miss()
    declare_winner()
    sleep(2)
    clrscr()
    print("Game ends")


def main_game():
    global number_of_ships, occupied_coordinates
    clrscr()
    game_instructions()
    if not input("\nProceed ? (y/n) default y: -").lower() == "n":
        start_game()
        while True:  # to replay the game
            print("play again? (y/n) default n: ")
            if input().lower() == "y":
                clrscr()
                sleep(0.75)
                start_game()
            else:
                break
        print("Thanks for playing game!!")
        clrscr()
    else:
        clrscr()
        print("Game ends")


main_game()
