# Get the first line in Act IV, scene II
from xml.dom import pulldom

hamlet_file = open("hamlet.xml")

events = pulldom.parse(hamlet_file)
act_counter = 0
for event, node in events:
    if event == pulldom.START_ELEMENT:
        if node.tag_name == "ACT":
            act_counter += 1
            scene_counter = 1
        if node.tag_name == "SCENE":
            if act_counter == 4 and scene_counter == 2:
                events.expand_node(node)
                # Traditional DOM processing starts here
                # Get all descendant elements named "LINE"
                line_nodes = node.get_elements_by_tag_name("LINE")
                # Print the text data of the text node
                # of the first LINE element
                print(line_nodes[0].first_child.data)
            scene_counter += 1
