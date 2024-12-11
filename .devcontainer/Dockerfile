FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    git \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Node.js
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - \
    && apt-get install -y nodejs \
    && rm -rf /var/lib/apt/lists/*

# Install uv and create virtual environment
ADD https://astral.sh/uv/install.sh /uv-installer.sh
RUN sh /uv-installer.sh && rm /uv-installer.sh
ENV PATH="/root/.cargo/bin:$PATH"
RUN uv venv

# Install Python dependencies
# COPY pyproject.toml /tmp/pyproject.toml
# RUN uv pip install -r /tmp/pyproject.toml

# Optional: Uncomment to create non-root user
# ARG USERNAME=vscode
# ARG USER_UID=1000\
# ARG USER_GID=$USER_UID
# RUN groupadd --gid $USER_GID $USERNAME \
#     && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

# Optional: Switch to non-root user
# USER $USERNAME

WORKDIR /workspaces/python_dev_uv
CMD ["bash"]
