# 336. 同一物理determinant和的有限域完成

2026-09-07。周期8第2动作。[T候选，独立复核待完成]。
得到的是包含完整Kloosterman和的精确恒等式；还不是可用的双线性节省。
所用有限域determinant Fourier公式是经典机制，不宣称其原创。

## 1. 无别名的模数与固定离纤维延拓

沿用335的X、L、Y、I_X、M=X^1/2、全部prime-power mask，
以及P_ab、K_X和共同平均bar K_X(M)。令U=floor(1.30Y)。
选素数p满足4U²<p<8U²；Bertrand定理保证可选，故p asymp Y²=X^3/2。
使用p区别于335原始正权q_ab；本篇不选择复合模数，不能使用特殊pq的更强节省。

令H=ceil(U²(exp(M/X)-1))。充分大X时H=O(X)<U²，
且所有335实际非零determinant均位于[-H,H]。
对a,b,c,d in I_X，|ad-bc|<=U²，故|ad-bc-h|<p。
因此对|h|<=H，
\[
 ad-bc\equiv h\pmod p\quad\Longleftrightarrow\quad ad-bc=h. \tag{1}
\]
这保留完整整数等式，不仅保留同余；没有遗漏同素数底或gcd>1分层。

为了在整个四维有限域上完成，必须明确离开determinant纤维后的系数。
令
\[
 C(a,b,c,d)=q_{ab}q_{cd}
 {\bf1}_{a,b,c,d\in I_X}
 {\bf1}_{\text{335的两个distinct-base条件}},
\]
仅在四者为prime powers时非零。对每个h≠0，设
t_h=X log(1+h/(bc))，若1+h/(bc)<=0则以下系数置0。
在本参数和支持下充分大X时这一异常不会发生。
定义
\[
 {\cal W}_{ab;cd}(\delta)
 ={1\over L}\int_{-L/2}^{L/2}P_{ab}(u)P_{cd}(u-\delta)\,du,
\]
\[
 F_h(a,b,c,d)=C(a,b,c,d)\,
 {\cal W}_{ab;cd}(t_h/X)
 {\bf1}_{|t_h|\le M}\{K_X(t_h)-\bar K_X(M)\}.             \tag{2}
\]
四个坐标使用0,...,p-1的整数代表，I_X外统一置0。
该延拓在本周期固定；不是为了优化Fourier范数而可自由改变的gauge。
在ad-bc=h上，t_h=X log(ad/bc)，故精确恢复335同一重叠与响应。
于是
\[
 {\cal R}_X=\sum_{0<|h|\le H}
       \sum_{\substack{A\in{\rm Mat}_2(\mathbb F_p)\\\det A=h}}
                     F_h(A),\qquad A=\begin{pmatrix}a&b\\c&d\end{pmatrix}.
                                                               \tag{3}
\]
这里F_h保留全部四Lambda、物理通道合并、六窗、共同中心项和h=0的删除。
不是对某一个通道单独作完成，也未将W取绝对值后改定义。

## 2. 自含推导完整Kloosterman核

对xi=(alpha,beta,gamma,delta) in F_p^4，记
xi·A=alpha a+beta b+gamma c+delta d，
D(xi)=alpha delta-beta gamma，e_p(z)=exp(2pi i z/p)。
标准未归一化Kloosterman和记为
S(m,n;p)=sum_{v in F_p^*}e_p(mv+n/v)。
有限域determinant纤维的Fourier和精确满足
\[
 T_h(\xi):=\sum_{\det A=h}e_p(\xi\cdot A)
     =p^3{\bf1}_{\xi=0}+p S(h,D(\xi);p).                \tag{4}
\]
本式对所有h也成立；应用(3)时只用0<|h|<p。

证明：用p^-1 sum_v e_p(v(det A-h))表示det条件。
v=0项为p³ 1_{xi=0}。
v≠0时，先求a、b的完整和，分别迫使
d=-alpha/v、c=beta/v，留下
p² e_p((beta gamma-alpha delta)/v)。
再乘e_p(-hv)/p，并令v变为-v，即得(4)。
符号、p因子以及xi=0项均由有限求和确定。
当h≠0，T_h(0)=p³-p，与SL2(F_p)的大小一致。

定义
\[
 \widehat F_h(\xi)=\sum_{A\in F_p^4}F_h(A)e_p(-\xi\cdot A).
\]
Fourier反演与(4)给
\[
 \boxed{{\cal R}_X={\cal M}_0+{\cal E}_{\rm Kl},}
\quad
 {\cal M}_0=(p^{-1}-p^{-3})\sum_{0<|h|\le H}\widehat F_h(0),
                                                               \tag{5}
\]
\[
 {\cal E}_{\rm Kl}
 =p^{-3}\sum_{0<|h|\le H}\sum_{\xi\ne0}
             \widehat F_h(\xi)S(h,D(\xi);p).             \tag{6}
\]
xi≠0但D(xi)=0的项仍在(6)，此时S(h,0;p)=-1；
不能把“去零Fourier模”误写成“去掉全部退化dual determinant”。
Kl2规范为p^-1/2 S(h,D;p)；h为非零单位时
S(h,D;p)=S(hD,1;p)，所以(6)也可写为p^-5/2乘对应Kl2和。
该规范变换不产生额外节省。

## 3. 与双线性定理还有哪些差别

把四维频率按D(xi)=n合并，可精确写
\[
 A(h,n)=\sum_{\substack{\xi\ne0\\D(\xi)=n}}\widehat F_h(\xi),
 \qquad
 {\cal E}_{\rm Kl}=p^{-3}\sum_{0<|h|\le H}\sum_{n\bmod p}
                           A(h,n)S(h,n;p).              \tag{7}
\]
这产生的是实际二维系数数组A(h,n)，不是已经证明可分离的alpha_h beta_n。
h的当前整段长度O(X)=O(p^2/3)，n可占全部模p。
四个Fourier坐标也各在全部模p范围；prime-power系数不是平滑权，
不能因原整数区间长Y约sqrt(p)，就认定Fourier支持截在p/Y约sqrt(p)。

Pascadi/MQW的所列定理针对两条分离系数序列及指定长度。
要从(7)应用它们，必须建立保留实际相消且范数可控的分离／局部化；
矩阵奇异值分解形式上的存在性不提供所需核范数预算。
全模数n范围及h长度也不能免费当作两条平方根长区间。

## 4. 一个合法但不够用的基准上界

以下只展示范数核算，绝不当作实际响应的下界或所有变换方法的障碍。
Chebyshev及Lambda(n)<=log n给
sum_{n in I_X}Lambda(n)²/n<=C L。
由|W|<=1、|K-bar K|<=2及全部四Lambda权，
\[
 \|F_h\|_{\ell^2(F_p^4)}\ll L^2.                         \tag{8}
\]
本式含I_X外的零延拓；不把系数视为1-bounded后漏掉归一化。
Parseval给||Fhat_h||2=p²||F_h||2，而频率数p4，
故sum_xi|Fhat_h(xi)|<=p4||F_h||2。
在h≠0时，经典点态Weil界统一给|S(h,n;p)|<=2sqrt(p)，
含n=0的-1。代入(6)只得到
\[
 |{\cal E}_{\rm Kl}|\ll H p^{3/2} L^2
                  \ll X^{13/4}L^2.                    \tag{9}
\]
这个上界远高于所需o(L4)，甚至可能弱于直接整数计数。
它说明此通用Parseval步骤没有产生可用节省，不证明E_Kl实际大。
不能把某个外部双线性p^-epsilon未经适用性检查乘到(9)上。

下一动作先控制(5)真正的零Fourier模及共同中心项，
再判断能否在保留物理方向时改善(7)的系数与长度。
没有遗漏外部负项或偷偷引入RH；当前只是一个准确的算术完成及范围账本。
