package main

import "fmt"

func main() {
	var username string
	var password int
	fmt.Print("Enter Username:")
	fmt.Scan(&username)
	fmt.Print("Password:")
	fmt.Scan(&password)
	if username == "admin" && password == 1234 {
		fmt.Println("Login successful")
	} else if username == "admnin" && password != 1234 {
		fmt.Println("Login Failed.")
	} else {
		fmt.Println("User not found.")
	}

}
