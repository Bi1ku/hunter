def convert(weight):
    return weight * 2.20462


print(convert(3))


def get_length(string):
    return len(string)


print(get_length("Hello, World!"))


def get_min(df):
    return df.iloc[:, 0].min()


def to_binary(num):
    result = ""

    while num != 0:
        result = str(num % 2) + result
        num = num // 2

    return result


print(to_binary(568))
