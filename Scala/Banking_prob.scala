package Banking
import java.util.jar.Attributes.Name
import scala.collection.mutable

class Banking_prob [T<:TraitClass] {
  var q1: mutable.Queue[T] = scala.collection.mutable.Queue[T]()
  //var q1 = mutable.Queue[String]()
  var current_amount = 20000
  def enqueue_1(t:T) {
    q1.enqueue(t)
  }
  def queueSize() {
    println("queue size: "+q1.size)
  }
  def deposite(amount:Int,ename:String,operation:String): Unit = {
    current_amount += amount
    println("person name is : "+ename)
    println("deposited amount: "+amount)
    println("current amount in the bank: "+current_amount)
    q1.dequeue()
    println("Next")

  }
  def withdrawn(amount:Int,ename:String,operation:String): Unit = {
    if (current_amount >= amount) {
      current_amount = current_amount - amount
      println("person name is: "+ename)
      println("withdrawn amount is : "+amount)
      println("current amount in the bank: "+current_amount)
      q1.dequeue()
      println("Next")

    }
    else {
      println("amount is insufficiant please visit again")
      q1.dequeue()
    }
  }
}
