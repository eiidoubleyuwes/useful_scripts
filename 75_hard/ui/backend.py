import json
from datetime import datetime, timedelta
import io

# Define recipes for Daniel Fast
daniel_fast_recipes = [
    "Lentil Soup: Simmer lentils with diced tomatoes, onions, garlic, carrots, and celery in vegetable broth.",
    "Sweet Potato Bowl: Baked sweet potato topped with black beans, avocado slices, and salsa.",
    "Stuffed Bell Peppers: Bell peppers stuffed with quinoa, spinach, and diced tomatoes, baked until tender.",
    "Vegetable Stir-Fry: Mixed vegetables sautéed with soy sauce and sesame oil, served over brown rice.",
    "Fruit Salad: A mix of fresh fruits like apples, oranges, bananas, and berries drizzled with lemon juice.",
    "Chickpea Salad: A bowl of chickpeas, cucumbers, tomatoes, and olive oil with a sprinkle of paprika.",
    "Zucchini Noodles: Spiralized zucchini topped with marinara sauce and fresh basil.",
    "Roasted Veggies: A tray of roasted sweet potatoes, broccoli, and cauliflower seasoned with olive oil and garlic.",
    "Black Bean Chili: Black beans cooked with tomatoes, onions, peppers, and spices like cumin and chili powder.",
    "Cucumber Avocado Wrap: Slices of cucumber and avocado wrapped in lettuce leaves.",
    "Vegetable Soup: A hearty soup made with carrots, potatoes, green beans, and kale in a light tomato broth.",
    "Quinoa Salad: Quinoa mixed with diced bell peppers, cucumbers, and parsley, drizzled with lemon juice.",
    "Baked Plantains: Slices of plantains baked until golden brown, served with a side of guacamole.",
    "Avocado Toast: Whole-grain toast topped with smashed avocado, cherry tomatoes, and a sprinkle of salt.",
    "Carrot Ginger Soup: Pureed carrots and ginger simmered in vegetable broth with a touch of coconut milk.",
    "Spinach Salad: Fresh spinach leaves topped with strawberries, walnuts, and balsamic vinaigrette.",
    "Stuffed Zucchini: Zucchini halves stuffed with a mixture of quinoa, diced tomatoes, and onions.",
    "Mango Smoothie Bowl: A blend of frozen mango, bananas, and almond milk topped with chia seeds.",
    "Vegetable Kebabs: Skewers of grilled vegetables like zucchini, mushrooms, and bell peppers.",
    "Rice and Beans: Brown rice served with seasoned black beans and a side of steamed broccoli.",
    "Tomato Cucumber Salad: Slices of fresh tomatoes and cucumbers with olive oil and vinegar dressing."
]

def lambda_handler(event, context):
    # Parse input from the API Gateway event
    body = json.loads(event['body'])
    start_date = body["startDate"]
    include_daniel_fast = body["danielFast"]

    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = start + timedelta(days=74)

    # Define daily template for the challenge
    daily_template = """
### Day {day_num} - {date}
- **Morning Routine**
  - [ ] Wake up early
  - [ ] Read a chapter of a book

- **Physical Activity**
  - [ ] Workout indoors
  - [ ] Workout outdoors

- **Nutrition**
  - [ ] {diet}
  - [ ] Hydrate (Drink at least 3 liters of water)

- **Education**
  - [ ] School study
  - [ ] Personal study

- **Work & Creativity**
  - [ ] Project work
  - [ ] Ideation session

- **Reflection**
  - [ ] Reflect and log progress
"""

    content = f"# 75 Hard Challenge\n\n## Overview\n- **Start Date:** {start.strftime('%B %d, %Y')}\n- **End Date:** {end.strftime('%B %d, %Y')}\n\n---\n\n## Daily Logs\n"
    for day in range(75):
        current_date = start + timedelta(days=day)
        formatted_date = current_date.strftime("%B %d, %Y")
        day_num = day + 1
        diet = "Follow Daniel Fast" if include_daniel_fast and day < 21 else "Follow clean, balanced diet"
        content += daily_template.format(day_num=day_num, date=formatted_date, diet=diet)
        if include_daniel_fast and day < 21:
            recipe = daniel_fast_recipes[day % len(daniel_fast_recipes)]
            content += f"\n#### Daniel Fast Recipe\n- {recipe}\n"
        content += "\n---\n"

    # Create a file-like object to return as response
    file_obj = io.BytesIO()
    file_obj.write(content.encode('utf-8'))
    file_obj.seek(0)

    # Prepare the response to return the file
    response = {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/octet-stream',
            'Content-Disposition': 'attachment; filename="75_Hard_Challenge.md"'
        },
        'body': file_obj.getvalue().decode('utf-8'),
        'isBase64Encoded': True
    }

    return response
