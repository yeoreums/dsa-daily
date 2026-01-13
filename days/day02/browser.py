history = []

def visit(page):
    # record a new page visit
    history.append(page)

def back():
    # go back to the previous page
    if history:
        history.pop()

def run():
    visit("google.com")
    visit("openai.com")
    visit("github.com")

    back()
    back()

    print(history)

if __name__ == "__main__":
    run()
