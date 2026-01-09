class NQueensProblem:
    def __init__(self, n):
        self.n = n

    def initial_state(self):
        return tuple()

    def is_goal(self, state):
        return len(state) == self.n and self.is_valid(state)

    def actions(self, state):
        row = len(state)
        for col in range(self.n):
            yield col

    def result(self, state, action):
        return state + (action,)

    def cost(self, state, action):
        return 1

    def is_valid(self, state):
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if state[i] == state[j]:
                    return False
                if abs(state[i] - state[j]) == abs(i - j):
                    return False
        return True
