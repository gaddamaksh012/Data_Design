object emp_wage{

	def main(args:Array[String]){
	
	val a = scala.util.Random
	val working_hrs = a.nextInt(8)
	val wage_per_hr = 20

	if ( working_hrs > 4 ){
		print("employee is full time and wages per day based on working hrs:"+working_hrs*wage_per_hr+"rps")
}
	else {
		print("employee is part time and wages per day based on working hrs:"+working_hrs*wage_per_hr+"rps")
}

}


}