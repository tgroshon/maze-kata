def solve(maze):
    if not maze.data:
        return None

    strategy = DefaultStrategy()
    return strategy.solve(maze)


class DefaultStrategy:
    def solve(self, maze):
        start_space = maze.get_start_space()

        if maze.shape.rows == 1:
            return [start_space]

        visited = []
        self.search(visited, maze, start_space)
        return visited

    def search(self, visited, maze, address):
        """Basically a naive depth-first search

        This will always find the end space. The 'stack' is implicitly the (a)
        adjacent space iteration and (b) the python frame stack.

        Complexities:
          - Time: O(Vertices + Edges)
          - Space: O(Vertices)

        FIXME: Naively returning the 'visited' data structure doesn't work for
        making a 'path', so it will give the wrong answer for mazes with rooms
        or deadends. Refactor to return the pruned steps to get to the end.

        """
        visited.append(address)
        if maze.is_end(address):
            return

        for neighbor in maze.get_adjacent_spaces(address):
            if neighbor not in visited:
                self.search(visited, maze, neighbor)
