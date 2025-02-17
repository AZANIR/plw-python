import random
import allure

def random_failure(probability=0.3):
    """
    Simulate a random test failure.
    """
    if random.random() < probability:
        allure.attach("Simulated failure triggered.", name="Failure Log", attachment_type=allure.attachment_type.TEXT)
        raise Exception("Simulated random failure for testing reporting")
