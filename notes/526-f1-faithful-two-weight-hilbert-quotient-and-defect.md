# 526. 忠实双权Hilbert商、实际近频率缺陷与临界退化

2026-10-12。[T/N] 接续[519](519-f1-closed-source-image-and-degree-moments.md)的真实闭源像、
[520](520-f1-source-quotient-spectrum-and-centered-growth.md)的完整商及
[523](523-f1-natural-hilbert-collapse-and-growth-gap.md)的单线退化。
双权完成可以忠实保留原商；其自然内积却不酉，而且不能由等价Hilbert范数酉化。
这个障碍只使用已经知道在中心线上的真实零点，不假设实际离线零点或重零点。
它不排除具有独立算术来源的其他非等价实现，也没有证明完整Weil负性或RH。

## 1. 保持实际源、全部jets及原商

仍取
\[
 F=\mathcal S_{\exp,\mathbb C},\qquad
 I=E\mathscr S_{e,0,\mathbb C}=\mathcal R_{\rm jet,\mathbb C},
 \qquad X=F/I,
 \qquad V_a=e^{-a/2}\tau_a,\quad \tau_af(t)=f(t-a).
\]
源像在V下双向不变。固定\(\delta\ge1/2\)，令
\[
 W_\delta(t)=e^t(e^{2\delta t}+e^{-2\delta t}),\qquad
 H_\delta=L^2(\mathbb R,W_\delta(t)dt),
 \quad K_\delta=\overline I^{\,H_\delta},\quad Y_\delta=H_\delta/K_\delta.
                                                               \tag{1}
\]
F连续嵌入Hδ，并因包含紧支光滑函数而稠密。
对每个真实非平凡零点ρ及每个整数j≥0，Mellin导数求值的Riesz核为
\[
 k_{\rho,j}(t)=\frac{t^je^{\overline\rho t}}{W_\delta(t)},
 \qquad \|k_{\rho,j}\|^2
 =\int\frac{t^{2j}e^{2\Re\rho t}}{W_\delta(t)}dt<\infty.     \tag{2}
\]
本文内积在第一变量线性，所以\(M_f^{(j)}(\rho)=\langle f,k_{\rho,j}\rangle\)。
(2)的准确范围是\(|\Re\rho-1/2|<\delta\)：正、负两端分别要求严格不等式；
端点相应一端的多项式不可积。δ≥1/2和无条件\(0<\Re\rho<1\)保证全部真实jets准入。

当j<mρ时，(2)杀掉I，连续性使它杀掉Kδ。
因此f∈F∩Kδ必然在全部零点消掉全部必要jets；519给f∈I。于是
\[
 \boxed{F\cap K_\delta=I,\qquad
             X\longrightarrow Y_\delta\text{连续、单射且像稠密}.}    \tag{3}
\]
这是线性忠实性，未声称原Fréchet拓扑与单一Hilbert商拓扑相同。
与523单线完成的零商相比，双权确实保留原X及其完整重数信息。

## 2. 实际群下降及准确的原空间费用

换元给
\[
 \|V_af\|_{H_\delta}^2
   =\int e^{-a}W_\delta(t+a)|f(t)|^2dt.
\]
乘子比是\(e^{2\delta a}\)和\(e^{-2\delta a}\)的正加权平均；
其上确界在相应远端取得极限，用远端紧支测试可逼近。因此
\[
 \boxed{\|V_a\|_{H_\delta}=e^{\delta|a|}.}                    \tag{4}
\]
稠密紧支输入上的连续性及局部一致界使V成为Hδ上的强连续群。
I双向不变且V有界，所以Kδ双向不变，群下降为Yδ上的强连续群Sδ,a，并有
\[
 \|S_{\delta,a}\|\le e^{\delta|a|}.                          \tag{5}
\]
这里没有把原空间(4)的等号直接传给商。

## 3. 原源商的交Gram与伴随非酉缺陷

记kρ=kρ,0。因Lρ杀掉Kδ，kρ∈Kδ的正交补，可视为商的对偶向量。
实际Mellin平移给
\[
 M_{V_af}(\rho)=e^{a(\rho-1/2)}M_f(\rho),\qquad
 S_{\delta,a}^*k_\rho=e^{a(\overline\rho-1/2)}k_\rho.          \tag{6}
\]
复共轭来自上述内积约定。闭包不会改变这一步；商伴随就是原伴随在Kδ正交补上的限制。

准确交Gram为
\[
 G_\delta(\rho,\lambda)=\langle k_\rho,k_\lambda\rangle
 =\int\frac{e^{(\overline\rho+\lambda-1)t}}{2\cosh(2\delta t)}dt
 =\frac\pi{4\delta}\sec\!\left(
              \frac{\pi(\overline\rho+\lambda-1)}{4\delta}\right).   \tag{7}
\]
证明：设q=barρ+λ−1、x=e^{4δt}，积分成为
\[
 (4\delta)^{-1}\int_0^\infty\frac{x^{u-1}}{1+x}dx,
 \qquad u=1/2+q/(4\delta),\quad0<\Re u<1.
\]
[Euler beta积分](https://dlmf.nist.gov/5.12#E3)及
[Gamma反射公式](https://dlmf.nist.gov/5.5#E3)给\(\pi/\sin\pi u\)，得到(7)。
收敛范围\(|\Re q|<2\delta\)已由(2)保证。该范围内交Gram永不零。

对任意两个真实零点，(6)直接支付
\[
 \|S_{\delta,a}S_{\delta,a}^*-1\|
 \ge |e^{a(\overline\rho+\lambda-1)}-1|
       \frac{|G_\delta(\rho,\lambda)|}{\|k_\rho\|\|k_\lambda\|}. \tag{8}
\]
这是计算\(\langle S^*k_\rho,S^*k_\lambda\rangle-
\langle k_\rho,k_\lambda\rangle\)后使用算子范数，不依赖未知离线零点。
取已经知道的两个不同中心线零点ρ=1/2+iγρ、λ=1/2+iγλ，Δ=γλ−γρ≠0，则
\[
 \|k_\rho\|^2=\pi/(4\delta),\qquad
 C_\delta(\Delta):=
 \frac{|G_\delta(\rho,\lambda)|}{\|k_\rho\|\|k_\lambda\|}
 =\operatorname{sech}(\pi\Delta/(4\delta))>0.                \tag{9}
\]
在a=π/Δ，(8)右边是2Cδ>0。
所以这个自然商的内积不酉，即使所有真实零点都在中心线、且全部简单，也不会自动修复它。

## 4. 经典近频率输入与更强的度量修正障碍

此节只消费[516](516-f1-global-mixed-radical-and-mellin-jets.md)已使用的经典输入：
Conrey1989证明简单中心线零点占正比例。
[原论文](https://aimath.org/~kaur/publications/24.pdf)PDF第3页给计数定义，第4页Theorem1给定理。
结合通常零点计数，高度T以下有至少cTlogT个不同中心线零点。
相邻高度差至少有一个不超过T/(cTlogT−1)，因此存在真实不同零点对\(\Delta_n\to0\)。
这不调用本项目近期比例结果，也没有重新研究或证明新的比例。

令u、v为这两个核的单位向量，调节v的单位相位，使内积为实C=Cδ(Δ)。
(6)给准确的二向量计算
\[
 \frac{\|S_{\delta,a}^*(u-v)\|^2}{\|u-v\|^2}
      =\frac{1-C\cos(a\Delta)}{1-C}.                          \tag{10}
\]
取a=π/Δ，得到
\[
 \boxed{\|S_{\delta,\pi/\Delta}\|
 \ge\sqrt{\frac{1+C}{1-C}}
 =\operatorname{coth}\!\left(\frac{\pi|\Delta|}{8\delta}\right).} \tag{11}
\]
故商群的自然Hilbert范数无统一有界性。
对每个固定a也可在(10)使用\(\Delta_n\to0\)和
\(C=1-\pi^2\Delta^2/(32\delta^2)+o(\Delta^2)\)，得到
\[
 \boxed{\|S_{\delta,a}\|\ge\sqrt{1+(4\delta a/\pi)^2},
                                                  \quad a\in\mathbb R.} \tag{12}
\]

若另一个内积与自然商范数等价，常数m、M满足
m‖x‖²≤‖x‖new²≤M‖x‖²，且S在其中酉，则自然范数应满足统一界√(M/m)，与(11)–(12)矛盾。
所以
\[
 \boxed{Y_\delta\text{没有与其自然Hilbert范数等价的酉内积。}}    \tag{13}
\]
更明确地，修正内积在对偶上的逆度量也有相同条件数。
不同频率u、v若在那里正交，则‖u+v‖new=‖u−v‖new；
原范数有‖u±v‖²=2(1±C)，故必要条件为M/m≥(1+C)/(1−C)，沿Δn→0发散。
这是实际无限高度近频率的费用，未假设重零点；它仍与次指数增长相容。

## 5. 固定有限正多实权的同一障碍

上述近频率论证可以推广，但对象仍明确限于固定权完成。
取
\[
 W(t)=\sum_{j=1}^r c_je^{2\sigma_jt},\quad c_j>0,
 \qquad\sigma_-:=\min\sigma_j<1/2<\sigma_+:=\max\sigma_j.
\]
定义HW、KW=closure I及YW如(1)。原群范数准确为
e^{(σ+−1/2)a}（a≥0）、e^{(σ−−1/2)a}（a≤0），证明与(4)相同；商群有相应上界。
全部Mellin jets的连续范围是σ−<Reρ<σ+；若σ−≤0且σ+≥1，(3)仍无条件成立。
仅实权带包含1/2时，就已经有已知中心线求值及非零商，不必声称保留全X。

令
\[
 Z_W=\int e^t/W(t)dt,
 \qquad d\mu_W(t)=Z_W^{-1}e^t/W(t)dt,\qquad v_W=\operatorname{Var}(\mu_W)>0.
\]
这是严格正概率密度，两端指数衰减，全部矩有限。
中心线核的归一化交Gram是\(\phi_W(\Delta)=\int e^{i\Delta t}d\mu_W(t)\)。
设均值mW，由有限二阶矩可展开
\[
 \phi_W(\Delta)=1+im_W\Delta-\tfrac12\mathbb E_{\mu_W}(t^2)\Delta^2+o(\Delta^2),
 \quad |\phi_W(\Delta)|=1-\tfrac12v_W\Delta^2+o(\Delta^2).
\]
密度在整条实线上严格正，故Δ≠0时|φW(Δ)|<1：否则三角不等式的等号要求e^{iΔt}几乎处处为同一相位，矛盾。
将单位核调相位，使交Gram为C=|φW(Δ)|，仍准确得到(10)，分母非零。
使用同一实际差值列、先固定a再取Δn→0，给
\[
 \boxed{\|S_{W,a}\|\ge\sqrt{1+a^2/v_W}.}                     \tag{14}
\]
因此每个这样的固定有限正多权自然商也没有等价酉内积。
没有把这个范围推广成“全部可能Hilbert实现都失败”。

## 6. 一个有限参数忠实、临界极限退化的三权修正族

固定δ≥1/2、R>0，令
\[
 W_R(t)=e^t\left[1+e^{-2\delta R}
                    (e^{2\delta t}+e^{-2\delta t})\right].   \tag{15}
\]
每个有限R有三个严格正权，极端实权为1/2±δ；完整jets连续，所以原X忠实进入其商YR。
原群范数仍是e^{δ|a|}，每个固定R也满足第5节的非等价酉化障碍。

定义实际源商范数
\[
 q_R([f])=\inf_{\theta\in\mathscr S_{e,0,\mathbb C}}
                                \|f-E\theta\|_{H_{W_R}}.
\]
对固定f∈F及ε>0，523允许先选一个固定合法源θ，使
‖f−Eθ‖H1/2<ε。f−Eθ∈F在固定双权Hδ中的范数有限，而
\[
 \|f-E\theta\|_{H_{W_R}}^2
 =\|f-E\theta\|_{H_{1/2}}^2
      +e^{-2\delta R}\|f-E\theta\|_{H_\delta}^2.
\]
再令R充分大，得
\[
 \boxed{q_R([f])\to0\quad\text{对每个固定 }[f]\in X.}        \tag{16}
\]
各有限R的qR正定，未重标定的极限却压掉整个固定商。

这与有限频率的表面对角化可以同时发生。
中心线核密度为hR(t)=1/(1+2e^{-2δR}cosh(2δt))；设ZR=∫hR。
换元t=Ru，hR(Ru)几乎处处趋于1|u|<1；对R≥1，外侧由e^{-2δ(|u|−1)}支配，含二阶矩仍可积。
所以ZR/R→2，Var(μR)/R²→1/3。
hR偶且单峰，总变差≤2；固定Δ≠0时分部积分给
|∫e^{iΔt}hR(t)dt|≤2/|Δ|。除以ZR，固定不同频率的归一化交Gram便趋零。
但(16)同时退化原商范数，每个固定R仍有无限高度近频率的条件数发散。
重标定、窗口依赖或极限正型须另付完整重数与全高度识别，不能从有限模态正交自动取得。

## 7. 完整Weil符号仍需独立来源

[405](405-f1-adelic-restriction-moments-and-radical.md)在双次数零空间给−2B(f,g)=T(f,g)。
真实源双矩基可将每个X类代表到此空间而不改变零点值。
固定显式公式直接给T(Vaf,Vag)=T(f,g)，不使用RH；复Hermitian延拓T(f,bar g)也不变。
若本文任一自然商内积在原X稠密像上等于这条完整型，连续性会使整个商群酉，与(13)或(14)矛盾。
所以正完成本身不能被直接识别为原完整Weil型。

源闭像、Möbius重建及Fourier–sharp相容提供关系，尚未提供余核正性。
[307](307-odd-polarization-and-elliptic-degree-benchmark.md)的几何基准另有独立次数正性与乘法相容；
[290](290-positive-euler-duality-model-and-mass-moment-nonidentification.md)排除正Euler与对偶数据自动补齐正极化；
[512](512-f1-finite-place-double-moment-sign-test.md)保留固定有限S的双矩零正自配对障碍。
若有重零点，完整标量型还允许[516](516-f1-global-mixed-radical-and-mellin-jets.md)已识别的根空间，
不能将忠实正定酉化这个更强目标当作普通RH的免费要求。

下一候选仍须从真实算术来源支付完整符号或实际源修正的有符号代价。
仅调固定正实权、作有界等价度量修正，或显示有限窗口交Gram趋零，均未支付这个合同。
本稿没有新的零点比例、无零条带、RH证明或全局HH／几何principal实现。
