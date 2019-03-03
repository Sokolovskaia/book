def capitalize(data):
    if data == "":
        return ""

    # first, *other = data
    # return first.upper() + "".join(other)
    return data[:1].upper() + data[1:]

data = "capitalize"
print(capitalize(data))

