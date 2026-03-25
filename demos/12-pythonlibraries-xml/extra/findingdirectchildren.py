import random


def random_child_element(self, node):
    choices = [e for e in node.child_nodes if e.node_type == e.ELEMENT_NODE]
    chosen = random.choice(choices)
    return chosen
