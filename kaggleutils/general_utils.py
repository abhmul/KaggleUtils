import logging


def dump_args(func):
    '''
    Decorator to print function call details - parameters names and effective
    values
    '''

    def wrapper(*func_args, **func_kwargs):
        arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]
        args = func_args[:len(arg_names)]
        defaults = func.__defaults__ or ()
        args = args + defaults[len(defaults) -
                               (func.__code__.co_argcount - len(args)):]
        params = list(zip(arg_names, args))
        args = func_args[len(arg_names):]
        if args:
            params.append(('args', args))
        if func_kwargs:
            params.append(('kwargs', func_kwargs))
        logging.info(
            func.__name__ + ' (' +
            ', '.join(
                '%s = %r' % p for p in params if p != "self"
            ) + ' )'
        )
        return func(*func_args, **func_kwargs)

    return wrapper
