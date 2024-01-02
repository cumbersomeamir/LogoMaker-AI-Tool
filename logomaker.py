from openai import OpenAI
import os

def create_logo(company_name):
    

    OPENAI_API_KEY = ""

    client = OpenAI()

    #Extracting the company initials
    initials = str(extract_initials(company_name))
    print(f"The initials for '{company_name}' are '{initials}'")

    
    prompt_injection = f"Minimalistic letterform logo for the company named {company_name}, incorporating the letters {initials}. The design should be stark, using only black and white colors, with the logo itself being black on a plain white background. No additional text or elements should be included, ensuring a clean, modern, and highly recognizable design that can be effectively used across various mediums."


    response = client.images.generate(
      model="dall-e-3",
      prompt= prompt_injection,
      n=1,
      size="1024x1024"
    )

    return response

def extract_initials(company_name):
    words = company_name.split()  # Split the company name into words
    initials = ''.join(word[0] for word in words)  # Extract the first letter of each word
      return initials.upper()  # Return the initials in uppercase


#Creating the logo

company_name = input("Enter a company name")
resp = create_logo(company_name)

print(resp)
