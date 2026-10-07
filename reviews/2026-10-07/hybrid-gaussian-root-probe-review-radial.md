# Gaussian root-weight probe 第二独立全文审查

2026-10-07。作者：radial_review。全文读取最终研究稿，独立重算 Gaussian
Poisson、两个符号的 hop、所有 good-prime valuation、实际字符聚合和
二维大筛；另核 DDHL v5 与固定 math 源的准确接口。只新增本报告，
不编辑被审稿、旧笔记、论文、脚本、输出、math、Goal 或 Git。

**限定 PASS，无数学阻断。**已证明的是同一任意有限阶 target 的真实
Schwartz probe / unit-dual identity，以及共同符号、互不重叠的一次素数槽
下的窄预算
\[
 \sum_{0<Nu\le U}|M_u\prod_iQ_{i,u}|^2
 \ll (U+T_{\rm col}^2)(UT_{\rm col})^\epsilon\prod_iA_i^2.
 \tag{R1}
\]
这不是原 raw 在每个 \(c>0,\ U\ge D^{1+c}\) 下的付款。
两个符号的线性 row-numerator 改善成立，但没有新 cancellation、
新无零边界、完整 marked/plain 合同或 RH/RR 证明。

## 1. canonical LF 证据与审查范围

canonical LF 指 CRLF 和 lone CR 转 LF 后按 UTF-8 哈希。

| 对象 | canonical LF SHA256 | bytes / 行 |
|---|---|---:|
| [最终研究稿](hybrid-gaussian-root-weight-probe-research.md) | 4a6b33cae1944bc904216c202a62f04d48d2f47b0ff5a852f13a3af5a063bc3d | 30381 / 482 |
| [既有 Gaussian 来源报告](hybrid-gaussian-quartic-feasibility-research.md) | f1dbf0e478bd5972da9c3072e52f3d9fd9524394bedf96ffd433f51f317c6638 | 16902 / 323 |
| [457](../../notes/457-number-field-choice-and-relative-amplification.md) | 75079970955602644a9290709f66e2be331ad6116d2a637ed8fc97fb0dde5791 | 15254 / 327 |
| 固定 math September-30 paper.tex | 42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3 | 766316 / 16677 |

固定 math commit 为 adc7f1241b42e322a6451854ab7e4b4c146bf78a。
本轮实读 9220–9268 的共同 \(\nu,\varepsilon_\chi\)、disjoint once-slot、
原 norm weight；12343–12475 的 raw / 放大及 heights；9311–9314 的
coefficient 限制。这些是接口比较，原场上的 theorem 没有被直接迁移到
Gaussian 场。没有重审原 math 全部证明。

外部 primary input 是
[DDHL v5 §§3、4.4–4.5](https://arxiv.org/html/2306.11875v5#S3)。
本轮核对其 (3.4)–(3.11)、(4.26)–(4.28)、(4.38)–(4.39)；
Gauss normalization、有限 cusp / angular 参数均保留。
arbitrary finite target 的 completed reflection 不是 DDHL 给出的原输入。

## 2. trace-2 到 Re 的精确 Gauss 归一化

报告 (1.2) 使用实双线性 pairing \(\Re(z\xi)\)，无隐含 conjugation。
在此 pairing 下 \(\mathbf Z[i]\) 自对偶、covolume 为1。
DDHL 的 additive character 则是 \(e(2\Re z)\)。对 odd modulus，
\(2\) 可逆，故严格有
\[
 G_{*,j}(1,n)=\chi_n(2)^jG_j(1,n),\qquad
 G_{*,j}(k,n)=\chi_n(k)^{-j}G_{*,j}(1,n).
 \tag{R2}
\]
非单位 numerator 时，primitive local characters 的 Gauss 和正好为零。
负幂按 conjugate character 的零延拓理解，不对零值取数值倒数。
\(\chi_n(2)\) 不是可省的常数；最终物理 coefficient 显式保留其逆。

squarefree signal \(\gamma_1(n)^2=\mu(n)\alpha(n)\) 与 v5 phase 相容：
degree-one 的新增因子经 quadratic reciprocity 降为 fixed-ray sign，
inert 处只需实 Gauss 和的平方；CRT cross factor 的平方为1。
本稿没有使用旧版本错误的统一 Gauss 定号。

theta 的 square coefficient 仅解释 root Gauss weight 的来源。
实际 probe 直接用有限 Gauss 和定义；不需要未知 exponent-one core
来定义它。取 root、剥去 Bessel、插入 \(\eta(n)\) 和旋转窗口，是新的
operator；不是已获得完整 theta automorphy 的变换。

## 3. 真实 Poisson、arbitrary target 与固定 unit 窗口

独立按 \(h=a+n\ell\) 求和得到报告 (3.2)：
\[
 \sum_h\chi_n(h)F(\beta h/\sqrt H)
 =\frac H{q_n}\sum_kG_{*,1}(k,n)
             \widehat F\!\left(\frac{\sqrt H k}{\beta n}\right).
 \tag{R3}
\]
缩放的二维 Jacobian 是 \(H\)，dual lattice 是 \(k/n\)；
实 pairing 的方向和旋转的 \(1/\beta\) 均正确。
取 \(\beta=\bar\alpha(n)\) 后 \(\beta n=|n|\)。
外 coefficient 与 (R2) 相乘时，
\[
 \chi_n(2)^{-1}\gamma_1(n)\bar\alpha(n)\,
 \chi_n(2)\gamma_1(n)=\mu(n).
 \tag{R4}
\]
这精确支付报告 (3.3)。\(\eta(n)\) 从始至终只出现一次，
没有变成 \(\eta(n)^2\)；外乘同一个 row \(\chi_n(u)^\varepsilon\)
也逐 row 保留，包括全部非互素 zeros。

报告 §4 的旋转设计比固定 angular sector 更直接。
\(t=\sqrt{X/q_n}\in I=[1/\sqrt2,1]\) 时，任一 \(k\ne1\)：
非实 Gaussian integer 有 imaginary distance 至少 \(1/\sqrt2\)；
实整数 \(k\ge2\) 满足 \(tk\ge\sqrt2\)；
实整数 \(k\le0\) 距 \(I\) 至少 \(1/\sqrt2\)。
因此统一距离至少 \(\sqrt2-1\)，包括其他三个 units 和0。
取 support 在 \(I\) 的 \(1/4\)-tube、在其邻域等于1的固定
\(\widehat F\)，便严格隔离 \(k=1\)，包括 norm-bin 两个端点。
报告 (4.2)–(4.3) 是精确恒等式，无遗失 lattice dual。

任意 \(\eta\) 作为外 coefficient，不影响上述线性恒等式。
但 \(F\) 通常复值、非 radial，且 physical window 对 \(n\) 旋转；
不能领取原 positive-radial profile 的估计。
angular expansion 的参数 \(\ell+1\) 及其 seminorm 成本确实存在。

有限截断最终明确只声称 \(H=X\ge2\)。例如对 Schwartz order \(B>2\)，
绝对外尾可界为
\[
 C_B X^{3/2-\delta(B-2)}.
 \tag{R5}
\]
先给 \(A,\delta>0\)，再取足够大的固定 \(B\)，可得 \(O(X^{-A})\)。
这不声称 unrestricted superpolynomial \(H\) 的统一尾项。
精确 Poisson 使用全 Schwartz 和；所有正 \(X,H\) 下绝对收敛。
bounded unit-modulus 初始情形可直接处理，反射部分使用 \(X\ge2\)。

## 4. 两个 incoming signs 的实际 hop 与参考完成

固定正 hop \(j=1\) 时，正 incoming row 给
\(\nu=2(uh)^3\)，负 incoming row 给 \(\nu=2h^3u\)；
报告最终没有把它们混为同一长度。

新增 §5.1 是另外实际定义的 probe。对 \(j=1,3\)，
\[
 \gamma_3(n)=\chi_n(-1)\bar\gamma_1(n),\qquad
 \gamma_j(n)^2=\mu(n)\alpha(n)^{\sigma_j},
 \quad \sigma_1=1,\ \sigma_3=-1.
 \tag{R6}
\]
\(\chi_n(-1)^2=1\)，所以第二式确切成立。
取 \(j\equiv-\varepsilon_\chi\pmod4\)、物理 coefficient
\(c_j=\chi_n(2)^{-j}\gamma_j\alpha^{-\sigma_j}\)，
同一个 Poisson / tube-window 给 (5.6)–(5.7)。
固定 dyadic \(t^{-1/2}\) profile 和外 \(X^{-1/2}\)
把未归一化 sum 换成原 inverse norm weight，没有改 target。

未 Poisson 的 coefficient 满足
\[
 \chi_n(2)^{-j}\chi_n(h)^j\chi_n(u)^{-j}
 =\chi_n(2h^3u)^{-j},
 \tag{R7}
\]
因为 \(-3j\equiv j\)、\(-j\equiv\varepsilon_\chi\pmod4\)。
故两种 signs 均是真实 \(G_j(2h^3u,n)\)：
\(N\nu=4q_h^3q_u\)，reference dual norm length 为 \(q_h^3q_u/X\)。
这确实消除正 incoming 固定正 hop 的额外 \(q_u^2\)，
没有消除 typical \(q_h^3\) 或证明 moment saving。

对 all odd moduli，包括非互素 numerator，
\(G_3(\nu,c)=\chi_c(-1)\overline{G_1(\nu,c)}\)。
固定 mod4 sectors、系数 conjugation、\(\bar s\) 与 angular flip
给 untwisted conjugate completion，norm conductor不变。
实际 physical angular 参数是 \(\ell+\sigma_j\)。

最终准确保留 normalized DDHL 的三个
\(\Gamma_{\mathbf C}(s+|\ell|/2-1/4)\)、
\(\Gamma_{\mathbf C}(s+|\ell|/2)\)、
\(\Gamma_{\mathbf C}(s+|\ell|/2+1/4)\)，以及
\(N\nu^{1/2-s}\alpha(\nu)^{-\ell}\) phase。
这里仅是原 untwisted / cusp 接口的核查；
finite target、moving ramified data、pole terms、完整 angular / Mellin
uniformity 和实际 reflected cancellation 仍未证明。

## 5. 全部 good-prime valuation 与 squarefree \(h\) 因子

独立 lift \(a=a_0+\pi y\) 核准 (6.1) 的表：
modulus \(\pi^2\) 在 unit numerator 时全部为零；
valuation1 时 nonprincipal exponent 给
\(q\chi(\kappa)^{-e}G_{*,e}\)，principal-zero-extension 给 \(-q\)；
valuation至少2时分别给0与 \(q(q-1)\)。
因此只有指定 twist 分支产生 \(G_1\)，且有效 conductor 回到 \(\pi\)，
不是保留 square modulus 的新 reflector。

对一般 \(L\ge1\)，lift 到最后一层给：
若 \(v_\pi(\nu)<L-1\)，为零；
若 \(v_\pi(\nu)=L-1=k\)，为
\(q^k\chi(\kappa)^{-e}G_e\)，\(e=L\bmod4\)；
若 \(v_\pi(\nu)\ge L\)，只有 \(4\mid L\) 的 principal 分支非零，
值 \(\varphi(\pi^L)\)。\(e=0\) 的 \(G_0=-1\) 也被保留。
这核准完整 (6.5)，含 powerful numerator；sign-adapted \(G_j\)
只将 \(e\) 换成 \(jL\bmod4\)，principal 分支不改。

对 \(h\ne0\) squarefree、\(u=1\)，odd \(\pi\mid h\)
只有 modulus exponent \(L=4\) 的 \(-q^3\) 项。
除去归一化 \(\sqrt{N\pi^4}=q^2\)，其贡献恰为
\(-q^{1-4s}\alpha(\pi)^{-4\ell}\)。
其他 good primes 只有 exponent1。
\(\pi^4\) 的 CRT cross factor为1，故 (6.6) 精确成立。
乘积只取 odd primes；\(\lambda\) 的 numerator / cusp 数据未删除。
formal target 只将局部项乘 \(\eta(\pi)^4\)，不产生新 FE。

cube-residue vanishing 最终限定 odd squarefree 部分非单位、
且满足 coprimality；\(h=\lambda\) 等 pure 2-part rows
没有据此被错误删除。单位、powerful / incoming rows和 remainder 仍保留。
在 \(X\ge2\) 的 physical \(h=0\) 项为零，不送入非零-numerator DS。

square-map 候选的两个结论也正确：
\(\chi(-1)=-1\) 时 odd exponent 成对抵消；
\(q\equiv1\pmod8\) 时 square pushforward 分成两个 order-eight characters，
乘指定 quartic incoming 后仍为 order eight。
这些只排除指定候选，不排除一切 Gaussian probe。

## 6. 实际 inverse × once slots 的 primitive 类与 norm energy

最终定理明确 \(D,P_i\ge1\)、profiles support \([1,2]\)，
slot 数固定，prime lists mutually disjoint、odd、outside \(S\)。
\(S\) 明含 \(\lambda\)，理想使用唯一 primary generators。
\(a_i(p)\) 与 rows 无关；所有 factors 用同一个 \(\eta,\varepsilon_\chi\)。
这与固定源 9225–9248 的 actual orientation、once-product 和 common-target
合同相符，但没有直接调用其 Eisenstein marked theorem。

展开 \(m=n\prod p_i\) 后，每个 prime 的指数只有1或2。
共同正符号的 local character 是 \(\chi_\pi\) 或 \(\chi_\pi^2\)，
共同负符号则为 \(\chi_\pi^3\) 或 \(\chi_\pi^2\)；
都是 primitive nonprincipal。overlap 产生 quadratic，仍保留零掩码。
conductor 是 \(\operatorname{rad}(m)\)，不是未减幂的 \(m\)。

不同 \(m\) 必给不同 conductor或不同 local character，故注入；
同一个 \(m\) 的 n/slots 分解可能重复，已先聚合。
fixed slot 数使 fiber 至多 \(d(m)^{k_0+1}\ll T_{\rm col}^{\epsilon}\)。
Gaussian ideal counting 和 annular weights 给
\(\sum_{n\asymp D}1/Nn=O(1)\)，每个 prime-slot 正和也 \(O(1)\)。
Cauchy 所以准确支付 \(\sum_m|A_m|^2\ll
T_{\rm col}^{\epsilon}\prod_iA_i^2\)。
log weights、fixed real norm powers和固定 height twists 分别明列，
没有从 coefficient normalization 中制造 saving。

mixed signs 的 overlap 指数0会降导子，却保留 varying coprimality mask。
最终例子已用真实 \(b_p\) normalization：
coherent energy 是 \(U|\sum b_p|^2\)，等尺度时约
\(U(\#p/D)^2\)，不是未归一化的 \(U(\#p)^2\)。
这阻止直接复用 primitive proof；它本身并未反证 (R1) 的最终粗预算。
mixed-sign theorem没有在本稿支付。

## 7. 同 conductor 正交与二维完整 Schur 付款

primitive Gauss identity对所有 rows成立，包括 nonunits：
\[
 \chi(u)=\frac{1}{\sqrt{Nc}\,\tau_{\bar\chi}}
          \sum_{a\in(\mathcal O/c)^*}\bar\chi(a)e_*(au/c).
 \tag{R8}
\]
先把同一个 conductor 的 coefficients合并，再对单位 residue group正交，
恰得
\[
 \sum_a|B(c,a)|^2
 =\frac{\varphi(c)}{Nc}\sum_{\operatorname{cond}\chi=c}|A_\chi|^2.
 \tag{R9}
\]
这是准确 Gauss normalization；不同 characters 没有先按 \(\ell^1\) 付费，
natural zeros没有因 Gauss 展开消失。

reduced \(a/c\) 与 primary conductor使 torus fractions无重合。
非零差的 Gaussian numerator模 lattice仍有模至少1，
所以 torus spacing \(\delta_0\ge1/T_{\rm col}\)。
同一 fraction 的 lattice lifts也相距至少1，包含在统一 packing中。
trace-2 convention可用 odd modulus 上的 \(2a\) reduced classes；
只是固定转换，不增加 moving conductor。

Gaussian majorant \(g_U(u)=e^{-|u|^2/U}\ge e^{-1}\) on row disk，
lattice Poisson后的 kernel为
\(\pi U\sum_v e^{-\pi^2U|v-\delta|^2}\ge0\)。
以 separation/3 的 disjoint disks比较面积，点数
\(O((1+r/\delta_0)^2)\)；径向积分严格给
\[
 \sum_{\xi',v}e^{-\pi^2U|v+\xi'-\xi|^2}
 \ll1+(U\delta_0^2)^{-1}.
 \tag{R10}
\]
中项由 \(x\le1+x^2\) 吸收，Hermitian kernel的 Schur norm
为 \(O(U+T_{\rm col}^2)\)。
这与 (R9) 及真实 column energy 合并，完整证明 (R1)。

这里实际使用 positive Gaussian，不是假称 Gaussian bandlimited。
最终提到的 compact alternative也可严格实现：取足够小的 even smooth
frequency bump，平方其 real inverse Fourier transform，尺度
\(\asymp\min(T_{\rm col}^{-1},U^{-1/2})\)，在 row disk上有正下界，
Fourier support严格小于 spacing。Poisson off-diagonal 消失、质量
\(O(U+T_{\rm col}^2)\)。Gaussian proof已独立完成，不依赖此替代简述。
全平面 majorant包含 row disk、units和各类 residues；没有 whole-tail缺口。

## 8. 尚未付款的 critical raw 与有限 evidence 范围

无 slots、\(D\ge1\) 时，\(T_{\rm col}\asymp D\)。
只有 \(U\ge D^2\) 时，重命名任意小 \(\epsilon\) 才给
\(O_\epsilon(U^{1+\epsilon})\)；有槽要求相应 product-length squared。
固定源真正要求每个 \(c>0\)，包括 \(0<c<1\) 的
\(D^{1+c}\le U\ll D^2\)。这一范围仍未支付。
没有取 \(c=1\) 后冒称满足全部放大前件。

若只作 order-four formal amplification，
\(H=\max(2U,D^2)\)、\(P=(H/U)^{1/4}\) 给
\(H/P=U^{1/4}H^{3/4}\)，故 envelope为
\(\max(1,1/4+3r/2)\)。不能将它改成理想
\(\max(1,1/4+3r/4)\)，也不能推出新 \(\sigma\)。

arbitrary \(\eta\) 的线性 identity和窄二矩均成立；
arbitrary \(\eta\) 的新 24-cusp completed reflection、
angular / Mellin polynomial uniformity、ramified / residue付款、
critical raw covariance及新的 marked/plain actual capacity仍开放。
参考 FE没有在本审查中升级为这些尚缺 theorem。

作者记录的32个 prime-power与22个 square-map floating checks
只作 normalization sanity evidence。本代理没有重跑或生成输出，
也不把记录的误差小数当成无限分析认证。
unit isolation、valuation table和 (R1) 的依据是上述逐式解析审核。

最终验收：**指定最终 canonical LF SHA 的完整研究稿限定 PASS，
无数学阻断。**该稿给出具体的新 physical probe、两个符号的 linear
row-numerator 设计及可证明窄 moment；尚未取得改善无零边界所需的
critical raw saving。
