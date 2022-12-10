package main

type PutPatternRequest struct {
	Colors   []string `json:"colors"`
	Modifier string   `json:"modifier"`
	Name     string   `json:"name"`
}
