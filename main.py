text = input("Enter text:")
cleaned_text = text.strip()

if bool(cleaned_text) == True:
    print("You have entered valid text.")
else:
    print("You have not entered any valid text.")