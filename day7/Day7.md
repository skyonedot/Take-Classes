# :pencil: Day7-Lesson

##### :cat: 循环算数

今有鸡翁一，值钱伍；鸡母一，值钱三；鸡雏三，值钱一。凡百钱买鸡百只，问鸡翁、母、雏各几何？ 出自《张邱建算经》

> 如何用两重循环实现？
>
> 把第三个变量用一、二变量表示出来
>
> ```python
> def chick_calc( ):
>     """ 今有鸡翁一，值钱伍；鸡母一，值钱三；鸡雏三，值钱一。凡百钱买鸡百只，
>     问鸡翁、母、雏各几何？ 出自《张邱建算经》
>     """
>     result = []
>     for rooster in range(100//5 +1 ):
>         for hen in range((100-rooster*5)//3 + 1):
>             if 7 * rooster + 4 * hen == 100:    #  300 = 5*3 rooster + 3*3 hen + (100-rooster-hen)
>                 result.append((rooster,hen,100-rooster-hen))
> print('总共有%d个解' % len(result))
> for index,value in enumerate(result,1):
>     print('解%d:鸡翁 %d 鸡母 %d 鸡雏 %d' % (index, *value))
> ```

---

##### :monkey: 数据分析

先找到每日机票价格的均值

机票价格随时间的变化

---

##### :dog: 数据结构

🖊️ *给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。*

🍎 例如,给定数组 nums = [-1,2,1,-4], 和 target = 1与 target 最接近的三个数的和为 [2][]. (-1 + 2 + 1 = 2).





---

# :pencil: Day7-Homework

##### :pen: 循环算数

今有雉（鸡）兔同笼，上有三十五头，下有九十四足。 问雉兔各几何。

---

##### :pen: 数据结构

🖊️ *一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。*

🍎 给定数组 nums = [-1, 0, 1, 2, -1, -4]，满足要求的三元组集合为：[ [ [-1, 0, 1], [-1, -1, 2] ]][]