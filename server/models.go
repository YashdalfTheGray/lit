package main

type LightModifier string

const (
	None    LightModifier = "none"
	Fade    LightModifier = "fade"
	Twinkle LightModifier = "twinkle"
)

// Requests

type PutPatternRequest struct {
	Colors   []string      `json:"colors"`
	Modifier LightModifier `json:"modifier"`
	Name     string        `json:"name"`
}

// Responses

type ServerStatusResponse struct {
	Status          string `json:"status"`
	RemoteConnected bool   `json:"remoteConnected"`
}

// Errors

type ErrorResponse struct {
	Reason string `json:"reason"`
}
