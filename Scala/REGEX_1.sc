import scala.util.matching.Regex
import scala.io.StdIn.readLine



object regex{


	def main(args: Array[String]){
	
	val pattern = "^[A-Z][a-z]+\\s[A-Z][a-z]+$".r
	val name = readLine("Enter your name: ")

	if (pattern.matches(name)) {
		
		println("name is valid")
			}	

	else {

		println("name is not valid")
		}

					}
	  }