from django.shortcuts import render
# Create your views here.
from django.http import JsonResponse

# Simple rule-based chatbot
responses = {
    "pregnancy diet": "During pregnancy, include iron-rich foods, fruits, vegetables, and drink plenty of water.",
    "cramps": "Mild cramps are common. Rest, hydrate, and avoid sudden movements. If severe, consult a doctor.",
    "exercise": "Light walking and prenatal yoga are usually safe. Avoid heavy lifting.",
    "headache": "Drink water and rest. If headache is persistent, consult a doctor.",
    "water": "Aim to drink 7-8 glasses of water daily during pregnancy.",
    "labor signs": "Frequent contractions, water breaking, and severe pain may be signs. Contact doctor immediately.",
    "default": "I'm here to help! Ask me about diet, exercise, cramps, labor signs, or anything related to pregnancy."
}

def chatbot_reply(request):
    user_msg = request.GET.get("msg", "").lower()

    for key in responses.keys():
        if key in user_msg:
            return JsonResponse({"reply": responses[key]})

    return JsonResponse({"reply": responses["default"]})
