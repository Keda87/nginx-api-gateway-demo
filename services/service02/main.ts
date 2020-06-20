import { serve } from "https://deno.land/std@0.58.0/http/server.ts"

const s = serve({ port: 5000 })
console.log("Listening on port 5000")

for await (const req of s) {
  req.respond({ body: "{\"message\": \"Hello from service 2\"}"})
}