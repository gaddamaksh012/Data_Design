package Banking

import play.api.Logger

import scala.io.Codec.fallbackSystemCodec.name
import scala.io.StdIn.readLine
object BankObject extends App {
  var logger = Logger(this.getClass)
  var members = readLine("Enter the number of people in the bank: ").toInt
  var obj_bank = new Banking_prob[TraitClass]
  var count = 1
  logger.info(message = "log massage here")

  while (count <= members) {
  var ename = readLine("Enter your name: ")
  var eType = readLine("Enter you are an employee or Customer(1.Customer,2.employee): ")
  var operation = readLine("enter the operation: (deposit or withdraw) :->")
  var amount = readLine("Enter the Amount :").toInt
  //var obj_1 = new Banking_prob
  obj_bank.queueSize()
    if (eType == 1) {
      var customer = new Customer(ename,amount,operation)
      obj_bank.enqueue_1(customer)
    }
    else {
      var employee = new Employee(ename,amount,operation)
      obj_bank.enqueue_1(employee)
    }

  operation match {
    case "d" => obj_bank.deposite(amount:Int,ename:String,operation:String)

    case "w" => obj_bank.withdrawn(amount:Int,ename:String,operation:String)
  }
  count = count+1
  }
}
