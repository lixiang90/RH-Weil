# 同一整数系统的正、自对偶 Mellin 核也能制造离线零点

2026-10-20；root 提议的具体 completion-gauge 反测试之独立核验。
同 C027 的一次直接检验，不增迭代；不改公共状态或 Git。
以下代数与估计独立重算，不读取任何未知 ζ 零点位置。

## 1. 固定对象、核与规范

算术系统始终是同一组普通正整数；prime/prime-power/integer 测度完全不改。
取 Mellin 与 Fourier 约定
\[
\mathcal Mg(s)=\int_0^\infty g(x)x^{s-1}\,dx,\qquad
\mathcal Ff(\xi)=\int_{\mathbb R}f(x)e^{-2\pi ix\xi}\,dx.
\]
令
\[
g_0(x)=e^{-\pi x^2},\quad
G_0(s)=\tfrac12\pi^{-s/2}\Gamma(s/2),\quad
F_0(x)=\sum_{n\ge1}g_0(nx),\quad
\Psi_0(s)=G_0(s)\zeta(s).
\]
Gaussian Fourier/Poisson 身份给出
\[
F_0(x)=x^{-1}F_0(x^{-1})+\tfrac12(x^{-1}-1). \tag{1}
\]
标准输入可核于 Hilberdink–Lapidus
[§3.2 的 theta identity](https://arxiv.org/html/math/0410270)，
以及 [DLMF §25.4](https://dlmf.nist.gov/25.4) 的完成化反射关系。
本文不以 RH 或未知零点为这些标准身份的前件。

固定 λ=2、A=λ^{1/4}，不是拟合参数。定义
\[
B(s)=(1+A\lambda^{-s})(1+A\lambda^{s-1})
=1+A^2/\lambda+A\lambda^{-s}+(A/\lambda)\lambda^s. \tag{2}
\]
则 B(1−s)=B(s)，B 是实型、指数型整个函数。

## 2. 真正正核证书，不是形式商

定义
\[
g_B(x)=(1+A^2/\lambda)g_0(x)+A g_0(\lambda x)
       +(A/\lambda)g_0(x/\lambda). \tag{3}
\]
三个系数严格正，故 g_B(x)>0。其偶延拓是 Schwartz 函数。
尺度变换的 Mellin 公式直接给
\[
\mathcal M[g_0(\lambda\cdot)](s)=\lambda^{-s}G_0(s),\qquad
\mathcal M[g_0(\cdot/\lambda)](s)=\lambda^sG_0(s).
\]
所以
\[
G_B=G_0B,\qquad F_B(x)=\sum_{n\ge1}g_B(nx),\qquad
\Psi_B(s)=G_B(s)\zeta(s)=B(s)\Psi_0(s)\quad(\Re s>1). \tag{4}
\]
Tonelli/绝对积分换序合法：所有实绝对值都受有限个 Gaussian Mellin
积分及 ζ(Re s) 控制。

还存在比“核正”更强的证书：Gaussian 自 Fourier，且
\[
\mathcal F[g_0(\lambda\cdot)](\xi)=\lambda^{-1}g_0(\xi/\lambda).
\]
故 (3) 的第二、第三项在 Fourier 下恰互换，第一项不变：
\[
\boxed{\mathcal Fg_B=g_B>0.} \tag{5}
\]
因此它同时满足点态正、Fourier 正型及精确 Fourier 自对偶。
g_B(0)=B(0)=\int_{\mathbb R}g_B，除以 B(0)>0 后甚至可同时规范成
g_B(0)=1 与全实轴积分 1；这些标量规范仍不消去下面的零点。

## 3. theta 对偶、HL 前件及全部极点

由 (1) 逐项缩放得到
\[
F_B(x)=(1+A^2/\lambda)F_0(x)+A F_0(\lambda x)
       +(A/\lambda)F_0(x/\lambda).
\]
反射项精确重排，缺陷系数为
\[
\tfrac12(1+A^2/\lambda+A+A/\lambda)
=\tfrac12(1+A)(1+A/\lambda)=\tfrac12B(0).
\]
所以
\[
\boxed{F_B(x)=x^{-1}F_B(x^{-1})+\tfrac12B(0)(x^{-1}-1).} \tag{6}
\]
这里没有丢掉有限缺陷；全部极点都在下一式显式保留。

g_B 于 0 有界、于无穷 Gaussian 衰减；F_B 连续，
F_B(x)=O(x^{-1}) 于 0，且于无穷比任意幂衰减。
所以它满足 HL Theorem 3.2 的连续性和两端增长，对任意 β>1 均可使用。
将 (6) 代入 0<x<1 的 Mellin 积分，给出全平面精确延拓
\[
\Psi_B(s)=\int_1^\infty F_B(x)(x^{s-1}+x^{-s})\,dx
           +\frac{B(0)}{2s(s-1)}. \tag{7}
\]
积分项整个，且关于 s↦1−s 对称。因此 Ψ_B(1−s)=Ψ_B(s)，
仅有 0、1 两个简单极点，留数分别 −B(0)/2、B(0)/2，均不为零。
任意固定闭竖带的积分部分由一致 Riemann–Lebesgue 引理趋零，
有理项亦趋零；这也支付 HL 的竖直衰减与每带有限极点前件。

置 ξ(s)=s(s−1)Ψ₀(s)，则去极点对象为
\[
E_B(s):=s(s-1)\Psi_B(s)=B(s)\xi(s). \tag{8}
\]
它整个、实型、自对偶，阶≤1。有限阶可直接由 (7) 核，不借用零点：
F_B(x)≤C e^{-c x²} 于 x≥1，故 |s|≤R 时积分受
C∫₁∞e^{-cx²}(x^{R+1}+x^R)dx 控制，
\(\log\max_{|s|\le R}|E_B(s)|\le C R\log(R+2)\)。
因此通常 genus≤1 的 canonical-product 范围也没有自动排除此例。

## 4. 无条件存在的离线零点

(2) 的两个因子分别给出
\[
s_{k,-}=\tfrac14+\frac{(2k+1)\pi i}{\log2},\qquad
s_{k,+}=\tfrac34+\frac{(2k+1)\pi i}{\log2},\quad k\in\mathbb Z. \tag{9}
\]
两族不重叠，均是 B 的简单零点。Ψ₀ 仅在 0、1 有极点；(9) 不在其上。
故 Ψ_B 与 E_B 在 (9) 必有零点；即便那里恰也是 ξ 的零点，也只增加重数，
绝不取消。结论无需 RH、无需已算零点或数值核验。

此外令 r=A/√λ=2^{-1/4}<1，则临界线本身满足
\[
B(\tfrac12+it)=1+r^2+2r\cos(t\log2)
=|1+r e^{it\log2}|^2\ge(1-r)^2>0. \tag{10}
\]
所以在临界线上它甚至只是一个严格正乘子，那里零点集合与 Ψ₀ 相同。
临界线上的乘子正性、正核及 Fourier 自对偶，均不能排除这两列额外离线除子。

## 5. 消费范围与结论

这是对“一切允许 Mellin completion 的全部零点都居中”这一候选定义的
严格反例；它已经发生在同一个普通整数系统，不需要制造异常 g-primes。
因此可用的 RH 推广必须先指定 canonical completion，或者使用相对除子，
在既定 Γ/kernel 因子的已知贡献中明确扣除 B 这样的 gauge 零点。
“模 gauge”必须预先规定允许类，不能观察零点后任意除因子。

这不是经典 RH 的反例：普通 ξ 未改；E_B 是不同的 completed 目标。
它也不是 actual Weil 正性的负向数值证据。若对 E_B 的全部零点建立完整
Weil 分布，562 的全测试判据确使其正性失败；该分布包含新增 gauge 除子，
不是原始经典 ζ 的固定 Γ/prime-power/pole 泛函。

对象/norm/量词收据：算术 N/P/Π 相同；测试核 g_B 是物理 x 核，
不是零点谱测度；等式 (3)–(10) 对全部 x>0/允许 s 精确，无截断误差。
Fourier 使用全 L²(R) 的标准单位酉规范；Mellin 初域 Re s>1 后由 (7) 精确延拓。
本检验不提供原 du/Dlog Weil 源的独立正能量、不改善经典 whole 4/5 或成长 core/Ξ。
