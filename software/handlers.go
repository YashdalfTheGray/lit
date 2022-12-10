package main

import (
	"net/http"

	"github.com/labstack/echo/v4"
)

func StatusHandler(c echo.Context) error {
	s := &ServerStatus{
		Status:          "okay",
		RemoteConnected: true,
	}
	return c.JSON(http.StatusOK, s)
}
