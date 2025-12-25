package main
import "fmt"
func main(){
	var username string
	var password string
	var failed_attempts int =0
	fmt.Print("Enter Username:")
	fmt.Scan(&username)
	fmt.Print("Enter Password:")
	fmt.Scan(&password)
	fmt.Print("failed attempts:")
	fmt.Scan(&failed_attempts)
	if(failed_attempts>=3){
		fmt.Println("Account Locked due to multiple failed attempts.")
	}else if(username=="mahim" && password=="mahim"){
		fmt.Println("Login Successful!")
	}else if(username=="mahim"&& password!="mahim"){
		fmt.Println("Incorrect Password!")
		failed_attempts++
	// }else if(failed_attempts>=3){
	// 	fmt.Println("Account Locked due to multiple failed attempts.")
	}else{
		fmt.Println("Login Failed!")
	}

}