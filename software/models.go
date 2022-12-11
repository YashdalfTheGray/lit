package main

type LightModifier string

const (
	Fade    LightModifier = "fade"
	Twinkle LightModifier = "twinkle"
)

type PutPatternRequest struct {
	Colors   []string      `json:"colors"`
	Modifier LightModifier `json:"modifier"`
	Name     string        `json:"name"`
}
