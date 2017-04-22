package main

import (
	"html/template"
	"log"
	"net/http"
	"os"
)

//Compile templates on start
var templates = template.Must(template.ParseGlob("assets/templates/*"))

// MAIN //
func main() {
	// open a file for the logging system
	var logFile, err = os.OpenFile("trace_debug.log", os.O_APPEND|os.O_CREATE|os.O_RDWR, 0666)
	isError(err, true)
	log.SetFlags(log.Ldate | log.Ltime | log.Lshortfile)

	// don't forget to close the log
	defer logFile.Close()

	// assign it to the standard logger
	log.SetOutput(logFile)
	log.Output(1, "Run Apoio")

	http.HandleFunc("/index", indexHandler)
	http.HandleFunc("/volunteer", volunteerHandler)
	http.HandleFunc("/faqs", faqsHandler)

	//static file handler.
    assets := http.FileServer(http.Dir("./assets/"))
    http.Handle("/static/", http.StripPrefix("/static/", assets))

	//Listen and serve
	err = http.ListenAndServe(":8981", nil)
	isError(err, true)
}
