import os
import requests

WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK_URL")

# Zuordnung der Strecken zu Ihren Discord Thread-IDs
STRECKEN_THREADS = {
    "Bahrain": "1532475398175330517",
    "Le Mans": "1532476680617070612",
    "Barcelona": "1532475831337619536",
    "Paul Ricard": "1532477003540861119",
    "Fuji": "1532477180003745995",
    "Imola": "1532477267840598127",
    "Interlagos": "1532477337914839060",
    "Qatar": "1532477406386983133",
    "Monza": "1532477461533556786",
    "Portimao": "1532477568345702521",
    "Silverstone": "1532477690165067977",
    "Daytona": "1532477901050609866",
    "Cota": "1532477998744207501",
    "Sebring": "1532478177622888488",
    "Laguna Seca": "1532478315066036284",
    "Spa": "1532478265447678294"
}

def send_bop_updates():
    if not WEBHOOK_URL:
        print("Fehler: keine DISCORD_WEBHOOK_URL gefunden!")
        return

    for track_name, thread_id in STRECKEN_THREADS.items():
        # Exaktes Nachbauen der Bot-Nachricht als Discord Embed
        payload = {
            "username": "LMU Bop Tourist",
            "avatar_url": "https://bop-tourism.com/favicon.ico",
            "embeds": [
                {
                    "title": f"BoP Rankings – GT3 @ {track_name}",
                    "url": "https://bop-tourism.com/",
                    "color": 14101832,  # Roter Seitenbalken wie im Screenshot
                    "description": (
                        f"Die aktuellen Rundenzeiten, Car-Strength und BoP-Einstufungen für **{track_name}** wurden aktualisiert.\n\n"
                        f"📊 **Klicke hier für die vollständige Rangliste & Live-Zeiten:**\n"
                        f"🔗 **[bop-tourism.com ({track_name})](https://bop-tourism.com/)**\n\n"
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
            print(f"❌ Fehler bei {track_name}: Status {response.status_code}")

if __name__ == "__main__":
    send_bop_updates()
