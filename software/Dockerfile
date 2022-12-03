FROM golang:buster as builder

WORKDIR /app
COPY . .
RUN CGO_ENABLED=0 go build

FROM scratch

COPY --from=builder /app/golit /bin/
EXPOSE 8080-8085
ENTRYPOINT [ "/bin/golit" ]
