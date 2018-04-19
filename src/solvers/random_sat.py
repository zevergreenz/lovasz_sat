from collections import defaultdict
from sys import stderr
import secrets

def solve(instance):
    """
    Random Sat Solver (naive trial-and-error algorithm).
    We keep generating a random assignment until we obtain one valid assignment.
    """
    values = [0, 1]

    # Start with a random assignment for all variables.
    assignment = [secrets.choice(values) for _ in range(len(instance.variables))]
    num_clauses = len(instance.clauses)
    for i in range(1000000 * num_clauses):
        # Check if any clause is violated.
        violated_clause = None
        for clause in instance.clauses:
            satisfy = False
            for number in clause:
                var = number >> 1
                neg = number & 1
                if assignment[var] != neg:
                    satisfy = True
                    break
            if not satisfy:
                violated_clause = clause
                break
        if violated_clause == None:
            # print('Terminate after %d iterations' % (i+1))
            return [assignment, i+1]
        else:
            # Uniformly reassign all variables
            assignment = [secrets.choice(values) for _ in range(len(instance.variables))]
    return [None, i+1]