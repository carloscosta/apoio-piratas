package main

import (
    "fmt"
	"log"
	"net/http"
)

func indexHandler(w http.ResponseWriter, r *http.Request) {
	log.Output(1, "INDEX Handler")
    err := templates.ExecuteTemplate(w, "index.html", nil)
	if err != nil {
	    log.Output(1, fmt.Sprintf("Template execution failed: %s", err))
    }
}

func volunteerHandler(w http.ResponseWriter, r *http.Request) {
    log.Output(1, "VOLUNTEER Handler")
	err := templates.ExecuteTemplate(w, "volunteer.html", nil)
	if err != nil {
	    log.Output(1, fmt.Sprintf("Template execution failed: %s", err))
    }
}

func faqsHandler(w http.ResponseWriter, r *http.Request) {
    log.Output(1, "FAQS Handler")
    err := templates.ExecuteTemplate(w, "volunteer.html", nil)
	if err != nil {
	    log.Output(1, fmt.Sprintf("Template execution failed: %s", err))
    }
}
