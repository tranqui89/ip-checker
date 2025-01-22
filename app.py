import requests
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def get_ip_info():
    # Get the client's public IP address
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    # Fetch geolocation data from ip-api.com
    geo_data = {}
    if client_ip:
        response = requests.get(f'http://ip-api.com/json/{client_ip}')
        if response.status_code == 200:
            geo_data = response.json()

    # Extract relevant details
    country = geo_data.get('country', 'Unknown')
    isp = geo_data.get('isp', 'Unknown')
    city = geo_data.get('city', 'Unknown')
    region = geo_data.get('regionName', 'Unknown')

    # Get the client's user agent
    user_agent = request.headers.get('User-Agent')

    return render_template(
        'index.html',
        ip=client_ip,
        country=country,
        isp=isp,
        city=city,
        region=region,
        user_agent=user_agent
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
