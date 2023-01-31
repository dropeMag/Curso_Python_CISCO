seasons = ['Spring', 'Summer', 'Fall', 'Winter']

print(list(enumerate(seasons)))
print(list(enumerate(seasons, start=2)))

"""
EQUIVALENTE A:

def enumerate(sequence, start=0):
    n = start
    for elem in sequence:
        yield n, elem
        n += 1
"""
