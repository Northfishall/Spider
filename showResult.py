import matplotlib.pyplot as plt
import MongoDB

List = ['dmjc','blygjw','eyzxdp','hbjh','hdcj','yhzf','zbzp']

result = MongoDB.GetDataByCollection("c5",List)
for i in range(0,len(List)):
    Number = result[i][0]
    price = result[i][1]
    x = []
    for j in range(0,len(Number)):
        x.append(j)
    plt.plot(x, Number, color="r", linestyle="-", marker="^", linewidth=1)
    plt.twinx()
    plt.plot(x, price, color="b", linestyle="-", marker="s", linewidth=1)
    plt.show()
    plt.savefig(str(i)+".png",dpi=120)
