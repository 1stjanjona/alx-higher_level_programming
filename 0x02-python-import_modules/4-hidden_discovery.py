#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    for hide in dir(hidden_4):
        if hide[:2] != "__":
            print(hide)
