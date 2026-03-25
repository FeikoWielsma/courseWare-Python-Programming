import json
# import logging
# from logging_.exception_log import create_logger
book = {}
book['title'] = 'Light Science:  Introduction to Photographic Lighting'
book['tags'] = ('Photography', 'Kindle', 'Light')
book['published'] = True
book['comment_link'] = None
book['id'] = 1024
book['ref'] = {}
print(book)
with open('ebookq.json', 'w') as f:
    json.dump(book, f, indent=4)
# logger = create_logger()
# with open('ebook2.json', 'w') as f:
#     logging.warning("Dumpimg")
#     logger.log(logging.WARN, "Dumping")
#     json.dump(book, f, indent=3)