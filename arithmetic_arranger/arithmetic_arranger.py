def bigger(num1, num2):
  if len(num1) > len(num2):
    return len(num1)
  else:
    return len(num2)


def arithmetic_arranger(lst: list, display: bool = False):
  value = []
  line1 = []
  line2 = []
  dash = []
  if len(lst) > 5:
    arranged_problems = "Error: Too many problems."
    return arranged_problems
  for i in lst:
    x = i.split(" ")
    num1 = x[0]
    num2 = x[2]
    operator = x[1]
    if len(num1) > 4 or len(num2) > 4:
      arranged_problems = "Error: Numbers cannot be more than four digits."
      return arranged_problems
    if num1.isdigit() == False or num2.isdigit() == False:
      arranged_problems = "Error: Numbers must only contain digits."
      return arranged_problems
    if operator not in ["+", "-"]:
      arranged_problems = "Error: Operator must be '+' or '-'."
      return arranged_problems
    else:
      temp = bigger(num1, num2)
      line1.append(" " * int(2 + temp - len(num1)) + num1)
      line2.append(operator + " " * int(1 + temp - len(num2)) + num2)
      dash.append("-" * int(2 + temp))
      v = str(int(eval(i)))
      if len(v) <= temp:
        v = " " + v
      value.append(" " + v)
  if display == True:
    arranged_problems = f"{'    '.join(line1)}\n{'    '.join(line2)}\n{'    '.join(dash)}\n{'    '.join(value)}"
  if display == False:
    arranged_problems = f"{'    '.join(line1)}\n{'    '.join(line2)}\n{'    '.join(dash)}"
  return arranged_problems
