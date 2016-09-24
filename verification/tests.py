"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": [
              ['Logan', 'Mike']
            ],
            "answer": True
        },
        {
            "input": [
              ['Logan', 'Mike'],
              ['Logan', 'Jack']
            ],
            "answer": True
        },
        {
            "input": [
              ['Logan', 'Mike'],
              ['Logan', 'Jack'],
              ['Mike', 'Alexander']
            ],
            "answer": True
        },
        {
            "input": [
              ['Logan', 'Mike'],
              ['Logan', 'Jack'],
              ['Mike', 'Logan']
            ],
            "answer": False
        },
        {
            "input": [
              ['Logan', 'Mike'],
              ['Logan', 'Jack'],
              ['Mike', 'Jack']
            ],
            "answer": False
        },
        {
            "input": [
              ['Logan', 'William'],
              ['Logan', 'Jack'],
              ['Mike', 'Alexander']
            ],
            "answer": False
        }
    ]
}
