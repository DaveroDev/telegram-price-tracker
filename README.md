# 📈 Telegram Price Tracker Bot

Un script automatizado en Python que realiza web scraping para monitorear variaciones de precios o tasas en tiempo real y envía alertas instantáneas con formato HTML a un chat de Telegram.

## Características

- **Web Scraping Ligero:** Utiliza `httpx` y `BeautifulSoup4` para descargas ultrarrápidas sin sobrecargar el servidor objetivo.
- **Alertas de Telegram:** Notificaciones dinámicas que calculan la diferencia de precio e incluyen emojis indicativos (📈 / 📉).
- **Auto-instalación de dependencias:** El código detecta e instala automáticamente los paquetes faltantes en la primera ejecución.
- **Seguridad por variables de entorno:** Gestión de Tokens de Telegram aislados mediante `python-dotenv`.
- **Persistencia Local:** Almacenamiento del historial de precios en formato JSON para evitar alertas duplicadas.

## 🛠️ Requisitos e Instalación

1. **Clonar el repositorio:**
   git clone [https://github.com/DaveroDev/telegram-price-tracker.git](https://github.com/DaveroDev/telegram-price-tracker.git)
   cd telegram-price-tracker

2. **Configurar las Variables de Entorno:**
   Copia el archivo de plantilla .env.example y nómbralo .env:
   cp .env.example .env
   
   Edita el archivo .env introduciendo las credenciales de tu Bot de Telegram:

   TELEGRAM_TOKEN=tu_token_aqui
   TELEGRAM_CHAT_ID=tu_chat_id_aqui
3. **Ejecutar el Bot:**

   python price_tracker.py
   
   Nota: Las librerías necesarias (httpx, beautifulsoup4, python-dotenv) se instalarán automáticamente si no están presentes en tu entorno.
   
📂 Estructura del Proyecto
    ├── price_tracker.py        # Código principal del bot y lógica de scraping
    ├── .env.example            # Plantilla pública para variables de entorno
    ├── .gitignore              # Archivos y credenciales excluidos del control de versiones
    ├── requirements.txt        # Lista estándar de dependencias de Python
    └── README.md               # Documentación del proyecto

TELEGRAM_TOKEN=tu_token_aqui
TELEGRAM_CHAT_ID=tu_chat_id_aqui
