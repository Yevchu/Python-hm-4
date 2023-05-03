from utility_func import hello_user, add_user, change_phone, show_all, show_phone, unknown_command, input_error, goodbye

HANDLERS = {
    'hello': hello_user,
    'add': add_user,
    'change': change_phone,
    'show all': show_all,
    'phone': show_phone,
    'exit': goodbye,
    'good bye': goodbye,
    'close': goodbye
}
@input_error
# def parse_input(user_input):
#     command, *args = user_input.strip().split(' ', 1)



#     handler = HANDLERS.get(command.lower(), unknown_command)
    # try:
    #     handler = HANDLERS[command.lower()]
    # except KeyError:
    #     if args:
    #         command = command + ' ' + args[0]
    #         args = args[1:]
    #     handler = HANDLERS.get(command.lower(), unknown_command)
#     return handler, args

def main():
    while True:
        user_input = input('Please enter command or command and args: ')
        command, *args = user_input.strip().split(' ', 1)

        if HANDLERS.get(command):
            handler = HANDLERS.get(command.lower())
            if args:
                args = args[0].split(' ')
        else:
            if HANDLERS.get(command) is None:
                command = command + ' ' + args[0]
                handler = HANDLERS.get(command.lower())
            handler = HANDLERS.get(command.lower(),unknown_command(command))
        result = handler(*args)
        if result is None:
            break
        else:
            print(result)
        # try:
        #     result = handler(*args)
        #     if not result:
        #         break
        #     print(result)
        # except TypeError:
        #     print("Give me a command or command and args")

if __name__ == '__main__':
    main()