import os
from app import app

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))  # Cloud Run 要求用 PORT 環境變數
    app.run(host='0.0.0.0', port=port)
