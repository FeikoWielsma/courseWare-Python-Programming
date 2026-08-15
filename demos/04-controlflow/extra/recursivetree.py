Tree = {
    'name': 'animals',
    'left_branch': {
        'name': 'birds',
        'left_branch': {
            'name': 'seed eaters',
            'left_branch': {
                'name': 'house finch',
                'left_branch': None,
                'right_branch': None,
            },
            'right_branch': {
                'name': 'white crowned sparrow',
                'left_branch': None,
                'right_branch': None,
            },
        },
        'right_branch': {
            'name': 'insect eaters',
            'left_branch': {
                'name': 'hermit thrush',
                'left_branch': None,
                'right_branch': None,
            },
            'right_branch': {
                'name': 'black headed phoebe',
                'left_branch': None,
                'right_branch': None,
            },
        },
    },
    'right_branch': None,
}

Indents = ['    ' * idx for idx in range(10)]

def walk_and_show(node, level=0):
    if node is None:
        return
    print(f"{Indents[level]}name: {node['name']}")
    level += 1
    walk_and_show(node['left_branch'], level)
    walk_and_show(node['right_branch'], level)

def test():
    walk_and_show(Tree)

if __name__ == '__main__':
    test()

