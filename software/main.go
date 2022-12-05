package main

import (
	"net/http"

	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

type ServerStatus struct {
	Status          string `json:"status"`
	RemoteConnected bool   `json:"remoteConnected"`
}

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

	e.GET("/status", func(c echo.Context) error {
		s := &ServerStatus{
			Status:          "okay",
			RemoteConnected: true,
		}
		return c.JSON(http.StatusOK, s)
	})

	// Start server
	e.Logger.Fatal(e.Start(":1323"))
}
