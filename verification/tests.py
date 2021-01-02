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
            "answer": True,
            "explanation": "One father, one son"
        },
        {
            "input": [
              ['Logan', 'Mike'],
              ['Logan', 'Jack']
            ],
            "answer": True,
            "explanation": "Two sons"
        },
        {
            "input": [
              ['Logan', 'Mike'],
              ['Logan', 'Jack'],
              ['Mike', 'Alexander']
            ],
            "answer": True,
            "explanation": "Grandfather"
        },
        {
            "input": [
              ['Logan', 'Mike'],
              ['Logan', 'Jack'],
              ['Mike', 'Logan']
            ],
            "answer": False,
            "explanation": "Can you be a father to your father?"
        },
        {
            "input": [
              ['Logan', 'Mike'],
              ['Logan', 'Jack'],
              ['Mike', 'Jack']
            ],
            "answer": False,
            "explanation": "Can you be a father to your brother?"
        },
        {
            "input": [
              ['Logan', 'William'],
              ['Logan', 'Jack'],
              ['Mike', 'Alexander']
            ],
            "answer": False,
            "explanation": "Looks like Mike is stranger in Logan's family"
        },
        {
            "input": [
              ['Jack', 'Mike'],
              ['Logan',  'Mike'],
              ['Logan', 'Jack'],
            ],
            "answer": False,
            "explanation": "Looks like Mike has two fathers"
        }
    ],
    "Extra": [
      {
         "input": [
            ['Logan', 'William'],
            ['Logan', 'Jack'],
            ['Mike', 'Mike']
          ],
          "answer": False,
          "explanation": "Can you be a father to yourself?"
      },
      {
         "input": [
            ['Logan', 'William'],
            ['William', 'Jack'],
            ['Jack', 'Mike'],
            ['Mike', 'Alexander']
          ],
          "answer": True,
          "explanation": "Long family"
      },
      {
         "input": [
              ['Logan', 'William'],
              ['Mike', 'Alexander'],
              ['William', 'Alexander']
          ],
          "answer": False,
          "explanation": "Who's Your Daddy?"
      },
      {
         "input": [
              ['Logan', 'Mike'],
              ['Alexander', 'Jack'],
              ['Jack', 'Alexander']
          ],
          "answer": False,
          "explanation": "Can you be a father to your father?"
      },
      {
          "input": [
              ['Logan', 'Mike'],
              ['Alexander', 'Jack'],
              ['Jack', 'Logan']
          ],
          "answer": True,
          "explanation": "Family connections can be listed in any directions"
      },
      {
          "input": [
              ['Logan', 'Mike'],
              ['Alexander', 'Jack'],
              ['Jack', 'Logan'],
              ['Alex', 'Bob']
          ],
          "answer": False,
          "explanation": "It's complex. You can't be a father of your grandfather and Alex is not in Logan's Family."
      },
      {
          "input": [
              ['Logan', 'Mike'],
              ['Alexander', 'Jack'],
              ['Mike', 'Alexander']
          ],
          "answer": True,
          "explanation": "Grandfather, Father, Son."
      },
    ]
}
