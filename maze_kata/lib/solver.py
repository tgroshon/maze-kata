def solve(maze):
    if not maze.data:
        return None

    strategy = DefaultStrategy()
    return strategy.solve(maze)


class DefaultStrategy:
    def solve(self, maze):
        """Basically a naive depth-first search

        This should always find the end space, but may not find the shortest path.

        Complexities:
          - Time: O(Vertices + Edges)
          - Space: O(Vertices)

        FIXME: Naively returning the 'visited' data structure doesn't work
        great for making a 'path', because it overreports steps for mazes with
        rooms or deadends. Refactor to return the pruned steps to end.

        FIXME: using a list for the `visited` data structure could make
        membership checks less efficient than a set.
        """
        start_space = maze.get_start_space()

        if maze.shape.rows == 1:
            return [start_space]

        visited = []
        stack = [start_space]
        self.fill_deadends(maze)

        while len(stack):
            address = stack.pop()

            if address not in visited:
                visited.append(address)

            if maze.is_end(address):
                """Break the loop we're done!"""
                break

            for neighbor in maze.get_adjacent_spaces(address):
                if neighbor not in visited:
                    stack.append(neighbor)

        return visited

    def fill_deadends(self, maze):
        """Fill dead-ends so that they cannot be followed

        NOTE: can be a costly operation. Consider breaking out into a separate
        strategy.
        """
        visited = set()
        stack = [cell for cell in maze.cell_iter() if maze.is_deadend(cell)]

        while len(stack):
            address = stack.pop()

            neighbors = maze.get_adjacent_spaces(address)
            if len(neighbors) == 1:
                stack.append(neighbors[0])

            if maze.is_deadend(address):
                maze.fill_space(address)
