package main

import (
	"net/http"

	"github.com/labstack/echo/v4"
)

func StatusHandler(c echo.Context) error {
	s := &ServerStatusResponse{
		Status:          "okay",
		RemoteConnected: true,
	}
	return c.JSON(http.StatusOK, s)
}

func PutPatternHandler(c echo.Context) error {
	foundRequest := PutPatternRequest{}
	err := c.Bind(&foundRequest)
	if err != nil {
		errResponse := &ErrorResponse{
			Reason: "bad request",
		}
		return c.JSON(http.StatusBadRequest, errResponse)
	}

	s := &ServerStatusResponse{
		Status:          "okay",
		RemoteConnected: true,
	}
	return c.JSON(http.StatusOK, s)
}
