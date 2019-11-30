import pandas as pd
import matplotlib.pyplot as plt



data = pd.read_csv("FemPreg.csv")


# 6a print preg outcomes for caseid 10229
case10229 = data[data.caseid == 10229]
print("A)")
print(case10229['outcome'])
print('A) One born alive\n\n')


# 6b show all caseids with more then 12 lb babys
birth = data[data.birthwgt_lb > 12][['caseid','birthwgt_lb']]
print("B)")
print(birth)
print("\n***\nYes one case 11829 gave birth to two babies weighing 14 pounds each\n***\n\n")

#6c find distribution
print("C)")
birthord = data.birthord.value_counts()
print(birthord)

#6d find distribution
print("\n\nD)")
prglgnth_counts = data.prglngth.value_counts()
print(prglgnth_counts.sort_values(ascending=True))

#6e find distribution
plt.hist(data.prglngth)
plt.xlabel('Length of pregnancy')
plt.ylabel('Number of cases')
plt.title('6f')
plt.show()

#6f scatter plot
plt.scatter(data.birthwgt_lb, data.prglngth)
plt.xlabel('Birthwgt')
plt.ylabel('Length of pregnancy')
plt.title('6f')
plt.show()