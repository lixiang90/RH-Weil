# 原四高素数窄方面比：短正周期、完整时间尾与产品余类系数

2026-10-08，perron_reviewer；基线 main 6666ad6。本稿只新增此研究源。
结论是原真实核心的一条有费用的准确归约：全部时间扭曲可分离为可积参数；
primitive 系数有真实产品纤维 Fourier 结构及完整平方和 \(O(q)\)。
窄方面比支付 BC 相位增长因子，但尚不能把实际系数改成 BC 的三个独立系数。
没有新 whole 四矩、中心常数、比例、无零边界或核心省幂。

## 1. 全文输入、准确族与外部读取范围

本轮全文重读下表；身份为 UTF-8 canonical LF，不 trim 文件结尾。

| 输入 | 行数 | SHA256 |
|---|---:|---|
| [497完整归约](../../notes/497-original-prefix-projection-and-low-label-mixed-core.md) | 141 | 872324f23ea3135568722bd3fc753a0bdef0743b5f9a0649cedde2aac41c273f |
| [完整前缀投影](hybrid-original-prime-prefix-minor-projection-research-perron.md) | 185 | 2971ae080d520d4a2d1209cfd0b86aaf722302169ee3f516df423f6c1f3aad32 |
| [489完整双mask](../../notes/489-original-high-product-rational-minor-slice.md) | 85 | c39081acaf5d1bd22685df4a918d42b1bffa635bb15a09b41b66794654ecdddd |
| [464原minor](hybrid-original-unit-band-minor-lift-research-pc8.md) | 464 | b6018e1254049b77dd5d7f73f4d3a7dc7272d5fe5dd3568f3c5ddf8cf73928b4 |
| [188准确primitive变换](hybrid-original-unit-band-primitive-reciprocal-transform-research-root.md) | 188 | 4b13bec23ff399739b26003954a28e0d9d889617955bf6e7a43e428ab3a7aa2c |
| [425实际unit](hybrid-whole-fourth-unit-unit-actual-research-whole.md) | 425 | b3f14cf4ee5659f8e23bd51dc9bf71e853e783bd2d55e42ee8846d6e8d1e41dc |
| [191真实period能量](hybrid-original-coherent-period-energy-research-checkpoint-audit.md) | 191 | fe19e50f955c47b7abb22933d0b406a9bc339ac68056d8d115d1f7277be22c5f |

外部工具读取 [Bettin–Chandee v1](https://arxiv.org/html/1502.00769v1)：
完整 §1 Theorem 1/Remark 1、§2证明组织、§§5–7证明完成及§9 Corollary 1证明。
未独立重证其§§3–4放大器全部估计；以下仅核主定理合同与本对象的代入费用。

保持原 \(X=T/(2\pi),L,N_L,\nu,\chi\) 平均、C² profiles、same-u 及全部 Fourier/Mellin 参数。
令 \(Z=X^{9/10}\)，四个 genuine primes \(q,s,p,r>Z\)，且 \(s,p,r<q\le X\)。
固定原 dyads \(q\asymp Q,s\asymp S,p\asymp P,r\asymp R\)，\(PR\asymp QS\)，故 \(q/s<X^{1/10}\)。
原 \(p,r\ne s\)、graph、两套最大标签 profile 和全部端period保留；不改真实标签排序。
两套删弧为 \(d\le W=X^{1/10}\)、半径 \(W/(dS)\)，以及 \(W<d\le B=X^{1/5}\)、半径 \(1/S\)。
其完整 complement \(\Omega_q(a)\) 只依 \(a=n\bmod q\)，并包括 \(q\nmid n\)。
497已证 \(\mathcal U_T=\mathfrak K_{489,\mathrm{all}>Z}+O_\phi(X^{7/10}L^C)\)；本稿不重新认领该付款。

## 2. 原时间支撑强制正短周期，端点没有丢弃

425(13)原 \(\nu\) 支撑在 \([\theta_-,\theta_+]\)，
\(\theta_-=T+3s_T/8>T,\ \theta_+=T+(d-1)\eta+5s_T/8\ll T\)。
实际权为 \(\nu(2\pi sn/q)\)。因 \(s\le X\)，所有 \(n\le q\) 上该权准确为零。
因此在任何 Mellin 分离**之前**可取
\[
 J_q^+=J_q\cap[q+1,\infty),\qquad n=a+qj,\quad1\le a\le q-1,\quad j\ge1. \tag{1}
\]
这里 \(J_q\) 仍是原共同有限频带，不以 individual-s 私选窗口。
原支撑与 \(S>X^{9/10}/2\) 给 \(j+a/q\asymp X/S\)，从而 \(j\ll X/S\ll X^{1/10}\)；
小 \(X/S=O(1)\) 时只需保留全部有限正整数 \(j\)，没有作连续近似。
设 \(J_q^+=[\ell_q^+,h_q]\cap\mathbb Z\)，完整周期仍用 \(I_j=(jq,(j+1)q]\)，
\[
 j_0=\left\lceil(\ell_q^+-1)/q\right\rceil,\qquad j_1=\lfloor h_q/q\rfloor-1. \tag{2}
\]
两段不完整端period用准确指示 \(1_{a+qj\in J_q^+}\) 保存；没有套用491的低产品edge付款。
若某周期没有 unit residue，贡献就是零；\(j=0\) 消失来自原 \(\nu\) 的零支撑。
所有真实非零频率及原高产品位移仍在(1)中。

## 3. 准确分离 \(n^{it_\nu}\)，全部参数尾只付日志

置 \(V(y)=X\nu(2\pi Xy),h(v)=V(e^v)\)。425原光滑权给每个固定 \(m\)
\(\|h\|_1\ll1,\ \|h^{(m)}\|_1\ll L^{m/2}\)；支撑位于固定正紧区间。
取 \(\mathcal M_\nu(t)=(2\pi)^{-1}\int h(v)e^{-itv}dv\)，
\(V(y)=\int_{\mathbb R}\mathcal M_\nu(t)y^{it}dt\)。
由四次分部积分及 \(\sqrt L\) 分界，
\[
 \int_{\mathbb R}(1+|t|)^2|\mathcal M_\nu(t)|\,dt\ll L^{3/2}. \tag{3}
\]
只有这一真实 \(\nu\) 获得 weighted moment；原 C² \(\phi\)、\(g\) 的参数仍只需旧绝对 L¹ 包络。

固定 \(\zeta_0\in C^\infty([0,\infty))\)，于 \([0,1]\) 为1、于 \(z\ge2\) 为0。
令 \(H_t(z)=((1+z)^{it}-1)\zeta_0(z)\)，\(k_t(v)=H_t(e^v)\)。
当 \(v\to-\infty\)，\(k_t(v)=O(|t|e^v)\)；上端紧支撑。
直接链式微分给 \(\|k_t\|_1+\|k_t''\|_1\ll(1+|t|)^2\)。
故 \(\widehat k_t(\omega)=(2\pi)^{-1}\int k_t(v)e^{-i\omega v}dv\) 满足
\(\int|\widehat k_t(\omega)|d\omega\ll(1+|t|)^2\)，且 Fourier inversion 全域成立。
对(1)中 \(z=a/(qj)\in(0,1)\)，准确得到
\[
 \left(\frac n{qX}\right)^{it}
 =\left(\frac jX\right)^{it}
 \left[1+\int_{\mathbb R}\widehat k_t(\omega)
                 a^{i\omega}q^{-i\omega}j^{-i\omega}\,d\omega\right]. \tag{4}
\]
(3)支付(4)的全部 \((t,\omega)\) 参数；没有截任何时间尾或取低频模型。
原 \(s^{it}\) 已在素数 \(s\) 系数中，其他原 twists 模长为1。
完整周期的 \(j\) 因子因此可分离；edge 的有限联合指示仍不能叫作独立三系数。
共同参数按旧包络恢复；不要求其他 twists 的 weighted moments。

## 4. 实际 primitive 系数是产品纤维 Fourier 矩阵

固定一组旧共同参数，先写 \(F_q(a)=\sum_{s\in\mathcal S_q}u_s e_q(as)\)，
\(G_q(n)=\sum_{Z<p,r<q}v_pz_r e_{q^2}(-npr)\)。
\(\mathcal S_q\) 是原准确素数区间；系数保留 q-prefix 及原 twists，不能随 \(a,j\) 选择。
先保留 \(p=s,r=s\)。191§6对同一 mask、period/edge 的准确减两点加双点修正
以正 Parseval 付 \(O_\phi(X^{1/2}L^C)\)，故不需 signed-subset 单调性。
对 \(1\le a,c\le q-1\)，定义
\[
 C_{q,a,c}=\sum_{\substack{Z<p,r<q\\-apr\equiv c\ (q)}}v_pz_r e_{q^2}(-apr).
 \tag{5}
\]
188(14)给原核的准确有限身份
\[
 \mathcal T_q=\sum_{a=1}^{q-1}\Omega_q(a)F_q(a)
 \sum_{c=1}^{q-1}C_{q,a,c}
 \sum_{\substack{j\ge1\\a+qj\in J_q^+}}w_q(a+qj)e_q(cj\bar a). \tag{6}
\]
\(w_q\) 含(4)的原时间权、有限指示及全部公共参数。原 box 外 prefactor 为 \(S/(QX)\)，
还有真实 \(b_q\) 和同-u 积分；(6)没有将这些归一化改为 canonical 全时间四矩。

令 \(d_{q,k}=\sum_{pr=k}v_pz_r\)。每个实际整数 \(k\) 至多两个有序 prime factor pairs，
而 \(0<k<q^2,\ q\nmid k\)。真实 \(b_p=\log p/(a_LL\sqrt p)\) 给
\[
 \sum_k|d_{q,k}|^2\le2\sum_p|v_p|^2\sum_r|z_r|^2\ll_\phi1. \tag{7}
\]
唯一写 \(k=qz+v,\ 0\le z<q,\ 1\le v<q\)。对固定 \(a,c\)，取 \(v=-c\bar a\bmod q\)，则
\[
 C_{q,a,c}=e(-av/q^2)\sum_{z=0}^{q-1}d_{q,qz+v}e_q(-az). \tag{8}
\]
固定 \(a\) 时 \(c\mapsto v\) 是 permutation。补入 \(a=0\) 后作完整正 Parseval 得
\[
 \sum_{a,c=1}^{q-1}|C_{q,a,c}|^2
 \le\sum_{v=1}^{q-1}\sum_{a=0}^{q-1}
        \left|\sum_zd_{q,qz+v}e_q(-az)\right|^2
 =q\sum_k|d_{q,k}|^2\ll_\phi q. \tag{9}
\]
这是本稿新证明的实际有限系数矩阵范数；原 prime masks/q-prefix 没有被换成稠密整数。
它没有自动估计 \(\Omega_q(a)F_q(a)\) 与该矩阵的联合相关，也不把 \(C_{q,a,c}\) 因子化。
例如 untwisted 完整 \(j\)-区间长 \(J\ll X/S\) 时，单独(9)及 \(c\)-Parseval
只给 \(|\mathcal T_q|\ll q^{3/2}\sqrt J\)，全 box 为 \(QS\sqrt J/X\)；
191的 \(QS/X\) 仍较强。范数身份自身不认领新省幂。

## 5. BC主定理的真实窄方面比费用

若暂时有合法独立系数 \(\alpha_a\beta_q\gamma_j\)，固定非零整数 \(c\)，
BC Theorem 1 对 \(a\asymp H,q\asymp Q,j\asymp J\) 的 \(e_q(cj\bar a)\) 给
\[
 \|\alpha\|_2\|\beta\|_2\|\gamma\|_2
 \left(1+\frac{|c|J}{HQ}\right)^{1/2}
 \left[(JHQ)^{7/20+\varepsilon}(H+Q)^{1/4}
       +(JHQ)^{3/8+\varepsilon}(JQ+JH)^{1/8}\right]. \tag{10}
\]
这里没有 Dirichlet 家族或零点前件。实际旧 \(d=1\) 删弧强制
\(a>qW/S,\ q-a>qW/S\)，故所有实际 dyads \(H\gg QW/S\)。
结合 \(c<q,\ J\ll X/S,\ Q\gg X^{9/10}\)，有 \(|c|J/(HQ)\ll X/(QW)\ll1\)。
这是本对象真正付清的相位增长因子，不需假设 \(a\asymp q\)。
但相对纯 product 系数的 Cauchy 量 \(\|\alpha\|\|\beta\|\|\gamma\|\sqrt{JHQ}\)，
(10)两项的净省因子仅为
\[
 \min\{J^{3/20}H^{3/20}Q^{-1/10},\,H^{1/8}\}. \tag{11}
\]
因 \(H\ll Q\le X,J\ll X^{1/10}\)，该理想比较至多 \(X^{13/200+O(\varepsilon)}\)；
顶端 \(Q,S\asymp X\) 的 \(J=O(1),H\asymp Q\) 只有 \(X^{1/20+O(\varepsilon)}\)。
若(11)小于1，(10)本身不改进平凡界；仍可另用平凡界。
这是定理 RHS 的指数账本，不是实际和的下界、方法不可能性或已获省幂；
真实 \(c\)-求和、mask、edge 和(5)系数均尚未符合 product 合同。

连外腿也不能免费称作小扰动。固定真实 \(s\asymp S\)，其相位 \(f(a,q)=as/q\)。
BC Remark 1 的导数合同需要扰动参数 \(Y\gg SH^2\)，
故增加 \((1+Y/(HQ))^{1/2}\asymp(1+SH/Q)^{1/2}\)。
在实际 \(H\gg QW/S\) 上至少耗 \(W^{1/2}\)，\(H\asymp Q\) 时耗 \(S^{1/2}\)。
不作这项付款就不能把 \(F_q(a)\) 的逐素数相位放进(10)。
Corollary 1允许两条所有阶光滑腿和两条 arbitrary 腿；
四个真实 prime masks 不满足前两腿合同，窄比本身不能修复该缺口。

## 6. 剩余确切联合算术，而非重新付款误差

(8)使不可免费分离的对象具体化为
\(\Omega_q(a)F_q(a)e(-av/q^2)d_{q,qz+v}\)，其中 \(v=-c\bar a\bmod q\)。
它同时取决于素数产品余类、商 \(z\)、真实 \(s\) 和 rational complement。
把 \(c\bar a=-pr\bmod q\) 求回去，仍恢复原 \(-jpr/q\) 相位，不能只留下独立 \(c/a\)。
进一步消费相消必须控制(6)这个完整矩阵与逆元短窗的联合 pairing，
或证明有明确范数费用的独立系数分解；(9)是可供该证明使用的真实正输入。
所有参数与端period需按(3)–(4)恢复，原 \(p,r\ne s\) 修正另有已付正界。
顶端旧费用是 \(X L^C\)，跨过已准入 \(B_*\) 仍需真实幅度省幂
\(r>0.285801997046972\)，不是把平方能量节省当同一个 \(r\)。
当前没有这样的联合估计；497的 \(7/10\) 误差与全局 \(5/7\)/既有 \(B_*\) 不变。
