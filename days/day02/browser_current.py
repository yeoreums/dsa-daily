history = []
current_page = None

def visit(page):
    # TODO:
    # if there is a current page, push it to history
    # set current_page to the new page
    global current_page
    if current_page is not None:
        history.append(current_page)
        print(history)
    current_page = page
    print(current_page)

def back():
    # TODO:
    # if history is not empty:
    # pop from history and make it the current page
    global current_page
    if history:
        current_page = history.pop()
        print(history)

def run():
    visit("google.com")
    visit("openai.com")
    visit("github.com")

    back()
    back()

    print("Current:", current_page)
    print("History:", history)

if __name__ == "__main__":
    run()
