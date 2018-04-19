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

    watcher = defaultdict(set)
    for i, clause in enumerate(instance.clauses):
        for number in clause:
            var = number >> 1
            watcher[var].add(i)

    # Start with a random assignment for all variables.
    assignment = [secrets.choice(values) for _ in range(len(instance.variables))]
    modified_var = None
    for iteration in range(1000000 * num_clauses):
        # Optimization: We only look at the clauses which contains modified variables.
        violated_clause = None
        modified_clauses_idx = range(num_clauses)
        if modified_var != None:
            modified_clauses_idx = set()
            for var in modified_var:
                modified_clauses_idx = modified_clauses_idx.union(watcher[var])

        # Find the first violated clause.
        for clause_idx in modified_clauses_idx:
            clause = instance.clauses[i]
            satisfy = True
            for number in clause:
                var = number >> 1
                neg = number & 1
                if assignment[var] != neg:
                    satisfy = False
                    break
            if not satisfy:
                violated_clause = clause
                break

        if violated_clause == None:
            print('Terminate after %d iterations' % iteration)
            return [assignment]
        else:
            # Resample the variable in the violated clause.
            modified_var = []
            for number in clause:
                var = number >> 1
                new_val = secrets.choice(values)
                if new_val != assignment[var]:
                    assignment[var] = new_val
                    modified_var.append(var)
    return []