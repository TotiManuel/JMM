import os

class Config:
    SECRET_KEY = "clave_secreta"
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_ENGINE_OPTIONS = {
        "pool_pre_ping": True,
        "pool_recycle": 280
    }

    SUPABASE_URL = "https://gucthjhfrlmbgkaiidad.supabase.co"
    SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Imd1Y3RoamhmcmxtYmdrYWlpZGFkIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc3MzY0MTYxMSwiZXhwIjoyMDg5MjE3NjExfQ.dlL6pRZH56vjyofybWo7j01luu1px7S_eNrV0iiNCV4"  # ⚠️ Usar service_role key