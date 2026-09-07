# Convert emoji into text

import demoji

# Remove emojis from text 
text = "Hello, world! 🌍😊"
t1 = demoji.replace(text, "")
print(t1)  # Output: Hello, world!

# Replace emojis with descriptive text
text = "I love pizza! 🍕❤️"
t2 = demoji.replace_with_desc(text)
print(t2)  # Output: I love pizza! :pizza: :red_heart:

# Detect emojis in text
text = "Good morning! ☀️🌸"
t3 = demoji.findall(text)
print(t3)  # Output: {'☀️': 'sun', '🌸': 'cherry_blossom'}

