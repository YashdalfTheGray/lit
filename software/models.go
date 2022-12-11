package main

type LightModifier string

const (
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

type ServerStatus struct {
	Status          string `json:"status"`
	RemoteConnected bool   `json:"remoteConnected"`
}
