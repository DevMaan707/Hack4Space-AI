---
{
  "codes": "{{codes}}",
  "objective": [
    "Analyze the provided list of code snippets.",
    "Identify the programming language or framework used in each snippet.",
    "Determine the topics covered by each snippet.",
    "Format the response in the specified JSON structure."
  ],
  "example_code": "def hello_world():\n    print(\"Hello, world!\")\n\nconsole.log(\"Hello, world!\");",
  "instructions": [
    "Analyze the provided code snippets.",
    "Identify the programming language or framework used.",
    "Determine the topics covered by each snippet.",
    "Provide a clear and concise title summarizing the identified language or framework.",
    "List all relevant topics covered by the code snippets.",
    "Ensure the output is in valid JSON format."
  ],
  "example_interaction": [
    {
      "input": "def hello_world():\n    print(\"Hello, world!\")\n\nconsole.log(\"Hello, world!\");",
      "output": {
        "Title": "Python and JavaScript Examples",
        "Topics": [
          "Basic syntax",
          "Hello World program"
        ]
      }
    },
    {
      "input": "class Person {\n    constructor(name) {\n        this.name = name;\n    }\n\n    greet() {\n        console.log(`Hello, ${this.name}`);\n    }\n}\nconst john = new Person('John');\njohn.greet();",
      "output": {
        "Title": "JavaScript Class Example",
        "Topics": [
          "Classes",
          "Constructors",
          "Methods"
        ]
      }
    }
  ]
}
---

**User Prompt** : {{prompt}}

---
