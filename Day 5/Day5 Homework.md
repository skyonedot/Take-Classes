## Day5 Homework

##### :pen: 将两个数据表按照用户名、成交总金额、省份、年龄、成交时间合并



##### :pen: 去掉数据表中的空值



##### :pen: 改变数据表的列索引（Index）



##### :pen: 按照省份,统计每个省份的成交总金额的总值,均值



##### :pen: 画出省份的成交总金额柱状图

> 代码提示
>
> zhifang1 = data_dropna.groupby('省份').sum()['成交总金额']
> zhifang2 = data_dropna.groupby('省份').mean()['成交总金额']
> plt.bar(zhifang1.index, zhifang1)
> plt.ylabel('成交总金额/元')
> plt.title('总金额')

> 结果显示应类似于
>
> ![image-20200613203638810](\image-20200613203638810.png)
>
> 



> 

