#Unit Conversion
def kg_to_lbs(weight_kg):
    """
    Convert weight from kilograms to pounds.
    
    Args:
    weight_kg (float): The weight in kilograms.
    
    Returns:
    float: The weight in pounds.
    """
    return weight_kg * 2.20462

def lbs_to_kg(weight_lbs):
    """
    Convert weight from pounds to kilograms.
    
    Args:
    weight_lbs (float): The weight in pounds.
    
    Returns:
    float: The weight in kilograms.
    """
    return weight_lbs / 2.20462

def cm_to_inches(height_cm):
    """
    Convert height from centimeters to inches.
    
    Args:
    height_cm (float): The height in centimeters.
    
    Returns:
    float: The height in inches.
    """
    return height_cm / 2.54

def inches_to_cm(height_inches):
    """
    Convert height from inches to centimeters.
    
    Args:
    height_inches (float): The height in inches.
    
    Returns:
    float: The height in centimeters.
    """
    return height_inches * 2.54