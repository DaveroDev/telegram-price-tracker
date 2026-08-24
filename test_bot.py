import httpx

CHAT_ID = "1923492978"
TOKEN = "8844016644:AAF0jxPnNgvRvthdBShJXBEZ5ZyQJiH4pWQ"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
data = {
    "chat_id": CHAT_ID,
    "text": "🚀 ¡Funcionó! Mensaje enviado desde la terminal de la laptop."
}

response = httpx.post(url, json=data)

if response.status_code == 200:
    print("¡Listo! Revisa tu Telegram.")
else:
    print(f"Ocurrió un error: {response.text}")