FROM python:3.9.5

ARG WORKINGDIR="/workspace/"

RUN apt-get -y update && apt-get install -y --no-install-recommends \
        g++ \
        make \
        cmake \
    && rm -rf /var/lib/apt/lists/*

RUN pip install fastapi
RUN pip install uvicorn[standard]

WORKDIR ${WORKINGDIR}
RUN mkdir -p ${WORKINGDIR}
COPY src/* ${WORKINGDIR}

ENTRYPOINT [ "python", "app.py"]
