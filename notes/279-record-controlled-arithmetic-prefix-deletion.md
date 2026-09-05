# 279. 历史包络控制的实际算术前缀删除

日期：2026-09-06。主线：NCE-8 / B1z；论文归属：Vaughan--Brownian response。

状态：[T] 275新记录序列上的质量相对、有限频带前缀删除；
[T] 原/尾部实际正源响应的预算转移；[O] 尾部算术中频预算。
本篇独立闭合一个实际误差项，不只给出响应的另一种表示；
但没有闭合剩余中频、证明 RH/GRH、改进零点比例或主张文献新颖性。
本轮仅 Markdown。附属显式公式和有限模式审计见
[280](280-finite-zero-interface-and-fixed-mode-audit.md)。

## 1. 对象、量词和端点

固定可计算的 \(0<\sigma<\beta<1/2\)，记
\[
 \delta=\beta-\sigma,\quad a=1-\sigma,\quad L=\log Y,\quad
 \tau=\log N,\quad w_Y(x)=x^{-\sigma}e^{-x/Y}.
 \tag{1}
\]
只沿[275](275-record-envelope-and-growing-low-frequency-closure.md)新认证共尾序列取
dyadic \(Y\) 及整数 \(Y\le N\le2Y\)。其已独立证明的输入为
\[
 |M|>Y^{1/2-\sigma}\sqrt{\ell(Y)},\qquad
 P_\beta(N)N^\delta<C_{\sigma,\beta}|M|,
 \tag{2}
\]
\[
 M=M(Y,N),\quad M(Y,t)=\sum_{2\le n\le t}\Lambda(n)w_Y(n)
                   -\int_1^t w_Y(x)\,dx,\quad
 P_\beta(N)=\max_{1\le n\le N}\frac{|\psi(n)-n|}{n^\beta}.
\]
其中 \(\ell(Y)=\max(1,\log\log\log Y)\)，充分大 \(Y\) 下使用。
不能把(2)回填给271旧算法的任意输出、每个 dyadic 窗口或浮点最大者。
共尾存在性沿用275的 Littlewood 振荡和记录选择，不是本篇另加 RH 型假设。

取整数 \(2\le K\le Y/2\)，在共同 lag \(u=\log x\) 上拆分正源：
\[
 \alpha_e=\sum_{2\le n\le K}\Lambda(n)w_Y(n)\delta_{\log n},\quad
 \alpha_l=\sum_{K<n\le N}\Lambda(n)w_Y(n)\delta_{\log n},
 \tag{3}
\]
\[
 b_e=(\log)_*(w_Y(x)\,dx|_{[1,K]}),\qquad
 b_l=(\log)_*(w_Y(x)\,dx|_{(K,N]}).
 \tag{4}
\]
下标 \(e,l\) 分别指早段和尾部。**整数 \(K\) 的素数幂质量只归早段**；
尾部不是 \(K\le n\le N\)。连续端点没有原子，写成同一半开约定以便核对。
全部中心化仍用原 lag，不把尾部平移到零：
\[
 k_u=(\delta_u+\delta_{-u})/2-\delta_0,\quad
 p_j=\int k_u\,d\alpha_j,\quad c_j=-\int k_u\,db_j,\quad r_j=p_j+c_j.
 \tag{5}
\]
于是 \(p=p_e+p_l,c=c_e+c_l,r=r_e+r_l\) 精确成立。
记 \(A_j=\alpha_j(\mathbb R),B_j=b_j(\mathbb R),S_j=A_j+B_j\)，
\[
 m_e=A_e-B_e=M(Y,K),\quad M_l=A_l-B_l=M-m_e,\quad S=S_e+S_l.
\]
对零质量紧支撑测度 \(v\) 和可测频带 \(E\)，定义
\[
 Q_E(v)=\frac1{2\pi}\int_E\frac{|\widehat v(\xi)|^4}{\xi^2}\,d\xi .
 \tag{6}
\]
所有进入 \(Q\) 的本篇测度均满足相应能量有限；近零的中心化消失也消除表面奇点。

## 2. 实际早段的质量相对四阶误差 [T]

### 定理279-A

沿(2)，对每个上述整数 \(K\)、每个 \(T>0\)，一致有
\[
 \boxed{\quad Q_{|\xi|\le T}(r_e)
 \ll_{\sigma,\beta}M^4(K/N)^{4\delta}(L+T^2).\quad}
 \tag{7}
\]
因此任意可测 \(E\subset\{|\xi|\le T\}\) 满足
\[
 \boxed{\quad
 \frac{|Q_E(r)^{1/4}-Q_E(r_l)^{1/4}|}{|M|L^{1/4}}
 \ll_{\sigma,\beta}
 \varepsilon(Y,K,T):=(K/N)^\delta(1+T^2/L)^{1/4}.
 \quad} \tag{8}
\]
常数不依赖 \(Y,N,K,T,E\)。

证明。令 \(u_0=\log K\)、\(H(u)=M(Y,e^u)\)，先限制到
\([0,u_0]\)，不作会新增右端跳跃的 Stieltjes 零延拓。
275-C 在整个 \([0,\tau]\) 上逐点给
\[
 |H(u)|\ll_{\sigma,\beta}P_\beta(N)e^{\delta u}
            \ll_{\sigma,\beta}|M|e^{\delta(u-\tau)}.
 \tag{9}
\]
所以对早段（下述范数均仅在 \([0,u_0]\) 取）
\[
 |m_e|,\ \|H\|_1\ll_{\sigma,\beta}|M|(K/N)^\delta,\qquad
 \|H\|_2^2\ll_{\sigma,\beta}M^2(K/N)^{2\delta}.
 \tag{10}
\]
这里积分的是衰减指数，不是长度为 \(L\) 的常数上界。

为说明275的有限路径估计可用于 \(K\ll Y\)，直接复写其证明。
原有限测度的分部积分、\(H(0)=0,H(u_0)=m_e\) 给
\[
 \widehat r_e(\xi)=m_e(\cos(u_0\xi)-1)
                   +\xi\int_0^{u_0}H(u)\sin(\xi u)\,du .
 \tag{11}
\]
令 \(h(u)=\operatorname{sgn}(u)H(|u|)/2\) 于 \(0<|u|<u_0\)，其余为零。
则 \(\widehat h=-i\int_0^{u_0}H(u)\sin(\xi u)\,du\)，且
\[
 \frac1{2\pi}\int_{\mathbb R}|\widehat h|^4
 =\|h*h\|_2^2\le\|h\|_1^2\|h\|_2^2
 =\tfrac12\|H\|_1^2\|H\|_2^2 .
 \tag{12}
\]
另有
\[
 \frac1{2\pi}\int_{\mathbb R}
       (1-\cos(u_0\xi))^4\,\frac{d\xi}{\xi^2}=\tfrac54u_0 .
 \tag{13}
\]
例如 \(k_{u_0}*k_{u_0}\) 的 primitive 在四个长为 \(u_0\) 的相邻区间
依次为 \(1/4,-3/4,3/4,-1/4\)，平方积分即(13)。
用 \(|z+w|^4\le8(|z|^4+|w|^4)\)、截带后的 \(\xi^2\le T^2\)，得
\[
 Q_{|\xi|\le T}(r_e)\le10m_e^4u_0+4T^2\|H\|_1^2\|H\|_2^2 .
 \tag{14}
\]
这一步没有要求截断端点等于 \(Y\) 或 \(2Y\)。代入(10)，用
\(u_0\le\tau\asymp L\) 即得(7)。最后在测度
\(\mathbf1_Ed\xi/(2\pi\xi^2)\) 上应用 \(L^4\) 三角不等式及其反向式，
得 \(|Q_E(r)^{1/4}-Q_E(r_l)^{1/4}|\le Q_E(r_e)^{1/4}\)，证明(8)。\(\square\)

(8)两边统一用原 \(M\) 归一化。在尚未控制 \(Q_E(r_l)\) 时，不能仅凭
\(M_l/M\to1\) 把它改成不同分母下两个未知大数的加性 \(o(1)\) 差。
下节只作有界性转移，避开此漏洞。

## 3. 实际正源分母和响应的转移 [T]

对 \(j=l\) 及完整源，分别记
\[
 D_j=\|F_{p_j}\|_2^2+\|F_{c_j}\|_2^2,\qquad
 J_{4,E}^{\,j}=\frac{1}{S_j^4D_j}\frac1{2\pi}
 \int_E\frac{|\widehat r_j|^4(|\widehat p_j|^2+|\widehat c_j|^2)}{\xi^2}d\xi .
 \tag{15}
\]
完整源省略下标，\(\mu=M/S,\mu_l=M_l/S_l\)。

### 引理279-B

若 \(K/Y\to0\)，则沿(2)
\[
 \frac{S_e}{S}=O_\sigma((K/Y)^a),\quad
 \frac{S_l}{S}=1+O_\sigma((K/Y)^a),\quad
 \frac{D_l}{D}=1+O_\sigma((K/Y)^a),\quad
 \frac{M_l}{M}=1+O_{\sigma,\beta}((K/N)^\delta).
 \tag{16}
\]
且存在仅依赖 \(\sigma\) 的固定阈值 \(K_\sigma>0\)，对完整和尾部源同时有
\[
 |\widehat p_j|^2+|\widehat c_j|^2\asymp_\sigma S_j^2
 \quad(|\xi|\ge K_\sigma),\qquad D_j\asymp_\sigma S_j^2L .
 \tag{17}
\]

证明。实际 Chebyshev 上界及部分求和给
\(A_e\ll_\sigma K^a\)，直接积分给 \(B_e\ll_\sigma K^a\)。
实际 \(A\ll_\sigma Y^a\)，而连续 \([Y/2,Y]\) 的质量 \(\gg_\sigma Y^a\)，
故 \(S\asymp_\sigma Y^a\)，得到前两式。最后一式来自(10)。
Brownian 正核恒等式为
\[
 D=\tfrac12\iint\min(u,v)\,[d\alpha(u)d\alpha(v)+db(u)db(v)].
 \tag{18}
\]
减去仅尾部的(18)，全部剩余项非负；\(\min(u,v)\le\tau\) 给
\[
 0\le D-D_l
 \le\tau(A_lA_e+B_lB_e)+\tfrac{\tau}2(A_e^2+B_e^2)
 \le\tau SS_e .
 \tag{19}
\]
又 \(D\gg_\sigma S^2L\)，故得第三式。

为核对尾部(17)，\(K\le Y/2\) 保留整个连续 bulk。log 密度
\(g(u)=e^{au-e^u/Y}\) 在 \([\log K,\tau]\) 零延拓后的总变差
不超过 \(2a^ae^{-a}Y^a\)，包括两个截断端点。
所以 \(|C_l(\xi)|\ll_\sigma Y^a/|\xi|\)，而 \(B_l\gg_\sigma Y^a\)；
取固定 \(K_\sigma\) 充分大，便有
\(\widehat c_l=B_l-\Re C_l\ge B_l/2\)。
与 \(|\widehat p_l|\le2A_l,|\widehat c_l|\le2B_l\) 合用即通道双边比较。
(18)只保留同一连续 bulk，lag 至少 \(L-\log2\)，给 \(D_l\gg S_l^2L\)；
上界用 \(\tau\ll L\)。完整源同证，也正是277-A。\(\square\)

### 推论279-C

若 \(K/Y\to0\)、\(\varepsilon(Y,K,T)=O(1)\)，对任意随尺度变化的
可测 \(E\subset\{K_\sigma\le|\xi|\le T\}\)，沿同一序列
\[
 \boxed{\quad
 J_{4,E}=O(\mu^4)
 \ \Longleftrightarrow\ Q_E(r_l)=O(M_l^4L)
 \ \Longleftrightarrow\ J_{4,E}^{\,l}=O(\mu_l^4).
 \quad} \tag{20}
\]
证明。(17)使每套实际响应除以其 \(\mu_j^4\) 后，双边比较于
\(Q_E(r_j)/(M_j^4L)\)。(8)给统一 \(M\) 分母下的有界性等价，
(16)再将尾部分母换成 \(M_l\)，它最终非零。三步合成即(20)。\(\square\)

若 \(\varepsilon=o(1)\)，还独立有 \(Q_E(r_e)=o(M^4L)\)。
这并不要求剩余能量已知有界，也不把 \(O\) 预算自动提高成完整 \(o\) 预算。

## 4. 两个可直接使用的频率--长度区域 [T]

### 多对数频带

固定 \(A>1/2,h>0\)，取
\[
 T=L^A,\qquad K=\lfloor N/L^h\rfloor .
\]
最终 \(2\le K\le Y/2\)，并且
\[
 \varepsilon\ll_{\sigma,\beta,A,h}L^{-h\delta+(2A-1)/4}.
 \tag{21}
\]
所以 \(h\ge(2A-1)/(4\delta)\) 即可应用(20)；严格大于时早段为
\(o(M^4L)\)。**等号只给 \(O\)，这里不能声称 \(o\)。**
于是每个固定多对数频带 \(\sqrt L<|\xi|\le L^A\)，均可在明确的
误差预算内删去实际 \(n\le N/L^h\) 与匹配连续前缀。
例如 \(\sigma=1/4,\beta=3/8,\delta=1/8,A=1\)，\(h>2\) 给 little-oh，
\(h=2\) 给有界转移。

### 幂级频带

固定 \(0<\kappa<1,\theta>0\)，取 \(K=\lfloor Y^\kappa\rfloor,T=Y^\theta\)。
则
\[
 \varepsilon\ll_{\sigma,\beta,\kappa,\theta}
 Y^{\theta/2-\delta(1-\kappa)}L^{-1/4}.
 \tag{22}
\]
因此
\[
 \boxed{\quad\theta\le2\delta(1-\kappa)
       \ \Longrightarrow\ Q_{|\xi|\le Y^\theta}(r_e)=o(M^4L).\quad}
 \tag{23}
\]
**此处等号也成立**，因为还保留 \(L^{-1/4}\)；与(21)的等号不同。
例如 \(\sigma=1/4,\beta=3/8,\kappa=1/2\)，删除 \(n\le\lfloor\sqrt Y\rfloor\)
可覆盖到 \(|\xi|\le Y^{1/8}\)。超出(23)只表示这个上界不足，不是失败定理。
形式上的 \(K=1\) 早段恒零，无须借助此幂级推论。

## 5. 算术输入、循环性及止损审计

| 输入 | 具体作用 | 删除后的失效位置 |
|---|---|---|
| 275由独立振荡证明存在的历史相对包络 | (9)--(10)产生真实 \((K/N)^\delta\) saving | 仅端点大质量不足；275-D正源运输反例否定替代 |
| 固定 \(\delta>0\) | 指数积分得到(10)，不损失额外历史长度 | \(\delta=0\) 时本证明的积分界及长度 saving 消失 |
| 同一个有限 Stieltjes 源和准确半开截断 | (11)及 \(r=r_e+r_l\) 精确 | 把 \(K\) 原子算两次或删去中心质量会改变被估计对象 |
| 实际正源、Chebyshev 上界、保留连续 bulk | (16)--(19)及响应双边接口 | 一般有符号系数不自动有这些分母和通道下界 |
| 有限频带及显式 \(\varepsilon\) 门槛 | (14)只付 \(T^2\)，(20)能吸收早段 | 不能令 \(T\to\infty\) 后丢弃增长项 |

(2)中的强质量阈值用于新序列的存在、与274高频及280固定模式接口；
定理279-A自身只需 \(M\ne0\) 和相对历史包络，而不另用质量下界。
没有假设 Weil 全正性、酉性、统一有限负指数或平方根均方误差。
这是显式公式型配置的 prime--continuum 子系统，通过256-C的条件性
capture/Schur 接口接入；Gamma 与上同调桥梁仍须另证。

与265的区别：265控制绝对尺度的 signed-PNT 截断，本篇(7)相对于同一
实际 \(M^4L\) 控制有限频带早段。与263的 positive-TV 截断障碍不冲突：
本篇在(7)的响应误差估计中保留早段素数和连续项的**带符号联合差异**，
没有用分开的总变差替换它；(16)的正源分母比较则确实分别控制 \(A_e,B_e\)。
与278一致：其坏的固定正整数模型振荡放在 \(x\asymp Y\)，删除早段
不删除该坏块；所以本篇没有从历史包络自动推出剩余中频。
275的实际序列已证明存在，但278并没有否定该序列的实际 \(\Lambda\) 预算。

适用范围：路径估计可用于具备对应包络的实误差模型；上述无条件算术应用
只在 Riemann \(\Lambda\) 源上建立。Dirichlet、自守或函数域情形的系数、
振荡选择与正通道须分别核验，不能直接称为 GRH 或函数域统一定理。

## 6. 本轮探索记录与下一最小引理

晋级的是(7)、(20)--(23)的实际长度删除，而非显式公式的重写。
下一最小问题可先取 \(\sigma=1/4,\beta=3/8\)，固定 \(h>2\)：
\[
 Q_{\sqrt L<|\xi|\le L}(r_l)
 \ll M^4L,\qquad K=\lfloor N/L^h\rfloor ,
 \tag{24}
\]
(24)中的 \(r_l\) 严格按(3)--(5)定义；离散和连续推前分别处理。
该式仍为[O]，
应估计实际系数的交叉相关；即使闭合也只是全中频的第一子区间。
完整剩余仍是275--277的 \(\sqrt L<|\xi|\ll T_*\)，其中任意固定
正倍数 \(T_*=Y\sqrt{\log(2L)/L}\) 以上已经由274闭合，不能再列作新缺口。

已检查但没有获得新上界的候选：

- 在 \(|\xi|\asymp L\) 上代入有限高度显式公式，尚未获得实际四阶 saving；
  280只登记可审计接口，不把“换成零点和”算作又一次缩小算术输入。
- 完整 Abel Mellin 积分的 Gamma 指数衰减不能套用在 \(N\in[Y,2Y]\)
  的硬截断上；必须保留有限端点及其代数 Fourier 尾。
- “大多数 \(Y\) 好”的均方定理不能自动与275的共尾记录子集相交；
  需要独立的好集交叉选择证明，本轮没有得到它。

周期决策：保留一条实际尾部中频主线；有限低位零点实验及接口强度审计仅作辅助。
若下一轮只能继续改写(24)，不再延伸等价表示，须拿出新估计、具体反例或修改目标。
David--Lapidus 线继续限额登记、未启动；本轮不更新 PDF。

独立复核记录：carrier_audit 已独立核对(7)--(23)的幂次、两个等号边界、
半开端点及 \(S,D,M\) 比较，落盘全文逆向复核通过。主代理采纳其参数可计算性、
测度量词、(24)记法及总变差作用域四处文字建议，并完整复核证明。
内部[T]不等于外部独立同行评审或 Goal 的论文级阶段完成。
