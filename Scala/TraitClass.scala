package Banking

trait TraitClass {
  var name:String
  var amount:Int
  var operations:String
}
class Customer(ename:String,amounts:Int,operation:String) extends TraitClass {
  override var amount:Int=amounts
  override var operations: String = operation
  override var name:String = ename
}
class Employee(ename:String,amounts:Int,operation:String) extends TraitClass{
  override var amount:Int=amounts
  override var operations: String = operation
  override var name:String = ename
}

