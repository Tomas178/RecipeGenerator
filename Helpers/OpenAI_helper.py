import re
import openai
from openai import OpenAI
from typing import Optional
from Models.Ingredient import Ingredient
from Models.GroceryList import GroceryList
from Models.Recipe import Recipe


def get_AI_response_from_image(client: OpenAI, base64_image: str) -> GroceryList:
    """Sends an image to OpenAI API and returns the AI's response."""

    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": (
                            "Give me a list of the ingredients that are in the fridge. "
                            "Your response should follow this format: 'ingredient0, ingredient1, ingredient2'. "
                            "Please don't respond with anything else. "
                            "All I need is the format and absolutely nothing else."
                        ),
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        },
                    },
                ],
            }
        ],
    )

    response_text = completion.choices[0].message.content.strip()
    ingredient_list = [
        Ingredient(name.strip().strip("`")) for name in response_text.split(",")
    ]

    return GroceryList(ingredient_list)


def get_AI_response_for_recipe(
    client: OpenAI,
    groceryList: GroceryList,
    cuisine: str,
    diet_type: str,
    preparation_time: str,
) -> Optional[Recipe]:
    """Sends ingredients and filtering choices to OpenAI API and returns the AI's generated recipe."""

    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "I have the following ingredients in the fridge: "
                            + ", ".join(
                                [
                                    str(ingredient)
                                    for ingredient in groceryList.ingredients
                                ]
                            )
                            + ". I would like to make a recipe with these ingredients. Please suggest a recipe that is of "
                            + cuisine
                            + " cuisine, "
                            + diet_type
                            + " diet type, and "
                            + preparation_time
                            + " preparation time. The response must strictly follow this format:\n"
                            "Title: <recipe title>\n"
                            "Ingredients: <ingredient1>, <ingredient2>, <ingredient3>, ...\n"
                            "Instructions: 1. <step1> 2. <step2> 3. <step3> ...\n"
                            "Ensure that ingredients are comma-separated, and instructions are numbered in a single line.\n"
                            "Please do not leave empty lines between the title, ingredients, and instructions.",
                        }
                    ],
                }
            ],
        )
    except openai.AuthenticationError as e:
        print(f"Authentication Error! Please check OPENAI_API_KEY")
        return None

    response_text = completion.choices[0].message.content.strip()

    recipe = response_text.split("\n")

    recipe_name = recipe[0].split(": ")[1].strip()

    recipe_ingredients = recipe[1].split(": ")[1].split(", ")
    recipe_ingredients = GroceryList(
        [Ingredient(ingredient.strip()) for ingredient in recipe_ingredients]
    )

    instructions_text = recipe[2].split(": ")[1].strip()
    recipe_instructions = re.split(r"\d+\.\s", instructions_text)
    recipe_instructions = [
        instruction.strip()
        for instruction in recipe_instructions
        if instruction.strip()
    ]

    return Recipe(recipe_name, recipe_ingredients, recipe_instructions)
