# 265. 实际带符号PNT能量与四份差异的截断桥梁

日期：2026-09-05。路线：NCE-8 / B1u。论文归属：Vaughan--Brownian response。

状态：[T] 所有matched cutoff一致的实际signed primitive指数界；
[T] 全源 \(J_4\) 的更强无条件绝对衰减；
[T] 小窗口实际response差的signed改进及四阶充分证书；
[O] 相对实际质量差的双discrepancy算术估计。
只记录Markdown；不证明RH/GRH、零点比例或完整Gamma响应增益。

## 1. 固定输入与归一化

沿用258、263的实际一侧源，固定
\[
 0<\sigma<1,\quad a=1-\sigma,\quad Y\longrightarrow\infty,\quad
 L=\log Y,\quad Y\le N<\infty .
 \tag{1}
\]
\(\alpha\) 的系数为 \(\Lambda(n)n^{-\sigma}e^{-n/Y}\)，
\(\beta\) 对应 \(\int_1^N x^{-\sigma}e^{-x/Y}dx\)，同一endpoint匹配。
记 \(A,B,S=A+B,M=A-B\)，
\[
 p=\int k_\lambda d\alpha,\quad c=-\int k_\lambda d\beta,\quad
 r=p+c,\quad k_\lambda=(\delta_\lambda+\delta_{-\lambda})/2-\delta_0,
\]
\[
 K=A^2+B^2,\quad D=\|F_p\|_2^2+\|F_c\|_2^2,\quad
 \mathbf P=(F_{r*r*p},F_{r*r*c}),\quad
 J_4=\frac{\|\mathbf P\|^2}{S^4D},\quad \mu=M/S.
 \tag{2}
\]

唯一外部算术误差输入 [R] 为263核验过的
Fiori--Kadiri--Swidinsky, Corollary 1.4：
\[
 |\psi(x)-x|\ll x(\log x)^{3/2}e^{-c_*\sqrt{\log x}},
 \quad c_*=0.8476836 .
 \tag{3}
\]
对每个固定 \(0<d<c_*\)，令
\[
 E=E_d(Y)=e^{-d\sqrt L}.
 \tag{4}
\]
所有本轮常数允许依赖 \(\sigma,d\)；涉及窗口时还依赖一个先固定的 \(k>0\)。
不取 \(d=c_*\)，不宣称该外部常数为当前最佳。

263-C及连续源bulk给 \(S\asymp_\sigma Y^a\)。
正minimum kernel还给
\[
 D\ge c_\sigma L S^2.
 \tag{5}
\]
证明：只保留 \(\beta\) 在 \(x\in[Y/2,Y]\) 的质量 \(b_\sigma Y^a\)，
两个lag的minimum至少 \(L-\log2\)，且其kernel系数为 \(1/2\)。
这不需要对未知零点作假设。

## 2. 加权部分和与全源primitive [T]

置 \(w_Y(x)=x^{-\sigma}e^{-x/Y}\)、\(R_\psi(x)=\psi(x)-x\)，并定义
\[
 K_Y(X)=\sum_{2\le n\le X}\Lambda(n)w_Y(n)-\int_1^X w_Y(x)dx.
 \tag{6}
\]

### 引理265-A：统一prefix界

当 \(2\le X\le Y\)，有
\[
 |K_Y(X)|\le C_{\sigma,d}X^a e^{-d\sqrt{\log X}}.
 \tag{7}
\]
允许端点采用 \(n<X\)；常数调整后同一结论成立。

证明：精确分部积分为
\[
 K_Y(X)=w_Y(1)+w_Y(X)R_\psi(X)
                   -\int_1^X R_\psi(x)w_Y'(x)dx .
 \tag{8}
\]
\(w_Y(1)\) 来自 \(R_\psi(1)=-1\)，不可删除。
选 \((d/c_*)^2<\theta<1\) 和 \(d/\sqrt\theta<d_1<c_*\)。
在 \(x\ge X^\theta\) 上，(3)给
\(|R_\psi(x)|\le Cx e^{-d\sqrt{\log X}}\)。
因 \(Y\ge X\)，
\[
 \int_0^X x|w_Y'(x)|dx
 \le \int_0^X(\sigma x^{-\sigma}+Y^{-1}x^a)dx
 \le C_\sigma X^a.
\]
低段仅用 \(|R_\psi(x)|\ll x\log(2x)\)，得
\(O(X^{a\theta}\log X+1)\)，由固定 \(\theta<1\) 吸收。
endpoint同样受控。改变闭端点最多减去
\(\Lambda(X)w_Y(X)\le X^{-\sigma}\log X\)，也被(7)吸收。
有限小 \(X\) 调整常数即可。\(\square\)

### 定理265-B：全源signed primitive的统一能量界

对全部有限 \(N\ge Y\)，有
\[
 \boxed{\ \|F_r\|_2\le C_{\sigma,d}S\sqrt L\,E.\ }
 \tag{9}
\]

证明：令
\[
 R_Y(X,N)=\sum_{X<n\le N}\Lambda(n)w_Y(n)-\int_X^N w_Y(x)dx
 \quad(1\le X\le N),
 \tag{10}
\]
在 \(X>N\) 时定义为0。258-B的已有恒等式给
\[
 \|F_r\|_2^2=\frac12\int_0^\infty |R_Y(e^u,N)|^2du.
 \tag{11}
\]
当 \(1\le X\le Y\)，用263-C和(7)比较
\(R_Y(X,N)=M(Y,N)-K_Y(X)\)。
函数 \(X^a e^{-d\sqrt{\log X}}\) 最终递增，且趋于无穷，因此
\(|R_Y(X,N)|\le CY^aE\)，一致覆盖较小的固定 \(X\)。

当 \(Y\le X\le N\)，在Stieltjes公式的全部积分变量上都有
\(|R_\psi(x)|\le CxE\)，从而
\[
 |R_Y(X,N)|
 \le CE\left[X^ae^{-X/Y}+N^ae^{-N/Y}
 +\int_X^N(\sigma x^{-\sigma}+Y^{-1}x^a)e^{-x/Y}dx\right]
 \le CY^aE e^{-X/(2Y)}.
 \tag{12}
\]
最后一步代换 \(x=Yv\)，用指数吸收所有固定幂；所有常数与 \(N\) 无关。
于是(11)在 \(0\le u\le L\) 的贡献至多 \(CLY^{2a}E^2\)，
而其余部分用
\(\int_L^\infty e^{-e^{u-L}}du<\infty\) 给 \(CY^{2a}E^2\)。
由 \(S\asymp Y^a\) 得(9)。\(\square\)

### 推论265-C：更强的实际绝对四阶响应界

有
\[
 \boxed{\ \sup_{N\ge Y}J_4(Y,N)
          \le C_{\sigma,d}e^{-2d\sqrt{\log Y}}.\ }
 \tag{13}
\]
证明：仅在一份 \(r\) 上保留signed primitive，另一个因子及第三正通道用Young：
\[
 \|\mathbf P\|^2
 \le \|r\|_{\rm TV}^2
       \bigl(\|p\|_{\rm TV}^2+\|c\|_{\rm TV}^2\bigr)\|F_r\|_2^2
 \le16S^2K\|F_r\|_2^2.
 \tag{14}
\]
除以 \(S^4D\)，用 \(K\le S^2\)、(5)、(9)即可。\(\square\)

这是对259绝对 \(O((\log L)/L)\) ceiling的改进，不是新的PNT。
也不推出 \(J_4=O(\mu^4)\)：263只有 \(|\mu|\le CE\)，没有所需的质量下界；
即使另有 \(|\mu|\asymp E\)，(13)仍比质量四次预算多损失两个 \(E\) 因子。

## 3. 实际signed窗口误差 [T]

对先固定的 \(k>0\)，允许
\[
 0\le H\le k\sqrt L,\quad I_H=[L-H,L+H],
 \quad \alpha_H=\alpha|_{I_H},\quad\beta_H=\beta|_{I_H}.
 \tag{15}
\]
令下标 \(H\) 表示局部centered源，out表示补集源，
\(e=r-r_H\)、\(S_{\rm out}=A_{\rm out}+B_{\rm out}\)。
定义 \(X=Ye^{-H}\)、\(Z=Ye^H\)；当 \(N<Z\) 时高尾为空。

### 定理265-D

一致有
\[
 S_{\rm out}\le CS e^{-aH},\qquad
 \|F_e\|_2\le CS\sqrt L\,e^{-aH}E,\qquad
 \|F_{r_H}\|_2\le CS\sqrt L\,E,\qquad
 |M-M_H|\le CS e^{-aH}E .
 \tag{16}
\]

证明：正低尾质量由 \(\psi(x)\ll x\) 与分部积分给 \(O(X^a)\)；
正高尾质量给 \(O(Y^ae^{-Z/(2Y)})\)。
因为 \(e^{-e^H/2}\le C_a e^{-aH}\)，得到第一式。

对signed低尾，其正半轴tail在 \(u<\log X\) 时为
\(K_Y(X^-)-K_Y(e^u)\)，其余为0。
(7)使其绝对值至多
\(CX^a e^{-d\sqrt{L-H}}\)。
这里 \(X\to\infty\) 一致成立，并且
\[
 e^{-d\sqrt{L-H}}
 =E\exp\left(\frac{dH}{\sqrt L+\sqrt{L-H}}\right)
 \le C_{d,k}E .
 \tag{17}
\]
积分长度至多 \(L\)，故该primitive范数至多 \(CS\sqrt L e^{-aH}E\)。
边界原子约定由(7)的开端点版本处理。

signed高尾在 \(u\le\log Z\) 时为常数 \(R_Y(Z,N)\)，
在 \(u>\log Z\) 时为 \(R_Y(e^u,N)\)；
(12)及其平方积分给范数上界
\(CY^aE\sqrt{L+H+1}\,e^{-e^H/2}\)。
用 \(H\le k\sqrt L\) 与同一指数比较，即得第二式。
第三式由 \(r_H=r-e\) 的范数三角不等式。

最后的质量差界直接使用同一低尾prefix界及高尾(12)，不作primitive积分。
\(\square\)

它仍不是 \(|M_H|=O(|M|)\)：后者还需要相对于实际 \(M\) 的控制。

### 推论265-E

以full-source分母定义 \(\mathbf P_H=(F_{r_H*r_H*p_H},F_{r_H*r_H*c_H})\)，则
\[
 \boxed{\ \frac{\|\mathbf P-\mathbf P_H\|}{S^2\sqrt D}
       \le C_{\sigma,d,k} e^{-aH}e^{-d\sqrt L}.\ }
 \tag{18}
\]

证明：记 \(K_{\rm out}=A_{\rm out}^2+B_{\rm out}^2\)。
精确telescoping及Young给
\[
 \|\mathbf P-\mathbf P_H\|
 \le8S\sqrt K\,\|F_e\|_2
       +4S\sqrt{K_{\rm out}}\,\|F_{r_H}\|_2 .
 \tag{19}
\]
第一项使用 \(\|r+r_H\|_{\rm TV}\le4S\)，第二项使用
\(\|r_H\|_{\rm TV}\le2S\)，通道TV向量分别至多 \(2\sqrt K,2\sqrt{K_{\rm out}}\)。
再用(5)、(16)、\(\sqrt{K_{\rm out}}\le S_{\rm out}\)得(18)。\(\square\)

相较正源绝对tail，这是真正由实际算术抵消获得的额外 \(E\) 因子，
不是因为把误差改名。它不与263冲突：263给的是positive majorant的下界，
不是signed response误差下界。(18)仍不自动达到 \(O(\mu^2)\)；
只知道 \(\mu=O(E)\) 不能将右侧除以未知且可能很小的 \(\mu^2\)。

## 4. 保留两份discrepancy的四阶充分证书 [T/O]

定义可由四份实际signed源直接计算的量
\[
 A_4=\|F_{e*(r+r_H)}\|_2,\qquad
 B_4=\|F_{r_H*r_H}\|_2 .
 \tag{20}
\]
本节的 \(A_4,B_4\) 是范数，不是源质量或假定的矩常数。
对任何具有有限一阶lag矩的有限正源与任何可测限制，均有
\[
 \boxed{\ \|\mathbf P-\mathbf P_H\|
           \le2\sqrt K\,A_4+2\sqrt{K_{\rm out}}\,B_4.\ }
 \tag{21}
\]
证明：逐通道 \(\tau=p,c\) 使用measure恒等式
\[
 r*r*\tau-r_H*r_H*\tau_H
 =e*(r+r_H)*\tau+r_H*r_H*(\tau-\tau_H).
 \tag{22}
\]
只对最后一个正通道的centered测度用Young，不对两份discrepancy取TV。
通道TV向量界即给(21)。\(\square\)

例如
\[
 A_4^2=\frac1{2\pi}\int_{\mathbb R}
       \frac{|\widehat r(\xi)^2-\widehat r_H(\xi)^2|^2}{\xi^2}d\xi ;
 \tag{23}
\]
这保留低/高尾与bulk的共同符号，不是任意系数Bessel界。
在(15)的实际窗口中，一条明确的充分算术输入为
\[
 \boxed{\ A_4+e^{-aH}B_4=O(M^2\sqrt L).\ }
 \tag{24}
\]
(5)、(16)、(21)表明它推出所需signed transfer。
它把第三正通道用质量预算去除，留下四份而不是六份源的量；
一般不声称必要，也没有证明其比RH弱。
无条件(19)再次把一个signed因子换为TV才得到(18)，所以目前只实现一份抵消，
不能宣称两份算术saving已经同时得到。新一轮只研究(24)的实际联合卷积，
不把它列作已证明的正性公理。

## 5. 审计、失败尝试与范围

初次用Stieltjes得到全频
\(|\widehat r(\xi)|/S\ll \min(1,(1+|\xi|)E)\)，
在 \(1\) 与 \(E^{-1}\) 切分频带只给 \(J_4=O(E/L)\)。
(9)保留物理primitive，比这个频率逐点majorant更强，故采用(13)。
这两个推导均不提供相对质量差下界。

独立输入及其作用：

1. matched endpoint与 \(x=1\) 的非零边界项保证(8)精确；
2. 外部定量PNT给signed估计(7)、(12)，定性PNT本身不给本轮指数率；
3. 正源bulk给(5)，正通道TV只在(14)、(19)、(21)指定位置使用；
4. \(k,d,\sigma\) 先固定，保证(17)的常数与 \(Y,N,H\) 无关；
5. 源的有限一阶lag矩允许primitive及卷积能量；本轮仅陈述有限 \(N\)，无未证finite-to-infinite跳步。

删除正源时 \(K\) 不能代替通道TV；不匹配cutoff时需另记endpoint mismatch。
若 \(H\) 增长到固定比例的 \(L\)，(17)不再有同一个 \(E\) rate，
不能直接扩大(18)的范围。\(H=0\)、空局部源或质量零点不需相除，均被定理包含。

应用范围为实际Riemann正源；其他实正系数模型须独立提供同型PNT及bulk。
复Dirichlet/一般自守通道、Gamma-complete和上同调桥梁仍开放。
本轮没有假设酉性、完整Weil正性或有限负指数。

[R] 外部PNT出处：[Fiori--Kadiri--Swidinsky v3, Corollary 1.4](https://arxiv.org/pdf/2204.02588v3)，
发表于JMAA 527(2) (2023), article127426；书目及版本审计见263。
经典PNT、分部积分与Young不等式本身不作为新颖性主张。

运行 `python -B scripts/signed_truncation_bridge_audit.py`，
用30个有理正源/窗口实例，逐measure检查(22)，并独立比较primitive/distance能量、
(14)及(21)的有理平方形式；覆盖零宽窗口、全删/全留、质量平衡及端点原子。
有限精确运算为[E]，不认证(3)或任何渐近PNT结论。
证明还经独立逆向检查；发表价值与文献优先权保持[O]。
