def strip_text(text):
    return text.strip()

def lower_text(text):
    return text.lower()

def replace_spaces(text):
    return text.replace(" ", "-")

def pipeline(text):
    text = strip_text(text)
    text = lower_text(text)
    text = replace_spaces(text)
    return text

print(pipeline(" Machine Learning "))
