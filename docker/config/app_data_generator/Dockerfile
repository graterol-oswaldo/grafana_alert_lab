FROM python:3.13-alpine AS base


ARG VERSION
ARG BUILD_DATE


LABEL org.opencontainers.image.version="$VERSION"
LABEL org.opencontainers.image.created="$BUILD_DATE"


WORKDIR /
ADD ["../src/requirements.txt","."]
RUN ["pip3.13","install","-r","requirements.txt"]
RUN ["mkdir","app"]
FROM base AS app
COPY src /app/
WORKDIR  /app
ENTRYPOINT [ "python3.13" ]
CMD [ "main.py" ]





