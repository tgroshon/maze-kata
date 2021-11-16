def solve(maze):
    if not maze.data:
        return None

    strategy = DefaultStrategy()
    return strategy.solve(maze)


class DefaultStrategy:
    def solve(self, maze):
        if maze.shape.rows == 1:
            return maze.get_start_space()

        return None
