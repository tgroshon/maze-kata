from collections import deque


def solve(maze, strategy=None):
    if not maze.data:
        return None

    if strategy is None:
        strategy = DefaultStrategy()

    return strategy.solve(maze)


def _drop_keys_from_dict(keys, d):
    for k in keys:
        d.pop(k)
    return d


class ImprovedStrategy:
    def solve(self, maze):
        """Improved DFS Search"""
        start_space = maze.get_start_space()

        if maze.shape.rows == 1:
            return [start_space]

        visited = {}  # as of CPython3.6, dicts maintain key insertion order
        stack = deque([start_space])
        branch_steps = []
        route = {}

        while len(stack):
            address = stack.pop()

            branch_steps.append(address)

            if address not in visited:
                route[address] = None
                visited[address] = None

            if maze.is_end(address):
                """Break the loop we're done!"""
                break

            if maze.is_deadend(address):
                _drop_keys_from_dict(branch_steps, route)
                branch_steps.clear()

            if maze.is_branch(address):
                branch_steps.clear()

            for neighbor in maze.get_adjacent_spaces(address):
                if neighbor not in visited:
                    stack.append(neighbor)

        end_space = maze.get_end_space()
        if end_space not in route:
            return None

        return list(route)


class DefaultStrategy:
    def solve(self, maze):
        """Basically a naive depth-first search

        This should always find the end space, but may not find the shortest path.

        Complexities:
          - Time: O(Vertices + Edges)
          - Space: O(Vertices)

        NOTE: Naively returning the 'visited' data structure works here because
        we first fill all the dead-ends so that only valid paths remain. So
        every visited node of depth-first search will be a valid step.
        """
        start_space = maze.get_start_space()

        if maze.shape.rows == 1:
            return [start_space]

        visited = {}  # as of CPython3.6, dicts maintain key insertion order
        stack = deque([start_space])
        self.fill_deadends(maze)

        while len(stack):
            address = stack.pop()

            if address not in visited:
                visited[address] = None

            if maze.is_end(address):
                """Break the loop we're done!"""
                break

            for neighbor in maze.get_adjacent_spaces(address):
                if neighbor not in visited:
                    stack.append(neighbor)

        end_space = maze.get_end_space()
        if end_space not in visited:
            return None

        return list(visited)

    def fill_deadends(self, maze):
        """Fill dead-ends so that they cannot be followed

        NOTE: Can be a costly operation. Consider breaking out into a separate
        strategy.
        """
        stack = deque([cell for cell in maze.cell_iter() if maze.is_deadend(cell)])

        while len(stack):
            address = stack.pop()

            neighbors = maze.get_adjacent_spaces(address)
            if len(neighbors) == 1:
                stack.append(neighbors[0])

            if maze.is_deadend(address):
                maze.fill_space(address)
