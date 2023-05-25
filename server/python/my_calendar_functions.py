from datetime import datetime, timedelta


def last_water(plant_name):
    """Gets the date the user last watered their plant"""
    last_watered_string = input(f"When did you last water your {plant_name}? dd/mm/yy \n")
    last_watered = datetime.strptime(last_watered_string, "%d/%m/%y")
    return last_watered


def days_since_watered(last_watered, days):
    """A count that shows how many days it's been since the plant was last watered"""
    last_date = last_watered
    now = datetime.today()
    days_lapsed = now - last_date
    if days_lapsed.days > days:
        print(f"It's been {days_lapsed.days} days since you last watered me")
        return "overdue"
    elif days_lapsed.days <= 1:
        print(f"It's been {days_lapsed.days} day since you last watered me")
    else:
        print(f"It's been {days_lapsed.days} days since you last watered me")


def date_to_water(plant_name, last_watered, days):
    """Tells user the date they should next water their plant"""
    water_due = last_watered + timedelta(days)
    water_due = water_due.strftime("%A %dth %B %Y")
    return f"You should next water your {plant_name.title()} on {water_due}."


overwatering = " - Take houseplant off the soil to do a quick check-up on roots and throw away this oil (as root rot is"\
               " contagious" \
               "\n - Using a clean pair of scissors, cut off the roots with root rot (they would look rotten,"\
               "brown/black and slimy) only leaving healthy roots behind"\
               "\n - Take a bowl and fill it with a mix of 2 parts water and 1 part hydrogen peroxide"\
               "\n - Soak the health roots in the bowl for 30 minutes"\
               "\n - Using a new pot, fill it with new healthy well-draining soil (using the correct soil for your plant"\
               "and re-pot.  Lightly water."\
               "\n - In the future, reduce watering by adhering to your watering schedule"\
               "\n    -> Going forward you can test whether your plant needs watering by pushing a stick to the bottom"\
               "and seeing if it's dry"\

underwatering = " - Increase watering frequency and ensure soil doesn't stay too dry for long periods"\
                "\n - You may wish to install a moisture meter"\
                "\n - Mist the leaves occasionally to increase humidty around the plant"\
                "\n - Group plants together to create a microclimate with higher humidity"\
                "\n - If your plant has not been wet for long periods, it might become hydrophobic."\
                "If this is the case, you could try bottom watering (which gradually wets the soil along an osmosis gradient)"

yellowing_leaves = " - Check for overwatering or underwatering issues and adjust watering accordingly" \
                   "(as sign of yellowing leaves could mean either of both)."\
                   "\n - Ensure that your plant is receiving the appropriate lighting (too much or too little light can"\
                   "cause yellowing). To learn more about which type of lighting conditions is good, you can head"\
                   "to My Plant Friend for more details."\
                   "\n - Check for nutrient deficiencies and provide appropriate fertilizer (your plant might be waking up"\
                   "for spring and would need require more power up to do so)."\
                   "\n - Trim off severely yellowed leaves to promote new growth."

fungal_disease = " - Remove affected leaves to prevent the spread of disease. When removing the affected leaves, ensure"\
                 "that it doesn’t touch the other healthy leaves."\
                 "\n - Using a microfibre cloth (soaked with soap water), you can wipe down the affected leaves"\
                 "(as soap kills fungi)."\
                 "\n - Ensure proper air circulation around the plant (i.e., putting near a window/ away from high humidity areas)."\
                 "\n - Avoid overhead watering, as it can promote fungal growth. Try bottom watering instead."\
                 "\n - Apply a fungicide following the manufacturer's instructions (different brand work differently)."

leggy_growth = " - Leggy growth oftentimes suggest that your plant is not getting enough sunlight. Please provide adequate"\
               "light exposure, as insufficient light can cause stretching. (if there isn’t enough natural light,"\
               "you can use growth lights instead). To learn more about house plant lighting conditions and growth"\
               "lights, please visit My Plant Friendfor details."\
               "\n - Ensure that you rotate your plant periodically to encourage even growth (unless you prefer otherwise)."\
               "\n - Regularly pruning your plant could promote bushier growth."\
               "\n - If you plant is large and is scrambling to find sunlight/trying to train, please provide it more"\
               "support, such as attaching a moss poles, stakes or trellises, for climbing plants (i.e., Monstera)."\
               "Apply small amount of Keiki clone paste to less bushier areas (at the nodes) to promote new leaf growth"\
               "points (overtime, this could lead to a much bushier plant)."

fungus_gnats = " - Allow the soil to dry out between waterings to eliminate the moisture that attracts fungus gnats."\
               "\n - Place yellow sticky traps near the plant to capture adult gnats (fastest and most effective way)."\
               "\n - Apply a biological control product containing beneficial nematodes to the soil to target the gnat larvae."\
               "\n - Don’t overwater and consider using a top layer of sand/gravel/ chemical mosquito bits on the soil"\
               "surface to deter adult gnats from laying eggs."

thrips_infestation = " - Inspect the undersides of leaves for thrips or their larvae."\
                     "\n - Using a pair of clean scissors, prune and discard heavily infested leaves."\
                     "\n - Spray the plant with a solution of water and insecticidal soap, ensuring thorough coverage."\
                     "Consider using predatory insects like lacewings or predatory mites as a natural control method."

spider_mites = " - Isolate the infested plant to prevent the mites from spreading to other plants."\
               "\n - Rinse the plant with a strong spray of water (with high pressure) to dislodge the mites from the leaves."\
               "\n - Apply a solution of water and insecticidal soap or neem oil to the plant, focusing on the undersides of the leaves."\
               "\n - Repeat the treatment every 7-10 days to target newly hatched mites and break their life cycle."

mealy_bugs = " - Use a cotton swab dipped in rubbing alcohol to individually remove and kill mealybugs (you could just"\
             "squash them or swab them away)."\
             "Alternatively, use a soft brush dipped in soapy water to gently scrub the affected areas."\
             "\n - For severe infestations, apply a solution of water and insecticidal soap directly to the mealybugs."\
             "\n - Repeat the treatment every 7-10 days until the infestation is eradicated."\
             "\n - They can bounce back very easily, so make sure to be patient and repeat the treatment."

aphids = " - Use a strong/ high pressure stream of water to wash off aphids from the affected plant parts."\
         "\n - Apply insecticidal soap or neem oil spray to the plant, covering both sides of the leaves thoroughly."\
         "\n - Introduce beneficial insects such as ladybugs or lacewings to control aphid populations naturally."\
         "\n - Monitor the plant regularly and repeat treatments as necessary."\
         "\n - They can bounce back very easily, so make sure to be patient and repeat the treatment if needed."

plant_friend_link = "Head to My Plant Friend for video tutorials to learn more about watering and diseases and how to prevent them"

def disease_treatments(disease):
    print(f"Your plant is currently showing signs of this: {disease}")
    print(f"The following treatment steps should be followed:")
    disease = disease.split(" ")
    if "overwatering" or "rot" or "wilting" in disease:
        return overwatering
    elif "underwatering" or "dryness" in disease:
        return underwatering
    elif "yellowing" in disease:
        return yellowing_leaves
    elif "spot" or "fungal" in disease:
        return fungal_disease
    elif "gnats" in disease:
        return fungus_gnats
    elif "thrips" in disease:
        return thrips_infestation
    elif "spider" in disease:
        return spider_mites
    elif "mealy" in disease:
        return mealy_bugs
    elif "aphids" in disease:
        return aphids
    print(plant_friend_link)








