package main
import "fmt"
func main(){
	var withdraw_amount float64
	var balance float64
	fmt.Print("Enter your balance: ")
	fmt.Scan(&balance)
	fmt.Print("Enter withdraw amount: ")
	fmt.Scan(&withdraw_amount)

	if(withdraw_amount<=0){
		fmt.Println("Invalid amount")
	}else if(withdraw_amount<=balance){
		fmt.Println("Successful")
	}else {
		fmt.Println("Insufficient funds")
	}

}