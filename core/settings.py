from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class DataBaseSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix='postgres_')
    user: str = ...
    password: str = ...
    db: str = ...
    host: str = ...
    port: int = ...

    @property
    def url(self):
        return f'postgresql+psycopg://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}'


class Settings(BaseSettings):
    debug_mode: bool = True
    app_port: int = 8000
    project_name: str = 'My api service'
    project_description: str = 'Light api microservice'

    db: DataBaseSettings = DataBaseSettings()
    log_sql_queries: bool = False


settings = Settings()
