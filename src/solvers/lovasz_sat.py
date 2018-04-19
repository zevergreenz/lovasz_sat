from collections import defaultdict
from sys import stderr
import secrets

def solve(instance, watchlist, assignment, d, verbose):
    """
    Algorithmic Sequential Solver (from the constructive Lovasz Local Lemma paper).
    We start with a random assignment for all variables. Then, we find the first violated 
    clause, and resample the variables in that clause (assigning a new values to each of
    them independently and uniformly at random). We repeat the process until we find a valid
    assignment.
    """
    values = [0, 1]
    num_clauses = len(instance.clauses)

    # Start with a random assignment for all variables.
    assignment = [secrets.choice(values) for _ in range(len(instance.variables))]
    modified_var = None
    for iteration in range(1000000 * num_clauses):
        # Find the first violated clause.
        violated_clause = None
        for clause in instance.clauses:
            if not is_satisfied(clause, assignment):
                violated_clause = clause
                break

        if violated_clause == None:
            print('Terminate after %d iterations' % iteration)
            return [assignment]
        else:
            # Resample the variable in the violated clause.
            # Optimization: We keep resampling this clause until it is satisfied.
            while not is_satisfied(violated_clause, assignment):
                modified_var = []
                for number in violated_clause:
                    var = number >> 1
                    new_val = secrets.choice(values)
                    if new_val != assignment[var]:
                        assignment[var] = new_val
                        modified_var.append(var)
    return []

def is_satisfied(clause, assignment):
    for number in clause:
        var = number >> 1
        neg = number & 1
        if assignment[var] != neg:
            return True
    return False