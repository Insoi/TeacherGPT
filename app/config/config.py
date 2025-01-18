# *************************************************
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# *************************************************

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    openai_token: SecretStr = SecretStr("")

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


config = Settings()
