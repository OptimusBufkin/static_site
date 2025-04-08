from textnode import TextNode, TextType


def main():

    node = TextNode("This is some anchor text", TextType.LINKS, "www.test.com")
    print(node.__repr__())

main()
