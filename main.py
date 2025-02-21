import duckdb


def main():
    print("Hello from vscode-ide!")
    get_fake_data()


def get_fake_data():
    fake_data = duckdb.sql(query="select 1").fetchall()
    for f_data in fake_data:
        print(f_data, type(f_data), f_data[0], len(f_data))
    return fake_data


def some_function(some_input_param_1: int, param_2: str) -> str:
    return param_2 * some_input_param_1  


if __name__ == "__main__":
    main()
