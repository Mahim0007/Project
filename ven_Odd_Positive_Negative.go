package main
import "fmt"
func main(){
	var number  int
	fmt.Print("Enter your number: ")
	fmt.Scan(&number)
	if(number>0){
		if (number%2==0){
			fmt.Println("Positive even number ")
		}else{
			fmt.Println("positive odd number ")
		}
	}else if(number<0){
		if(number%2==0){
			fmt.Println("Negative even number ")
		}else{
			fmt.Println("Negative odd number ")
		}
	}else{
		fmt.Println("the number is zero")
	}



}