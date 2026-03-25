import random

def randomChildElement(self, node): 
    choices = [e for e in node.childNodes 
               if e.nodeType == e.ELEMENT_NODE]    
    chosen = random.choice(choices)                
    return chosen