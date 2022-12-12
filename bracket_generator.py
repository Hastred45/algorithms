def gen_binary(control, len1, len2, prefix):
    if len1 == 0 and len2 == 0:
        print(prefix)
    else:
        if len1 > 0:
            gen_binary(control + 1, len1 - 1, len2, prefix + '(')
        if control > 0 and len2 > 0:
            gen_binary(control - 1, len1, len2 - 1, prefix + ')')


if __name__ == '__main__':
    lenght = 2
    control = 0
    len1 = lenght
    len2 = lenght
    gen_binary(control, len1, len2, '')
