from app.webscrapper import Webscrapper
from app.quiz_manager import QuizManager
import time 

def webscrapper_unit_test():
    """
    Runs a functional integration test on the Webscrapper class using real browser automation.

    Returns:
        bool: True if all steps succeed, False otherwise.
    """
    print("🔍 Running Webscrapper unit test...")

    try:
        scraper = Webscrapper(amount="10", category="General Knowledge", difficulty="Easy", type_="Multiple Choice")

        # Test amount
        scraper._api_amount_setter("10")
        value = scraper._api_amount_getter()
        assert value == "10", f"Amount mismatch: got {value}"

        # Test category
        categories = scraper._api_category_getter()
        assert any(cat.text == "General Knowledge" for cat in categories), "Category not found"
        scraper._api_category_setter("General Knowledge")

        # Test difficulty
        difficulties = scraper._api_difficulty_getter()
        assert any(diff.text == "Easy" for diff in difficulties), "Difficulty not found"
        scraper._api_difficulty_setter("Easy")

        # Test type
        types = scraper._api_type_getter()
        assert any(t.text == "Multiple Choice" for t in types), "Type not found"
        scraper._api_type_setter("Multiple Choice")

        # Test URL generation
        api_url = scraper.api_url_generator()
        assert api_url and "api.php?" in api_url, "URL not generated correctly"

        print(f"✅ TEST PASSED — Generated URL: {api_url}")
        scraper._api_close_driver()
        return True

    except AssertionError as ae:
        print(f"❌ TEST FAILED — {ae}")
    except Exception as e:
        print(f"❌ Unexpected error during test: {e}")

    if scraper.driver:
        scraper._api_close_driver()
    return False


def main(unit_test=False):
    if unit_test:
        result = webscrapper_unit_test()
        print(f"\n🎯 Test Result: {'✅ SUCCESS' if result else '❌ FAILURE'}")
    else:
        # Initialisation des paramètres utilisateur (tu peux les rendre dynamiques plus tard)
        amount = "10"
        category = "General Knowledge"
        difficulty = "Medium"
        question_type = "Multiple Choice"

        # Étape 1 : Générer l'URL via Webscrapper
        scraper = Webscrapper(amount, category, difficulty, question_type)
        api_url = scraper.api_url_generator()
        
        if not api_url:
            print("❌ Unable to generate API URL.")
            return

        # Étape 2 : Utiliser QuizManager pour jouer
        quiz = QuizManager(api_url)
        if quiz.fetch_questions():
            quiz.run_quiz()
        else:
            print("❌ Failed to fetch questions.")

        # Fermer le navigateur à la fin
        scraper._api_close_driver()


if __name__ == "__main__":
    main(unit_test=False)