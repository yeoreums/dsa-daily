max_scores = {}

def add_score(record):
    # record is a tuple: (name, score)
    # TODO: store the max score per name
    key, value = record
    if key not in max_scores or value > max_scores[key]:
        max_scores[key] = value

def run():
    scores = [
        ("alice", 80),
        ("bob", 75),
        ("alice", 90),
        ("bob", 60),
        ("alice", 85),
    ]

    for r in scores:
        add_score(r)

    print(max_scores)

if __name__ == "__main__":
    run()
