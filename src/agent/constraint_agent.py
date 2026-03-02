def relax_constraints(preferences):
    if preferences.get("max_violence") == "low":
        preferences["max_violence"] = "medium"
    return preferences
