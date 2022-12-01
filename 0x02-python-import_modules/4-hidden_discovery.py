#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for str in dir(hidden_4):
        if str[:2] != '__':
            print(str)
