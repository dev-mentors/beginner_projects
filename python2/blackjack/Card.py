class Card(object):
    # suite C, H, S, D

    # rank 1-13


    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank

        score = -1

        if rank == 1:
            score = 11 or 1
        elif rank >= 10:
            score = 10
        else:
            score = rank

        self.score = score

    def __repr__(self):
        return self.suite + " " + str(self.rank) + " " + str(self.score)
