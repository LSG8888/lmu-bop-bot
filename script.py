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

# Fahrzeugklassen und deren URL-Pfade / Farben
CLASSES = [
    {"name": "GT3", "slug": "gt3", "color": 14101832},        # Rot
    {"name": "Hypercar", "slug": "hypercar", "color": 3447003} # Blau
]

def send_bop_updates():
    if not WEBHOOK_URL:
        print("Fehler: keine DISCORD_WEBHOOK_URL gefunden!")
        return

    for track_name, (thread_id, track_slug) in STRECKEN_DATA.items():
        for car_class in CLASSES:
            class_name = car_class["name"]
            class_slug = car_class["slug"]
            embed_color = car_class["color"]

            track_url = f"https://bop-tourism.com/bop/{class_slug}/{track_slug}"

            payload = {
                "username": "LMU Bop Tourist",
                "avatar_url": "https://bop-tourism.com/favicon.ico",
                "embeds": [
                    {
                        "title": f"BoP Rankings – {class_name} @ {track_name}",
                        "url": track_url,
                        "color": embed_color,
                        "description": (
                            f"Die aktuellen Rundenzeiten, Car-Strength und BoP-Einstufungen für **{class_name}** auf **{track_name}** wurden aktualisiert.\n\n"
                            f"📊 **Klicke hier für die vollständige Rangliste & Live-Zeiten:**\n"
                            f"🔗 **[{track_name} {class_name} BoP Rankings]({track_url})**\n\n"
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
                print(f"✅ Erfolgreich gesendet: {class_name} @ {track_name}")
            else:
                print(f"❌ Fehler bei {class_name} @ {track_name}: Status {response.status_code} - {response.text}")

            # Kurze Pause für Discord Rate Limits
            time.sleep(1.5)

if __name__ == "__main__":
    send_bop_updates()
