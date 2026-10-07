import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask
from yeriasdk import YeriaApp, YeriaAppConfig


ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")

def _load_private_key() -> str:
    pem = os.environ.get("SERVICE_ED25519_PRIVATE_KEY", "").strip()
    if pem:
        return pem.replace("\\n", "\n")
    key_path = Path(
        os.environ.get("SERVICE_PRIVATE_KEY_PATH", ROOT_DIR / "service_private.pem")
    )
    if not key_path.is_absolute():
        key_path = ROOT_DIR / key_path
    if not key_path.exists():
        raise FileNotFoundError(
            "Clé privée Ed25519 introuvable. Placez-la dans service_private.pem "
            "ou définissez SERVICE_ED25519_PRIVATE_KEY."
        )
    return key_path.read_text(encoding="utf-8")


def create_app() -> Flask:
    app = Flask(__name__)
    app.url_map.strict_slashes = False
    app_id = os.environ.get("YERIA_APP_ID", "").strip() or "green-cart"
    config_kwargs = {
        "app_id": app_id,
        "base_url": os.environ.get("YERIA_BASE_URL", "https://yeria.app"),
        "private_key": _load_private_key(),
        "view_expiration_minutes": 60,
    }
    dev_key_id = os.environ.get("YERIA_DEV_KEY_ID", "").strip()
    if dev_key_id:
        config_kwargs["dev_key_id"] = dev_key_id
    app.extensions["yeria"] = YeriaApp(YeriaAppConfig(**config_kwargs))

    from .integrations.yeria_routes import yeria_app

    app.register_blueprint(yeria_app)

    return app