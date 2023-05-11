from utility_func import input_error, hello_user, add_user, change_phone, show_phone, unknown_command, input_error, goodbye

HANDLERS = {
    'hello': hello_user,
    'add': add_user,
    'change': change_phone,
    'show': show_phone,
    'exit': goodbye,
    'good bye': goodbye,
    'close': goodbye
}

@input_error
def main():
    while True:
        user_input = input('Please enter command or command and args: ')
        command, *args = user_input.strip().split(' ', 1)

        if HANDLERS.get(command):
            handler = HANDLERS.get(command.lower())
            if args:
                args = args[0].split(' ')
        else:
            handler = HANDLERS.get(command.lower(),unknown_command(command))
        result = handler(*args)
        if result is None:
            break
        else:
            print(result)

if __name__ == '__main__':
    main()