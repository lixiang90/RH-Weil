# 294. PNT 包络节省与固定源饱和审计

日期：2026-09-06。B1z 新周期第4轮；论文归属：独立 response 论文。
状态：[T/R] 实际匹配 Abel 前缀及记录交点的定量节省；
[T/R] 定性 PNT 已足以给严格 little-o 改进；
[T] 一般缓慢变化误差的交点接口；[N] 295给出的固定源饱和边界；
[O] 正确右侧绝对负迹预算。
本篇不证明 RH，不提出新的 PNT，也不把同义 RH 判据登记为新结构。

## 1. 最少算术输入与两个尺度量词

沿用[293](293-poisson-transport-and-right-shifted-record-currents.md)，固定
\(0<\sigma_0<\beta<1/2\)，记
\[
 d=\beta-\sigma_0,\qquad a_0=1-\sigma_0,\qquad
 \lambda=1-\beta,
 \qquad L=\log Y.
 \tag{1}
\]
本节的前缀估计适用于全部实数 \(Y\ge1\)、\(1\le X\le Y\)。
应用记录定理时才限制到284-D的同一整数 \(Y=N\to\infty\) 序列。
实际权与端点为
\[
 w_Y(x)=x^{-\sigma_0}e^{-x/Y},\qquad
 H_Y(u)=\sum_{n\le e^u}\Lambda(n)w_Y(n)
                 -\int_1^{e^u}w_Y(x)dx,
 \quad 0\le u\le L,
 \tag{2}
\]
\[
 E(x)=\psi(x)-x+1,\qquad E(1)=0,
 \qquad M=H_Y(L).
 \tag{3}
\]
\(\psi\) 和和式均取右连续完整原子，连续项使用相同端点。
这里保留整个因子 \(e^{-x/Y}\)，没有将它替换成1。
“匹配 Abel 权”不表示本篇已经控制 \(n>Y\) 的未截断 Abel 候选。

唯一用于明确速率的外部算术输入 [R] 是某个固定 \(c>0\) 下
\[
 |E(x)|\le C_c x e^{-c\sqrt{\log x}}\qquad(x\ge1).
 \tag{4}
\]
例如[Fiori--Kadiri--Swidinsky作者预印本v3](https://arxiv.org/abs/2204.02588)
给出 \(|\psi(x)-x|\ll x(\log x)^{3/2}
e^{-0.8476836\sqrt{\log x}}\)；任取固定 \(0<c<0.8476836\)，
吸收对数因子、常数1和有限小区间即得(4)。不取该端点常数，
不声称它为当前最优，也不把预印本核验写成正式出版全文审读。
经典 de la Vallée Poussin 形式的任意正 \(c\) 已足够；第3节还会去掉速率要求。

下面只需一个初等积分账本：对 \(A>0,C\ge0\)，令
\[
 \mathcal J(A,C)=\int_0^\infty e^{-Av+C\sqrt v}\,dv
 \le\frac2A\exp\!\left(\frac{C^2}{2A}\right)<\infty.
 \tag{5}
\]
不等式来自 \(C\sqrt v\le Av/2+C^2/(2A)\)。对 \(0\le v\le U\)，
\[
 \frac{e^{A(U-v)-C\sqrt{U-v}}}{e^{AU-C\sqrt U}}
 \le e^{-Av+C\sqrt v},
 \tag{6}
\]
因为 \(\sqrt U-\sqrt{U-v}\le\sqrt v\)。这避免假设小 \(u\) 上的包络递增。

### 引理294-A：所有匹配前缀，保留同一个 \(c\) [T/R]

由(4)可得
\[
 |H_Y(u)|\le C_{\sigma_0,c}
          e^{a_0u-c\sqrt u}
 \quad(0\le u\le\log Y),
 \tag{7}
\]
常数与 \(Y,u\) 无关。这里 \(c\) 在吸收原 PNT 对数因子之后，不再损失。

证明。Stieltjes 分部积分精确给
\[
 H_Y(\log X)=w_Y(X)E(X)
                    +\int_1^X E(x)(-w_Y'(x))dx .
 \tag{8}
\]
下端没有遗漏项，因为 \(E(1)=0\)；上端包括 \(n=X\) 的完整原子。
由 \(x\le X\le Y\)，
\(-w_Y'(x)=(\sigma_0/x+1/Y)w_Y(x)
\le(\sigma_0+1)x^{-\sigma_0-1}\)。
令 \(X=e^u\)，(4)、(8)的绝对值至多
\[
 C_c\left\{e^{a_0u-c\sqrt u}
       +(\sigma_0+1)\int_0^u e^{a_0v-c\sqrt v}dv\right\}
 \le C_c\{1+(\sigma_0+1)\mathcal J(a_0,c)\}
                   e^{a_0u-c\sqrt u}.
 \tag{9}
\]
最后一步是(6)的倒序积分。这就证明(7)。\(\square\)

265-A已证明匹配前缀的同型指数界；(7)不是重新发现该算术估计。
本篇重建它以核对保持 \(c\)、完整端点以及下面参数交点的统一性。

## 2. 正确右移：全部尺度上界与记录交点节省 [T/R]

取 \(\sigma'\in[1/2,3/4]\)，令
\[
 a=\sigma'-\sigma_0,\qquad r=1-\sigma',\qquad
 b=\sigma'-\beta,\qquad r+b=\lambda,
 \quad\theta=\frac r\lambda.
 \tag{10}
\]
因此 \(r\ge1/4\)、\(b\ge1/2-\beta>0\)，所有常数可在该区间统一。
令 \(P_a\) 为293-(3)的同一未中心化符号，\(W_a=e^{-au}H_Y(u)\)。
293的端点保留公式直接给
\[
 \tau_C|P_a|
 \le |M|e^{-aL}+a\|W_a\|_1+\|W_a\|_2/\sqrt2.
 \tag{11}
\]
所有范数仍对原变量 \(u\in[0,L]\)，\(\tau_C\) 仍是原 Cauchy 概率迹。

### 推论294-B：不使用记录的全部尺度估计

对全部 \(Y\ge1\)，由(7)有 \(|W_a(u)|\le C e^{ru-c\sqrt u}\)。
用(6)分别估计一、二次积分及端点，得到
\[
 \boxed{\quad \tau_C|P_{\sigma',Y,Y}|
       \ll_{\sigma_0,\beta,c}Y^{1-\sigma'}e^{-c\sqrt{\log Y}}.\quad}
 \tag{12}
\]
这里若 \(Y\) 非整数，素数和仍严格按 \(n\le Y\) 取值。
具体地 \(\|W_a\|_p\le C e^{rL-c\sqrt L}
\mathcal J(pr,pc)^{1/p}\)（\(p=1,2\)），端点同界；代入(11)即可。
式(12)只有经典 PNT 的绝对节省，没有用实际质量作归一化。

### 定理294-C：同一实际记录上的交点改进

现在且仅现在沿284-D的同一整数记录取 \(Y=N\)。记录历史给
\(|H_Y(u)|\le C|M|e^{-d(L-u)}\)，记
\[
 B=\max(1,|M|Y^{-d}),\qquad z=\log B\ge0,
 \qquad v_* =\frac{c+\sqrt{c^2+4\lambda z}}{2\lambda},
 \qquad U=v_*^2,\qquad T=B e^{-bU}.
 \tag{13}
\]
则在(10)全部参数中统一有
\[
 \boxed{\quad \tau_C|P_a|\ll_{\sigma_0,\beta,c}T
 \asymp_{\sigma_0,\beta,c}
 B^\theta\exp\!\left(-\frac{bc}{\lambda^{3/2}}\sqrt{\log B}\right).
 \quad}
 \tag{14}
\]
其中 \(\asymp\) 只比较两个**上界表达式** \(T\) 和右侧显式函数，
不表示实际 \(\tau_C|P_a|\) 已有同阶下界。

证明。由(7)和记录历史，选一个共同常数可使
\[
 |W_a(u)|\le C\,m(u),\qquad
 m(u)=\min\{e^{ru-c\sqrt u},B e^{-bu}\}.
 \tag{15}
\]
方程 \(\lambda U-c\sqrt U=z\) 的较大非负解正是(13)。
对 \(0\le u\le U\)，第一包络不大于第二包络；对 \(u\ge U\) 则相反。
在 \(B=1\) 时 \(u=0\) 也是交点，这不改变上述分段。
二者在 \(U\) 的共同值为 \(T=e^{rU-c\sqrt U}\)。

不用假设 \(U\le L\)。将区间扩大至 \([0,\infty)\)，对 \(p=1,2\)
先在 \([0,U]\) 反向代换 \(u=U-v\)，用(6)，再积指数尾，得到
\[
 \int_0^\infty m(u)^pdu
 \le T^p\left\{\mathcal J(pr,pc)+\frac1{pb}\right\},
 \qquad
 \sup_{u\ge0}m(u)\le e^{c^2/(4r)}T.
 \tag{16}
\]
最后一个式子来自 \(\sup_{v\ge0}e^{-rv+c\sqrt v}=e^{c^2/(4r)}\)，
在 \(u\ge U\) 的尾部则直接 \(m(u)\le T\)。
故(15)--(16)同时控制(11)中的端点、\(L^1\) 与 \(L^2\) 项，给第一上界。
所有 \(\mathcal J\)、\(b^{-1}\) 和指数常数均由(10)一致控制。

又有
\[
 \sqrt{z/\lambda}\le v_*\le\sqrt{z/\lambda}+c/\lambda,
 \qquad T=B^\theta e^{-(bc/\lambda)v_*}.
 \tag{17}
\]
因而
\[
 e^{-bc^2/\lambda^2}B^\theta e^{-bc\sqrt z/\lambda^{3/2}}
 \le T\le B^\theta e^{-bc\sqrt z/\lambda^{3/2}},
 \tag{18}
\]
即得(14)的表达式比较。\(\square\)

沿记录 \(B\gg Y^{1/2-\beta}\ell(Y)\to\infty\)，其中
\(\ell(Y)=\max(1,\log\log\log Y)\)。因为 \(b\) 有统一正下界，
\[
 \tau_C|P_a|=o(B^\theta)
 \quad\text{一致于 }\sigma'\in[1/2,3/4].
 \tag{19}
\]
因此(14)严格改进293-C，不只是重新说明右移量相对 \(|M|\) 小。
包含 \(B=\max(1,|M|Y^{-d})\) 的(14)不得移用于任意 \(Y\)：
质量很小的非记录点未必控制其内部历史。(12)才是本篇不需记录的版本。

## 3. 定性 PNT、输入作用与循环性边界

### 命题294-D：严格 little-o 不需要 PNT 误差率 [T/R]

对同一记录与固定参数，只用 \(\psi(x)=x+o(x)\) 即可得到(19)。
这里说的是一个足够弱的 PNT 形式，不断言它是逻辑上的必要条件。

证明。由(8)，对每个 \(\varepsilon>0\)，存在固定 \(U_\varepsilon\)，使
\[
 |H_Y(u)|\le\varepsilon e^{a_0u}
 \quad(U_\varepsilon\le u\le\log Y)
 \tag{20}
\]
一致于所有 \(Y\ge e^u\)。具体先在 \(x\ge X_0\) 上使 \(|E(x)|/x\)
任意小，再用 \(-w_Y'(x)\le(\sigma_0+1)x^{-\sigma_0-1}\)；
\(x<X_0\) 的固定积分除以 \(e^{a_0u}\) 后趋零。这个证明不取依赖 \(Y\) 的阈值。

取 \(0<\varepsilon<1\)。在 \(u\ge U_\varepsilon\) 的区域，(20)与历史给
\[
 |W_a(u)|\le C\min\{\varepsilon e^{ru},B e^{-bu}\}.
 \tag{21}
\]
两个纯指数在 \(u_\varepsilon=\lambda^{-1}\log(B/\varepsilon)\) 相交，
共同值为 \(\varepsilon^{b/\lambda}B^\theta\)。直接分段积分给一、二次范数
和上确界均为该量的 \(O(1)\) 倍，参数常数一致。
固定低段 \([0,U_\varepsilon]\) 仅用Chebyshev或局部有限源控制，贡献
为 \(C_\varepsilon\)，与 \(Y,\sigma'\) 无关；充分大记录有 \(L>U_\varepsilon\)。
代入(11)，得到
\[
 \frac{\tau_C|P_a|}{B^\theta}
 \le C\varepsilon^{(1/2-\beta)/\lambda}
              +C_\varepsilon B^{-\theta}.
 \tag{22}
\]
先令记录 \(Y\to\infty\)，利用 \(B\to\infty\) 及 \(\theta\ge1/(4\lambda)\)，
再令 \(\varepsilon\to0\)，证明统一的(19)。\(\square\)

### 3.1 这一步究竟减少了什么

- 独立算术输入是 PNT 的有符号误差；Chebyshev 只控制正源总量，单独没有(20)。
- 同一实际记录只负责 \(B e^{-bu}\) 历史包络，不由 PNT 自动产生新的质量选择。
- 匹配权、完整端点和 \(E(1)=0\) 负责(8)、(11)，不能改成两个独立正源的尾预算。
- 固定 \(\sigma_0<\beta<1/2\) 负责统一的 \(b>0\)；令 \(\beta\) 随尺度趋近中心线须重审记录与全部常数。
- 原 Cauchy 迹及293的真实端点公式保持物理归一化；(14)没有除以实际质量冒充负迹。

293的有限完成候选、Gamma紧参数区间 \(L^1\) 界和均值界已经独立建立，故
\[
 \kappa_Y^\sharp=\tfrac12\tau_C|P_a|+O(1)
 \ll_{\sigma_0,\beta,c}1+T .
 \tag{23}
\]
在任何 \(\delta_Y>0\to0\)、\(\sigma'_Y=1/2+\delta_Y\) 的同一记录上适用。
本篇没有证明 \(\kappa_Y^\sharp=O(1)\)：\(T\) 仍为
\(\exp(\theta\log B-O(\sqrt{\log B}))\to\infty\)。
上界表达式发散不等于实际负迹发散，但它明确说明本项 PNT 节省尚未关闭目标。
对293-(35)的明确日程，绝对有界预算已有 RH 等价强度；本篇没有将它变成更弱公理。
条件 RH 估计、未知零点的正实部或非构造完备化均未用于(7)--(23)。

265已有 PNT 前缀，293已有 Chebyshev/历史交点；本轮有限进展只登记二者在正确
右侧原迹中的严格剩余量节省。不是新 PNT、不是新半群框架，也未认证文献新颖性。
下一最小输入仍应给真实有符号误差的新节省，或审计此包络机制是否可被固定源饱和；
只再改写相同积分或 Gram 不晋级。

## 4. 一般次幂 PNT 误差的统一接口 [T]

为检验上界是否已经被模型饱和，不能只针对某个选定的平方根常数。
下述解析命题给出一个明确的包络类；不预设它对所有算术源都成立。

### 命题294-E：缓慢变化误差包络

设 \(\omega:[0,\infty)\to[0,\infty)\) 连续、最终为 \(C^1\)，且
\[
 \omega(u)\longrightarrow\infty,\qquad \omega'(u)\longrightarrow0.
 \tag{24}
\]
特别地 \(\omega(u)=o(u)\)。设一个固定右连续实局部BV误差 \(E\) 满足
\(E(1)=0\) 及
\[
 |E(x)|\le Cx\exp(-\omega(\log x)).
 \tag{25}
\]
以相同匹配权定义 \(H_Y(u)=\int_{(1,e^u]}w_Y(x)\,dE(x)\)、
\(M=H_Y(L)\)，并假设在所选尺度上有293的历史包络
\[
 |H_Y(u)|\le C_e|M|e^{-d(L-u)}\quad(0\le u\le L).
 \tag{26}
\]
定义 \(B=\max(1,|M|e^{-dL})\)。当 \(B\) 足够大时，方程
\[
 \lambda U-\omega(U)=\log B
 \tag{27}
\]
有唯一充分大的解 \(U=U_\omega(B)\)。对
\(\sigma'\in[1/2,3/4]\)、\(a,r,b,\theta\) 如(10)，一致有
\[
 \tau_C|P_a|\ll_{\sigma_0,\beta,\omega,C,C_e}T_\omega(B,\sigma'),
 \qquad
 T_\omega=B e^{-bU}
   =B^\theta\exp\!\left(-\frac b\lambda\omega(U)\right).
 \tag{28}
\]
该命题同样适用于固定正整数源减连续背景的误差，只要(25)--(26)
独立验证；不要求未知零点、Euler乘积、函数方程或某个极化。
本节常数允许依赖固定源的两个界 \(C,C_e\)，不声称对任意放大源统一。

证明。先由(24)的导数控制积分，得 \(\omega(u)=o(u)\)。
取固定 \(u_0\)，使当 \(u\ge u_0\) 时
\[
 |\omega'(u)|\le
 \min\{a_0/2,\lambda/2,1/8\}.
 \tag{29}
\]
于是 \(a_0u-\omega(u)\) 的导数至少 \(a_0/2\)；
与(8)相同的分部积分并分开固定低段，给出
\[
 |H_Y(u)|\le C_{\sigma_0,\omega,C}
                  e^{a_0u-\omega(u)}\quad(0\le u\le L).
 \tag{30}
\]
具体地，高段指数积分至多
\(2e^{a_0u-\omega(u)}/a_0\)，低段为固定常数；
因右侧最终趋于无穷且在固定紧集有正下界，这个常数可统一吸收。
同一论证对全部 \(Y\ge e^u\) 有效。

函数 \(g(u)=\lambda u-\omega(u)\) 在 \([u_0,\infty)\) 严格递增且趋于无穷。
取 \(\log B>\max_{[0,u_0]}g\)，就得到(27)的唯一大解，且
\[
 |e^{-au}H_Y(u)|\le C\,
 m_\omega(u),\qquad
 m_\omega(u)=\min\{e^{ru-\omega(u)},B e^{-bu}\}.
 \tag{31}
\]
在 \([u_0,U]\) 第一个包络较小，\([U,\infty)\) 第二个较小。
并且 \(ru-\omega(u)\) 的导数至少 \(r/2\)，因为 \(r\ge1/4\)。
对 \(p=1,2\)，因此有
\[
 \int_{u_0}^U m_\omega(u)^pdu\le \frac{2}{pr}T_\omega^p,
 \qquad
 \int_U^\infty m_\omega(u)^pdu=\frac1{pb}T_\omega^p.
 \tag{32}
\]
固定区间 \([0,u_0]\) 的范数与上确界由第一包络统一控制；
而 \(T_\omega=e^{rU-\omega(U)}\to\infty\) 一致于全部 \(\sigma'\)，故低段可吸收。
高段上确界至多 \(T_\omega\)。于是
\(\|e^{-au}H_Y\|_1+\|e^{-au}H_Y\|_2+|M|e^{-aL}\ll T_\omega\)，
不要求 \(U\le L\)。应用(11)，并用(27)消去 \(U\) 的线性部分，即得(28)。
\(\square\)

### 4.1 常数变化稳定性与不能跨越的量级

若 \(U_j\to\infty\)，且
\[
 B_j\asymp e^{\lambda U_j-\omega(U_j)},
 \tag{33}
\]
则 \(U_\omega(B_j)=U_j+O(1)\)。这是(29)和
\(g(U_\omega(B_j))-g(U_j)=O(1)\) 的直接后果。
从而在相同紧参数区间上
\[
 T_\omega(B_j,\sigma')\asymp
                    e^{(1-\sigma')U_j-\omega(U_j)}.
 \tag{34}
\]
这些常数允许依赖(33)的两个比较常数，但不依赖 \(j,\sigma'\)。
这是将真实端点质量与模型构造振幅对应时需要的稳定性，不是改变迹归一化。

在(24)下，(28)右侧为 \(B^{\theta-o(1)}\)，仍然趋于无穷；
不论选取哪一个固定的这类次幂误差，单独使用该上界均不能证明绝对有界。
这句话只评价**上界表达式**。真正的模型同阶下界另见
[295](295-fixed-positive-source-right-trace-saturation.md)，不能用表达式发散替代。
平方根误差(4)属于该类；更一般的光滑次线性误差需分别验证(24)--(25)，
本文不在没有来源核验的情况下宣布某个更强形状为当前算术纪录。

## 5. 独立审计与停止接口

### 5.1 可复现的有限包络检查 [E]

[pnt_record_envelope_probe.py](../scripts/pnt_record_envelope_probe.py)
只检查合成包络，不筛素数，也不把任意小尺度伪称为实际记录。
它使用MP50，在 \(\sigma'=0.5,0.6,0.75\)、
\(c=1/8,1/2,2\)、\(\log B=0,4,16,64,256\) 的45组配置中，
检查交点、完整半轴的一二次范数、安全上确界因子与平方根对数节省系数。
这些 \(c\) 只是模型参数，不是经本脚本认证的算术PNT常数。

为了独立核对(5)的积分，脚本还使用其初等闭式
\[
 \mathcal J(A,C)=\frac1A+
 \frac{C\sqrt\pi}{2A^{3/2}}
 e^{C^2/(4A)}
 \operatorname{erfc}\!\left(-\frac{C}{2\sqrt A}\right).
 \tag{35}
\]
证明是先令 \(v=x^2\)，再将
\(\int_0^\infty2x e^{-Ax^2+Cx}dx\) 分部积分并完成平方。
主证明只需(5)的上界，不依赖浮点积分。

~~~text
python -B scripts/pnt_record_envelope_probe.py
~~~

作者和主代理分别复跑PASS；主代理约1.73秒。
\(\mathcal J\)闭式与真正无限积分的最大相对误差约
\(2.93\cdot10^{-51}\)，交点残差约 \(3.42\cdot10^{-49}\)。
包络范数用交点前数值积分加交点后的**精确指数尾**，没有丢掉半轴尾部。
12个有限样本显示不能简单写 \(\sup m\le T\)：例如
\(\sigma'=0.75,c=2,B=1\) 时 \(\sup m/T\approx46.5255\)。
正式证明使用(16)的安全因子，不依赖这些样本外推。
全部浮点结果只标[E]，不是区间认证、渐近下界或RH证据。

### 5.2 逆向审计记录

主代理重建一般命题294-E及根稳定性，carrier_audit完整逆向审计。
审计发现并已补清：对一般BV源，(28)的常数还须依赖
(25)--(26)中的 \(C,C_e\)，不能省略而声称对任意放大源统一。
修订后全文复核PASS；midband_compute另行完整读取全文及一般推广，
独立复核也PASS，并明确脚本不验证实际记录、一般 \(\omega\) 或统一渐近。
295的固定源证明已由主代理、carrier_audit和midband_compute各自全文复核通过。

仓库布局检查、11项布局回归测试与检查注册覆盖测试通过。
后者仅核验core=75、B1h=1、B1i=1，共77项的注册与mock调度，
不是执行77项重计算；本轮没有运行heavy全套或更新PDF。

### 5.3 本四轮周期的实际决策

291--295依次完成低代价平方证书、固定左侧负迹障碍、真实右移的同阶补偿，
以及本篇的PNT剩余量节省。295把(28)的上界做到指定固定源上的同阶下界，
所以仅更换固定的光滑次幂PNT包络，不再作为可推进的普遍估计路线。
但295的germ非亚纯，已被真实zeta的已知解析结构排除；
因此不能停止所有实际右侧路线，也不能把这个模型当作完整Weil反例。

下一最小测试先核对285/287/289的已有结果，再对固定有限非实Mellin极点包
研究正确右侧交点尺度的严格缺口，必须明确极点数和高度增长时失去一致性的项。
只重复已有有限零点展开、Landau论证或重新命名RH等价预算则不晋级。
需要的仍是模型未保留的算术或解析结构所给的独立有符号估计。
内部证明与有限计算均不替代新颖性审查、外部同行评审或Goal阶段验收。
