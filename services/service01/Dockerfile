FROM golang:1.14.4-alpine AS builder

RUN mkdir /sourcecode
WORKDIR /sourcecode
COPY main.go /sourcecode
RUN go build -o app-bin

FROM alpine
WORKDIR /app
COPY --from=builder /sourcecode/app-bin /app/
EXPOSE 8090
CMD [ "./app-bin"]