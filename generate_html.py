# Difference between composition and aggregation.
# Comment aggregation code and its corresponding code in main method.
# Then uncomment composition related code to see how they behave the same.


# object is passed for python 2
class Tag(object):
    def __init__(self, tag, content):
        self.start_tag = '<{}>'.format(tag)
        self.close_tag = '</{}>'.format(tag)
        self.content = content

    def __str__(self):
        return '\n{0.start_tag}{0.content}{0.close_tag}'.format(self)

    def parse_to_file(self, file):
        print(self, file=file)


class DocType(Tag):
    def __init__(self):
        super().__init__('!DOCTYPE html', '')
        self.close_tag = ''


class Head(Tag):
    def __init__(self, title=None):
        super().__init__('head', '')
        self._title = Tag('title', title) if title else None
        self.content = self._title


class Body(Tag):
    def __init__(self):
        super().__init__('body', '')
        self._body_content = []

    def add_tag(self, tag, content):
        new_tag = Tag(tag, content)
        self._body_content.append(new_tag)

    def parse_to_file(self, file=None):
        for tag in self._body_content:
            self.content += str(tag)
        super().parse_to_file(file=file)


# Composed from other classes - this demonstrates the use of composition:
# class HtmlDoc(object):
#     def __init__(self, title=None):
#         self._doc_type = DocType()
#         self._head = Head(title)
#         self._body = Body()
#
#     def new_tag(self, tag, content):
#         self._body.add_tag(tag, content)
#
#     def generate(self):
#         with open('index.html', 'w') as html_file:
#             self._doc_type.parse_to_file(file=html_file)
#             print('<html>', file=html_file)
#             self._head.parse_to_file(file=html_file)
#             self._body.parse_to_file(file=html_file)
#             print('\n</html>', file=html_file)


# Aggregates functions on the instances passed to HtmlDoc class:
class HtmlDoc(object):
    def __init__(self, doc_type, head, body):
        self._doc_type = doc_type
        self._head = head
        self._body = body

    def add_tag(self, tag, content):
        self._body.add_tag(tag, content)

    def generate(self):
        with open('index.html', 'w') as html_file:
            self._doc_type.parse_to_file(file=html_file)
            print('<html>', file=html_file)
            self._head.parse_to_file(file=html_file)
            self._body.parse_to_file(file=html_file)
            print('\n</html>', file=html_file)


if __name__ == '__main__':
    # corresponding composition main method would look like:

    # new_page = HtmlDoc('Basic HTML Generator')
    # new_page.add_tag('h1', 'Main Header')
    # new_page.add_tag('h2', 'Sub Header')
    # new_page.add_tag('p', 'The purpose is to demonstrate composition in Python...')
    # new_page.generate()

    # corresponding aggregation main method would look like:
    doc_type = DocType()
    page_head = Head('Basic HTML Generator')

    page_body = Body()
    page_body.add_tag('h1', 'Main Header')
    page_body.add_tag('h2', 'Sub Header')
    page_body.add_tag('p', 'The purpose is to demonstrate aggregation in Python...')

    doc = HtmlDoc(doc_type, page_head, page_body)
    doc.generate()
