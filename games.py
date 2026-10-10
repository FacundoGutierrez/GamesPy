path = "data.txt"

def listGames(path):
    formated_games = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                if not line.strip():
                    continue
                # print(f"{line.strip()}, raw line")
                game_info = line.strip().split(';')
                game_info[1] = game_info[1].title()
                game_info[3]= game_info[3].upper()
                print(f"ID: {game_info[0]}, Titulo: {game_info[1]}, Estudio: {game_info[2]}, Genero: {game_info[3]}")
            
    except FileNotFoundError:
        print("No games found. The file 'games.txt' does not exist.")
def gamesByTitle(path, game_name):
    game_name_query = game_name.strip().casefold() 
    outpath = "exit.txt"
    game_found = []
    if not game_name_query:
        print("must enter a game name or part of it")
    try:
        with open(path, 'r', encoding='utf-8') as file, open(outpath, 'w', encoding='utf-8') as exitFile:
            exitFile.write(f"Queries done by the user: {game_name_query}\n")
            for line in file:
                if not line.strip():
                    continue
                game_line = line.strip().split(';')

                if game_line[1] == '':
                    print(f"line has no game name {line}")
                    continue
                title = game_line[1].strip()
                if game_name_query in title.casefold():
                    game_found.append(game_line)
                    exitFile.write(line)
            for game in game_found: 
                print(f"Game: {game}")
                 
    except FileNotFoundError:
        print("No games found. The file doesnt exist.")
    
# def orderGamesByDescPrices(path):
#     pivot = 0
#     try:
#         with open(path, 'r', encoding='utf-8') as file:
#             for line in file:
#                 if not line.strip():
#                     continue
#             game_price = line[4]
#             if game_price > line



             



# listGames(path)
gamesByTitle("data.txt", 'craft')