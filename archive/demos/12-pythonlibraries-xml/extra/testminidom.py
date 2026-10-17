import xml.dom.minidom

document = """\
<slideshow>
<title>Demo slideshow</title>
<slide><title>Slide title</title>
<point>This is a demo</point>
<point>Of a program for processing slides</point>
</slide>

<slide><title>Another demo slide</title>
<point>It is important</point>
<point>To have more than</point>
<point>one slide</point>
</slide>
</slideshow>
"""

dom = xml.dom.minidom.parse_string(document)


def get_text(nodelist):
    rc = []
    for node in nodelist:
        if node.node_type == node.TEXT_NODE:
            rc.append(node.data)
    return "".join(rc)


def handle_slideshow(slideshow):
    print("<html>")
    handle_slideshow_title(slideshow.get_elements_by_tag_name("title")[0])
    slides = slideshow.get_elements_by_tag_name("slide")
    handle_toc(slides)
    handle_slides(slides)
    print("</html>")


def handle_slides(slides):
    for slide in slides:
        handle_slide(slide)


def handle_slide(slide):
    handle_slide_title(slide.get_elements_by_tag_name("title")[0])
    handle_points(slide.get_elements_by_tag_name("point"))


def handle_slideshow_title(title):
    print("<title>%s</title>" % get_text(title.child_nodes))


def handle_slide_title(title):
    print("<h2>%s</h2>" % get_text(title.child_nodes))


def handle_points(points):
    print("<ul>")
    for point in points:
        handle_point(point)
    print("</ul>")


def handle_point(point):
    print("<li>%s</li>" % get_text(point.child_nodes))


def handle_toc(slides):
    for slide in slides:
        title = slide.get_elements_by_tag_name("title")[0]
        print("<p>%s</p>" % get_text(title.child_nodes))


handle_slideshow(dom)
