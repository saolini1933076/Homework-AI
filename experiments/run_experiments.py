from astar.problem import NQueensProblem
from astar.astar import astar_search
from astar.heuristics import conflict_heuristic
from csp.nqueens_csp import solve_nqueens_csp

import csv


def run():
    ns = [4, 6, 8, 10, 12]

    with open("results.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            "Algorithm", "N", "Time",
            "Expanded", "Generated", "MaxFrontier",
            "Branches", "Conflicts"
        ])

        for n in ns:
            print(f"Running A* for n={n}")
            problem = NQueensProblem(n)
            result = astar_search(problem, conflict_heuristic)

            writer.writerow([
                "A*",
                n,
                result["time"],
                result["expanded"],
                result["generated"],
                result["max_frontier"],
                "", ""
            ])

            print(f"Running CSP for n={n}")
            csp_result = solve_nqueens_csp(n)

            writer.writerow([
                "CSP",
                n,
                csp_result["time"],
                "", "", "",
                csp_result["branches"],
                csp_result["conflicts"]
            ])


if __name__ == "__main__":
    run()
