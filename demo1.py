import google.generativeai as genai

api_key = 'google_api_key'

genai.configure(api_key=api_key)



model_gemini_pro = genai.GenerativeModel('gemini-pro')

print("\nOlá! Sou um chatbot. Você pode conversar comigo ou digitar 'sair' para encerrar.")

while True:
    user_input = input('Você: ')

    if user_input.lower() == 'sair':
        print("Até logo!")
        break

    response = model_gemini_pro.generate_content(user_input)
    print('Chatbot:', response.text)
