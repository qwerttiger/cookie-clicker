def numbershortener(num):
  if num<1000000:
    return str(num)
  elif num<1000000000:
    return str(round(num/1000000,3))+" million"
  elif num<1000000000000:
    return str(round(num/1000000000,3))+" billion"
  elif num<1000000000000000:
    return str(round(num/1000000000000,3))+" trillion"
  elif num<1000000000000000000:
    return str(round(num/1000000000000000,3))+" quadrillion"
  elif num<1000000000000000000000:
    return str(round(num/1000000000000000000,3))+" quintillion"
  elif num<1000000000000000000000000:
    return str(round(num/1000000000000000000000,3))+" sextillion"
  elif num<1000000000000000000000000000:
    return str(round(num/1000000000000000000000000,3))+" septillion"
  elif num<1000000000000000000000000000000:
    return str(round(num/1000000000000000000000000000,3))+" octillion"
  elif num<1000000000000000000000000000000000:
    return str(round(num/1000000000000000000000000000000,3))+" nonillion"
  elif num<1000000000000000000000000000000000000:
    return str(round(num/1000000000000000000000000000000000,3))+" decillion"
  else:
    return "Infinity"
