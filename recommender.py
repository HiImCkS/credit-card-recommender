import json

def load_cards():
    with open("cards.json", "r") as f:
        return json.load(f)

def recommend_cards(user_input: str) -> str:
    preferences = extract_preferences(user_input)
    cards = load_cards()
    matched = []

    for card in cards:
        if any(pref in card["category"] for pref in preferences):
            matched.append(card)

    if not matched:
        return "No matching cards found."

    response = ""
    for card in matched[:3]:
        response += f"**{card['name']}** by {card['issuer']} - Fee: ₹{card['fee']}\n"
        response += f"Perks: {', '.join(card['perks'])}\n\n"
    return response

def extract_preferences(user_input: str):
    habits = ["fuel", "travel", "groceries", "dining", "shopping", "entertainment"]
    return [h for h in habits if h in user_input.lower()]
