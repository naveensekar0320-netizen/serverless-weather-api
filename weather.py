import os
import requests

def handler(request):
    city = request.args.get("city")

    if not city:
        return {
            "statusCode": 400,
            "body": "City parameter is required"
        }

    api_key = os.environ.get("OPENWEATHER_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()

    return {
        "statusCode": 200,
        "body": {
            "city": data.get("name"),
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
            "description": data["weather"][0]["description"]
        }
    }
