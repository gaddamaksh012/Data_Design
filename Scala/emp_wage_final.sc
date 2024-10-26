import scala.util.Random
import util.control.Breaks._
object emp_details {


	def main(args: Array[String])  {

	


	val random = scala.util.Random
	val x = random.nextInt(50)
	val wageper_hr = 20
	var full_timehrs = 8 
	var a = 1

	while (a <=20) {

	x match {
	
	case x if x > 25 =>
		
	
		val list = List(8,4)
		val random = new Random
		val z = list(random.nextInt(list.length))
				
			
		
		
		z match {
			case 8 =>
				val emp_type = "Full time"
				val duty_hrs = 8
				 
				overall_details (a,emp_type,wageper_hr,duty_hrs)
		                  
						
			case 4 => 
				 val emp_type = "part time"
				 val duty_hrs = 4
		                           
				 overall_details (a,emp_type,wageper_hr,duty_hrs)
		
			}

	
	case _ =>

		println("employeeis absent "+a)

			}
		a = a+1

	                 }
		

	def overall_details (a : Int ,emp_type : String, full_timehrs : Int,  duty_hrs : Int): Unit = {

			val payments :Map[String,Int] = Map("day" -> a , "daily_emp_wage" -> duty_hrs*wageper_hr , "total_wage" -> duty_hrs*wageper_hr*a )
			
				
			
			println("day"+a+":"+"working_type:"+emp_type+"/ndaily wage:"+duty_hrs*wageper_hr+payments)

	              
		 }

	}

}







	





















