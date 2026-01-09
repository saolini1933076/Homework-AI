import heapq
import time

class Node:
    def __init__(self, state, parent=None, g=0, h=0):
        self.state = state
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f


def astar_search(problem, heuristic):
    start_time = time.time()

    start_state = problem.initial_state()
    start_node = Node(start_state, g=0, h=heuristic(start_state))

    frontier = []
    heapq.heappush(frontier, start_node)
    explored = set()

    expanded = 0
    generated = 1
    max_frontier = 1

    while frontier:
        max_frontier = max(max_frontier, len(frontier))
        node = heapq.heappop(frontier)

        if problem.is_goal(node.state):
            return {
                "solution": reconstruct_path(node),
                "expanded": expanded,
                "generated": generated,
                "max_frontier": max_frontier,
                "time": time.time() - start_time
            }

        explored.add(node.state)
        expanded += 1

        for action in problem.actions(node.state):
            child_state = problem.result(node.state, action)

            if not problem.is_valid(child_state):
                continue

            if child_state in explored:
                continue

            child_node = Node(
                child_state,
                parent=node,
                g=node.g + problem.cost(node.state, action),
                h=heuristic(child_state)
            )

            heapq.heappush(frontier, child_node)
            generated += 1

    return None


def reconstruct_path(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return list(reversed(path))
