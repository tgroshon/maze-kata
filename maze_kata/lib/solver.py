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

        """
        start_space = maze.get_start_space()

        if maze.shape.rows == 1:
            return [start_space]

        visited = []
        stack = [start_space]

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
