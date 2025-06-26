# coping_prompts.py
import random

coping_prompt_library = {
    "admiration": [
        "Admiration reminds us that inspiration is all around — you’re noticing beauty in others, and that’s a beautiful strength.",
        "Let admiration fuel your own growth — what you see in others often lives inside you too.",
        "Feeling admiration? Let it be your reminder that greatness is not rare — it’s reachable.",
    ],
    "amusement": [
        "Let amusement lighten your day — joy doesn’t always need a reason.",
        "Amusement means your inner child is still alive — honor that spark.",
        "Let yourself laugh fully — amusement is a tiny rebellion against heaviness.",
    ],
    "anger": [
        "Anger is valid — it's often pain or injustice trying to speak. Listen gently.",
        "You don’t need to suppress your anger — but you *can* choose how to transform it.",
        "Let your anger guide you to what matters — then let calm choose your next step.",
    ],
    "annoyance": [
        "Annoyance is your boundary whispering — take a step back and breathe.",
        "It’s okay to be annoyed. You’re human — not everything needs to be okay.",
        "Annoyance shows you're reaching your limit. Give yourself grace, not guilt.",
    ],
    "approval": [
        "Receiving approval feels good — but your worth was always there, with or without it.",
        "Let approval be a reflection, not a requirement. You are already enough.",
        "Celebrate approval when it comes — and remember your value isn’t tied to it.",
    ],
    "caring": [
        "Caring deeply is a strength, not a flaw — protect your softness, don’t hide it.",
        "Your caring nature makes the world lighter — don’t forget to care for yourself too.",
        "It’s okay to feel drained by caring — even the kindest hearts need rest.",
    ],
    "confusion": [
        "Confusion is a sign that you're learning — uncertainty is where growth begins.",
        "It’s okay to feel confused. Clarity comes after chaos, not before.",
        "Confusion doesn’t mean failure — it means you’re asking the right questions.",
    ],
    "curiosity": [
        "Curiosity is your inner spark seeking connection — follow it gently.",
        "Let curiosity lead without pressure. Not all questions need quick answers.",
        "Being curious keeps you open — that’s a gift, not a weakness.",
    ],
    "desire": [
        "Desire is natural — it shows you what matters. Let it guide, not rule.",
        "Feeling desire? That means you're alive and reaching — and that’s human.",
        "Desire doesn’t make you needy. It makes you honest.",
    ],
    "disappointment": [
        "It’s okay to feel disappointed — it means you hoped for something good.",
        "Disappointment hurts, but it also shows you cared deeply. That’s a beautiful thing.",
        "Even in disappointment, you’re still worthy. This moment doesn’t define you.",
    ],
    "disapproval": [
        "Disapproval can sting, but your worth isn’t built on someone else’s opinion.",
        "It’s okay to feel hurt by disapproval — just don’t let it silence your truth.",
        "Disapproval happens to everyone — let it refine you, not define you.",
    ],
    "disgust": [
        "Disgust is your body’s way of setting a boundary — listen with curiosity.",
        "Feeling disgust is valid — but pause to ask where it’s coming from.",
        "Let disgust inform you, not consume you. You’re allowed to feel, then release.",
    ],
    "embarrassment": [
        "Embarrassment is a flash — it fades. Your dignity stays.",
        "We all stumble. Embarrassment means you were real and present — that’s brave.",
        "Let yourself laugh at the moment. Embarrassment loses power when met with kindness.",
    ],
    "excitement": [
        "Excitement is your body’s ‘yes!’ — let it carry you toward what matters.",
        "Let excitement bubble without guilt — joy deserves to be felt fully.",
        "Feel the excitement. Let it remind you: something good is here or coming.",
    ],
    "fear": [
        "Fear shows up to protect you — but not every fear is a fact.",
        "You can carry fear without letting it lead. Courage walks beside it.",
        "It’s okay to be afraid and still move gently forward.",
    ],
    "gratitude": [
        "Gratitude doesn’t need to be big — even noticing small good things is healing.",
        "Let gratitude ground you in the present — not everything needs to be perfect to be good.",
        "When gratitude fills you, let it soften the edges of your day.",
    ],
    "grief": [
        "Grief is love trying to find a place to go — let it move gently through you.",
        "It’s okay if grief comes in waves. You’re allowed to feel it all, over and over.",
        "There is no right timeline for grief. Honor your heart’s pace.",
    ],
    "joy": [
        "Let joy be loud. You don’t have to shrink your happiness for anyone.",
        "Joy doesn’t always mean life is perfect — it means you found light anyway.",
        "Soak in the joy — even a single moment can nourish your whole self.",
    ],
    "love": [
        "Love isn’t weakness — it’s the strongest force you carry.",
        "Feeling love? Let it flow freely, with kindness toward yourself too.",
        "You deserve love — in giving it and in receiving it without conditions.",
    ],
    "nervousness": [
        "Nervousness often comes before something brave — you’re stepping into growth.",
        "It’s okay to feel nervous — it means you care about the outcome.",
        "Let nervousness ride with you, not steer. You’re more ready than you think.",
    ],
    "optimism": [
        "Let optimism guide you — even the tiniest hope can light the way forward.",
        "It’s okay to feel optimistic, even when things are uncertain — you’re choosing belief.",
        "Optimism isn’t denial — it’s resilience in motion.",
    ],
    "pride": [
        "Take pride in how far you’ve come — your effort matters, even when unseen.",
        "Feeling proud? Let that feeling remind you that your growth is real and earned.",
        "Pride doesn’t make you arrogant — it means you’re finally seeing your worth.",
    ],
    "realization": [
        "Realization can be heavy — let it sink in slowly and gently.",
        "Not every realization needs to change everything at once — let it guide, not rush.",
        "Your new awareness is a gift — take your time to make sense of it.",
    ],
    "relief": [
        "Feel the relief fully — it means your heart was holding on for a long time.",
        "Let relief settle into your body like a soft exhale — you’ve made it through something.",
        "Relief is a reminder: peace is possible, and you deserve more of it.",
    ],
    "remorse": [
        "Remorse shows you care about your impact — let that awareness guide growth, not guilt.",
        "It’s okay to feel remorse. Just remember you are more than your past actions.",
        "Let remorse move you forward with gentleness — you’re learning, not failing.",
    ],
    "surprise": [
        "Surprise shakes things up — let it open space for possibility, not panic.",
        "Not all surprises are bad — some are just life’s way of reminding you to stay curious.",
        "Let the surprise settle before you react — there might be beauty in the unexpected.",
    ],
    "neutral": [
        "Feeling neutral is okay — you don’t have to be up or down all the time.",
        "Neutral isn’t numbness. It’s often your mind finding calm in the in-between.",
        "Sometimes, being neutral is your nervous system’s way of resting — honor that.",
    ],
    "numbness": [
        "Numbness doesn’t mean you don’t care — it means you’ve been carrying too much for too long.",
        "It’s okay to feel nothing — your feelings may just be resting before they return.",
        "When you're numb, try gentle reconnection — light, music, movement, anything soft.",
    ],
    "burnout": [
        "Burnout is not a personal failure — it’s a sign you’ve been trying to do too much for too long.",
        "If you're feeling burnt out, your mind and body are asking for rest, not judgment.",
        "You don’t need to push through burnout. You need to pause — and heal.",
    ],
    "motivation_loss": [
        "Losing motivation doesn’t mean you’ve lost your purpose — just that you need rest or redirection.",
        "It’s okay to feel unmotivated. Start with the tiniest step — even stillness counts.",
        "Motivation fades sometimes — it doesn’t mean you’ve failed, it means you’re human.",
    ],
     "stress": [
        "Stress is your body asking for care — even small pauses can help you return to center.",
        "You are not your stress. You are the calm underneath it, waiting to be remembered.",
        "Let the stress move through, not build up — one breath, one moment at a time.",
    ],
    "frustration": [
        "Frustration is a signal — not failure. Let it guide your next gentle step.",
        "It’s okay to feel stuck or irritated — take space, not blame.",
        "Your frustration is valid. You’re trying — and that matters.",
    ],
    "tiredness": [
        "Tiredness means you’ve been carrying a lot. Rest is not a reward — it’s a right.",
        "You don’t have to earn rest. Being tired is reason enough.",
        "It’s okay to stop, to lay down the weight. Your energy will return in time.",
    ],
    
    "anxiety": [
        "I hear that you’re feeling anxious, and that’s completely okay — anxiety can be overwhelming at times.\n",
        "You're not alone in this. Try grounding yourself with a quick exercise:\n",
        "Name 5 things you can see, 4 you can touch, 3 you can hear, 2 you can smell, and 1 you can taste.\n",
        "Would you like to try a guided calming activity, or just talk more about what’s on your mind?",
    ],

    "sadness": [
        "It sounds like you're feeling really sad right now. That’s okay — emotions like these deserve space.",
        "Sadness can be heavy, but you don’t have to carry it alone. Would you like a comforting activity?",
        "I'm here with you. Sometimes, letting yourself feel sad is the first step toward healing.",
        "It's okay to feel low. If you'd like, we can try something uplifting together.",
    ],

    "stress": [
        "Stress can build up fast, and I’m really sorry you’re going through that.\n",
        "You're doing the best you can — that’s enough right now.\n",
        "How about taking a few slow, deep breaths? Inhale for 4 seconds, hold for 4, exhale for 4.\n",
        "Would it help to walk through a quick de-stress activity or talk through what’s stressing you out?",
    ],

    "fatigue": [
        "Feeling completely drained is a sign you might be pushing yourself too hard — and it's okay to pause.\n",
        "Your body and mind need rest, not guilt.\n",
        "If you can, take a short break — lie down, stretch, or step away from your screen for a moment.\n",
        "Do you want help setting a short timer for rest or hear a gentle reminder that it's okay to take it slow?",
    ],

    "overwhelm": [
        "When everything feels like too much, it’s important to step back and take things one at a time.\n",
        "You're not expected to handle it all at once.\n",
        "Try writing down the 3 most urgent things — then pick just one small thing to do.\n",
        "Want help breaking things into smaller steps, or do you just want space to breathe?",
    ]
    
    
    
}

def get_coping_prompt(emotion: str) -> str:
    """
    Returns a coping prompt for a given emotional state.
    If the emotion is not recognized, returns a default supportive message.
    """
    prompts=coping_prompt_library.get(emotion)
    if prompts:
        return random.choice(prompts)
    else:
        return "I'm here for you. It's okay to not be okay. Would you like to talk or try a calming activity?"
    
