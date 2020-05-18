import time, random
import os
import math
from plyer import notification #, tts


if __name__ == "__main__":
    
    # You can add your custom message
    list = ["Adult humans are 60 percent water, and our blood is 90 percent water.",
                "Water is essential for the kidneys and other bodily functions.",
                "Drinking water instead of soda can help with weight loss.",
                "Sipping water at regular intervals increases the amount of calories that you burn in increasing your REE (resting energy expenditure) – it represents the amount of calories required by the body during a non-active period.",
                "When dehydrated, the skin can become more vulnerable to skin disorders and wrinkling.",
                "Dehydration can affect brain structure and function. It is also involved in the production of hormones and neurotransmitters. Prolonged dehydration can lead to problems with thinking and reasoning.",
                "Water may also help with weight loss, if it is consumed instead of sweetened juices and sodas. “Preloading” with water before meals can help prevent overeating by creating a sense of fullness.",
                "It makes minerals and nutrients accessible, Thus These dissolve in water, which makes it possible for them to reach different parts of the body.",
                "Water Helps to Maximize Physical Performance",
                "The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women."] 
    path = os.path.dirname(__file__)
    while True:
        
        n =  int(random.randint(0,9))
        #tts.speak("Please drink Water!!")
        notification.notify(

            title="Please drink Water!!",  
            app_icon= path + "\glass.ico" ,
            message = f"{list[n]}",
            timeout=15,

            )
    
        time.sleep(60*60)     #change your time interval here input in seconds curr 1 hr.
    
