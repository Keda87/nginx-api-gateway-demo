package main

import (
	"fmt"
	"net/http"
)

func indexHandler(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusOK)
	w.Write([]byte(`{"message": "hello from service 1"}`))
}

func main() {
	http.HandleFunc("/api/greetings", indexHandler)

	fmt.Println("Listening on port 8090")
	http.ListenAndServe(":8090", nil)
}
