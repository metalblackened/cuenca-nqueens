from models import SolutionModel
from base import Session

def get_or_create_solution(n_queens,solution):
    session = Session()
    sol = session.query(SolutionModel).filter_by(solution = ";".join(str(v) for v in solution)).first()
    if sol:
        return sol
    else:
        sol = SolutionModel(n_queens = n_queens,solution = ';'.join(str(v) for v in solution))
        session.add(sol)
        session.commit()
        return sol 