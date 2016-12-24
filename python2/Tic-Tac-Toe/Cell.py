class Cell(object):

    def __init__(self):
        self.mark = None
    """
    allows X or O to be passed in
    """
    def mark_cell(self, mark):
        self.mark = mark

    def __repr__(self):
        if self.mark is None:
            return str(" ")
        else:
            return self.mark
