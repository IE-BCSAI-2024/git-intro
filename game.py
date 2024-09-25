from typing import Self
from game.backgammonboard import BackgammonBoard
from game.dice import Dice
from game.piece import Piece
import pygame

#this class represents the players in the Backgammon game
class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.pieces_off_board = 0 

# Here initalise the pieces onto the fields on the board in init

class Game:
    def __init__(self):
        self.board = BackgammonBoard()
        self.dice = Dice()
        self.players = [Player("Player 1", "white"), Player("Player 2", "black")]
        self.current_player_index = 0  # Index of the current player in the 'players' list
        self.player1_pieces_off_board = 0 
        self.player2_pieces_off_board = 0
        self.game_over = False
        self.points = []
        self.positions = []
        self.center_stacks = {}

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index

    def startGame(self):
        #put button here
        Player1_score = Dice.roll()
        player2_score = Dice.roll()
        if Player1_score > player2_score:
            self.current_player_index = 0
        else:
            self.current_player_index = 1

    def move_options(self):
        move_option_1 = Dice.roll()
        move_option_2 = Dice.roll()
        move_option_3 = move_option_1 + move_option_2
        move = input("Would you like to move the first die, second die, or both?") #change this to be determined by the dragging movement
        original = 0 #this represents the starting stack
        new = original + move #where move represents the dice selection quantity 
        #the error cases in which the user isn't able to move
        if len(self.positions[original]) == 0: #if there is nothing in the stack to draw from
            print("There is nothing to move")
        elif self.players[self.current_player_index].color != self.positions[original].peek().colour: #if the player tries to draw from the other player's stack
            print("This is not your stack to move from")
        elif len(self.positions[new]) > 1 and self.players[self.current_player_index].color != self.positions[new].peek().colour: #if the player tries to move into the other player's stack
            print("This is not your stack to move into")
        elif len(self.positions[new]) == 1 and self.players[self.current_player_index].color != self.positions[new].peek().colour: #circleCollide
            remove_piece()
            #append to center stack
        else:
            add_piece(new, remove_piece(original))
        

    def initalise_pieces(self):
        # Define the starting position of all the pieces on the board
        # Backgammon has specific starting positions for the pieces.
        self.positions = {
            # Points are listed for the white player. For black, the points are mirrored.
            1: [Piece('white') for _ in range(2)],  # white's 24-point
            6: [Piece('black') for _ in range(5)],  # black's 19-point
            8: [Piece('black') for _ in range(3)],  # black's 17-point
            12: [Piece('white') for _ in range(5)],  # white's 13-point
            13: [Piece('black') for _ in range(5)],  # black's 12-point
            17: [Piece('white') for _ in range(3)],  # white's 8-point
            19: [Piece('white') for _ in range(5)],  # white's 6-point
            24: [Piece('black') for _ in range(2)],  # black's 1-point
        }

        # Ensure all points have a list to avoid key errors
        for point in range(1, 25):
            if point not in self.positions:
                self.positions[point] = []
    
        return self.positions
    
    def add_piece(self, point, piece: Piece): 
        self.points[point].append(piece)

    def remove_piece(self, point):
        return self.points[point].pop() if self.points[point] else None
    
    #only if we know the user wants to move the piece off the board... users must roll the dice first
    def final_counter(self):
        sum_0 = 0
        sum_1 = 0
        player0_pieces_off_board = 0
        player1_pieces_off_board = 0
        for i in range(18,24):
            if len(self.positions[i]) > 0 and self.players[0].color == self.positions[i].peek().colour:
                sum_0 = sum_0 + len(self.positions[i])
        if sum == 15:
            remove_piece()#point

        for i in range(6):
            if len(self.positions[i]) > 0 and self.players[1].color:
                sum_1 = sum_1 + len(self.positions[i])
        if sum == 15:
            #start popping and appending to a new list off the board
            print("delete this")

    #if the user selects to move off the board
    def game_over(self):
        if self.player1_pieces_off_board == 15:
            print("Player 1 wins")
            self.game_over = True
        if self.player2_pieces_off_board == 15:
            print("Player 2 wins")
            self.game_over = True
            
