# quiz_manager.py
import requests
import random
import html


class QuizManager:
    def __init__(self, api_url):
        """
        Initializes the quiz manager with the API URL.

        Args:
            api_url (str): Fully formatted OpenTDB API URL.
        """
        self.api_url = api_url
        self.questions = []
        self.current_score = 0

    def fetch_questions(self):
        """
        Calls the OpenTDB API and retrieves questions.

        Returns:
            bool: True if questions fetched successfully, False otherwise.
        """
        try:
            response = requests.get(self.api_url)
            data = response.json()
            if data["response_code"] == 0:
                self.questions = data["results"]
                return True
            else:
                print("API returned no questions.")
                return False
        except Exception as e:
            print(f"Error fetching quiz questions: {e}")
            return False

    def run_quiz(self):
        """
        Starts the quiz loop in the terminal.
        """
        if not self.questions:
            print("No questions loaded.")
            return

        for index, question in enumerate(self.questions, 1):
            print("\n" + "=" * 40)
            print(f"Question {index}: {html.unescape(question['question'])}")

            answers = question["incorrect_answers"] + [question["correct_answer"]]
            answers = [html.unescape(a) for a in answers]
            random.shuffle(answers)

            for i, answer in enumerate(answers, 1):
                print(f"{i}. {answer}")

            try:
                user_input = int(input("Your answer (number): "))
                if answers[user_input - 1] == html.unescape(question["correct_answer"]):
                    print("✅ Correct!")
                    self.current_score += 1
                else:
                    print(f"❌ Wrong! Correct answer was: {html.unescape(question['correct_answer'])}")
            except:
                print("Invalid input. Skipping question.")

        print("\n" + "=" * 40)
        print(f"🎉 Quiz finished! Your score: {self.current_score}/{len(self.questions)}")
