from chess_board import ChessBoard
from lfu import LFUCache


def lfu_run():
    lfu_cache = LFUCache(4)

    lfu_cache.set('1', 1)
    lfu_cache.set('2', 2)
    lfu_cache.set('3', 3)
    lfu_cache.set('4', 4)

    print(lfu_cache.get('1'))
    print(lfu_cache.get('2'))
    print(lfu_cache.get('3'))

    lfu_cache.set('5', 5)
    print(lfu_cache.get('5'))
    print(lfu_cache.get('4'))

    lfu_cache.set('6', 6)

    print(lfu_cache.get('6'))


def chess_board():
    n = 3
    bishops = [(0, 1), (1, 0), (1, 2)]
    board = ChessBoard(n, bishops)
    print(board.number_of_bishops_killed())


if __name__ == '__main__':
    # lfu_run()
    chess_board()
