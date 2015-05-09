#AWK——输出重定向  
到目前为止我们显示的数据都是输出到标准输出流中。但是我们可以将数据重定向到文件中。重定向操作往往出现在 print 或者 printf 语句中。 AWK 中的重定向方法与 shell 重定向十分相似，除了 AWK 重定向是用于 AWK 程序中。本章节将讲述重定向的使用方法：  
##重定向操作符  
重定向操作符的语法如下：  
```
print DATA > output-file
```  
上述将数据重定向输出到 output-file中。 如果 output-file 文件不存在，则创建该文件。使用这种方式重定向时，数据输出前会将 output-file 文件中之前的数据删除后才输出数据。下面的示例中将 Hello,World!!! 消息输出到文件中。  
先创建文件并在文件中输入一些数据。  
```
[jerry]$ echo "Old data" > /tmp/message.txt 
[jerry]$ cat /tmp/message.txt
```  
执行上面的代码可得到如下结果：  
```
Old data
```  
再用 AWK 重定向操作符重定向数据到文件 message.txt 中。  
```
[jerry]$ awk 'BEGIN { print "Hello, World !!!" > "/tmp/message.txt" }'
[jerry]$ cat /tmp/message.txt
```  
执行上面的代码可得到如下结果：  
```
Hello, World !!!
```  
##赋加操作符  
赋加操作符的语法如下：  
```
print DATA >> output-file
```  
用这种重定向方式将数据赋加到 output-file 文件的末尾。如果文件不存在则创建该文件。示例如下：  
创建文件并输入一些数据：  
```
[jerry]$ echo "Old data" > /tmp/message.txt 
[jerry]$ cat /tmp/message.txt
```  
执行上面的代码可得到如下结果：  
```
Old data
``` 
再使用 AWK 赋加操作符赋加内容到文件中：  
```
[jerry]$ awk 'BEGIN { print "Hello, World !!!" > "/tmp/message.txt" }'
[jerry]$ cat /tmp/message.txt
```  
执行上面的代码可得到如下结果：  
```
Old data
Hello, World !!!
```  
##管道  
除了使用文件在程序之前传递数据外，AWK 还提供使用管道的方式将一个程序的输出传递给另一个程序。这种重定向方式打开一个管道，一个命令将值通过管道传递给另外一个命令来执行。下面是管道的使用方法：  
```
print items | command
``` 
我使用 tr 命令将小写字母转换成大写。  
```
[jerry]$ awk 'BEGIN { print "hello, world !!!" | "tr [a-z] [A-Z]" }'
```  
执行上面的代码可得到如下结果：  
```
HELLO, WORLD !!!
```  
##双向通信  
AWK 允许使用 |& 与一个外部进程通信，并且是双向通信。比如下面的例子中，使用 tr 命令将字母转换为大写字母。 command.awk 文件内容如下：  
```
BEGIN {
	cmd = "tr [a-z] [A-Z]"
	print "hello, world !!!" |& cmd
	close(cmd, "to")
	cmd |& getline out
	print out;
	close(cmd);
}
```  
执行上面的代码可得到如下结果：  
```
HELLO, WORLD !!!
``` 
脚本的内容看上支很神秘吗？让我们来揭开它神秘的面纱。  
第一条语句 cmd = "tr [a-z] [A-Z]" 在AWK 中建立了一个双向的通信通道。
第二条语句 print 为 tr 命令提供输入。&| 表示双向通信。  
第三条语句 close(cmd, "to") 完成任务后关闭 to 进程。  
第四条语句 cmd |& getline out 使用 getline 函数将输出存储到 out 变量中。  
接下来的输出语句打印输出的内容，最后 close 函数关闭 cmd。


