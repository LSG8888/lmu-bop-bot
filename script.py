import os
import time
import requests

WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")

# Zuordnung: Key/Name -> (Thread-ID, URL-Slug)
STRECKEN_DATA = {
    "Bahrain": ("1532475398175330517", "bahrain"),
    "Barcelona": ("1532475831337619536", "barcelona"),
    "Le Mans": ("1532476680617070612", "le-mans"),
    "Paul Ricard": ("1532477003540861119", "paul-ricard"),
    "Fuji": ("1532477180003745995", "fuji"),
    "Imola": ("1532477267840598127", "imola"),
    "Interlagos": ("1532477337914839060", "interlagos"),
    "Qatar": ("1532477406386983133", "qatar"),
    "Monza": ("1532477461533556786", "monza"),
    "Portimao": ("1532477568345702521", "portimao"),
    "Silverstone": ("1532477690165067977", "silverstone"),
    "Daytona": ("1532477901050609866", "daytona"),
    "Cota": ("1532477998744207501", "cota"),
    "Sebring": ("1532478177622888488", "sebring"),
    "Spa": ("1532478265447678294", "spa-francorchamps"),
    "Laguna Seca": ("1532478315066036284", "laguna-seca")
}

def send_bop_updates():
    if not WEBHOOK_URL:
        print("Fehler: keine DISCORD_WEBHOOK_URL gefunden!")
        return

    for track_name, (thread_id, track_slug) in STRECKEN_DATA.items():
        track_url = f"https://bop-tourism.com/bop/gt3/{track_slug}"

        payload = {
            "username": "LMU Bop Tourist",
            "avatar_url": "https://bop-tourism.com/favicon.ico",
            "embeds": [
                {
                    "title": f"BoP Rankings – GT3 @ {track_name}",
                    "url": track_url,
                    "color": 14101832,
                    "description": (
                        f"Die aktuellen Rundenzeiten, Car-Strength und BoP-Einstufungen für **{track_name}** wurden aktualisiert.\n\n"
                        f"📊 **Klicke hier für die vollständige Rangliste & Live-Zeiten:**\n"
                        f"🔗 **[{track_name} BoP Rankings]({track_url})**\n\n"
                        f"**Discount codes**\n"
                        f"Hymo – 10% off with code BOP (enter at checkout)\n"
                        f"GoSetups – 10% off with code BOPTOURISM (auto-applied)"
                    ),
                    "footer": {
                        "text": "Version: V1.4.0.1 • Updated daily • ⚠️ Setup-pack not up-to-date for marked entries"
                    }
                }
            ]
        }

        target_url = f"{WEBHOOK_URL}?thread_id={thread_id}"
        response = requests.post(target_url, json=payload)

        if response.status_code in [200, 204]:
            print(f"✅ Erfolgreich gesendet an: {track_name}")
        else:
            print(f"❌ Fehler bei {track_name}: Status {response.status_code} - {response.text}")

        # 1 Sekunde Pause zwischen den Anfragen gegen Rate Limits
        time.sleep(1)

if __name__ == "__main__":
    send_bop_updates()
