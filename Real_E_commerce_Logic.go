package main
import "fmt"
func main(){
	var total_price float64
	var is_member string
	var payment_method string
	var discount float64=0.0
	fmt.Print("Enter  the total price: ")
	fmt.Scan(&total_price)
	fmt.Print("Enter is he member (yes/no): ")
	fmt.Scan(&is_member)
	fmt.Print("Enter payment method (cash/credit/debit): ")
	fmt.Scan(&payment_method)
	if(total_price<1000){
		discount=0.0
	}else if(total_price>=1000 && total_price<5000){
		discount=5
		}else if(total_price>=5000 ){
			discount=10
		}
	if (is_member=="yes"){
		discount=discount+5
	}
	if(payment_method=="card"){
		discount=discount+2
	}
	if (discount>20){
		discount=20
	}
	var total1 float64=total_price*discount/100
	var last_price float64=total_price-total1
	fmt.Println("The final price after discount is: ",last_price)

}