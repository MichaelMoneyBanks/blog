def counting(string):
    d = {}
    for i in string:
        if i.isalpha():
            i = i.upper()
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
    return d
print(counting("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus."))
