import handler_funcs


def main():
    while True:
        user_input = input('>>> ').lower()
        if '.' in user_input:
            break
        elif user_input == 'hello':
            print(handler_funcs.hello(user_input))
        elif user_input.startswith('add'):
            handler_funcs.add(user_input)
        elif user_input.startswith('change'):
            handler_funcs.change(user_input)
        elif user_input.startswith('phone'):
            handler_funcs.phone(user_input)
        elif user_input == 'show all':
            print(handler_funcs.show_all(user_input))
        elif user_input in ["good bye", "close", "exit"]:
            print(handler_funcs.close(user_input))
            break


if __name__ == '__main__':
    main()
