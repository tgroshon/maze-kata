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

        return None
