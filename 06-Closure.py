"""
A closure in python refers to a function that retains access to variables from
outer or enclosing scope even after the outer function has finished executing
"""

def html_element(tag):
    start = f"<{tag}>"
    end = f"</{tag}>"
    def add_content(msg):
        content = start + msg + end
        return content
    return add_content


if __name__ == '__main__':
    # returns add_content function
    h1_element = html_element("h1")

    # The function_add content retains the value of start and end
    # from the outer function even when outer function is completed
    print(h1_element("This is first heading"))
    print(h1_element("This is another heading"))