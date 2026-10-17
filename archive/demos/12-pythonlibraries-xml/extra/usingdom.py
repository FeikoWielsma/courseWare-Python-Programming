import xml.dom.minidom

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("movies.xml")
collection = DOMTree.document_element
if collection.has_attribute("shelf"):
    print("Root element : %s" % collection.get_attribute("shelf"))

# Get all the movies in the collection
movies = collection.get_elements_by_tag_name("movie")

# Print detail of each movie.
for movie in movies:
    print("*****Movie*****")
    if movie.has_attribute("title"):
        print("Title: %s" % movie.get_attribute("title"))

    type = movie.get_elements_by_tag_name("type")[0]
    print("Type: %s" % type.child_nodes[0].data)
    format = movie.get_elements_by_tag_name("format")[0]
    print("Format: %s" % format.child_nodes[0].data)
    rating = movie.get_elements_by_tag_name("rating")[0]
    print("Rating: %s" % rating.child_nodes[0].data)
    description = movie.get_elements_by_tag_name("description")[0]
    print("Description: %s" % description.child_nodes[0].data)
