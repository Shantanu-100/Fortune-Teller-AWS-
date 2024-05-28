import json
import random

def lambda_handler(event, context):
    fortunes = [
        "You will have a great day!",
        "Something unexpected will happen soon.",
        "You will meet someone special.",
        "Challenges are ahead, but you will overcome them.",
        "Good news is on the way.",
        "You will find what you are looking for.",
        "Happiness is within your reach.",
        "Success is in your future.",
        "A pleasant surprise is waiting for you."
    ]
    
    fortune = random.choice(fortunes)
    question = event.get('queryStringParameters', {}).get('question', 'No question provided')

    response = {
        "statusCode": 200,
        "body": json.dumps({
            "question": question,
            "fortune": fortune
        }),
        "headers": {
            "Content-Type": "application/json"
        }
    }
    
    return response
