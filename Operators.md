#AWK——操作符　　

与其它编程语言一样，AWK 也提供了大量的操作符。这一章节中，我们将结合例子介绍　AWK 操作符的使用方法：　

## 算术运算符　　

AWK 支持如下的算术运算符：　　
  
###加法运算符　

加法运算由符号 + 表示，它求得两个或者多个数字的和。下面是一个使用示例：  

```
[jerry]$ awk 'BEGIN { a = 50; b = 20; print "(a + b) = ", (a + b) }'
```  

执行上面的命令可以得到如下的结果：  
 
```
(a + b) =  70
```  
　
###减法运算符　　

减法运算由符号 - 表示，它求得两个或者多个数值的差。示例如下：  

```
[jerry]$ awk 'BEGIN { a = 50; b = 20; print "(a - b) = ", (a - b) }'
```  

执行上面的命令可以得到如下的结果：  

```
(a - b) =  30
```  

###乘法运算符　　

乘法运算由星号( * )表示，它求得两个或者多个数值的乘积。示例如下：  

```
[jerry]$ awk 'BEGIN { a = 50; b = 20; print "(a * b) = ", (a * b) }'
```  

执行上面的命令可以得到如下的结果：　　

```
(a * b) =  1000
```  

###除法运算符　　

除法运算由斜线( / ) 表示，它求得两个或者两个以上数值的商。示例如下：  

```
[jerry]$ awk 'BEGIN { a = 50; b = 20; print "(a / b) = ", (a / b) }'
```  

执行上面的命令可以得到如下的结果：　　
  
```
(a / b) =  2.5
```　　
  
###模运算符　　

模运算由百分（％）表示，它表示两个或者多个数进行模除运算得到其余数。下面是示例： 　 

```
[jerry]$ awk 'BEGIN { a = 50; b = 20; print "(a % b) = ", (a % b) }'
```  　　

执行上面的命令可以得到如下的结果：　　
  
```
(a % b) =  10
```　　
  
##递增运算符与递减运算符　　

AWK 支持递增运算符与递减运算符：　　
  
###前置递增运算　　

前置递增运算由 ++ 表示。它将操作数加 1。这个运算符将操作值增加 1，然后再返回增加后的值。下面的示例中，将操作数　a　 值增加 1 后赋值给　ｂ　,　最终 a 与 b 的值均为 11 ：  　　

```
awk 'BEGIN { a = 10; b = ++a; printf "a = %d, b = %d\n", a, b }'
```  　

执行上面的命令可以得到如下的结果：  　

```
a = 11, b = 11
```　　
 
###前置递减运算符　　
  
前置递减运算由 -- 表示。它的语义是将操作数减 1。这个运算符先将操作数的值减 1， 再将被减小后的值返回。下面的示例中将操作数 a 与 b 的值均设置为 9 :　　
  
```
 [jerry]$ awk 'BEGIN { a = 10; b = --a; printf "a = %d, b = %d\n", a, b }'
```　　

执行上面的命令可以得到如下的结果：　　
  
```
a = 9, b = 9
```　　

###后置递增运算符 　　
 
后置递增运算由 ++ 表示。它同样将操作数的值加1。与前置递增运算符不同，它先将操作数的值返回，再将操作数的值加 1。下面的示例中会将操作数  a的值设置为10，b 的值设置为11。 　　

```
 [jerry]$ awk 'BEGIN { a = 10; b = a++; printf "a = %d, b = %d\n", a, b }'
```　　

执行上面的命令可以得到如下的结果：　　
  
```
a = 11, b = 10
```　　
  
###后置递减运算符　　

后置递增运算符由 -- 表示。它同样将操作数的值减1。该操作符先将操作数的值返回，然后将操作数减　1。下面的示例中将操作数 a 的值设置为 9，b 的值设置为10。　　

```
[jerry]$ awk 'BEGIN { a = 10; b = a--; printf "a = %d, b = %d\n", a, b }'
```　　

执行上面的命令可以得到如下的结果： 　　
 
```
a = 9, b = 10
```　　

##赋值操作符　　

AWK 支持下面这些赋值操作：　　
  
### 简单赋值　　

简单赋值操作由 = 表示。示例如下：　　
  
```
[jerry]$ awk 'BEGIN { name = "Jerry"; print "My name is", name }'
```　　

执行上面的命令可以得到如下的结果： 　　
 
```
My name is Jerry
```　　
  
###加法赋值　　

加法赋值运算符为 +=。下面为示例： 　　
 
```
[jerry]$ awk 'BEGIN { cnt=10; cnt += 10; print "Counter =", cnt }'
```　　

执行上面的命令可以得到如下的结果：  　　

```
Counter = 20
```  　　

上面的例子中，先给 cnt 变量赋值为 10。再使用加法赋值将 cnt 值增加 10。 　　
 
###减法赋值　　

减法赋值运算符为 -=。下面为示例：  　　

```
[jerry]$ awk 'BEGIN { cnt=100; cnt -= 10; print "Counter =", cnt }'
```　　

执行上面的命令可以得到如下的结果：  　　

```
Counter = 90
```　　
  
上面的例子中，先给 cnt 变量赋值为 100。再使用减法赋值运算将 cnt 值减少 10。  

###乘法赋值　　

乘法赋值运算符为 *=。下面为示例：  　　

```
[jerry]$ awk 'BEGIN { cnt=10; cnt *= 10; print "Counter =", cnt }'
```　　

执行上面的命令可以得到如下的结果： 　　

```
Counter = 100
```　　
  
上面的例子中，先给 cnt 变量赋值为 10。再使用乘法赋值运算符将 cnt 值乘以 10。　　
  
###除法赋值　　

除法赋值运算符为  /=。下面为示例：　　
  
```
[jerry]$ awk 'BEGIN { cnt=100; cnt /= 5; print "Counter =", cnt }'
```　　

执行上面的命令可以得到如下的结果：　　
  
```
Counter = 20
```　　
  
上面的例子中，先将 cnt 变量赋值为 100。再使用乘法赋值运算符将 cnt 值除以 5。　　

###模运算赋值　　

模运算赋值运算符为  %=。下面为示例：  　　

```
[jerry]$ awk 'BEGIN { cnt=100; cnt %= 8; print "Counter =", cnt }'
```　　

执行上面的命令可以得到如下的结果： 　　
 
```
Counter = 4
```　　
  
上面的例子中，先将 cnt 变量赋值为 10。再使用模运算赋值操作将 cnt 值乘以 10。　
    
###指数赋值　　

指数赋值运算符为  ^=。下面为示例：  　　

```
[jerry]$ awk 'BEGIN { cnt=2; cnt ^= 4; print "Counter =", cnt }'
```　　

执行上面的命令可以得到如下的结果：　　
  
```
Counter = 16
```　　
  
这个例子求　cnt 的四次幂。　　
  
##关系运算符  　　

AWK 支持如下关系运算符：　　
  
###等于　　

等于运算符为 ==。如果两个操作数相等则返回真，否则返回假。示例如下：　　
    
```
awk 'BEGIN { a = 10; b = 10; if (a == b) print "a == b" }'
```　　

执行上面的命令可以得到如下的结果：　　
  
```
a == b
```　　
  
###不等于  

不等于运算符为 !=。如果两个操作数相等则返回假，否则返回真。示例如下：　　
  
```
[jerry]$ awk 'BEGIN { a = 10; b = 20; if (a != b) print "a != b" }'
```　　

执行上面的命令可以得到如下的结果：　　
  
```
a != b
```　　
  
###小于 　　
 
小于运算符为 <。如果左操作数小于右操作数据则返回真，否则返回假。示例如下： 　　
  
```
[jerry]$ awk 'BEGIN { a = 10; b = 20; if (a < b) print "a < b" }'
```　　

执行上面的命令可以得到如下的结果：  　　

```
a < b
```　　
  
###小于或等于 　　

小于等于运算符为 <=。如果左操作数小于或等于右操作数据则返回真，否则返回假。示例如下：  　　

```
[jerry]$ awk 'BEGIN { a = 10; b = 10; if (a <= b) print "a <= b" }'
```　　

执行上面的命令可以得到如下的结果： 　　
 
```
a <＝ b
```　　
  
###大于　　

大于运算符为  >。如果左操作数大于右操作数则返回真，否则返回假。示例如下：  　

```
[jerry]$ awk 'BEGIN { a = 10; b = 20; if (b > a ) print "b > a" }'
```　　

执行上面的命令可以得到如下的结果： 　　
 
```
b > a
```　　
  
###大于或等于　　

大于等于运算符为  >=。如果左操作数大于或等于右操作数则返回真，否则返回假。示例如下：　　
  
```
[jerry]$ awk 'BEGIN { a = 10; b = 10; if (a >= b) print "a >= b" }'
```　　

执行上面的命令可以得到如下的结果：　　
  
```
b >＝ a
```　　
  
##逻辑运算符　

AWK 包括如下逻辑运算符：　　
  
###逻辑与　　

逻辑与运算符为 &&。下面是逻辑与运算符的语法：  

```
expr1 && expr2
```  

如果 expr1 与 epxr2 均为真，则最终结果为真；否则为假。请注意，只有当 expr1 为真时才会计算 expr2 的值，若　expr1　为假则直接返回真，而不再计算　expr2　的值。下面的例子判断给定的字符串是否是十进制形式：  

```
[jerry]$ awk 'BEGIN {num = 5; if (num >= 0 && num <= 7) printf "%d is in octal format\n", num }'
```  

执行上面的命令可以得到如下的结果：  

```
5 is in octal format
```  

###逻辑或　　

逻辑或运算符为 ||。该运算符语法如下： 　
 
```
expr1 || expr2
```  

如果 expr1 与 epxr2 至少其中一个为真，则最终结果为真；二者均为假时则为假。请注意，只有当 expr1 为假时才会计算 expr2 的值，若 expr1 为真则不会再计算　expr2 的值。示例如下：  

```
[jerry]$ awk 'BEGIN {ch = "\n"; if (ch == " " || ch == "\t" || ch == "\n") print "Current character is whitespace." }'
``` 

执行上面的命令可以得到如下的结果：  

```
Current character is whitespace.
```  

###逻辑非

逻辑非运算为感叹号(!)。此运算符语法如下：  

```
! expr1 
```  

逻辑非将 expr1 的真值取反。如果 expr1 为真，则返回 0。否则返回 1。下面的示例判断字符串是否为空：  

```
[jerry]$ awk 'BEGIN { name = ""; if (! length(name)) print "name is empty string." }'
``` 

执行上面的命令可以得到如下的结果：  

```
name is empty string.
```  

##三元运算符  

我们可以使用三元运算符来实现条件表达式。下面为其语法：  

```
condition expression ? statement1 : statement2
```   

当条件表达式（ condition  expression）为真时，statement1 执行，否则 statement2 执行。下面的示例将返回最大数值：  

```
[jerry]$ awk 'BEGIN { a = 10; b = 20; (a > b) ? max = a : max = b; print "Max =", max}'
```  

执行上面的命令可以得到如下的结果：  

```
Max = 20
```  

##一元运算符

AWK 支持如下几种一元运算符：  

###一元加运算

一元加运算符表示为 +。它将操作数乘以 +1。 

```
[jerry]$ awk 'BEGIN { a = -10; a = +a; print "a =", a }'
```  

执行上面的命令可以得到如下的结果：  

```
a = -10
```  

###一元减运算符

一元减运算符为 - 。它表示将操作数乘以 -1。

```
[jerry]$ awk 'BEGIN { a = -10; a = -a; print "a =", a }'
```  

执行上面的命令可以得到如下的结果：  

```
a = 10
```  

##指数运算符

下面将介绍两种形式的指数运算符：  

###幂运算符 ^

 ^ 运算符对操作数执行幂运算。下面的示例求 10 的二次幂。  

```
[jerry]$ awk 'BEGIN { a = 10; a = a ^ 2; print "a =", a }'
```  

执行上面的命令可以得到如下的结果：  

```
a = 100
```  

###幂运算符 **

 ** 运算符对操作数执行幂运算。下面的示例求 10 的二次幂。  

```
[jerry]$ awk 'BEGIN { a = 10; a = a ** 2; print "a =", a }'
```  

执行上面的命令可以得到如下的结果：  

```
a = 100
```  

##字符串连接操作符  

空格 (space) 操作符可以完成两个字符串的连接操作。示例如下：  

```
[jerry]$ awk 'BEGIN { str1="Hello, "; str2="World"; str3 = str1 str2; print str3 }'
```  

执行上面的命令可以得到如下的结果：  

```
Hello, World
```  

##数组成员操作符

数组成员操作符为 in。该操作符用于访问数组元素 。下面的示例用于此操作符输出数组中所有元素。  

```
[jerry]$ awk 'BEGIN { arr[0] = 1; arr[1] = 2; arr[2] = 3; for (i in arr) printf "arr[%d] = %d\n", i, arr[i] }'
```  

执行上面的命令可以得到如下的结果：  

```
arr[0] = 1
arr[1] = 2
arr[2] = 3
```  

##正则表达式操作符  

下面将介绍两种正则表达式操作符:  

###匹配（Match） 

匹配运算符为 ~。它用于搜索包含匹配模式字符串的域。下面的示例中将输出包括 9  的行：  

```
[jerry]$ awk '$0 ~ 9' marks.txt
```  

执行上面的命令可以得到如下的结果：  

```
2)	Rahul	Maths	90
5)	Hari	History	89
```  

###不匹配(Not match)  

不匹配操作符为 !~。 此操作符用于搜索不匹配指定字符串的域。如下示例输出不包含 9 的行：  

```
[jerry]$ awk '$0 !~ 9' marks.txt
```  

执行上面的命令可以得到如下的结果：  

```
1)	Amit	Physics	80
3)	Shyam	Biology	87
4)	Kedar	English	85
```  