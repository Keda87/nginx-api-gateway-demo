FROM hayd/alpine-deno:1.0.0

WORKDIR /sourcecode
COPY main.ts /sourcecode

EXPOSE 5000

CMD ["run", "--allow-net", "main.ts"]