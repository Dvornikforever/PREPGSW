def f(*args, **kwargs):
    print(args)
    print(kwargs)


f(*['first', 'second'], **{'one': 1, 'two': 2})
