from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "DM Assistant"
    debug: bool = True

    anthropic_api_key: str = ""

    neo4j_uri: str = ""
    neo4j_user: str = "neo4j"
    neo4j_password: str = ""

    postgres_url: str = ""

    class Config:
        env_file = ".env"

settings = Settings()