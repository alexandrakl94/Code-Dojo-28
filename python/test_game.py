"A test suite for a Three Men's Morris game"
from .game import Game
import mock

import unittest
  

def test_new_game_starts_with_valid_default_values():
  # act
  my_game = Game()

  # assert
  assert my_game.rows == 3
  assert my_game.columns == 3
  assert my_game.state == []
  assert my_game.whiteCount == 3
  assert my_game.blackCount == 3


def test_should_return_a_valid_piece():
  # act
  piece = Game.createPiece(x=1, y=2, isWhite=True)
 
  # assert
  assert piece == { 
    "x": 1,
    "x_original": 1,
    "y": 2,
    "y_original": 2,
    "isWhite": True
  }


def test_place_should_append_an_item_to_the_state():
  # arrange
  my_game = Game()
  
  # act
  my_game.place(x=2, y=1, isWhite=False)

  # assert
  assert len(my_game.state) == 1
  assert my_game.state[0]['x'] == 2
  assert my_game.state[0]['y'] == 1
  assert my_game.state[0]['isWhite'] == False
  

def test_place_should_decrement_white_count():
  # arrange
  my_game = Game()
  
  # act
  my_game.place(x=2, y=1, isWhite=True)

  # assert
  assert my_game.whiteCount == 2
  assert my_game.blackCount == 3
  

def test_place_should_decrement_black_count():
  # arrange
  my_game = Game()
  
  # act
  my_game.place(x=2, y=1, isWhite=False)

  # assert
  assert my_game.blackCount == 2
  assert my_game.whiteCount == 3
  

def test_has_piece_left_should_return_true_when_white_count_above_0():
  # arrange
  my_game = Game()
  my_game.whiteCount = 2
  
  # act
  hasPiece = my_game.hasPieceLeft(isWhite=True)

  # assert
  assert hasPiece == True
  

def test_has_piece_left_should_return_true_when_black_count_above_0():
  # arrange
  my_game = Game()
  my_game.blackCount = 2
  
  # act
  hasPiece = my_game.hasPieceLeft(isWhite=False)

  # assert
  assert hasPiece == True
  

def test_has_piece_left_should_return_false_when_black_count_equals_0():
  # arrange
  my_game = Game()
  my_game.blackCount = 0
  
  # act
  hasPiece = my_game.hasPieceLeft(isWhite=False)

  # assert
  assert hasPiece == False
  

def test_has_piece_left_should_return_false_when_white_count_equals_0():
  # arrange
  my_game = Game()
  my_game.whiteCount = 0
  
  # act
  hasPiece = my_game.hasPieceLeft(isWhite=True)

  # assert
  assert hasPiece == False


def read_input(question):
  print(question)

  if question == 'White player turn (x):':
      return '1 1'
  elif question == 'Black player turn (#):':
      return '1 2'
  elif question == 'Do you want to continue? (Y/n)':
      return 'n'
  else:
    return ''


# TODO: change code to make sure we can exit a loop
# 1. ask user if he she wants to exit
 
class TestNotMockedFunction(unittest.TestCase):
    def test_should_stop_after_one_turn(self):
        
        # arrange
        my_game = Game(read_input)

        # act
        my_game.start()

        # assert
        assert len(my_game.state) == 2

        assert my_game.state[0]['x'] == 0
        assert my_game.state[0]['y'] == 0
        assert my_game.state[0]['isWhite'] == True

        assert my_game.state[1]['x'] == 0
        assert my_game.state[1]['y'] == 1
        assert my_game.state[1]['isWhite'] == False
        
        assert my_game.status == 'stopped'


if __name__ == '__main__':
    unittest.main()
  