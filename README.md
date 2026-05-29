# Docker Container Security Sandbox 🛡️🐳

Bu proje, modern mikroservis mimarilerinde ve DevSecOps süreçlerinde karşılaşılan kritik **Docker konteyner güvenliği zafiyetlerini** simüle etmek ve bu zafiyetlerin siber güvenlik standartlarına uygun olarak nasıl giderileceğini (**Remediation/Hardening**) uygulamalı olarak göstermek amacıyla geliştirilmiştir.

##  Proje Yapısı

Proje iki ana katmandan oluşmaktadır:
1. `vulnerable-stack/`: Bilerek zafiyetli bırakılmış, şifre ifşası, aşırı yetkilendirme ve container escape riskleri barındırır.
2. `secure-stack/`: CIS Docker Benchmark standartlarına göre sıkılaştırılmış (hardened) güvenli altyapı.

---

## Tespit Edilen Zafiyetler ve Risk Analizi (Vulnerable Stack)

* **Zafiyet 1: Ağır ve Güvensiz Base İmaj Kullanımı (Ubuntu 22.04):** Gereksiz paket barındırarak atak yüzeyini genişletir.
* **Zafiyet 2: Katmanlarda Statik Gizli Bilgi İfşası (Hardcoded Secrets):** `Dockerfile` içine yazılan hassas API token'ları (`CRITICAL_AI_TOKEN`) imaj geçmişinden (`docker history`) düz metin olarak okunabilmektedir.
* **Zafiyet 3: Konteynerden Kaçış Riski (Docker Socket Mounting):** `/var/run/docker.sock` dosyasının bağlanması, izole konteyner içindeki bir saldırganın ana makinede root yetkisi kazanmasına yol açar.
* **Zafiyet 4: Eski Sürüm ve CVE Riskleri:** Güncel olmayan Redis 6.0 sürümü bilinen kritik zafiyetlere (RCE) açıktır.

---

## Alınan Güvenlik Önlemleri ve Sıkılaştırma (Secure Stack)

* **Distroless/Slim İmaj Geçişi:** Atak yüzeyini minimuma indirmek için `python:3.11-slim` ve `redis:7.2-alpine` kullanılmıştır.
* **Çevre Değişkenleri İzolasyonu:** Hassas şifreler imaj dışına çıkartılarak runtime aşamasında `.env` dosyasından okunacak şekilde izole edilmiştir.
* **Ağ İzolasyonu:** Konteynerler dış dünyaya kapatılarak yalnızca kendi aralarında konuşabilen izole bir köprü ağa (`secure-cyber-net`) dahil edilmiştir.
* **Root Yetkilerinin Kaldırılması:** Uygulama root yetkileri yerine kısıtlı `security_user` (UID 10001) ile çalıştırılmıştır.
* **Kernel Yeteneklerinin Düşürülmesi:** Saldırganların yetki yükseltmesini engellemek için Linux Kernel yetenekleri `cap_drop: - ALL` ile tamamen elinden alınmıştır.

---

## Nasıl Çalıştırılır?

### Güvenli Sürümü Başlatma
```bash
cd secure-stack
copy .env.example .env
docker compose up --build