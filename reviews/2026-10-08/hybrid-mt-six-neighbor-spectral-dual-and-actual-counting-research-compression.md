# 原MT核的六邻点谱对偶、全域分簇支付与实际比例

2026-10-08。作者：compression。基线为根线程已推送的main0305760及477。
只新增研究源与新核证书，不修改旧研究、旧检查器或Git。

本稿给一个已经闭合的原MT位置约束，绕过一般correlation矩阵的flat-rank取等配置。
使用原19/5000七点证书，不导入增强Schwarz目标。完整实轴核界、
所有点列的分簇支付与原固定平滑零点接口给
\[
 p_6=\frac{65025C_0-130}{64778}
     =0.6730581101107435\ldots>p_{280},
 \qquad C_0=\frac32-\frac1{\sqrt2}\cot(1/\sqrt2).
 \tag{1}
\]
对应简单临界线比例67.3058110110…%，不同点比例83.6529055055…%。
这是项目实际比例的提高，不是世界纪录、RH完成百分比或新的零条带。
有限谱与计数推导为[T]，原二阶算术接口为[R]；
数值接受来自全域Arb区间证书，非优化器或抽样。

## 1. 已付输入与本轮真正新增的有限对象

置
\[
 f_0(u)=\frac{\cos(\sqrt2u)}{\sqrt2\sin(1/\sqrt2)}
        1_{[-1/2,1/2]}(u),\quad
 k_0(x)=\int f_0(u)e^{-2\pi ixu}\,du,\quad w(x)=k_0(x)^2 .
 \tag{2}
\]
已完整执行原ainta七点全域不等式
\[
 F_6(g)=\frac1{3000}\sum_{i=1}^6g_i+
 \sum_{r=1}^6\frac2{7-r}\sum_{i=1}^{7-r}
   w(g_i+\cdots+g_{i+r-1})\ge\tau=\frac{19}{5000}
 \quad(g_i\ge0).
 \tag{3}
\]
来源、代码全文阅读、707901个盒子以及两次完整执行见
[477作者源](hybrid-original-multipoint-envelope-and-actual-counting-research-compression.md)，
canonical LF SHA256
59b399445a3022ce9b5ee6c064660e1602dab6d5641d3793649f16f509fc5efa。
冻结 [七点输出](../../output/hybrid-multipoint-seven-primary-replay.json)
canonical LF SHA256
aa6885489c1d0086bca32b72d27fc7a2a5f44a48f78483a057f23a59e5a828e6。
本轮不声称重新证明或增强该局部目标。

已知[347/351谱对偶及实际传递](../../notes/351-fixed-radius-stability-and-actual-zero-transfer.md)
和[355短簇支付](../../notes/355-short-cluster-payment-and-separated-five-gap-reduction.md)
提供先行机制。旧357–359的连续subaction没有全域证明，不能调用。
本轮区别是：原MT、半径6、均一可行谱试探矩阵，
以及已经支付的(3)直接封闭全部gap域；
没有新五gap势、未来续接函数或未认证图插值。

## 2. 原MT核的完整实轴界 [T，计算机辅助]

取
\[
 d_0=\frac{3809}{4000},\qquad
 (M_1,\ldots,M_6)=\frac1{10000}(1805,1064,757,588,480,406).
 \tag{4}
\]
本轮证书证明
\[
 k_0(x)>\frac1{10}\quad(0\le x\le d_0),\qquad
 |k_0(x)|<M_r\quad(x\ge r d_0,\ 1\le r\le6).
 \tag{5}
\]
验证器为
[hybrid_mt_six_neighbor_geometry_certificate.py](../../scripts/hybrid_mt_six_neighbor_geometry_certificate.py)，
canonical LF SHA256
b7bac147d76b7e1fb2bbe1307518acf4642cb0aedbba2c0fd8eebc610d1d3a8c。
[输出](../../output/hybrid-mt-six-neighbor-geometry-certificate.json)
canonical LF SHA256
0b587847baa23014d947a7621f491a5f9175d714341b2bc9026465073aceee95。

完整证明域如下。令 \(\beta=1/\sqrt2\)、\(a=\beta\cot\beta\)、
\(t=\pi x\)。在 \(x\ge d_0\) 无可去点，
\[
 k_0(x)=\frac{a t\sin t-\tfrac12\cos t}{t^2-\tfrac12}.
 \tag{6}
\]
在128bit Arb下对 \([d_0,7]\) 的全部241910个宽1/40000闭cell，
用精确fmpq中心与半径直接区间计算(6)；
每格按适用的最大 \(r\le6\) 验最严格的 \(M_r\)，其余界由 \(M_r\) 递减继承。
阈值 \(r d_0\) 均为grid整数，跨阈值无遗漏。
各半径最严格cell数为38090五组及51460一组。
所有格严格余量超过1/10^8，接受不使用float。
closed-cell ball SHA256为
42d5d94ab916327d36705f6ee1385a7779ad931cb4ade50989579891f2f7bc5e。

无限尾也完整支付。Arb证明 \(0<a<5/6\)、\(\pi>157/50\)，
且 \(t>1/\sqrt2\) 时
\[
 |k_0(x)|\le\frac{a t+1/2}{t^2-1/2}.
 \tag{7}
\]
此函数的导数分子为 \(-a t^2-t-a/2<0\)。
故 \(x\ge7\) 时由精确有理数给
\[
 |k_0(x)|\le
 \frac{(5/6)(1099/50)+1/2}{(1099/50)^2-1/2}
 =\frac{141125}{3619653}<\frac{203}{5000}=M_6.
 \tag{8}
\]
最后在 \(x=d_0\) 直接认证 \(k_0(d_0)>1/10\)。
正偶概率密度与 \(d_0<1\) 给
\[
 k_0'(x)=-4\pi\int_0^{1/2}u f_0(u)\sin(2\pi xu)\,du\le0
 \quad(0\le x\le d_0),
 \tag{9}
\]
从而得到(5)第一式。原float极值只用于选参数，不参与上述接受。
首次final参数全域执行耗时0.8570191秒。

## 3. 有界Hermitian试探矩阵的合法谱对偶 [T]

沿用
\[
 j(t)=(t-1)^2-(t-2)_+^2\quad(t\ge0).
 \tag{10}
\]
对任何有限 \(G\succeq0\) 和Hermitian \(B\) 满足 \(\|B\|_{\rm op}\le1\)，
\[
 \operatorname{tr}j(G)\ge
 2\operatorname{tr}(B(G-I))-\operatorname{tr}B^2 .
 \tag{11}
\]
不要求 \(B\succeq0\)，不要求 \(B\) 与 \(G\) 交换。
证明：对 \(b\in[-1,1]\)、\(t\ge0\)，
\(j(t)\ge2b(t-1)-b^2\)。
\(t\le2\) 时差为 \((t-1-b)^2\)；
\(t\ge2\) 时差为
\((1-b)(2(t-1)-(1+b))\ge0\)。
在 \(B\) 的本征基对 \(G\) 用标量Jensen，
\(\operatorname{tr}j(G)\ge\sum_i j(\langle Ge_i,e_i\rangle)\)，
逐项应用此式即得(11)。没有operator convexity或PSD假试探。

现令 \(y_1<\cdots<y_n\) 的相邻gap至少 \(d_0\)，
\(G_0=(k_0(y_i-y_j))\)，并取
\[
 u=\frac{50}{51},\qquad
 B_{ij}=
 \begin{cases}
 u k_0(y_i-y_j),&1\le|i-j|\le6,\\0,&\text{其余}.
 \end{cases}
 \tag{12}
\]
它是Hermitian、对角0；第 \(r\) 邻点距离至少 \(r d_0\)。
由(4)–(5)，每行绝对和至多
\[
 2u\sum_{r=1}^6M_r
 =2\frac{50}{51}\frac{51}{100}=1 .
 \tag{13}
\]
Schur给 \(\|B\|_{\rm op}\le1\)。
等号预算合法，不需strict小于1；端部只减少项。
边效率为
\[
 c=2u-u^2=\frac{2600}{2601}.
 \tag{14}
\]
所以(11)精确给
\[
 \operatorname{tr}j(G_0)\ge
 c E_6(y),\quad E_6(y)=2\sum_{\substack{i<j\\j-i\le6}}w(y_j-y_i).
 \tag{15}
\]
完整Gram内部未删除：截断只发生在可行试探 \(B\)，(11)仍对完整 \(G_0\) 应用。
初试权1,…,1,3/4被均一50/51严格加强；仅final权进入结论。

## 4. 已付七点证书的全链端项 [T]

对上述 \(n\ge7\) 点，把(3)在全部 \(n-6\) 个七点连续窗口求和。
每个跨度 \(r\le6\) 的pair至多出现 \(7-r\) 次，
每个gap至多出现6次；皆非负。故
\[
 E_6(y)+\frac{{\rm span}(y)}{500}\ge\tau(n-6).
 \tag{16}
\]
特别是(16)使用半径6能量而非完整所有pair能量。
对 \(0\le n\le6\)，右侧非正，(16)按空/span0约定仍成立。
联立(15)得到
\[
 \operatorname{tr}j(G_0)\ge
 \alpha n-\eta\,{\rm span}(y)-6\alpha,\qquad
 \alpha=c\tau=\frac{247}{65025},\quad
 \eta=\frac c{500}=\frac{26}{13005}.
 \tag{17}
\]
只有一个全链端项，不是每个小簇扣一份端项。

## 5. 所有点列的短簇支付 [T]

现在对任意有序位置 \(x_1<\cdots<x_s\)，
按相邻gap \(<d_0\) 形成极大连续分量。
大小1的分量汇集为单点集合 \(S\)，大小 \(m\ge2\) 的分量为短簇。
相邻单点的距离至少 \(d_0\)，故 \(S\) 作为一个大主块可用(17)；
\({\rm span}(S)\le{\rm span}(x)\)，空或单点跨度为0。

每个短簇按原顺序取 \(\lfloor m/2\rfloor\) 个不交相邻pair。
所有pair距离 \(<d_0\)，由(5)其2×2单位对角Gram的谱为
\(1\pm|k_0(g)|\in[0,2]\)，因而
\[
 \operatorname{tr}j(G_{\rm pair})=2|k_0(g)|^2>\frac1{50}.
 \tag{18}
\]
\(\lfloor m/2\rfloor\ge m/3\) 对每个 \(m\ge2\) 成立，
所以每簇付至少
\[
 \frac m{150}>\alpha m.
 \tag{19}
\]
奇数簇中未配节点已由这个节点预算支付；不另丢节点或重复计算。

将完整Gram指标pinch为：单点集合 \(S\) 一个主块、
各不交pair、剩余单个点。
标量Jensen给完整 \(J\) 至少这些块的 \(J\) 之和。
设 \(S\) 有 \(n_s\) 点、短簇合计 \(n_b\) 点，\(n_s+n_b=s\)。
由(17)–(19)，\(\eta\ge0\)，得到对全部位置配置的
\[
 \boxed{\operatorname{tr}j(G_0(x))
       \ge\alpha s-\eta\,{\rm span}(x)-6\alpha .}
 \tag{20}
\]
不依赖low-F6盒子包含所有真实gap；分簇使全gap域被完整覆盖。
同一个谱余项只pinch一次，没有把(15)与其他Gram增益重复相加。

## 6. 原固定平滑实际零点算子的增长一致传递 [T/R]

用[304 §5](../../notes/304-mt-triple-geometry-and-second-moment-stability.md)
及477作者源§7的原合同：
先固定实偶光滑 \(\eta_\delta\)、\(\int\eta_\delta^2=1\)，
\(f_\delta=\eta_\delta^2\to f_0\) 于 \(L^1\cap L^2\)，
令 \(\varepsilon_\delta=\|f_\delta-f_0\|_1\)、\(k_\delta=\widehat f_\delta\)。
实轴全域一致
\(|k_\delta-k_0|\le\varepsilon_\delta\)，且两个核模至多1。
原全部复零点特征构成真实有限自伴算子
\[
 \operatorname{tr}A_{\delta,T}=N(T),\qquad
 \|A_{\delta,T}\|_{\rm HS}^2=(R_\delta+o_\delta(1))N(T),
 \qquad R_\delta\to R_0=2-C_0.
 \tag{21}
\]
这里 \(N(T)\) 计 \(0<\gamma\le T\) 的全部重数；
全复零点带符号双和及离线正负块全部保留。
简单临界线列为真实单位特征
\(\eta_\delta(u)e^{-2\pi ixu}\)，位置 \(x=\gamma\log T/(2\pi)\)。
其Gram条目精确为 \(k_\delta(x_i-x_j)\)，
位置长度 \(X_T=T\log T/(2\pi)=N(T)+o(N(T))\)。

仍按实际位置与固定 \(d_0\) 分簇，几何划分不依赖profile。
对分离单点主块，在(11)取按原 \(k_0\) 造的同一 \(B\)；
它的可行性由(13)精确证明，无须重新证明平滑核的行和。
对真实Gram \(G_\delta\)，
\[
 2\operatorname{tr}B(G_\delta-G_0)
 \ge-2\varepsilon_\delta\sum_{i,j}|B_{ij}|
 \ge-2n_s\varepsilon_\delta.
 \tag{22}
\]
因此单点主块(17)只损失 \(2n_s\varepsilon_\delta\)。
这是一阶稀疏对偶误差，非整个增长稠密Gram的operator norm比较。
短簇实际pair每个付至少 \(2(1/10-\varepsilon_\delta)^2\)；
每节点费用
\(\beta_\delta=(2/3)(1/10-\varepsilon_\delta)^2\)。
先固定充分小 \(\delta\)，如 \(\varepsilon_\delta<1/10000\)，则
\[
 \alpha_\delta=\alpha-2\varepsilon_\delta>0,\qquad
 \beta_\delta>\alpha_\delta .
 \tag{23}
\]
相同pinching完整支付所有 \(s=S(T)\) 个实际简单点，得
\[
 J_\delta\ge\alpha_\delta s-\eta X_T-6\alpha .
 \tag{24}
\]
误差只有 \(2s\varepsilon_\delta=O(N\varepsilon_\delta)\)，
不依赖实际四矩、最高特征值或增长列数乘稠密矩阵误差。

令不同重复实点有 \(r\) 个、不同非实共轭对有 \(k\) 对，
则 \(b=r+k\)、\(N\ge s+2b\)、\(D\ge s+b\)，
去掉简单列后的 \(Q\) 满足 \(n_+(Q)\le b\)。
477作者源(4)–(5)的有限惯性余项逐式给
\[
 s\ge2N-\|A_{\delta,T}\|_{\rm HS}^2+J_\delta,\qquad
 2D\ge3N-\|A_{\delta,T}\|_{\rm HS}^2+J_\delta .
 \tag{25}
\]
不同点没有免费使用 \(D\ge(N+s)/2\)。
代入(21),(24)，先 \(T\to\infty\)，得
\[
 \liminf_T S(T)/N(T)\ge
 p_\delta=\frac{2-R_\delta-\eta}{1-\alpha_\delta},\qquad
 \liminf_T D(T)/N(T)\ge(1+p_\delta)/2 .
 \tag{26}
\]
第二式将第一式代入同一HS/inertia账本；\(\alpha_\delta>0\) 保证方向。
最后 \(\delta\to0\)，得(1)及 \((1+p_6)/2\)。
profile固定→高度极限→profile极限，未使用 \(\delta(T)\) 统一算术界。
这里是前缀实际零点比例；未另宣称短区间dyadic比例或有限高度零点验证。

## 7. 精确数值、审查范围与已知更高主张

使用477冻结
[有理代数输出](../../output/hybrid-multipoint-cap-exact-algebra.json)
中 \(C_0\) 的128bit严格包络，canonical LF SHA256
d84077ab71b47d1ea253cad9675fa8c25f9aa4dade775ad73ff53033167625c3，
对(1)直接精确Fraction计算得区间
\[
 \frac{14836092823842124897870604079776674894402895}
      {22042811164404551786230480320215081201696768}
 \le p_6\le
 \frac{7418046411921062448935302039888337450550235}
      {11021405582202275893115240160107540600848384}.
 \tag{27}
\]
下端严格大于 \(673058110/10^9\) 及477的 \(p_{280}\) 上端。
相对 \(p_{280}\) 净提升约 \(0.0000484578316066\)，
即0.00484578316066个百分点。
旧三点或七点余项没有再加一次；增长四矩没有插入capacity作常数。

本轮证明对任意位置全域，原MT核界包括无限尾。
旧359的finite graph PASS未被误用作连续域证书。
本轮谱对偶和分簇有上述先行笔记，不能以这一步的新支付声称首次发现其机制。
[305](../../notes/305-post-6725-literature-baseline-audit.md)的
67.3316977%、67.3399%等更高公开主张继续保留比较；
本轮较弱结果不认证或否定它们，也不申报世界纪录。

新验证器默认禁止覆盖输出，--check完整重算全部核cells与尾、再比较确定字段。
它只认证有限核界与有理预算，不认证外部二阶相关解析定理；
实际传递由本稿(21)–(26)给出并需独立全文审查。
原[R]条带、full signed近共振与常数级高四矩仍不由本稿解决。
