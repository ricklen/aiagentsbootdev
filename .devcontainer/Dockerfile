FROM mcr.microsoft.com/devcontainers/python:3.12


RUN apt-get update && apt-get upgrade --yes \
        && pip install --upgrade pip \
        && pip install uv && \
        wget https://go.dev/dl/go1.24.4.linux-amd64.tar.gz && \
        tar -C /usr/local -xzf go1.24.4.linux-amd64.tar.gz && \
        rm go1.24.4.linux-amd64.tar.gz

ENV PATH="/usr/local/go/bin:$PATH"
ENV GOPATH="/go"
ENV GOROOT="/go"
ENV GOBIN="/go/bin"

RUN mkdir -p /go/src /go/bin /go/pkg
RUN chown -R $USER:$USER /go
RUN go install github.com/bootdotdev/bootdev@latest