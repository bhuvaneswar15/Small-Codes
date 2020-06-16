taxslab = input().split()
taxpercent =input().split()
rebate = int(input())
taxpaid = input().split()
taxamount = []
income =[]
# first calculate the taxamount according to input
for i in range(len(taxslab)-1):
    d = (int(taxslab[i+1]) - int(taxslab[i]))
    d = (int(taxpercent[i]) * d) / 100
    taxamount.append(d)
print(taxamount)
#calculate salary according to the tax payable
for j in range(len(taxpaid)):
    if int(taxpaid[j])>=int(taxamount[0]):
        slab=int(taxpaid[j])-int(taxamount[0])
        if slab > int(taxamount[1]):
            slab = slab - int(taxamount[1])
            salary = (slab*100)/int(taxpercent[2])
            income.append(salary +int(taxslab[2])+rebate)

        elif slab < taxamount[1]:
            salary = (slab*100)/int(taxpercent[1])

            income.append(salary + int(taxslab[1]) + rebate)

    else:
        salary = (int(taxpaid[j])*100)/int(taxpercent[0])
        income.append(salary+rebate+int(taxslab[0]))
#sum all the incomes to give total of all income
totalincome =0
for h in range(len(income)):
    totalincome =totalincome + income[h]
print(totalincome)


