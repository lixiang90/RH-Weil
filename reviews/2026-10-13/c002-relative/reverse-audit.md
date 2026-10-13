# C002 相对反向核界：不同组织方式逆审

2026-10-13；基线 `3a72930e9f9f554b03b41d17d8c8002f1813ca82`。
本次恢复已读AGENTS/README/STATE，执行check/show，读长期Goal、
C002、D20261013B及527来源原件、qw函数。
恢复时仅c002-relative新文件未跟踪；Get-Process未列出Python。
不改STATE/cadence，不启动谱样本，不计算零点。

**结论：** `reflection-relative-bound-audit.md`的固定L=log13结论成立，
量词确为 `∀有限实C ∀M0 ∃M≥M0`，而非单个向量或有限cutoff。
背景5常数安全，但可用复数能量核给严格常数1及完整渐近
`hBG(vM)=1/(8M³)+O_L(M^-4)`。
真实prime余项、Cesaro负子序列和密度论证正确。
无需额外样本，同证明适用于每个素数端点P≥3。
这是辅助反向核的严格方法类边界；不等于完整Weil下界失败或长期Goal完成。

## 1. 原证明逐项核验

原件中的 `|r'_t|≤4tx/(t²+x²)²` 使用y≤2x，
以及 `|s'_t|≤1/(t²+x²)` 均正确。
平方相加中r项的比值16t²x²/(t²+x²)²≤4，s项≤1，
所以 `|Δr|²+|Δs|²≤5κ²/(t²+x²)²`没有漏项。
步长2、起点1/2的递减和积分上界
`sum(tj²+x²)^−2≤x^-4+π/(8x³)`亦正确。
527的背景Gram通道、正原权、完整素数幂清单及端点sine零均保留。

对vM=eM−e(M+1)，prime单源的两条diagonal与off-diagonal直接合并给

\[
h_R(v_M)=\sum_k\frac{w_k}{\pi(2M+1)}
\left(\frac{\sin M\theta_k}{M}
-\frac{\sin(M+1)\theta_k}{M+1}\right).
\tag{1}
\]

两系数相对于1/(2M²)的误差绝对值分别是
`1/[2M²(2M+1)]≤1/(4M³)`、
`(3M+1)/[2M²(M+1)(2M+1)]≤3/(4M³)`。
后一个不等式乘正分母归为
`4M(3M+1)≤6(M+1)(2M+1)`，右减左为14M+6>0。
所以 `hR=T_M/(2πM²)+E_M`，`|E_M|≤W/(πM³)`正确，
其中W=sum w_k，所有k<13的实际素数幂都参与。
没有换权、移动原子、漏掉实偶原子对或多乘2。

## 2. 不同能量核组织：精确相邻差与背景渐近

令κ=2π/L、x=κM、y=κ(M+1)、tj=2j+1/2、
γ=8sinh²(L/4)/L、cj=1−exp(−tjL)。
把原件的两个实Gram通道组织成一个复数Cauchy通道

\[
F_t(z)=r_t(z)+i s_t(z)=\frac1{t-iz}.
\]

其相邻差不是仅有导数上界，而是有严格恒等式

\[
|F_t(x)-F_t(y)|^2
=\frac{(y-x)^2}{(t^2+x^2)(t^2+y^2)}
=\frac{\kappa^2}{(t^2+x^2)(t^2+y^2)}.
\tag{2}
\]

因此精确地

\[
h_A(v_M)=\frac{2\kappa^2}{L}\sum_{j\ge0}
\frac{c_j}{(t_j^2+x^2)(t_j^2+y^2)},\quad
h_P(v_M)=\frac{\gamma\kappa^2}{(1/4+x^2)(1/4+y^2)}.
\tag{3}
\]

有限非零vM使hA>0。由y>x，(2)直接给
`|Δr|²+|Δs|²≤κ²/(t²+x²)²`，
原5常数可降为1，无需均值定理和y≤2x。
于是对所有M≥1

\[
0<h_{BG}(v_M)\le K_L M^{-3},\qquad
K_L=\frac2L\left(\kappa^{-2}+\frac\pi{8\kappa}\right)
+\gamma\kappa^{-2}<\infty.
\tag{4}
\]

**完整渐近的证明。** 设
`f(t)=1/[(t²+x²)(t²+y²)]`，它正且递减。
递减和积分比较给

\[
\frac12\int_{1/2}^\infty f(t)dt
\le\sum_{j\ge0}f(t_j)
\le f(1/2)+\frac12\int_{1/2}^\infty f(t)dt.
\]

减去从0开始的半积分，差的绝对值≤f(0)≤x^-4。
指数修正的绝对值≤x^-4 qL，其中
`qL=sum_j exp(−tjL)=exp(−L/2)/(1−exp(−2L))`。
分式积分可直接分解为两条arctan积分，精确为

\[
\int_0^\infty f(t)dt=\frac\pi{2xy(x+y)}.
\]

代入(3)，得到严格误差账本

\[
\left|h_A(v_M)-\frac1{4M(M+1)(2M+1)}\right|
\le\frac{2(1+q_L)}{L\kappa^2}M^{-4}.
\tag{5}
\]

pole项由(3)在0与γκ^-2M^-4间；所以

\[
h_{BG}(v_M)=\frac1{8M^3}+O_L(M^{-4}).
\tag{6}
\]

大O已由(5)和pole界完全支付。
这里L固定；虽然主系数1/8不依赖L，余项常数依赖L，
不能免费交换M→∞与L→∞或称为联合一致渐近。
这从能量核恒等式得到，不依赖原导数估计或新数值采样。

## 3. 不同频率组织：指数系数与Cesaro二阶

固定L=log13，K={2,3,4,5,7,8,9,11}，
zk=exp(iθk)，θk=2πlogk/log13，wk=Λ(k)/sqrt(k)>0。
写

\[
b_k=\frac{w_k(1-z_k)}{2i},\qquad
T_M=\sum_{k\in K}\left(b_kz_k^M+\overline{b_k}\overline{z_k}^{,M}\right).
\tag{7}
\]

这从 `T_M=Im sum wk(1−zk)zk^M`直接得到，
与原件的cosine差公式组织不同。
各zk≠1。zk=zl迫使k=l；zk=bar(zl)迫使kl=13。
有效k,l均在(1,13)，13为素数，后者不可能；
尤其zk=bar(zk)的自碰撞会要求k²=13，也不可能。
不需要logk有理独立；k=2,4,8的整倍关系不影响这里的±成对频率分离。

对ζ≠1，`Q^-1 sum_(M=1)^Q ζ^M→0`由有限几何和直接成立。
把(7)平方，只有同k的 `zk^M·bar(zk)^M` 两个有序项留下：

\[
\langle T\rangle_Q\longrightarrow0,\qquad
\langle T^2\rangle_Q\longrightarrow
S=2\sum_k|b_k|^2
=2\sum_k w_k^2\sin^2(\theta_k/2)>0.
\tag{8}
\]

这直接核验了所有二阶项，没有遗漏同原子2θk频率。
每个非零b_k也说明生成函数
`sum_(M≥1)T_M z^M`
由极点互异的有限有理项
`b_k zk z/(1−zk z)+bar(bk) bar(zk)z/(1−bar(zk)z)`组成，
不是恒零序列；但(8)比“非恒零”更强，足以支付固定负幅度。

## 4. 固定负幅度、下密度与量词

取B=2sum|bk|=2sum wk sin(θk/2)>0，则|T_M|≤B，
`T_M²≤B|T_M|`。由(8)

\[
\liminf_Q\langle (T_M)_-\rangle_Q
=\frac12\liminf_Q\langle |T_M|-T_M\rangle_Q
\ge\frac{S}{2B}.
\]

选c=S/(4B)。逐M有
`(T_M)_-≤c+B 1_(T_M<−c)`，因此

\[
\liminf_Q\frac{\#\{1\le M\le Q:T_M<-c\}}Q
\ge\frac{S}{4B^2}>0.
\tag{9}
\]

strict不等号没有边界漏洞：T=−c时负部恰为c，仍满足逐项界。
这保证任意大M在负子序列，不只是出现一次负值。

给定任意有限实C及M0，令C+=max(C,0)，在该子序列上

\[
h_R(v_M)+C h_{BG}(v_M)
<-\frac{c}{2\pi M^2}
+\frac{W/\pi+C_+K_L}{M^3}.
\]

选择M≥M0并大于 `(2π/c)(W/π+C+ KL)` 即严格负。
所有常数在选择M前固定；这证明要求的

\[
\forall C\in\mathbb R\ \forall M_0\in\mathbb N\
\exists M\ge M_0:\quad h_R(v_M)+C h_{BG}(v_M)<0.
\tag{10}
\]

hBG严格正，因此负子序列上比值趋向负无界；(6)还显式说明
ratio具有 `hR/hBG=(4/π) M T_M+O_L(1)`，T_M有统一界使误差合法。
正规化vM只同除2，结论不变。
对固定N仍有某个有限CN，因为有限HBG严格正；(10)不否认有限截面事实。

## 5. 素数端点的无新样本泛化

应父代理追加要求审查：令μ=P为任意素数P≥3，L=logP，
K为所有素数幂k<P，wk使用同一实际原权。
527的背景表达及(2)–(6)对每个L>0均成立。
K至少含k=2，zk≠1；所有±频率碰撞仍只可能是k=l或kl=P，
素性排除kl=P，包括self k²=P。
所以(7)–(10)逐个端点同样成立，准确量词为

\[
\forall P\ge3\ (P\text{ prime})\quad
\forall C\in\mathbb R\quad\forall M_0\in\mathbb N\quad
\exists M\ge M_0:\ h_{R,P}(v_M)+C h_{BG,P}(v_M)<0.
\tag{11}
\]

c、B、S、KL及选择M的门槛可依赖P，没有宣称单个M同时处理全部P。
该族实际lambda=sqrt(P)无界，但(11)并不提供λ/M联合一致极限。
μ=2无内部原子且endpoint sine零，R=0，不能包含。
一般μ有反射频率共振，必须先合并；例如μ=4的k=2有θ=π，
其实际sine序列为零，若照搬无碰撞二阶式会错误记入正贡献。
这说明不能无审查声称任意μ；并不说明μ=4的整体结论必失败，
因为其k=3仍是有效非共振原子。

## 6. 相对基线、完整W及后续准入

016排除的是完整QW=P−V中指定逐块绝对范数步骤的lambda线性损失。
本结果在固定L、M→∞保留signed原子，排除辅助H的统一背景相对常数。
对象、极限和估计类别不同；不把016改名，也不重记527的单向量反例。
与基线相关件的局部核对足以说明该差别；没有全526篇逐篇审查或外部首创证明。

不得将H_R≥−C HBG失败改成完整W不存在下界。
H仅是W(n,−m)，没有同号B块、完整奇O能量、常数模d与a0。
W的正性完全可与(10)相容；这族vM也不是已识别真正奇最低态。
沿反例子序列绝对prime能量为O(M^-2)，
任意固定正质量误差epsilon||v||²不能由此族自动排除。
依赖N的常数、独立限制的低谱空间、同阶M^-2或更强的另背景，
以及完整O/H/d/a0联合估计都是未被排除的逃逸条件。

真实新增是整个有限支持域的固定背景相对费用不存在，
并给无样本的素数端点无界族；仍没有支付完整算术正性。
宏观瓶颈未改变，不能因此完成长期Goal。
停止：冻结所有有限正指标上这条无质量误差的背景相对下包技巧。
重新准入：空间限制有独立算术依据、明确可支付质量预算，
或同一完整实际对象的新联合coercivity；增加N/小数不改变(10)。
唯一下一动作：主代理消费本不同组织方式逆审及原证明后，
结算C002的限定方法边界，再选择能保留完整奇能量与常数交叉的新实际输入。
本子审查不消费轮数，不把合同结束当Goal完成。
