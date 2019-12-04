from context import UseDatabase

config = {}
config["dbconfig"] = {
    "host": "127.0.0.1",
    "user": "vsearch",
    "password": "hello",
    "database": "vsearchlogDB",
}


def view_the_log() -> str:
    """ Display the content of the log file as a HTML Table"""
    print("Before with statement")
    with UseDatabase(config["dbconfig"]) as cursor:
        print("inside with statement")
        _SQL = """select phrase, letters, ip, browser_string, results from log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()

    for content in contents:
        print(content)


if __name__ == "__main__":
    view_the_log()
