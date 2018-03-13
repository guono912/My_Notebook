//考虑到今天大计基讲了这个以及以前学的时候写过这个，决定再把进制转化这个例子拿出来练练
//Asc码什么的转换反应了半天才绕出来，真的是吃枣药丸
program jinzhi(input,output);  //虽然不涉及读写文件，但带上是个好习惯
var s,i,jz1,jz2:integer;
    num,res,ch:string;
    shi:longint;
begin write('number is?');read(num);writeln;
      write('jinzhi1=');read(jz1);writeln;
      write('jinzhi2=');read(jz2);writeln;
      for i:=1 to len(num) do
        begin
          if num[i] in ['0'..'9'] then s:=ord(num[i])-48   
          else s:=ord(num[i])-55;   //利用ascii码将字符串化为数字
          shi:=shi*jz1+s;     //很经典的一句，把这句放在循环中就可以实现乘方，而不必对乘以几次方进行判断
        end;
{以上实现了x进制转为十进制，以下继续由10进制转化为y进制}        
      while shi<>0 do
      begin
        if (shi mod n) in ['0'..'9'] then ch:=chr((shi mod n)+48)
        else ch:=chr((shi mod n)+55);    //又变回字符
        res:=res+ch;   //一位一位排好
        shi:=shi div n 
      end;
      writeln(res);
end.
