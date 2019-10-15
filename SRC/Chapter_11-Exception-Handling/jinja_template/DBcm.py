import mysql.connector


class ConnectionError(Exception):
    pass


class CredentialsError(Exception):
    pass


class UseDatabase:
    # this method performs initialization
    def __init__(self, config: dict) -> None:
        self.configuration = config

    # this method add's the setup code
    def __enter__(self) -> "cursor":
        try:
            self.conn = mysql.connector.connect(**self.configuration)
            self.cursor = self.conn.cursor()
            return self.cursor
        except mysql.connector.errors.InterfaceError as err:
            raise ConnectionError(err)
        except mysql.connector.errors.ProgrammingError as err:
            raise CredentialsError(err)

    # https://stackoverflow.com/questions/1984325/explaining-pythons-enter-and-exit
    # this method hold's the teardown code.
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.conn.commit()
        self.cursor.close()
        self.conn.close()
