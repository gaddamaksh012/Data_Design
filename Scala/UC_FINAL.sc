import scala.util.Random
import util.control.Breaks._
object emp_details  {


	def main(args: Array[String])  {

	


	val random = scala.util.Random
	val x = random.nextInt(50)
	val wageper_hr = 20
	var full_timehrs = 8 



	x match {
	
	case x if x > 25 =>
		println("employee is present employee daily wage is:"+wageper_hr*full_timehrs)	
		val list = List(8,4)
		val random = new Random
		val z = list(random.nextInt(list.length))
		
		z match {
			
			case 8 =>
				 
				 println("employee is full time")
			         var a = 1
				 while (a <= 20 )
		                                {

		                                println("day :"+a)
		                                println("full time daily emp wage:"+ full_timehrs*wageper_hr)
	
		                                a = a+1
		
		
		                                if (a == 20) {
			
			                               		println("total wage per month "+wageper_hr*full_timehrs*a)
			                               		
								break
							      }
						}
			case 4 => 
				 println("employee is part time")
				 var part_timehrs = 4
				 var b = 1
				 while (b <= 20 )
		                                {

		                                println("day :"+b)
		                                println("part time daily emp wage:"+ part_timehrs*wageper_hr)
	
		                                b = b+1
		
		
		                                if (b == 20)   {
			
			                               		println("total wage per month "+wageper_hr*part_timehrs*b)
			                               		break
							        }
						}
			case 4 => 	
				
				println("employee is part time")
	
		
			}

	
	case _ =>

		println("employee is absent")
	      }
	
		
	}



}







	





















