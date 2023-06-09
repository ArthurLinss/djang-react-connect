import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
import django

django.setup()
from app.models import Quote, Event



Quote.objects.all().delete()
Event.objects.all().delete()

###################################
# Quotes
###################################

q = Quote(
    title = "Snake Island"
    ,author = "Ukrainian soldier"
    ,category = "ukraine"
    ,text = "Russian warship, go fuck yourself"
    ,helpText = ""
    ,date = "24 February 2022"
    ,context = "Ukrainian soldier responds to a threat from a russian warship."
    ,sources_link = ""
)
q.save()

q = Quote(
    title = "Freedom"
    ,author = "Wolodymr Zelenskyy"
    ,category = "ukraine"
    ,text = "It's a victory, when the weapons fall silent and people speak up."
    ,helpText = ""
    ,date = "2022"
    ,context = "Ukrainian president's speech."
    ,sources_link = "https://ec.europa.eu/commission/presscorner/detail/en/speech_23_2724"
)
q.save()

q = Quote(
    title = "The Fight Is Here"
    ,author = "Wolodymr Zelenskyy"
    ,category = "ukraine"
    ,text = "I need ammunition, not a ride."
    ,helpText = ""
    ,date = "25 February 2022"
    ,context = "Ukrainian leader rejects U.S. offer to take him to a safe country."
    ,sources_link = "https://www.washingtonpost.com/politics/2022/03/06/zelenskys-famous-quote-need-ammo-not-ride-not-easily-confirmed/"
)
q.save()


q = Quote(
    title = "Public Resistance"
    ,author = "Ukrainian Woman"
    ,category = "ukraine"
    ,text = "Take these seeds and put them in your pockets so at least sunflowers will grow when you all die down here."
    ,helpText = ""
    ,date = "26 February 2022"
    ,context = "A Ukrainian resident confronts a Russian soldier in the first days after the invasion of Ukraine."
    ,sources_link = "https://www.storypick.com/ukraine-woman-sunflower-seeds-russian-soldier/"
)
q.save()




###################################
# Events
###################################

e = Event(
    date = "24 February 2022"
    ,category = "ukraine"
    ,title = "The War is here"
    ,subtitle = "... and so it begins"
    ,text = (
        "The Russian invasion of Ukraine began on the morning of 24 February, when Putin announced a special military operation to demilitarise and denazify Ukraine. Minutes later, missiles and airstrikes hit across Ukraine, including Kyiv, shortly followed by a large ground invasion along multiple fronts. Zelenskyy declared martial law and a general mobilisation of all male Ukrainian citizens between 18 and 60, who were banned from leaving the country."
        )
    ,info_link = ""
    ,sources_link = "https://en.wikipedia.org/wiki/Russo-Ukrainian_War"
    ,video_link = "https://www.youtube.com/embed/4WpjgtK2ryo"
    ,video_link2 ="https://www.youtube.com/embed/prfaWHQoxVg"
    ,image = None
    ,author = ""
    ,location = ""
)
e.save()

e = Event(
    date = "25 May 2023"
    ,category = "ukraine"
    ,title = "Belgorod Holds"
    ,subtitle = "... bringing the war back to Russia."
    ,text = "Pro-Ukrainian russian troops attack the Russian border at Belgorod."
    ,info_link = ""
    ,sources_link = ""
    ,video_link = ""
    ,video_link2 = ""
    ,image = None
    ,author = ""
    ,location = ""
)
e.save()

e = Event(
    date = "24 June 2023"
    ,category = "ukraine"
    ,title = "March on Moscau"
    ,subtitle = "Wagner's short revolution"
    ,text = (
        "On 23 June 2023, the Wagner Group, a Russian government-funded paramilitary and private military company, staged a rebellion. The rebellion occurred after a period of increasing tensions between the Russian Ministry of Defense and the leader of Wagner, Yevgeny Prigozhin."
        )
    ,info_link = ""
    ,sources_link = ""
    ,video_link = ""
    ,video_link2 =""
    ,image = None
    ,author = ""
    ,location = ""
)
e.save()


e = Event(
    date = "1960"
    ,category = "vietnamwar"
    ,title = "Cold War Heats Up"
    ,subtitle = "... Vietnam"
    ,text = "USA vs. Russia in Asia."
    ,info_link = ""
    ,sources_link = ""
    ,video_link = ""
    ,video_link2 = ""
    ,image = None
    ,author = ""
    ,location = ""
)
e.save()
