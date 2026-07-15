import urllib.request
import urllib.parse

payload = urllib.parse.urlencode({
    'N': '19', 'P': '4', 'K': '24', 'temperature': '32',
    'humidity': '0.98', 'ph': '6.5', 'rainfall': '202.9'
}).encode()
req = urllib.request.Request('http://127.0.0.1:5000/predict', data=payload, method='POST')
with urllib.request.urlopen(req, timeout=5) as resp:
    html = resp.read().decode('utf-8', 'ignore')
    print(html[:3000])
