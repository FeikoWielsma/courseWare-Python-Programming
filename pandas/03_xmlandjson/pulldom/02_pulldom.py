#Get the first line in Act IV, scene II
from xml.dom import pulldom    
hamlet_file = open("hamlet.xml")
 
events = pulldom.parse(hamlet_file)
act_counter = 0
for (event, node) in events:
    if event == pulldom.START_ELEMENT:
        if node.tagName == "ACT":
            act_counter += 1
            scene_counter = 1
        if node.tagName == "SCENE":
            if act_counter == 4 and scene_counter == 2:
                events.expandNode(node)
                #Traditional DOM processing starts here
                #Get all descendant elements named "LINE"
                line_nodes = node.getElementsByTagName("LINE")
                #Print the text data of the text node
                #of the first LINE element
                print (line_nodes[0].firstChild.data)
            scene_counter += 1
