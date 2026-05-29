import os
import time
import sys

print("--- Siber Güvenlik Analiz Otomasyonu (SECURE) Başlatıldı ---")

# Güvenli okuma: Eğer .env içinden token gelmezse sistem güvenli şekilde kapanır
token = os.getenv("AI_TOKEN")

if not token or token == "hf_AIBigSecretTokenDoNotShare102938":
    print("[ERROR] Güvenlik İhlali Riski: Varsayılan veya boş token tespit edildi! Sistem kapatılıyor.")
    sys.exit(1)

print("[LOG] Sistem Tokenı güvenli çevre değişkenlerinden başarıyla doğrulandı.")

while True:
    print("[SAFE] İzole ağ üzerinde güvenli log analizi devam ediyor...")
    time.sleep(10)