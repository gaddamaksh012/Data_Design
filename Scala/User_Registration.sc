import scala.util.matching.Regex
import scala.io.StdIn.readLine
import util.control.Breaks._



object regex{


	def main(args: Array[String]){
	
	val pattern_name = "^[A-Z][a-z]+\\s[A-Z][a-z]+$".r
	val pattern_mblno = "[9][1]+\\s[0-9]{10}$".r
	val pattern_mail = "^[a-z\\.-[a-z0-9]{2,}]+@[a-z]{2,3}\\.[a-z]{2,3}\\.[a-z]{2,3}$".r
	val pattern_password = "(?=.*[0-9])(?=.*[A-Z])(?=.*[a-z])(?=.*[@%#$]).{8,20}".r
	var list = List.empty[Any]
	
	

	var a = 1
	while(a < 5)
			{

	val name = readLine("Enter your name: ")

	if (pattern_name.matches(name)) {

			println("-----------name is valid------------") 
			list:+=name
			var b = 1
			while (b < 5) {
			
			val mobile = readLine("Enter your mobileno: ")

			if (pattern_mblno.matches(mobile)) {

				println("---------mbl number is valid-----------")
				list:+=mobile
				var c = 1
				while(c < 5) {
					
				val mail = readLine("Enter e mail adress: ")

				if (pattern_mail.matches(mail)) {


					println("---------email is valid----------")
					list:+=mail
					var d = 1
					while(d < 5) {

					val password = readLine("Enter your passward: ")
						
					if (pattern_password.matches(password)) {

						println("--------Welcome Succesfully Login completed----------")
						println("Your details are given here: "+list)
						break

					}
					else {

					println("password is not valid please enter it again")
					d = d+1
					}

					}				


				}
				else {

					println("entered mail is incorrect please enter again")
					c = c + 1

				}

				




				}

			}
			
			else  {

			println("Mobile number is not valid please enter again")
			b = b+1
	

	}
			





}
			
	
					}
	else {
	
		println("not valid enter name below again")
		a = a+1		
			
			}
		
		}
	}

}
 