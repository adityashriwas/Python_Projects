def quiz_app():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["1. Berlin", "2. Paris", "3. Madrid", "4. Rome"],
            "answer": 2
        },
        {
            "question": "Which programming language is known as the language of the web?",
            "options": ["1. Python", "2. Java", "3. JavaScript", "4. C++"],
            "answer": 3
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["1. Harper Lee", "2. J.K. Rowling", "3. George Orwell", "4. Mark Twain"],
            "answer": 1
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["1. Earth", "2. Mars", "3. Jupiter", "4. Saturn"],
            "answer": 3
        },
        {
            "question": "Which element has the chemical symbol 'O'?",
            "options": ["1. Oxygen", "2. Osmium", "3. Gold", "4. Hydrogen"],
            "answer": 1
        },
        {
            "question": "What is the square root of 64?",
            "options": ["1. 6", "2. 7", "3. 8", "4. 9"],
            "answer": 3
        },
        {
            "question": "What year did World War II end?",
            "options": ["1. 1945", "2. 1944", "3. 1943", "4. 1942"],
            "answer": 1
        },
        {
            "question": "Who is known as the 'Father of Computers'?",
            "options": ["1. Alan Turing", "2. Charles Babbage", "3. John von Neumann", "4. Bill Gates"],
            "answer": 2
        },
        {
            "question": "Which continent is known as the 'Dark Continent'?",
            "options": ["1. Asia", "2. Africa", "3. South America", "4. Europe"],
            "answer": 2
        },
        {
            "question": "How many states are there in the United States?",
            "options": ["1. 48", "2. 49", "3. 50", "4. 52"],
            "answer": 3
        },
        {
            "question": "What is the chemical formula of water?",
            "options": ["1. H2O", "2. CO2", "3. NaCl", "4. CH4"],
            "answer": 1
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["1. Vincent van Gogh", "2. Michelangelo", "3. Leonardo da Vinci", "4. Pablo Picasso"],
            "answer": 3
        },
        {
            "question": "What is the boiling point of water at sea level?",
            "options": ["1. 50°C", "2. 75°C", "3. 100°C", "4. 150°C"],
            "answer": 3
        },
        {
            "question": "What is the smallest prime number?",
            "options": ["1. 1", "2. 2", "3. 3", "4. 5"],
            "answer": 2
        },
        {
            "question": "What is the national animal of India?",
            "options": ["1. Elephant", "2. Peacock", "3. Tiger", "4. Lion"],
            "answer": 3
        }
    ]

    print("\nWelcome to the Quiz!")
    print("---------------------")
    score = 0

    for idx, q in enumerate(questions, start=1):
        print(f"\nQuestion {idx}: {q['question']}")
        for option in q["options"]:
            print(option)

        try:
            user_answer = int(input("Enter the number of your answer: "))
            if user_answer == q["answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {q['options'][q['answer'] - 1][3:]}")
        except ValueError:
            print("Invalid input. Please enter a number corresponding to your choice.")

    print("\nQuiz Completed!")
    print(f"Your final score is: {score}/{len(questions)}")
    if score == len(questions):
        print("Excellent job!")
    elif score >= len(questions) // 2:
        print("Good effort!")
    else:
        print("Better luck next time.")


quiz_app()
