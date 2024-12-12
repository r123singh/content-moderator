from openai import OpenAI
import pandas as pd

API_KEY = "sk-proj-"
client = OpenAI(api_key= API_KEY)

def moderate_content(input_text, image_url):
    response = client.moderations.create(
    model="omni-moderation-latest",
    input=[{"type": "text", "text": input_text},
           {"type": "image_url",
            "image_url": {
                "url": image_url
            }}])
    
    print(response)

def moderate_text(input_text):
    result = client.moderations.create(
        model="omni-moderation-latest",
        input= input_text
    )
    if result!= None:
        print("Model Id: "+result.id )
        print("Model Name: "+ result.model)
        moderation_results = result.results[0]
        flagged = moderation_results.flagged
        if flagged:
            data = moderation_results.categories.to_dict()
            confidence_scores = moderation_results.category_scores.to_dict()
            flag_categories = {key for key,value in data.items() if value}
            flag_scores = {key:value for key,value in confidence_scores.items() if key in flag_categories}
            print('Found Flagged Content')
            print('Content Violation Category: ',end='')
            print(flag_categories)
            print('Confidence Scores per Violated Category : ', end='')
            print(flag_scores)
        else:
            print('Content is OK')
    return
    
def start():
    keep_running =True

    print("*****************************************Content Moderation***************************************************")
    print('***************************************************************************************************************')
    print('Please read following instructions: ')
    print("Enter 1 to check Text based content")
    print("Enter 2 to check both Text and Image based content")
    print ("Enter 3 to Exit")
    print('***************************************************************************************************************')
    print('***************************************************************************************************************')

    while keep_running:
        option = input('Please enter your option: ')
        if option == '1':
            text_data = input("Enter the Text content: ")
            print("***************************************************************************************************************")
            moderate_text(text_data)
            print("***************************************************************************************************************")

        elif option == '2':
            text_data = input("Enter the Text content: ")
            image_link = input("Enter the Image link: ")
            moderate_content(text_data,image_link)
        elif option == '3':
            keep_running = False
        else:
            print("Incorrect option entered")
            print('***************************************************************************************************************')
    
        
# Program starting point
start()