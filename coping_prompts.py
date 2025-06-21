# coping_prompts.py

coping_prompt_library = {
    "anxiety": (
        "I hear that you’re feeling anxious, and that’s completely okay — anxiety can be overwhelming at times.\n"
        "You're not alone in this. Try grounding yourself with a quick exercise:\n"
        "Name 5 things you can see, 4 you can touch, 3 you can hear, 2 you can smell, and 1 you can taste.\n"
        "Would you like to try a guided calming activity, or just talk more about what’s on your mind?"
    ),

    "sadness": (
        "It sounds like you're feeling really sad right now. That’s a very human experience, and it's okay to let yourself feel this way.\n"
        "You might try writing out your feelings or listening to music that brings you comfort.\n"
        "If you’d like, I can share something uplifting or guide you through a short mindful check-in."
    ),

    "stress": (
        "Stress can build up fast, and I’m really sorry you’re going through that.\n"
        "You're doing the best you can — that’s enough right now.\n"
        "How about taking a few slow, deep breaths? Inhale for 4 seconds, hold for 4, exhale for 4.\n"
        "Would it help to walk through a quick de-stress activity or talk through what’s stressing you out?"
    ),

    "fatigue": (
        "Feeling completely drained is a sign you might be pushing yourself too hard — and it's okay to pause.\n"
        "Your body and mind need rest, not guilt.\n"
        "If you can, take a short break — lie down, stretch, or step away from your screen for a moment.\n"
        "Do you want help setting a short timer for rest or hear a gentle reminder that it's okay to take it slow?"
    ),

    "overwhelm": (
        "When everything feels like too much, it’s important to step back and take things one at a time.\n"
        "You're not expected to handle it all at once.\n"
        "Try writing down the 3 most urgent things — then pick just one small thing to do.\n"
        "Want help breaking things into smaller steps, or do you just want space to breathe?"
    )
    
}

def get_coping_prompt(emotion: str) -> str:
    """
    Returns a coping prompt for a given emotional state.
    If the emotion is not recognized, returns a default supportive message.
    """
    return coping_prompt_library.get(
        emotion.lower(),
        "I'm here for you. It's okay to not be okay. Would you like to talk or try a calming activity?"
    )
