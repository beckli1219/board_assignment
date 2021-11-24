import pytest
from board import Board

def test_mark_o():
    board = Board()
    board.mark_square([0, 0])
    assert board.squares == [
        ["O", None, None],
        [None, None, None],
        [None, None, None],
    ]
    
# YOUR CODE HERE
def test_mark_o_then_x():
    board = Board()
    board.mark_square([0,0])
    board.mark_square([1,1])
    assert board.squares == [
        ["O", None, None],
        [None, "X", None],
        [None, None, None],
    ]


def test_empty_board():
    board = Board()
    assert board.squares == [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]





def test_cannot_mark_a_square_twice():
    board = Board()
    board.mark_square([1,1])
    with pytest.raises(ValueError):  
        board.mark_square([1,1])