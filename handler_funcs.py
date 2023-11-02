phone_directory = {}


def input_error(func):
    def inner(string):

        if func.__name__ == 'add':
            try:
                if len(string.split()) != 3:
                    raise IndexError
                func(string)
            except IndexError:
                print('Input must consist of "add", "name" and "contact number"')
            except ValueError:
                print(f'"{string.split()[2]}" is not a contact number.')
            except KeyError:
                print(f"Contact '{string.split()[1]}' already exists.")

        elif func.__name__ == 'phone':
            try:
                if len(string.split()) != 2:
                    raise IndexError
                print(func(string))
            except IndexError:
                print('Input must consist of "phone" and "name".')
            except KeyError:
                print(f'"{string.split()[1]}" is not in the phone directory.')

        elif func.__name__ == 'change':
            try:
                if len(string.split()) != 3:
                    raise IndexError
                func(string)
            except IndexError:
                print('Input must consist of "change", "name" and "contact number".')
            except ValueError:
                print(f'"{string.split()[2]}" is not a contact number.')
            except KeyError:
                print(f'"{string.split()[1]}" is not in phone directory.')
    return inner


@input_error
def add(string):
    name, number = string.split()[1], string.split()[2]
    if name not in phone_directory:
        phone_directory.update({name: int(number)})
    else:
        raise KeyError


@input_error
def change(string):
    name, number = string.split()[1], string.split()[2]
    if name in phone_directory:
        phone_directory[name] = int(number)
    elif name not in phone_directory:
        raise KeyError


@input_error
def phone(string):
    number = string.split()[1]
    return phone_directory[number]


def show_all(string):
    return phone_directory


def hello(string):
    return 'How can I help you?'


def close(string):
    return 'Good bye!'
