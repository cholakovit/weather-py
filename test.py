from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/weather')
def get_weather():
  city = request.args.get('city')

  if city:
    return f"The weather for {city} is..."
  else:
    return "Please provide a city parameter"


