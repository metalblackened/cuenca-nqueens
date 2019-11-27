# content of test_class.py
from ga import create_chromosome, fitness, mutate, crossover
import copy

class TestClass:
    def test_chromosome_size(self):
        c1 = create_chromosome(1)
        c4 = create_chromosome(4)
        assert len(c1) == 1
        assert len(c4) == 4
    
    def test_mutate(self):
        c1 = create_chromosome(6)
        c2 = create_chromosome(7)
        c3 = create_chromosome(8)

        assert mutate(copy.deepcopy(c1)) != c1
        assert mutate(copy.deepcopy(c2)) != c2

    
    def test_crossover(self):
        c1 = [1,2,3,4,2,6]
        c2 = [6,5,3,4,2,6]

        child = crossover(c1,c2)
        assert child[2:] == [3,4,2,6]
        



    
        



