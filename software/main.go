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
	// Echo instance
	e := echo.New()

	// Middleware
	e.Use(middleware.Logger())
	e.Use(middleware.Recover())

	// Route => handler
	e.GET("/", func(c echo.Context) error {
		s := &ServerStatus{
			Status:          "okay",
			RemoteConnected: true,
		}
		return c.JSON(http.StatusOK, s)
	})

	// Start server
	e.Logger.Fatal(e.Start(":1323"))
}
