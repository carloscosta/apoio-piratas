package main

import (
	"fmt"
	"net/http"
	"os"
)

func isError(err error, flag bool) {
	if err != nil {
		fmt.Println(err.Error())
		if flag {
			os.Exit(666)
		}
	}
}

//Display the named template
func display(w http.ResponseWriter, tmpl string, data interface{}) {
	if data != nil {
		fmt.Fprintf(w, "<br><p class='bg-success'><b>%s</b> Your keyword is <b>%s</b></p>", data, 4)
	} else {
		templates.ExecuteTemplate(w, tmpl+".html", data)
	}
}
