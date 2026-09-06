# 新Kloosterman来源独立条款复核

2026-09-07。Gibbs只读内部模型复核。本文是主线程按报告整理的结论和处理，
不是外部同行评审，也不是三个长篇解析证明的完整认证。
被审screen原件SHA256：
0c3d753a226c76a2b5ba816693b165d68df3cac62ff2f690a69567abe71ad208。

## 核读范围与原件

- Pascadi arXiv v2，第1–5页；另定位第36页Thm7.1和41–42页Thm7.8陈述，
  未审技术证明。SHA256 88f94994462840e2b03bd9cea38776fa3b65d1023dc6dfe00475bb1fceb47e8e。
- Milićević–Qin–Wu v1，第1–4页。SHA256
  f53a2ef9040b1c6573a2290b372a0fe9c4fefda61882281ca6ce4ee90fc163c6。
- Choi–Kumchev v1，第1–2页。SHA256
  1165d6e6f7a41196bf60b1fc9d901587d7fad4881aaecb2f784a39e72d3bb768。

Pascadi正式GAFA PDF是主线程此后另行归档的70页版本，
不在这份独立复核范围。日期和版本不能混为同一原件。

## 发现与已采用的修正

1. 两种归一化及主要指数正确，但必须写出支撑、互素和系数族。
   (a,q)=1、(m,n,q)=1时，通过局部单位替换及CRT有
   S(am,n;q)=S(amn,1;q)=sqrt(q)Kl2(amn;q)；
   此条件不要求m,n各自都为单位。
   无互素条件不成立，例如S(2,2;4)=2而S(4,1;4)=0。
2. Pascadi Thm1.1的支撑是初始区间[1,M],[1,N]，不是任意平移短区间。
   另一条1-bounded alpha界是sqrt(M)||beta|| c^(1-1/276+o(1))，
   附(gcd(n,c)=1)，不能自由换sqrt(M)为||alpha||。
   Thm1.2允许任意整数区间，c=dd'e、d'|d、(d,e)=1，
   f=max{r:r²|cd}，界为norm乘c^(1+o)(f/min(c,d²))^(1/6)。
   c/d平方自由时f=d。特殊p²/平衡pq的c^-1/12是相对norm乘c，
   只有M,N约sqrt(c)才同样是相对组合平凡界的节省。
   对短长度，平凡尺度是norm乘sqrt(MNc)。
   较宽平衡长度范围来自Thm7.1三项式，并非统一1/12。
   Thm7.8仍使用初始区间。
3. MQW Thm1.1使用初始区间、任意复系数，没有gcd(mn,q)或gcd(m,n,q)限制。
   原screen三项式、长度条件与平衡指数-1/12,-1/100,-1/64正确；
   常数可依epsilon，其余参数统一。平移支撑零延拓须使用右端点，
   不能把长度直接代入M,N。第4页Thm2.1的dyadic版本另带s|q条件。
4. Choi–Kumchev完整族：m,r>=1,Q>=r,T,N>=2；
   chi=xi psi mod mq，xi为mod m的任意字符，psi为mod q本原字符，
   r<=q<=Q、r|q、(q,m)=1。它是未归一化L1总和。
   H=m r^-1 Q² T、L=log(HN)，C可取1100。
   权为Lambda，不是任意系数。GRH Remark2的NL+H N^.5 L²中
   NL只在含主字符时出现；无条件定理的N项不能据此删除。
5. 版本日期正确；Choi–Kumchev的PDF draft 2018字样本身
   不能证明有2018年实质新修订。

以上范围修正已写回screen。独立复核支持准确引用这些陈述，
并未建立实际四素数响应到任一双线性定理的合法映射。
