package main
import "fmt"
func main(){
	var unit float64
	fmt.Print("Enter the bill:")
	fmt.Scan(&unit)
	if(unit<=100){
		fmt.Println("1st electric bill: ",unit*5.00)
	}else if(unit>100 && unit<200){
		fmt.Println("2nd electric bill: ",unit*7.00)
	}else {
		fmt.Println("3rd electric bill: ",unit*10.00)
	}
}