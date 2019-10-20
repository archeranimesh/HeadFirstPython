import mysql.connector


class UseDatabase:
    # this method performs initialization
    def __init__(self, config: dict) -> None:
        self.configuration = config

    # this method add's the setup code
    def __enter__(self) -> "cursor":
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor

    # https://stackoverflow.com/questions/1984325/explaining-pythons-enter-and-exit
    # this method hold's the teardown code.
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
