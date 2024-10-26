object emp_wage {

	def main(args:Array[String])
{
	val wage_hr = 20
	val day_hrs = 8

	val x = new scala.util.Random
	
	val z = x.nextInt(50)
	
	if( z > 25 )
{
	println("employee is present")
	println("employee per day wage:"+wage_hr*day_hrs)
}
	else {
	println("employee is absent so no wage for this day")
}

}
}
