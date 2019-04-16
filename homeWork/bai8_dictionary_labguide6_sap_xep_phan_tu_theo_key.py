import math
import operator

d = {9: "S001", 6: "S002", 7: "S001", 10: "S005", 5: "S005", 4: "S009", 11: "S007"}

new_d = sorted(d.items(),key=lambda x:x[0])
# new_d = sorted(d.items(), key=operator.itemgetter(0))

print(new_d)