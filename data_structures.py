#You have an N-element tuple or sequence that you would like to unpack into a collection of N variables.
p = (4, 5)
x, y = p
print (x, y)

# _ will just discard the value stored in that place
t= (2, 'broth')
_, r = t
print(r)

#You need to unpack N elements from an iterable, but the iterable may be longer than N elements, causing a too many values to unpack exception.
record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print (phone_numbers)


records = [
    ('doi', 2, 3),
    ('patru', 5),
    ('doi', 9, 'zece')
]

def do_doi(x, y):
    print('doi', x, y)

def do_altceva(x):
    print('altceva', x)

for tag, *values in records:
    if tag == "doi":
        do_doi(*values)
    else:
        do_altceva(*values)

#---it can be used also when splitting
line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(fields)

#---it also works with lists
items = [2, 4, 7, 8, 5]
head, *middle, tail = items

print(middle)
