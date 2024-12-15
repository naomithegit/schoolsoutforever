import emoji
from emoji import emojize
import datetime

# Print various emojis
owls = emojize(":owl:") * 36
clowns = emojize(":clown_face:") * 36
dinosaurs = emojize(":sauropod:") * 36
flames = emojize(":fire:") * 36
four_leaf_clovers = emojize(":four_leaf_clover:") * 36
frogs = emojize(":frog:") * 36
rainbows = emojize(":rainbow:") * 36
blue_hearts = emojize(":blue_heart:") * 36

print(owls)
print(clowns)
print(dinosaurs)
print(flames)

thinkingface = emojize(":thinking_face:") * 16
print(thinkingface)

# Get the current date and time
today = datetime.datetime.now()
print(f"Today's date: {today.strftime('%B %d, %Y')}")

# Print a line of emojis
print(owls)

# Define important dates
lastdayofkeyin = "2024-12-15"
lastdayofkeyin = datetime.datetime.strptime(lastdayofkeyin, "%Y-%m-%d")
print(f"Last day of Keyin: {lastdayofkeyin.strftime('%B %d, %Y')}")

# Print a line of cute emojis
print(four_leaf_clovers)

# Calculate the number of days until important dates
sleepstilGraduation = lastdayofkeyin - today

# Print messages with calculated days
if today <= lastdayofkeyin:
    print(f"Only {sleepstilGraduation.days} sleeps til Keyin is over!!!")

# Print a line of emojis
print(clowns)

xmasday = "2024-12-26"
xmasday = datetime.datetime.strptime(xmasday, "%Y-%m-%d")

# Print a line of emojis
print(dinosaurs)

# Calculate the number of days until important dates
sleepstilsanta = xmasday - today

# Print messages with calculated days
print(f"Only {sleepstilsanta.days} sleeps til SANTA!!!")

# Print a line of emojis
print(flames)

# Check if the last day of Keyin has passed
if today > lastdayofkeyin:
    print("**WHAT ARE YOU STILL DOING HERE??? GO GET A LIFE!!!**")
    # Print a line of cute emojis
    print(blue_hearts)
    print(four_leaf_clovers)
    print(frogs)
    print(rainbows)