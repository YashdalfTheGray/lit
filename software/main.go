package main

import (
	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

func main() {
	e := echo.New()

	// global middleware
	e.Use(middleware.Logger())
	e.Use(middleware.Recover())
	e.Use(middleware.CORS())
	e.Use(middleware.CSRF())

	// static files
	e.File("/", "static/index.html")
	e.File("/favicon.ico", "static/assets/favicon.ico")
	e.File("/main.js", "static/main.js")
	e.File("/main.css", "static/main.css")

	e.GET("/status", StatusHandler)

	// Start server
	e.Logger.Fatal(e.Start(":1323"))
}
