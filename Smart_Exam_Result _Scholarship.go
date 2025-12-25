package main
import "fmt"

func main() {
	var marks int
	var attendance float64

	fmt.Print("Enter your marks: ")
	fmt.Scan(&marks)

	fmt.Print("Enter your attendance percentage: ")
	fmt.Scan(&attendance)

	// 1️⃣ Fail
	if marks < 40 {
		fmt.Println("Fail")

	// 2️⃣ Disqualified
	} else if marks >= 40 && attendance < 75 {
		fmt.Println("Disqualified due to low attendance")

	// 3️⃣ Full Scholarship
	} else if marks >= 90 && attendance >= 90 {
		fmt.Println("Full Scholarship")

	// 4️⃣ Grade A
	} else if marks >= 80 {
		fmt.Println("Grade: A")

	// 5️⃣ Grade B
	} else if marks >= 70 {
		fmt.Println("Grade: B")

	// 6️⃣ Pass
	} else {
		fmt.Println("Pass")
	}
}
