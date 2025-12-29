import functions_framework
import random

@functions_framework.http
def random_joke(request):
    jokes = [
        "Why did the web developer walk out of the restaurant? Because of the table layout.",
        "A SQL query walks into a bar, walks up to two tables, and asks, 'Can I join you?'",
        "Hardware is where the people in your company's software section will tell you the problem is."
    ]
    return {"joke": random.choice(jokes)}