package main

import (
	"encoding/json"
	"flag"
	"fmt"
	"net/http"
	"time"
)

type Status struct {
	Status    string `json:"status"`
	Connected string `json:"connected"`
}

func main() {
	var bindAddr string

	flag.StringVar(&bindAddr, "bind-address", "localhost", "the address to bind the ports to")
	flag.Parse()

	statusServeMux := http.NewServeMux()
	statusServeMux.HandleFunc("/", statusHandler)
	wrappedStatusHandler := logRequestHandlerWrapper(statusServeMux)
	fmt.Println("Started status server")
	http.ListenAndServe(fmt.Sprintf("%s:8080", bindAddr), wrappedStatusHandler)
}

func logRequestHandlerWrapper(h http.Handler) http.Handler {
	fn := func(w http.ResponseWriter, r *http.Request) {
		h.ServeHTTP(w, r)
		fmt.Println(generateLogLine(r.URL.String(), r.Method, r.Proto, r.RemoteAddr))
	}

	return http.HandlerFunc(fn)
}

func statusHandler(w http.ResponseWriter, r *http.Request) {
	status := Status{
		Status:    "okay",
		Connected: "maybe",
	}
	if err := json.NewEncoder(w).Encode(status); err == nil {
		w.Header().Set("Content-Type", "application/json; charset=UTF-8")
	} else {
		w.WriteHeader(http.StatusInternalServerError)
	}
}

func generateLogLine(uri, method, protocol, remote string) string {
	return fmt.Sprintf("[%s] \"%s %s %s\" %s", time.Now().UTC(), method, uri, protocol, remote)
}
