from sys import stderr
import secrets

def solve(instance, watchlist, assignment, d, verbose):
    """
    Recursively solve SAT by assigning to variables d, d+1, ..., n-1. Assumes
    variables 0, ..., d-1 are assigned so far. A generator for all the
    satisfying assignments is returned.
    """
    values = [0, 1]
    # Start with a random assignment for all variables.
    assignment = [secrets.choice(values) for _ in range(len(instance.variables))]
    print(instance.clauses)
    for _ in range(1000000):
        print(assignment)
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
            return [assignment]
        else:
            # Resample the variable in the violated clause.
            for number in clause:
                var = number >> 1
                assignment[var] = secrets.choice(values)
    return []