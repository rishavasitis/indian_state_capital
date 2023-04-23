states_capitals = {
    'Bihar': 'Patna',
    'Punjab': 'Chandigarh',
    'Haryana': 'Chandigarh',
    'Maharashtra': 'Mumbai',
    'Andhra Pradesh': 'Amravati',
    'Arunachal Pradesh': 'Itanagar',
    'Assam': 'Dispur',
    'Gujarat': 'Gandhinagar',
    'Chhattisgarh': 'Raipur',
    'Goa': 'Panaji',
    'Jharkhand': 'Ranchi',
    'Himachal Pradesh': 'Shimla',
    'Karnataka': 'Bengaluru',
    'Rajasthan': 'Jaipur',
    'Kerala': 'Thiruvananthapuram',
    'Madhya Pradesh': 'Bhopal',
    'Manipur': 'Imphal',
    'Meghalaya': 'Shillong',
    'Mizoram': 'Aizawl',
    'Nagaland': 'Kohima',
    'Sikkim': 'Gangtok',
    'Tamil Nadu': 'Chennai',
    'Telangana': 'Hyderabad',
    'Tripura': 'Agartala',
    'Odisha': 'Bhubaneswar',
    'Uttar Pradesh': 'Lucknow',
    'Uttarakhand': 'Dehradun',
    'Delhi(UT)': 'New DeLHI',
    'West Bengal': 'Kolkata'
}


state = input("Enter an Indian state: ")


if state in states_capitals:
    print(f"The capital of {state} is {states_capitals[state]}.")
else:
    print("Sorry, we don't have that state in our dictionary.")