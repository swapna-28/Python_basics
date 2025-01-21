import google.generativeai as genai
api_key='AIzaSyBQmCj7iQ1JPMvBnNiQY81aFyDepMjCYkY'
genai.configure(api_key=api_key)
model = genai.GenerativeModel('gemini-pro')
prompt = "what is the capital of INDIA?"
response = model.generate_content(prompt)
response.text
