import os
import time

print("--- Siber Güvenlik Analiz Otomasyonu (Vulnerable) Başlatıldı ---")

# Gizli verileri güvensiz şekilde ortam değişkeninden okuyoruz
token = os.getenv("CRITICAL_AI_TOKEN")
print(f"[LOG] Sistem Tokenı Belleğe Yüklendi: {token}")
print("[LOG] SSH Private Key Docker Layer üzerinde erişilebilir durumda.")

while True:
    print("[INFO] Şüpheli loglar ve malware örnekleri taranıyor...")
    time.sleep(10)