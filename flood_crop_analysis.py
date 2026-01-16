# flood crop survival analysis 
# Auther : Swarupa


# creating the crop dictionary:

crops = {
    "rice" : 12,
    "sugarcane" : 8,
    "soyabean" : 5,
    "cotton" : 3,
    "wheat" : 4
}

# getting the crop name and flood days from the user as a input:

crop = input("Enter crop name : ").lower()
if crop not in crops :
    print("crop data not available")
    exit()
flood_days = int(input("Enter flood duration in days : "))
if flood_days <= 0 :
    print("Invalid input. Flood duration should be a possible number.")
    exit()

# applying the basic formula and logic for survival percent:

survival_days = crops[crop]
if flood_days <= survival_days :
    survival_percent = 100 
    status = "SAFE"
    Recommendation = "Crop is SAFE."
else :
    survival_percent = (survival_days/flood_days)*100
    if survival_percent <= 40 :
        status = "HIGH RISK"
        Recommendation = "This crop is unlikely to survive. Immediate action is required."
    elif 41 <= survival_percent <= 70 :
        status = "MEDIUM RISK"
        Recommendation = "Crop survival is possible with proper care and monitoring."
    else :
        status = "LOW RISK"
        Recommendation = "Crop is safe under current flood conditions."

# printing survival report:

print("---Crop Survival Report---")
print(f"{crop} : {survival_percent :.2f}%" )
print(f"survival chance - {status}")
print(f"Recommendation : {Recommendation}")
