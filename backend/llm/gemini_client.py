import google.generativeai as genai

# 🔑 PASTE YOUR GEMINI API KEY HERE
genai.configure(api_key="AIzaSyB6Q4CsngQUO7jCE6ViLKqRYVyydZj-r1g")

model = genai.GenerativeModel("gemini-2.5-flash")

def call_gemini(prompt):
    response = model.generate_content(prompt)
    return response.text
