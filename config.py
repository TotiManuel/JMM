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
    SUPABASE_KEY = "sb_publishable_A86yFlKrNVkLucX-sgFnOA_PPHu4N8f"