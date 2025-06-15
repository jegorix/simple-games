
class Board:

    def __init__(self):
        self.field = []
    
    def draw_field(self):
        self.field = [Cell(i) for i in range(9)]

        
    def show_field(self):
        print("_________")
        for i in range(0,9,3):
            print(f"{self.field[i].symbol} | {self.field[i+1].symbol} | {self.field[i+2].symbol}")
            print("_________")
    
    def change_status(self, number, symbol):
        if not self.field[number].status:
            self.field[number].status = True
            self.field[number].symbol = symbol
            return True
        print(f"Cell-{number + 1} was filled.")
        return False
    
    
    def check_winner(self):
        for i in range(0, 9, 3):
            if (self.field[i].symbol == self.field[i+1].symbol == self.field[i+2].symbol) and self.field[i].status:
                return True
            
        for i in range(3):
            if (self.field[i].symbol == self.field[i+3].symbol == self.field[i+6].symbol) and self.field[i].status:
                return True
            
        if (self.field[0].symbol == self.field[4].symbol == self.field[8].symbol) and self.field[i].status:
            return True
        
        if (self.field[2].symbol == self.field[4].symbol == self.field[6].symbol) and self.field[i].status:
            return True
        
        if all(cell.status for cell in self.field):
            return 'draw'
        
        
        return False
            
    
    
    
    
class Cell:
    def __init__(self, number):
        self.number = number
        self.status = False
        self.symbol = ' '

          
      
            
class Player:
    def __init__(self, name, symbol):
        self.user_symbol = symbol
        self.name = name
        self.wins = 0
    
    def make_move(self):
        while True:
            try:
                move = int(input(f"{self.name} ({self.user_symbol}), enter number of cell (1-9): "))
                if move < 1 or move > 9:
                    raise ValueError
                return move-1
            except ValueError:
                print("Error! Wrong input!")
     
     
     
     
     
                           
class Game:
    def __init__(self, players, field):
        self.game_status = True
        self.players = players
        self.game_field = field
    
    def execute_move(self, player):
        while True:
            cell_number = player.make_move()
            if self.game_field.change_status(cell_number, player.user_symbol):
                break
            
        result = self.game_field.check_winner()
        self.game_field.show_field()
        
        if result is True:
            print(f"\nPlayer {player.name} wins!")
            player.wins += 1
            return True
        
        elif result == 'draw':
            print("Draw")
            return True
        
        return False
    
    def game_running(self):
        running = True
        while running:
            for player in self.players:
                if self.execute_move(player):
                    return
        
    
    def game_start(self):
        self.game_field.draw_field()
        self.game_field.show_field()
        self.game_running()
        
            

player_1 = Player('Thomas', 'X')
player_2 = Player('Jane', 'O')

players = [player_1, player_2]
board_1 = Board()

game = Game(players, board_1)
game.game_start()