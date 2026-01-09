from ortools.sat.python import cp_model
import time


def solve_nqueens_csp(n):
    start_time = time.time()

    model = cp_model.CpModel()
    queens = [model.NewIntVar(0, n - 1, f"Q{i}") for i in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            model.Add(queens[i] != queens[j])
            model.AddAbsEquality(
                model.NewIntVar(0, n, ""),
                queens[i] - queens[j]
            )
            model.Add(abs(i - j) != abs(queens[i] - queens[j]))

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        solution = [solver.Value(q) for q in queens]
        return {
            "solution": solution,
            "time": time.time() - start_time,
            "branches": solver.NumBranches(),
            "conflicts": solver.NumConflicts()
        }

    return None
