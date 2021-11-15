def solve(maze):
    if not maze.data:
        return None

    strategy = DefaultStrategy()
    return strategy.solve(maze)


class DefaultStrategy:
    def solve(self, maze):
        if maze.shape.rows == 1:
            idx = maze.get_row(1).index(True)
            if not idx:
                return None

            return [[1, idx + 1]]

        return None


def get_row(data, row_num):
    if row_num <= 0:
        raise Exception(f"Rows are 1-based, got: {row_num}")

    return data[row_num - 1]
