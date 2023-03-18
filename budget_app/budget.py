class Category:
  def __init__(self,description):
    self.ledger=[]
    self.description = description
    self.cr_balance=0

  def __repr__(self):
    header = self.description.center(30, "*") + "\n"
    le=""
    for i in self.ledger:
      ld="{:<23}".format(i["description"])
      la="{:>7.2f}".format(i["amount"])
      le += "{}{}\n".format(ld[:23], la[:7])
      totl = "Total: {:.2f}".format(self.cr_balance)
    res=header+le+totl
    return res
      
  def deposit(self,amount,description=""):
    self.ledger.append({"amount": amount, "description": description})
    self.cr_balance+=amount

  def withdraw(self, amount, description=""):
    total=0
    res=False
    for i in self.ledger:
      total+=i["amount"]
    if total>=amount:
      self.ledger.append({"amount": -amount, "description": description})
      self.cr_balance-=amount
      res=True
    return res
    
  def get_balance(self):
    return self.cr_balance

  def transfer(self,amount,budget_catagory):
    if self.withdraw(amount=amount,description=f"Transfer to {budget_catagory.description}"):
      budget_catagory.deposit(amount=amount,description=f"Transfer from {self.description}")
      res=True
    else: res=False
    return res
  def check_funds(self, amount):
        if self.cr_balance >= amount:
            return True
        else:
            return False

    
def create_spend_chart(categories):
  spendings=[]
  for cate in categories:
    spent=0
    for i in cate.ledger:
      if i["amount"]<0:
        spent+=abs(i["amount"])
    spendings.append(spent)

  total_money=sum(spendings)
  percent=list()

  spent_percentage = list(map(lambda amount: int((((amount / total_money) * 10) // 1)*10),spendings))

  header = "Percentage spent by category\n"
  chart = ""
  for value in reversed(range(0, 101, 10)):
    chart += str(value).rjust(3) + '|'
    for percent in spent_percentage:
       if percent >= value:
          chart += " o "
       else:
          chart += "   "
    chart += " \n"

  footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
  descriptions = list(map(lambda category: category.description, categories))
  max_length = max(map(lambda description: len(description), descriptions))
  descriptions = list(map(lambda description: description.ljust(max_length), descriptions))
  for x in zip(*descriptions):
      footer += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"

  return (header + chart + footer).rstrip("\n")