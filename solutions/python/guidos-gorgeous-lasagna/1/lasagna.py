EXPECTED_BAKE_TIME = 40

def bake_time_remaining(elapsed_bake_time):
    """Return the remaining baking time."""
    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Return the preparation time for the layers"""
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Return the total preparation and baking time"""
    return number_of_layers * 2 + elapsed_bake_time


        
    