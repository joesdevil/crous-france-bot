[tool.poetry]
name = "crous-accommodation-notifier"
version = "0.1.0"
description = ""
authors = ["Samuel Mallet  <69467005+SuperMuel@users.noreply.github.com>"]
readme = "README.md"
package-mode = false


[tool.poetry.dependencies]
python = "^3.12"
telepot = "^12.7"
python-dotenv = "^1.0.1"
requests = "^2.32.3"
beautifulsoup4 = "^4.12.3"
selenium = "^4.23.1"
pydantic-settings = "^2.4.0"
pydantic = "^2.8.2"
chromedriver-py = "^127.0.6533.99"


[tool.poetry.group.dev.dependencies]
ruff = "^0.5.7"
pytest = "^8.3.2"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"