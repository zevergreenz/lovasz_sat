from collections import defaultdict
from sys import stderr
import secrets

def solve(instance):
    """
    Algorithmic Sequential Solver (from the constructive Lovasz Local Lemma paper).
    We start with a random assignment for all variables. Then, we find the first violated 
    clause, and resample the variables in that clause (assigning a new values to each of
    them independently and uniformly at random). We repeat the process until we find a valid
    assignment.
    """
    values = [0, 1]

    # Start with a random assignment for all variables.
    assignment = [secrets.choice(values) for _ in range(len(instance.variables))]
    num_clauses = len(instance.clauses)
    for i in range(1000000 * num_clauses):
        # Find the first violated clause.
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
            print('Terminate after %d iterations' % i)
            return [assignment]
        else:
            # Uniformly reassign all variables
            assignment = [secrets.choice(values) for _ in range(len(instance.variables))]
    return []