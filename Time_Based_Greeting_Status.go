package main
import "fmt"
func main(){
	var hour int
	var is_working string
	fmt.Print("hour (0-23): ")
	fmt.Scan(&hour)
	fmt.Print("is working day (yes/no): ")
	fmt.Scan(&is_working)
	if(hour>=5 && hour<=11){
		fmt.Print("Good morning")
	}else if (hour>=12 && hour<=16){
		fmt.Print("Good afternoon")
	}else if(hour>=17 && hour<=20){
		fmt.Print("Good evening")
	}else if(hour>=21 && hour<=23){
		fmt.Print("Good night")
	}
	if(hour>=9 && hour<=17 &&is_working=="yes"){
		fmt.Println("-Working hours")
	}else{
		fmt.Println("-Off time")
	}

}