#!/usr/bin/env bash

# Install necessary system packages
apt-get update && apt-get install -y \
    libpango-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    libcairo2 \
    libgobject-2.0-0 \
    fonts-dejavu-core
