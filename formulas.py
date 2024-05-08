def calculate_bmi(weight_kg, height_m):
    """
    Calculate the Body Mass Index (BMI) given weight in kilograms and height in meters.
    
    Args:
    weight_kg (float): The weight of the person in kilograms.
    height_m (float): The height of the person in meters.
    
    Returns:
    float: The calculated BMI.
    """
    bmi = weight_kg / (height_m ** 2)
    return bmi

def calculate_bmr(weight_kg, height_cm, age, sex):
    """
    Calculate the Basal Metabolic Rate (BMR) using the Mifflin-St Jeor Equation.
    
    Args:
    weight_kg (float): Weight in kilograms.
    height_cm (float): Height in centimeters.
    age (int): Age in years.
    sex (str): sex 'male' or 'female'.
    
    Returns:
    float: The calculated BMR in calories per day.
    """
    bmr = 10*weight_kg + 6.25*height_cm - 5*age
    if sex.lower()=='male':
        bmr=bmr+5
    else:
        bmr=bmr-161
    return bmr

def calculate_daily_cal_needs(activity_level,bmr):
    """
    Calculates the users total daily calorie needs by multiplying their bmr by
    the appropriate activity factor

    sedentary = (little or no exercise) 
    lightly active = (light exercise/sports 1-3 days​/week)
    moderately active = (moderate exercise/sports 3-5 days/week) 
    very active = (hard exercise/sports 6-7 days a week) 
    extra active = (very hard exercise/sports & physical job or 2x training)

    Args:
    actvity_level (string): user's activity level. options listed above
    bmr (float): user's bmr in calories per day
    
    Returns:
    float: the calculated total daily calorie needs to maintain weight
    """
    activity_multipliers = {"sedentary":1.2,"lightly active":1.375,"moderately active":1.55,"very active":1.725,"extra active":1.9}

    return bmr*activity_multipliers[activity_level]
bmr=calculate_bmr(119.5,183,25,"male")
print(bmr)
tdc=calculate_daily_cal_needs("moderately active",bmr)
print(tdc)
def calculate_cal_deficit(tdc, pounds_to_lose, timeframe):
    """
    Calculates the calorie deficit needed for the user to lose the desired amount
    of weight in the specified timeframe.
    
    Args:
    tdc (float): The total daily calorie needs.
    pounds_to_lose (float): The desired number of pounds the user wants to lose .
    timeframe (int): Number of weeks to lose the desired weight.

    Returns:
    int : The calculated daily deficit to lose the desired weight in the timeframe. 
    """
    cals_per_pound=3500
    time_days=timeframe*7
    cals_to_lose=3500*time_da
    return deficit

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

"""
    desc
    
    Args:
     (): 
    
    Returns:
    : 
    """