def get_suggestion(emotion, intensity, stress, energy):

    
    if intensity >= 4:
        urgency = "immediately"
    elif intensity == 3:
        urgency = "within 1 hour"
    else:
        urgency = "later today"

    
    if emotion in ["stress", "anxiety"]:
        if stress > 7:
            return f"Do deep breathing and step away from work {urgency}"
        else:
            return f"Take a short break and relax {urgency}"

    elif emotion == "tired":
        if energy < 4:
            return f"Take a power nap or rest {urgency}"
        else:
            return f"Slow down and reduce workload {urgency}"

    elif emotion == "sad":
        return f"Talk to someone or listen to calming music {urgency}"

    elif emotion == "happy":
        return "Keep going, you are in a good state!"

    else:
        return f"Pause and reflect on your feelings {urgency}"