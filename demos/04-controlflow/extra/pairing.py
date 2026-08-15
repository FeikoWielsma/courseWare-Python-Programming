girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
letter_girls = {}
for girl in girls:
    letter_girls.setdefault(girl[0], []).append(girl)
print([b + '+' + g for b in boys for g in letter_girls[b[0]]])
