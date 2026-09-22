# Imagem base com Python 3.14 (mesma versao que usamos no Render)
FROM python:3.14-slim

# Copia o binario do uv de dentro da imagem oficial dele, pra usar o mesmo
# gerenciador de pacotes/venv que usamos localmente.
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

WORKDIR /app

# Copia SO os arquivos de dependencia primeiro (nao o codigo ainda).
# Por que separado? O Docker guarda cada instrucao como uma "camada" em
# cache. Se so o codigo (api.py, nucleo.py...) mudar depois, essa camada
# de instalacao de dependencias e reaproveitada do cache — nao reinstala
# tudo de novo a cada build. So invalida esse cache quando o
# pyproject.toml/uv.lock realmente mudam.
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project --no-dev

# Agora sim copia o resto do codigo da aplicacao.
COPY . .
RUN uv sync --frozen --no-dev

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
