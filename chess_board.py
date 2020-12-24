
class ChessBoard:

    def __init__(self, size, bishops_pos_list):
        self.size = size
        self.bishops_pos_list = bishops_pos_list

    def number_of_bishops_killed(self):
        killed = [False]*self.size
        for i in range(self.size):
            if not killed[i]:
                for j in range(i+1, self.size):

                    a, b = self.bishops_pos_list[i]
                    c, d = self.bishops_pos_list[j]

                    if abs(a-c) == abs(b-d):
                        killed[j] = True

        return sum(killed)
