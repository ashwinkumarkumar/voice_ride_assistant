"""
Comparison and decision engine for ride options.
"""

def recommend_ride(fares):
    """
    Compare Uber and Rapido fares and times and recommend the better ride.
    Args:
        fares (dict): Dictionary with fare and time estimates for Uber and Rapido.
    Returns:
        dict: Recommended ride service with fare and time.
    """
    uber = fares.get("uber", {})
    rapido = fares.get("rapido", {})

    # Simple scoring: lower fare and lower time preferred
    uber_score = uber.get("fare", float('inf')) + 0.5 * uber.get("time", float('inf'))
    rapido_score = rapido.get("fare", float('inf')) + 0.5 * rapido.get("time", float('inf'))

    if uber_score < rapido_score:
        return {
            "service": "Uber",
            "fare": uber.get("fare"),
            "time": uber.get("time")
        }
    else:
        return {
            "service": "Rapido",
            "fare": rapido.get("fare"),
            "time": rapido.get("time")
        }
