import scala.util.Random
object case_statements {

	def main(args:Array[String]) : Unit = {

	val a = scala.util.Random
	val b = a.nextBoolean()
	val wage_hr = 20
	val total_hrs = 8
	
	val list = List(8,4)
	val random = new Random
	val z = list(random.nextInt(list.length))


	
	b match {

	case true =>
	 
		println("employee is present and wage per day is:  "+wage_hr*total_hrs) 
		
		z match {

			case 8 => println("employee type is full time and wage is: "+wage_hr*z)

			case 4 => println("employee type is part time: "+wage_hr*z)

			}
	case false => println("employee is absent")
		
	
	

	

        }


        } 

}






