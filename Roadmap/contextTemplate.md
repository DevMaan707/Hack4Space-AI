---
{
  "topic": "{{topic}}",
  "difficulty": "{{difficulty}}",
  "questions": "{{questions}}",
  "objective": [
    "Generate educational content for the specified programming language topic.",
    "Provide a detailed and informative introduction to the difficulty level, concepts covered, syntaxes, and important points. The introduction should be between 50-100 words.",
    "Create the specified number of coding questions or problem-solving questions related to the topic.",
    "Each question should include: question, syntax, example input, example output, and explanation of input and output.",
    "Ensure every question adheres to the provided structure.",
    "Ensure the output is in valid JSON format and does not include any additional explanatory text."
  ],
  "example_input": {
    "topic": "Python Basics",
    "difficulty": "Beginner",
    "questions": "3"
  },
  "instructions": [
    "Generate content based on the specified topic and difficulty level.",
    "Include a detailed and informative introduction covering concepts and syntax, with a length of 300-500 words.",
    "Provide a set of coding or problem-solving questions with clear structure.",
    "Each question should focus on providing the code, example input, example output, and explanation of input and output.",
    "Format the response in the specified JSON structure.",
    "Ensure the response is strictly in JSON format without any additional explanatory text."
  ],
  "example_interaction": [
    {
      "input": {
        "topic": "Python Basics",
        "difficulty": "Beginner",
        "questions": "3"
      },
      "output": {
        "topic": "Python Basics",
        "introduction": "This beginner-level content covers basic Python syntax and concepts, including variables, data types, control structures, functions, and basic input/output operations. It provides a solid foundation for further learning in Python. Python is a versatile and powerful programming language that is widely used in many different fields, from web development to data science. It is known for its simple and easy-to-read syntax, which makes it an ideal language for beginners. Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming. In this course, you will learn the fundamentals of Python programming, including how to work with variables, data types, and control structures. You will also learn how to create and use functions, handle exceptions, and perform basic file operations. By the end of this course, you will have a solid understanding of Python programming and be able to write your own programs to solve real-world problems.",
        "data": [
          {
            "question": "Write a program to print 'Hello, World!' in Python.",
            "syntax": "print('Hello, World!')",
            "example_input": "",
            "example_output": "Hello, World!",
            "explanation": "This is a simple program that prints the string 'Hello, World!' to the console using the print function."
          },
          {
            "question": "Write a program to find the factorial of a number in Python.",
            "syntax": "def factorial(n):\n    if n == 0:\n        return 1\n    else:\n        return n * factorial(n - 1)",
            "example_input": "5",
            "example_output": "120",
            "explanation": "This program defines a recursive function to calculate the factorial of a given number. The factorial of 5 is 120."
          },
          {
            "question": "Write a Python program to calculate the length of a string using the `len()` function.",
            "syntax": "length = len('hello')",
            "example_input": "'hello'",
            "example_output": "5",
            "explanation": "This program calculates the length of the string 'hello' using the built-in len() function and prints the result."
          }
        ]
      }
    }
  ]
}
---

**User Prompt** : {{prompt}}

Please provide the output in valid JSON format and do not include any additional explanatory text.

---
