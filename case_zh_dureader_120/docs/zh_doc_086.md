# 中文复杂检索文档

## 背景材料1
用Mathematica求定积分 http://xuxzmail.blog.163.com/blog/static/251319162011784175529/用Mathematica求广义积分 http://xuxzmail.blog.163.com/blog/static/2513191620117842723766/用Mathematica求积分变限函数的导数 http://xuxzmail.blog.163.com/blog/static/251319162011781000989/

## 背景材料2
§1 Mathematica简述与函数求值.doc §10 用Mathematica进行级数运算.doc §10 用Mathematica进行级数运算练习参考解答.doc §11 用Mathematica进行广义积分运算.doc §11 用Mathematica进行广义积分运算练习参考.doc §2 Mathematica进行代数运算和求极限.doc §2 Mathematica进行代数运算和求极限练习解.doc §3 Mathematica求导数与微分.doc §3 Mathematica求导数与微分答案与提示.doc §4 Mathematica求不定积分与函数作图.doc §4 Mathematica解导数的应用问题.doc §4 Mathematica解导数的应用问题练习参考解.doc §5 Mathematica求不定积分与函数作图.doc §5 Mathematica求不定积分与函数作图练习参.doc §6 Mathematica求定积分以及相关应用问题.doc §6 Mathematica求定积分以及相关应用问题练.doc §7 用Mathematica求偏导数与多元函数的极值.doc §7 用Mathematica求偏导数与多元函数的极值参考答案.doc §8 用Mathematica求重积分以及相关的应用.doc §8 用Mathematica求重积分以及相关的应用练.doc §8 用Mathematica进行代数运算和求极限.doc §9 用Mathematica求曲线积分与曲面积分.doc §9 用Mathematica求曲线积分与曲面积分练习.doc

## 关键材料
1, 定积分的求解主要命令是Integrate[f,{x,min,max}]， 或者使用工具栏输入也可以。例如求 In[6]:=Integrate[x^2Exp[ax],{x,-4,4}]. 这条命令也可以求广义积分. 例如求 In[7]:=Integrate[1/(x-2)^2,{x,0,4}] 求无穷积也可以，例如 In[8]:=Integrate[1/x^4,{x,1,Infinity}] 如果广义积分发散也能给出结果，例如： In[9]:=Integrate[1/x^2,{x,-1,1}] 如果无法判定敛散性，就用给出一个提示. 2, 数值积分是解决求定积分的另一种有效的方法，它可以给出一个近似解。特别是对于用Integrate命令无法求出的定积分，数值积分更是可以发挥巨大作用。 它的命令格式为： Nintegrate[f,{x,a,b}] 在[a,b]上求f数值积分 3, 除了上述简单情形外, Integrate可以还可以求不定积分, 二重积分,三重积分. 具体参见其帮助文件.

## 补充材料1
PAGE PAGE 1 分别用复化梯形公式、复化Simpson公式计算定积分,取n=2,4,8,16分别验证结果(精确值I=4.006994)。复化梯形公式求定积分: function I=tquad(x,y) %复化梯形求积公式,其中, %x为向量,被积函数自变量的等距结点; %y为向量,被积函数在结点处的函数值; n=length(x); m=length(y); %积分自变量的结点数应与它的函数值的个数相同 h=(x(n)-x(1))/(n-1); a=[1 2*ones(1,n-2) 1]; I=h/2*sum(a.*y); 复化Simpson公式求定积分: function I=squad(x,y) %复化Simpson求积公式,其中, %x为向量,被积函数自变量的等距结点; %y为向量,被积函数在结点处的函数值; n=length(x); m=length(y); %积分自变量的结点数应与它的函数值的个数相同 if rem(n-1,2)~=0 I=tquad(x,y); return; end N=(n-1)/2; h=(x(n)-x(1))/N; a=zeros(1,n); for k=1:N a(2*k-1)=a(2*k-1)+1; a(2*k)=a(2*k)+4; a(2*k+1)=a(2*k+1)+1; end I=h/6*sum(a.*y);

## 补充材料2
Limit[expr,x-c,Direction--1] 微分:D[f,x] 函数f对x作微分 D[f,x1,x2,…] 函数f对x1,x2,…作微分 D[f,{x,n}] 函数f对x微分n次 D[f,x,NonConstants-{y,z,…}] 函数f对x作微分，将y,z,…视为x的函数 全微分:Dt[f] 全微分df Dt[f,x] 全微分 Dt[f,x1,x2,…] 全微分 Dt[f,x,Constants-{c1,c2,…}] 全微分，视c1,c2,…为常数 不定积分:Integrate[f,x] 不定积分 ∫f dx 定积分:Integrate[f,{x,xmin,xmax}] 定积分 Integrate[f,{x,xmin,xmax},{y,ymin,ymax}] 定积分 列之和与积:Sum[f,{i,imin,imax}] 求和 Sum[f,{i,imin,imax,di}] 求数列和，引数i以di递增 Sum[f,{i,imin,imax},{j,jmin,jmax}] Product[f,{i,imin,imax}] 求积 Product[f,{i,imin,imax,di}] 求数列之积，引数i以di递增
