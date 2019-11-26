from sqlalchemy import Column, String, Integer, Date

from base import Base


class SolutionModel(Base):
    __tablename__ = 'solutions'

    id = Column(Integer, primary_key=True)
    n_queens = Column(Integer)
    solution = Column(String)

    def __init__(self, n_queens, solution):
        self.n_queens = n_queens
        self.solution = solution