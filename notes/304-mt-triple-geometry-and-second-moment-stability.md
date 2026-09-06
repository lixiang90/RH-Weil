# 304. MT 三点几何与二阶稳定性增益：独立重建和证书接口

2026-09-06。有限准入问题：实际 Montgomery--Taylor 窗口的三点几何，
能否排除原二阶 rank--trace 不等式的渐近取等，而不新增四阶算术假设？
本轮主线为二阶稳定性审计；辅助为独立逆向证明和有理三点证书。
VIS-1 不再追加模型；MOM-1 的四阶算术任务、NCE-8、DL-AUDIT 均未重启。

状态：[T] 本篇完整证明的有限稳定性、三点几何和基于已知算术输入的后果；
[R] 无条件相关公式及固定平滑去权；[E] 未认证浮点优化；
[O] 具体贡献的优先权与外部审查；第8节的 \(1/10000\) 全域有理证书已验收。

**优先权警示。** Yuhang Shi 的公开工作稿
[A Schur--Jensen Gain in the Critical-Line Zero Problem](https://www.researchgate.net/publication/412210529_A_SCHUR-JENSEN_GAIN_IN_THE_CRITICAL-LINE_ZERO_PROBLEM)
（文内日期2026-08-12）已保留同类谱余项，再以不交配对和 MT 根避让取严格增益。
本轮在独立推导后检索到该稿，已核读其 Lemmas 2.1--2.2 和相关间距机制。
以下谱桥是独立重建，**不主张首次发现 Schur--Jensen 严格增益**。
本篇改用完整三点块、直接 Hilbert 特征及 Lamzouri 的固定平滑接口。
外部稿件的其他数值、Gabor边界及后续大规模证书不进入本篇证明链。

## 1. 结论形式和已知算术输入

记 \(N(T)\) 为正高度 \(0<\gamma\le T\) 的非平凡零点总重数，
\(s(T)\) 为简单临界线零点数，\(D(T)\) 为不同零点数。置
\[
 R_0=\tfrac12+\tfrac1{\sqrt2}\cot(1/\sqrt2),\qquad
 C_0=2-R_0=0.6725007036794\ldots .
 \tag{1}
\]
定义 sharp MT 概率密度及其 Fourier 核
\[
 f_0(u)=\frac{\cos(\sqrt2u)}{\sqrt2\sin(1/\sqrt2)}
                      1_{[-1/2,1/2]}(u),\qquad
 K_0(v)=\int f_0(u)e^{-2\pi ivu}\,du .
 \tag{2}
\]
对 \(B>0\)，本篇唯一有限几何证书是
\[
 \mathcal M(B,\mu):\qquad
 K_0(a)^2+K_0(b)^2+K_0(a+b)^2\ge\mu
 \quad(a,b\ge0,\ a+b\le B),\qquad 0<\mu<2 .
 \tag{3}
\]
变量 \(a,b\) 是归一化**间距**，不是假想零点的深度。

### 定理304-A：三点证书的实际比例接口 [T/R]

若 (3) 成立，则无条件有
\[
 \liminf_{T\to\infty}\frac{s(T)}{N(T)}
   \ge p(B,\mu):=\frac{C_0-\mu/B}{1-\mu/2},\qquad
 \liminf_{T\to\infty}\frac{D(T)}{N(T)}
   \ge\frac{1+p(B,\mu)}2 .
 \tag{4}
\]
“若”仅隔离有限初等函数证书，**不是**四矩或 RH 假设。
第4节完整解析证明
\[
 \mathcal M\bigl(4,(1/110000)^2\bigr).
 \tag{5}
\]
所以本篇已给一项无需计算机证书的严格 \(p>C_0\) 后果，
因为 \(C_0>1/2\)。第8节另以精确有理区间计算证明
\(\mathcal M(4,1/10000)\)，得到 \(p_*=0.672509329145868939\ldots\)。
浮点寻优不参与该下界的证明。
本篇不把 (4) 称为已获外部承认的新纪录或新颖性结论。

独立算术输入只有：

1. Riemann--von Mangoldt 计数 \(N(T)\sim T\log T/(2\pi)\)；
2. 对每个固定实偶 \(\eta\in C_c^\infty((-1/2,1/2))\)、
   \(\int\eta^2=1\)，令 \(K=\widehat{\eta^2}\)、\(Q=\eta^2*\eta^2\)，则
   \[
   \sum_{0<\gamma,\gamma'\le T}
    K\!\left(i(\rho-\rho')\frac{\log T}{2\pi}\right)^2
    =\bigl(C_\eta+o_\eta(1)\bigr)N(T),\qquad
   C_\eta=Q(0)+2\int_0^1uQ(u)\,du .
   \tag{6}
   \]

(6) 是 [Lamzouri, §3 Lemma3.2的证明](https://arxiv.org/html/2609.02882v1)
由 BGST 的无条件相关公式去权所得 [R]；第5节单独重建去权步骤和极限次序。
该输入对全零点求和，个别项未必非负；绝不从其中删除非实零点来上界正子和。
不需要短区间简单比例、RH、成对间距猜想或四点相关。
甚至不需要把已知 \(2/3\) 简单比例当作本篇的引导输入；第3节一次解线性不等式。

## 2. 可抵抗其余零点抵消的谱余项

本节为有限 Hermitian 线性代数。定义凸函数
\[
 j(t)=(t-1)^2-(t-2)_+^2
 =\begin{cases}(t-1)^2,&0\le t\le2,\\2t-3,&t\ge2.\end{cases}
 \tag{7}
\]
在 \([0,\infty)\) 上 \(j\ge0\)，只在 \(t=1\) 取零，导数单调不减。
本篇使用它的**标量凸性**，不假设 operator convexity。

### 引理304-B：带简单特征 Gram 的二阶稳定性 [T，独立重建]

设 \(b\) 是非负整数，\(Q\) 自伴，
\(v_1,\ldots,v_s\) 是有限维 Hilbert 空间中的单位向量，
\[
 P=\sum_{\ell=1}^s v_\ell\otimes v_\ell,\quad
 G=(\langle v_i,v_j\rangle)_{i,j\le s},\quad
 A=P+Q,\quad n_+(Q)\le b,\quad \operatorname{tr}A=N .
 \tag{8}
\]
向量允许相关，\(s=0\) 时空 Gram 的迹按0计。则
\[
 4N-\|A\|_{\rm HS}^2\le4b+3s-\operatorname{tr}j(G).
 \tag{9}
\]
若另有 \(N\ge s+2b\)，则
\[
 \|A\|_{\rm HS}^2-2N+s
 \ge2(N-s-2b)+\operatorname{tr}j(G)
 \ge\operatorname{tr}j(G).
 \tag{10}
\]

#### 证明

必要时给空间补零维，使其维数 \(d\ge s+b\)；
不改变迹、HS范数或惯性。令 \(p_1\ge\cdots\ge p_s\ge0\)
为 \(P\) 的谱补零到 \(s\) 个，即 \(G\) 的全部谱。
这时 \(\sum p_i=s\)，其余 \(P\) 的谱均为0；在下式中约定 \(i>s\) 时 \(p_i=0\)。
将 \(Q=Q_+-Q_-\) 分成谱正负部，\(\operatorname{rank}Q_+\le b\)。
最小最大原理给
\[
 \lambda_{i+b}(A)\le p_i,\qquad 1\le i\le d-b .
 \tag{11}
\]
具体地，把 \(P\) 的前 \(i-1\) 个谱方向与 \(Q_+\) 的像空间一并正交掉，
所得子空间余维至多 \(i-1+b\)，其 \(A\) Rayleigh商至多 \(p_i\)。
故 (11) 对负的 \(A\) 谱也有效，不要求 \(A\) 半正定。

令 \(F(t)=4t-t^2\)。有 \(F(t)\le4\)，且当 \(p\ge0\) 时
\[
 t\le p\quad\Longrightarrow\quad
 F(t)\le\phi(p):=\begin{cases}4p-p^2,&p\le2,\\4,&p\ge2.\end{cases}
 \tag{12}
\]
此外 \(t\le0\) 时 \(F(t)\le0\)。
对最前 \(b\) 个谱用4，对下一 \(s\) 个用 (11)--(12)，剩余非正谱只丢弃
非正的 \(F\) 值，得到
\[
 4N-\|A\|_{\rm HS}^2
   \le4b+\sum_{i=1}^s\phi(p_i)
   =4b+3s-\sum_{i=1}^sj(p_i).
 \tag{13}
\]
最后等式使用 \(\sum p_i=s\)。零特征值的 \(j(0)=1\) 也在 \(s\times s\)
Gram 中计入；没有把它们误当空间补零后的额外余项。证毕。

此机制与 Shi 工作稿§2的 Schur余项实质相同：若该稿使用
\(g(t)=t^2-2t-(t-2)_+^2\)，则 \(j(t)=g(t)+1\)，对单位对角 Gram，
其 Schur余项正好是 \(\operatorname{tr}j(G)\)。
本篇用谱移位给出独立证明，不把名称变化当新定理优先权。

### 引理304-C：不交三点块的可加下界 [T]

设 \(G\succeq0\)、对角全为1。对任意不交三元指标块 \(\mathcal T\)，
\[
 \operatorname{tr}j(G)
 \ge\sum_{I\in\mathcal T}\operatorname{tr}j(G_I)
 \ge\frac32\sum_{I\in\mathcal T}\sum_{\substack{a<b\\a,b\in I}}|G_{ab}|^2 .
 \tag{14}
\]

证明第一步：分别酉对角化各主块，并给未使用指标取单点块。
在所得到的正交基 \(e_i\) 中，对 \(G\) 的谱分解用标量 Jensen，
\[
 j(\langle Ge_i,e_i\rangle)
 \le\langle j(G)e_i,e_i\rangle .
 \tag{15}
\]
求和给 pinching 不等式；单点块是 \(j(1)=0\)。
每个 \(G_I\) 的谱位于 \([0,3]\)，因为它半正定且迹为3。
在此区间
\[
 j(t)\ge\tfrac34(t-1)^2 .
 \tag{16}
\]
\(t\le2\) 时直接成立；\(2\le t\le3\) 时差为
\(-\tfrac34(t-3)(t-5/3)\ge0\)。
故 \(\operatorname{tr}j(G_I)\ge(3/4)\|G_I-I_3\|_{\rm HS}^2\)，
而该HS平方等于两倍三对非对角项平方和。证毕。

这里没有使用可能错误的
\(\|A\|_{\rm HS}^2\ge\text{旧下界}+\|P\|_{\rm HS}^2-s\)；
其余零点可以抵消后一项。真正耐抵消的是 (9)--(10) 中的凸谱余项。
同一个 Gram 的配对余项、三点余项或别的稳定性证书不能重复相加；
本篇在每次应用中只使用一个不交块下界。

## 3. 有限几何到计数：不依赖旧比例的闭合

### 引理304-D：有限三点比例不等式 [T]

在 (8) 中，假定 \(N\ge s+2b\) 且一个计数 \(D\ge s+b\)。
设单位向量 \(v_i\) 带有位于 \((0,X]\) 的不同实位置 \(x_i\)，
且对于直径至多 \(B\) 的任意三个位置，
\[
 |\langle v_1,v_2\rangle|^2+
 |\langle v_2,v_3\rangle|^2+
 |\langle v_1,v_3\rangle|^2\ge\mu,\qquad0<\mu<2 .
 \tag{17}
\]
记 \(m=\lceil X/B\rceil\)，\(H=\|A\|_{\rm HS}^2\)。则
\[
 s\ge S_*:=\frac{2N-H-\mu m}{1-\mu/2},\qquad
 D\ge\frac{N+S_*}{2}.
 \tag{18}
\]

#### 证明

将 \((0,X]\) 分为 \(m\) 个半开箱 \(((i-1)B,iB]\)。
若第 \(i\) 箱有 \(c_i\) 个简单位置，可取 \(\lfloor c_i/3\rfloor\) 个
不交三点块。总块数 \(q\) 满足
\[
 q\ge\frac{s-2m}{3}.
 \tag{19}
\]
即使右端为负，这条下界也成立，不须先证明 \(s/N\) 的某个比例。
由 (14)、(17)，\(J:=\operatorname{tr}j(G)\ge(3\mu/2)q\)，从而
\[
 H-2N+s\ge J\ge\frac\mu2(s-2m).
 \tag{20}
\]
因 \(1-\mu/2>0\)，移项即得第一式。

另由 \(N\ge s+2b,D\ge s+b\) 得 \(4b+3s\le N+2D\)；
代入 (9) 得
\[
 D\ge\frac{3N-H+J}{2}
   \ge\frac{3N-H-\mu m+(\mu/2)s}{2}.
 \tag{21}
\]
使用 \(s\ge S_*\) 和
\((1-\mu/2)S_*=2N-H-\mu m\)，右端正好为 \((N+S_*)/2\)。
这不是一般性的 \(D\ge(N+s)/2\)；后者在高重数时可失败。证毕。

## 4. MT 窗没有正交三点：一份纯解析正下界

为避免两种尺度混淆，置
\[
 \beta=1/\sqrt2,\quad
 \alpha=\beta\cot\beta,\quad c=\beta\tan\beta,\quad
 k(x)=K_0(x/\pi).
 \tag{22}
\]
这里 \(\alpha c=1/2\)，且 \(1/2<\alpha,c<1\)。
因为 \(0<\beta<\pi/4\)，在 \([0,\beta]\) 积分 \(1<\sec^2t<2\)，
得 \(\beta<\tan\beta<2\beta\)；两常数的界随即成立。
直接积分 (2) 得整个延拓
\[
 k(x)=\frac{\sinc(x-\beta)+\sinc(x+\beta)}{2\sinc\beta}
     =\frac{\alpha x\sin x-\beta^2\cos x}{x^2-\beta^2}.
 \tag{23}
\]
后一表达式在 \(\pm\beta\) 取可去值。那里第一式严格为正，
所以不能把分子的这两个零点算作 \(k\) 的零点。

令 \(F(x)=x\sin x-c\cos x\)。
对 \(x,y>0,t=x+y\)，设 \(e_x=F(x),e_y=F(y)\)。恒等式为
\[
 \begin{split}
 F(t)={}&
 c\frac{x^2+xy+y^2+c^2}{xy}\cos x\cos y\\
 &+t\left(\frac{e_x\cos y}{x}+\frac{e_y\cos x}{y}\right)
 +\frac{c^2(e_x\cos y+e_y\cos x)}{xy}
 +\frac{ce_xe_y}{xy}.
 \end{split}
 \tag{24}
\]
将 \(\sin x=(c\cos x+e_x)/x\) 和对应的 \(y\) 代入加法公式即得。
若 \(x,y,t\) 都是 \(k\) 的零点，则三者的 \(F\) 都为零，
而 \(\cos x,\cos y\ne0\)；(24) 的第一行不可能为零。
因此任何三个不同频率的 MT 特征不能两两正交。
这个结论不需要假设它们来自零点。

### 引理304-E：显式三点核下界 [T]

置 \(\kappa=1/110000\)。若 \(a,b\ge0,a+b\le4\)，则
\[
 \max\{|K_0(a)|,|K_0(b)|,|K_0(a+b)|\}>\kappa.
 \tag{25}
\]
特别得到 (5)。

#### 证明

令 \(x=\pi a,y=\pi b,t=x+y\le4\pi<13=:R\)。
假设三项模均不超过 \(\kappa\)。
由于 (23) 同时是 \([-1,1]\) 上正概率密度的 cosine 积分，
若 \(0\le x\le1\)，有 \(k(x)\ge\cos1>1/2\)，矛盾；\(y\) 同理。
所以 \(x,y>1\)，也已避开可去点。
令 \(e=1/300=1/[20(R+2)]\)。由 (23) 及 \(\alpha>1/2\)，
\[
 |F(x)|,\ |F(y)|,\ |F(t)|
 \le2R^2\kappa=\frac{338}{110000}<e .
 \tag{26}
\]
又 \(x>1,c<1\) 给
\[
 1\le|\sin x|+|\cos x|
 \le(1+c)|\cos x|+e,\qquad
 |\cos x|\ge(1-e)/(1+c)>9/20,
 \tag{27}
\]
\(y\) 亦然。
(24) 第一行的模严格大于
\[
 3\cdot\frac12\left(\frac9{20}\right)^2=\frac{243}{800}.
 \tag{28}
\]
其余项的模总计不超过 \((2R+2)e+e^2\)。
再把 \(|F(t)|\le e\) 移到右边，必须有
\[
 \frac{243}{800}<(2R+3)e+e^2
   =\frac{29}{300}+\frac1{90000}<\frac1{10},
 \tag{29}
\]
矛盾。所有数值比较可用有理数精确检查。证毕。

此常数刻意保守，作用是给一条完全解析的严格增益，不把数值优化当作证明。
更强证书 (3) 可以替换它，而无需改动任何谱或算术步骤。

## 5. 固定平滑、完整零点算子与两个极限

本节核对实际应用，不能直接把 discontinuous \(f_0\) 代入只对
\(C_c^\infty\) 陈述的去权定理。
取实偶 \(\psi_\delta\in C_c^\infty((-1/2,1/2))\)，
\(0\le\psi_\delta\le1\)，在 \(|u|\le1/2-\delta\) 上为1，定义
\[
 a_\delta=\int\psi_\delta^2f_0,\quad
 \eta_\delta=\psi_\delta\sqrt{f_0}/\sqrt{a_\delta},\quad
 f_\delta=\eta_\delta^2,\quad K_\delta=\widehat f_\delta,\quad
 Q_\delta=f_\delta*f_\delta .
 \tag{30}
\]
有 \(a_\delta\to1\)、\(f_\delta\to f_0\) 于 \(L^1\cap L^2\)，故
\[
 \varepsilon_\delta:=\|f_\delta-f_0\|_1\to0,\qquad
 \sup_{v\in\mathbb R}|K_\delta(v)-K_0(v)|\le\varepsilon_\delta .
 \tag{31}
\]
每个核在实轴的模都不超过1。由 (3)，
\[
 K_\delta(a)^2+K_\delta(b)^2+K_\delta(a+b)^2
 \ge \mu_\delta:=\mu-6\varepsilon_\delta
 \quad(a,b\ge0,\ a+b\le B).
 \tag{32}
\]
充分小的固定 \(\delta\) 使 \(0<\mu_\delta<2\)。
这只需**实轴**上一致收敛，不对增长的复带声称同一误差。

### 5.1 去相关权的固定函数账本 [T/R]

BGST 的无条件 Lemma5
([作者预印本§3](https://arxiv.org/pdf/2306.04799)，
正式发表 Acta Arith.214(2024),357--376) 对固定实偶 \(q\in L^1(\mathbb R)\)、支撑于 \([-1,1]\)
且在0 Lipschitz 的 \(q\) 给
\[
 \sum_{0<\gamma,\gamma'\le T}
 \widehat q\!\left(i(\rho-\rho')\frac L{2\pi}\right)
 \frac4{4-(\rho-\rho')^2}
 =\frac{TL}{2\pi}
 \left(q(0)+2\int_0^1u q(u)\,du+O_q(L^{-1/2})\right),
 \quad L=\log T .
 \tag{33}
\]
本轮核读其 Lemma5、证明和所引 Theorem1 的范围；
不把应用于窄零点盒的其他定理前提移进 (33)。

**勘误核对。** 四作者后续论文
[2501.14545v3 §3](https://arxiv.org/html/2501.14545v3#S3)
修正旧Theorem1误差，脚注明确保留旧Lemma5；
其式(3.5)给前缀 \(0<\gamma,\gamma'\le T\) 的修正版。
这不是同一预印本的版本号，也不能把后文的窄盒假设搬来。
独立积分核验如下：令 \(\mathcal F_{(0,T]}(x)\) 为带相关权的
\(\sum x^{\rho-\rho'}\)，则修正公式除以 \(TL/(2\pi)\) 后，在
\(x=T^u,0\le u\le1\) 为
\[
 Le^{-2Lu}(1+O(L^{-1/2}))+u+O(L^{-1/2}).
\]
乘固定 \(2q(u)\) 积分时，Lipschitz条件给
\(2L\int_0^1 e^{-2Lu}q(u)\,du=q(0)+O_q(L^{-1})\)，
两个修正误差积分均为 \(O_q(L^{-1/2})\)。
故 (33) 的预算和无条件范围不变；允许带符号 \(q\)，也覆盖下面的 \(Q_\delta''\)。

对每个**固定** \(\delta\)，\(Q_\delta,Q_\delta''\) 都满足 (33)。
分部积分给 \(\widehat{Q_\delta''}(z)=-4\pi^2z^2K_\delta(z)^2\)，故
\[
 K_\delta(z)^2
 =\left(\widehat Q_\delta(z)
        -\frac{\widehat{Q_\delta''}(z)}{4L^2}\right)
        \frac4{4-(\rho-\rho')^2},
 \quad z=i(\rho-\rho')L/(2\pi).
 \tag{34}
\]
分别对两份固定函数用 (33)，再相减，得到
\[
 \sum_{0<\gamma,\gamma'\le T}K_\delta(z)^2
  =(C_\delta+o_\delta(1))N(T),\qquad
 C_\delta=Q_\delta(0)+2\int_0^1uQ_\delta(u)\,du\longrightarrow R_0.
 \tag{35}
\]
最后极限由 \(L^1\cap L^2\) 收敛和 MT 泛函的经典计算给出，
与 Lamzouri Lemma3.2 一致。没有对随 \(T\) 变化的测试函数直接套 (33)。

### 5.2 同一实际有限自伴配置

对每个实际零点放
\[
 z_\rho=-i(\rho-1/2)L/(2\pi),\qquad
 v_z(u)=\eta_\delta(u)e^{-2\pi izu}.
 \tag{36}
\]
这里 \(\Re z_\rho=\gamma L/(2\pi)>0\)；相对 Lamzouri 的符号整体翻转，
但 \(K_\delta\) 为偶函数，(35) 不变。
函数方程给该多重集共轭封闭。采用实 Hilbert 空间
\(\mathcal H_{\mathbb R}=\{v\in L^2:\overline{v(u)}=v(-u)\}\)，
通常复内积在其上取实数；\(v\otimes v\) 表示
\(w\mapsto\langle w,v\rangle v\)。以下 \(v_x,g_z,h_z\) 都属于此空间。
按不同实点及不同非实对各索引一次，定义
\[
 A_T=\sum_{\text{不同实 }x}m_xv_x\otimes v_x
       +2\sum_{\text{不同非实对}}m_z(g_z\otimes g_z-h_z\otimes h_z),
 \quad g_z=(v_z+v_{\bar z})/2,\ h_z=(v_z-v_{\bar z})/(2i).
 \tag{37}
\]
在这些实向量的有限维张成上，
\(\|v_x\|^2=1,\ \|g_z\|^2-\|h_z\|^2=1\)；
后式来自 \(\cosh^2-\sinh^2=1\) 及 \(\int\eta_\delta^2=1\)。
直接积分及张量展开给
\[
 \operatorname{tr}A_T=N(T),\qquad
 \|A_T\|_{\rm HS}^2=\sum_{z,w\in\mathcal Z_T}K_\delta(z-w)^2.
 \tag{38}
\]
为完整验证第二式，实算子复化不改变 HS 范数。置
\(S(u,v)=\sum_{z\in\mathcal Z_T}v_z(u)v_z(v)\)：每一非实对的
\(v_z\otimes_{\rm bil}v_z+v_{\bar z}\otimes_{\rm bil}v_{\bar z}\)
恰等于 \(2g_z\otimes_{\rm bil}g_z-2h_z\otimes_{\rm bil}h_z\)。
通常复线性积分算子的核为 \(S(u,-v)\)，因为每个实型向量满足
\(\overline{g(v)}=g(-v)\)；反射不改变 \(L^2(du\,dv)\) 范数。因此
\[
 \|A_T\|_{\rm HS}^2
 =\int\!\!\int|S(u,v)|^2\,du\,dv
 =\sum_{z,w\in\mathcal Z_T}K_\delta(z-\bar w)^2
 =\sum_{z,w\in\mathcal Z_T}K_\delta(z-w)^2 .
\]
最后一步以 \(w\mapsto\bar w\) 重排多重集；
不是把每个复数项误认作非负。

取 \(P\) 为所有简单实点的单位特征和；其余为 \(Q=A_T-P\)。
若不同重复实点有 \(r\) 个、不同非实对有 \(k\) 对，则
\[
 n_+(Q)\le r+k=b,\quad
 N\ge s+2b,\quad D=s+r+2k\ge s+b .
 \tag{39}
\]
这些是无条件重数/惯性账本，不要求离线点不存在，也不使用它们的具体位置。
简单实点的位置全部在
\((0,X_T]\)，\(X_T=TL/(2\pi)\)。
其 Gram 条目恰为 \(K_\delta(x_i-x_j)\)，所以 (32) 可用于304-D。

### 5.3 定理304-A的证明完成

令 \(m_T=\lceil X_T/B\rceil\)，则 \(m_T/N(T)\to1/B\)。
对每个足够小且**固定**的 \(\delta\)，(18)、(35) 给
\[
 \liminf_T s(T)/N(T)\ge
     \frac{2-C_\delta-\mu_\delta/B}{1-\mu_\delta/2},
 \qquad
 \liminf_T D(T)/N(T)\ge
     \frac12\left(1+
       \frac{2-C_\delta-\mu_\delta/B}{1-\mu_\delta/2}\right).
 \tag{40}
\]
左端与 \(\delta\) 无关，现在令 \(\delta\to0\)，即得 (4)。
没有取 \(\delta=\delta(T)\)，没有新增统一导数估计，
没有使用待证明的简单比例进行自举。证毕。

当 \(B=4\) 时
\[
 p(4,\mu)-C_0
   =\frac{\mu(C_0/2-1/4)}{1-\mu/2}>0 .
 \tag{41}
\]
MT 泛函本身仍以 \(R_0\) 为最优值；改进来自保留 (9) 的谱余项，
不是宣称把同一个 MT 变分问题优化到更小值。

## 6. 从303到本轮：已停止和真正新增的输入

起初检查 VIS-1 的实际局部节点信息。独立文献输入
[Bellotti--Wong Theorem1.1](https://arxiv.org/html/2412.15470v2)
给 \(|N(t)-t(2\pi)^{-1}\log(t/(2\pi e))|
\le0.10076\log t+0.24460\log\log t+8.08344\) [R]。
直接在 \(t\pm1/4\) 差分得到
\[
 N(t+1/4)-N(t-1/4)
 \le\bigl(1/(4\pi)+0.20152+o(1)\bigr)\log t
 =(0.28109747\ldots+o(1))\log t .
 \tag{42}
\]
这确实排除303那个含约 \(\log t\) 个新增实点的具体簇，
但不排除所有 \(O(\log t)\) 簇，也不给临界窗残余 Gram 的下界。
故不以 (42) 续开 VIS-1 的模型周期。

真正获得的可用输入是**同一实际 MT 特征的三点 Gram 几何**，
它通过 (9) 而非硬商接入二阶比例。
本篇不计算或使用商后的负迹，也不将 (10) 与四阶矩余项相加。
这是一条有限稳定性审计，不是重启原 MOM-1 的 determinant-correlation 估计。

## 7. 最小条件、反例与循环性

| 条件 | 作用 | 删除后的失效位置 |
|---|---|---|
| 单位简单特征、正 Gram | trP=s，(14)的单位对角与谱[0,3] | 任意缩放改变计数和谱余项；不能不补误差沿用 |
| \(n_+(Q)\le b\) | (11)的谱移位，承受其余零点抵消 | \(s=1,P=[1],Q=[1],b=0\) 会把(9)变成 \(4\le3\) |
| 重数账本 \(N\ge s+2b,D\ge s+b\) | 从(9)到比例及不同点计数 | 一般矩阵没有这些零点计数解释 |
| 不交三点块 | trace Jensen 只使用一次每个坐标 | 重叠匹配不能直接相加，会重复计算同一余项 |
| MT三点下界 | 固定密度强迫正余项 | 平窗核 sinc(πv) 在0,1,2的Gram正好I，三点常数为0 |
| 总位置区间 \(X_T\sim N(T)\) | 分箱代价 \(m_T/N\to1/B\) | 任意稀疏无界位置不强迫正比例小直径块 |
| 完整全谱的(35) | 以已知算术预算上界同一A的HS | 仅真实子集的正Gram上界不是同一算子 |
| 先固定平滑再取高度 | (33)合法与余量保留 | 直接取增长导数的δ(T)需要额外统一算术误差 |

本篇的“正性”只是有限 Gram 自动半正定及标量凸性，
不是完整 Weil 二次型正性、谱酉性或统一负惯性假设。
不新增任何与 RH 等价的结构公理。接口只属于显式公式型有限配置；
上同调、极化及两类 Weil 结构的桥梁仍开放。
选择和平滑只保留已经证明的正三点常数，没有从紧性制造算术正性。

一般谱模型只要独立满足 (35)、(38)--(39) 和位置长度账本，可复用 (4)；
原始Dirichlet、Dedekind及自守L函数须分别核验全谱二阶渐近与正规化。
本轮没有完成这些核验，不直接宣布GRH族比例改进。
函数域通常具有不同的高度周期及计数尺度，也不自动适用这里的MT数值。

## 8. 精确有理三点证书与独立复核

### 引理304-F：小型全域区间证书 [T，计算机辅助]

已用完整有理区间覆盖证明
\[
 \mathcal M(4,1/10000).
 \tag{43}
\]
代入已证定理304-A，得到无条件后果 [T/R]
\[
 p_*=\frac{C_0-1/40000}{1-1/20000}
     =0.672509329145868939\ldots,\qquad
 (1+p_*)/2=0.836254664572934469\ldots .
 \tag{44}
\]
小数只显示精确表达式；证明使用 \(B=4,\mu=1/10000\)。
相对本项目此前采用的 \(C_0\)，简单比例下界增加
\(0.000008625466457293\ldots\)。这不是对目前所有公开候选数值的纪录比较。
纯浮点优化在 \(B=4\) 找到三核平方和约 \(0.000222149\) 的候选极小 [E]；
它不证明全局下界，不被用于 (5) 或第2--5节的推导。

证书源码为 [mt_triple_slack_audit.py](../scripts/mt_triple_slack_audit.py)，
复算入口为 `python -B scripts/mt_triple_slack_audit.py`。
所有参与验收的端点是整数除以 \(S=2^{128}\)；加法精确，
乘除结果分别向下/向上取整。具体解析包络如下。

1. 用 Machin 恒等式
   \(\pi=16\arctan(1/5)-4\arctan(1/239)\)，分别取48项和12项交错级数，
   以相邻两个部分和给有理上下界。恒等式由正切加法公式及
   \(4\arctan(1/5)-\arctan(1/239)\in(0,\pi/2)\) 确定分支。
2. 用整数平方根
   \(r=\lfloor\sqrt{S^2/2}\rfloor\) 给
   \(\beta\in[r/S,(r+1)/S]\)。
3. 对每个实区间 \(I\)，区间计算
   \(\sum_{k=0}^{48}(-1)^kx^{2k}/(2k+1)!\)，再外扩
   \(\sup_{x\in I}|x|^{98}/99!\)。这是对 \(\sin x\) 用98阶
   Taylor余项再除以 \(x\) 的全实轴界；\(x=0\) 由连续性处理。
4. 在 (23) 第一式中代入上述区间；程序先验证
   \(2\sinc\beta\) 的区间下端严格为正，才作区间除法。

然后利用
\[
 |K_0'(v)|\le2\pi\int|u|f_0(u)\,du\le\pi
 \tag{45}
\]
把中心值转成整个二元箱的三核区间。在深度 \(d\)，箱为
\([4i/2^d,4(i+1)/2^d]\times[4j/2^d,4(j+1)/2^d]\)；
三个核的外扩半径分别不小于 \(2\pi/2^d,2\pi/2^d,4\pi/2^d\)。
中心为精确二进有理数。只有三份区间离0距离平方和
已达到 \(1/10000\) 的箱才验收；其余四分，
仅当 \(i+j>2^d\) 才作为全在三角域外而丢弃。
触及 \(a+b=4\) 的箱保留，交边箱在**整个箱**上认证，是安全外扩。
树从 \([0,4]^2\) 开始，待处理栈耗尽才成功；
达到深度、节点或时间限额会报错退出，绝不视为部分成功。

主代理复跑及两名只读审计者独立复跑得到相同的精确证书：

- 6109个访问箱，1527个四分内部节点，4252个验收叶箱，330个域外叶箱；
  \(6109=1+4\cdot1527=1527+4252+330\)，没有遗漏待验收分支。
- 最大验收叶深度12，479个缓存核中心。
- 全部验收叶下界的最小值为
  \[
  \frac{2898416747722058938503240917044843699509332263384631784618436683499041769}
  {28948022309329048855892746252171976963317496166410141009864396001978282409984}
  >\frac1{10000}.
  \]
  显示值约 \(0.00010012486230494542\) 不参与任何验收判断。

由每步包络正确性、根箱覆盖、保守剪枝和有限树完全验收，(43) 得证。
证书不使用实际零点、优化器或浮点舍入假设。
脚本另外运行的五组合成 Hermitian/Weil 矩阵、三个粗网格及72组三点测试
均是 MP80 的 [E]，不证明 (33) 或实际零点渐近。

独立全文逆审：carrier_audit 与 gap_exception_audit 均逐式检查
谱移位的负尾谱、Gram零特征值、不同点账本、固定平滑去权及两极限，
并逐行检查有理包络与全域覆盖，结论 PASS。
midband_compute 独立验证核心代数与平滑接口并编写证书；
主代理完整核读并复跑。这里只是内部交叉审计，非外部同行评审或形式化证明。

收尾复核又明确了§5.2通常积分核 \(S(u,-v)\) 与双线性张量
\(S(u,v)\) 的反射约定，二者范数相同；没有混淆算子核与张量表示。
另验证深度、节点、时间限额的三条失败路径均报错而不验收；
七个中心值的MP100包络检查仅[E]。
仓库轻量验收：目录/TeX链接及11项目录回归PASS，
80项注册覆盖与mock分发PASS（core78、B1h1、B1i1）。
这不是80项数学计算全部重跑，也不表示本提交的远程CI已完成。

## 9. 外部同类工作与下一轮准入

Shi 的首稿已使用同一凸谱机制和相邻间距加法避开MT根，
本篇不能以“只用二阶矩”或“严格超过0.6725”申报首次发现。
另有其自标 pending independent review 的
[后续候选仓库](https://github.com/yuhangshi888/zeta-simple-zeros-673316977)
声称更高常数；主代理只核读其状态与依赖说明，未执行远程代码，
未重跑所依赖的七点/九点大规模区间证书，也不认定该数字为已验纪录。
本篇全部证明和计算独立，不导入那些证书或其可加余项主张。

本轮已完成 (43) 的小型全域证书和本文的全链独立逆审。
下一步不是继续提高未经审计的小数，而是限额对照公开同类工作，
判断直接Hilbert接口、三点证书或适用模型
是否有可形成论文的独立贡献。若只是已知机制的较弱重建，
将本篇保留为复核基准，不以增加块数或排版掩盖新颖性缺口。
暂归独立二阶稳定性附注，Markdown为主，不并入四矩比例论文。
