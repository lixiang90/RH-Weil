# 原13标记付款、两个 parity Schur 与 even 反交换子的联合四矩预算

2026-10-08。作者 radial_review。新完整推导，待其他作者独立全文审查。
基线为 `dc19ebde221a43031bf4eb822a752b21aee4beec`。
全部原 carrier、内部 P、sharp prime coefficients、normalizer 与实高度不变。
新增实际付款是 marked entire13 的分量正交、原 low parity 四矩与新的
joint necessary inequalities。最后的有理 upper certificate仍要求既存而未付的
high 残差上界；没有新的实际零点比例、无零边界或 RH 证明。

## 1. 同一原对象与冻结输入

沿用 (X=T/(2\pi),\ell=\log X,d=\lfloor X\ell\rfloor)，
原 interval carrier (E)、(P=EE^*,Q=1-P)、原 even C² taper、
原 finite Hermitian genuine-prime matrices (H=C_H,L=C_L)。
定义 (J=M_{\operatorname{sgn}u},S=E^*JE,U=\operatorname{sgn}S)，
零特征值处选 (+1)，所以 U 是实际 finite involution。
同素数 diagonals 为原 (W,V)，并令
\[
 \Gamma=H^2-W,\quad \Delta=L^2-V,\quad Z=(HL+LH)/2.
 \tag{1}
\]
内积是 normalized real HS 内积 (\langle A,B\rangle=\operatorname{Tr}AB/d)。
记 (A_{\rm e}=(A+UAU)/2,A_{\rm o}=(A-UAU)/2)。
以下 high/low 算子自身的 parity 分解记为

\[
 H=H_{\rm e}+H_{\rm o},\qquad L=L_{\rm e}+L_{\rm o}.
 \tag{2}
\]
所有 fourth变量保留原 finite定义：
\[
 \begin{gathered}
 a_T=\operatorname{Tr}H^4/d,\quad e_T=\operatorname{Tr}L^4/d,\quad
 c_T=\operatorname{Tr}H^2L^2/d,\quad
 k_T=\|[H,L]\|_2^2/d,\\
 b_T=\operatorname{Tr}H^3L/d,\quad
 \eta_T=\operatorname{Tr}HL^3/d,\quad F_T=\operatorname{Tr}(H+L)^4/d .
 \end{gathered}
 \tag{2a}
\]
精确循环展开为 \(F_T=a_T+e_T+6c_T-k_T+4b_T+4\eta_T\)。

| 冻结输入 | canonical LF SHA-256 |
| --- | --- |
| [454 原 bounded-weight 二矩](../../notes/454-original-background-and-weighted-prime-mixed-traces.md) | 8ab99d60c1b748dc561cac57ee498057a0c9fb19b9778a041261b1bad0750db7 |
| [462 整个 low4](../../notes/462-original-low-prime-fourth-path-constant.md) | 868adfeb0d742043f39bd08e0783d66b7a9db11316067b0b3b43d80150cdf680 |
| [467 严格 finite Schur](../../notes/467-two-residual-schur-and-commutator-budget.md) | 0089fd92c70d5e2b7b48bef0084675707f2fe283833f8a97745766ccf6899cb8 |
| [原 parity 残差推导](../2026-10-07/hybrid-parity-resolved-residual-necessary-constraints-radial.md) | 6a5fb7db8467e80682d7351ee37a940af8d39de50fffe2f16b0b3a48d5dfc6f6 |
| [整个物理13](../2026-10-07/hybrid-signed-one-three-physical-resonance-research.md) | 0f7c0146e984c49d84fc057394aed1ab9ace658ae5b775b931bfd359a4c47bac |
| [原 actual13 的 P/全高度 bridge](../2026-10-07/hybrid-one-three-finite-band-admission-research.md) | bc6ad6b1a007422c7678cd540b4127b81d2adc168faf5b090a58b6676778e35f |
| [整个 low parity四矩与 exact diagonals](hybrid-whole-low-parity-fourth-research-root.md) | 02328b4cfaf902fc0f0d60e37f27989808aaae6bb88e6410c8d120a44487969d |
| [无增长前件的 whole high parity gap](hybrid-positive-tail-whole-high-parity-gap-research-compression.md) | 568f2c80d9773db7c13bc3605e7d56ed032e3fba7f5d4dc7c34bbea5ac7cb611 |

表中“整个物理13”及“原 actual13 的 P/全高度 bridge”使用
同一 conductor-one [R]：固定 zeta zero-free gap
\(\theta<9/10\) 与原 fixed-gap logarithmic control；先取固定
\(\theta<a<9/10\)，原 \(7/8\) 可取 \(a=89/100\)。
本稿继续相对于这一准确 [R]，不认证其分析内核。
low4、weighted2、原 U 的二范数 parity 不需该 [R]。

记 (q_T=\|\Gamma\|_2^2/d,r_T=\|\Gamma_{\rm o}\|_2^2/d)，
其中 \(\|\cdot\|_2\) 是 HS norm。
本稿从第3节的 sharp high/low 四词恢复开始，明确增加
\(q_T=O(1)\)；这使原 \(\operatorname{Tr}H^4/d=S_H+q_T+o(1)\) 有界。
不会从 \(H+UHU=o_{S_2}(\sqrt d)\) 免费推出 high 的 S4 parity。

## 2. 固定光滑 marks 的整个13与全部原 P

**Marked13 引理。** 在 one H、three L 的四词任意位置插入固定有限个
\(E^*M_{g(u/\ell)}E\)，其中每个 g 是 fixed bounded C² 函数，
normalized finite trace仍为 o(1)。不要求 high4 bounded。

完整准入如下。物理展开仍为原四次 prime translation，插入只把原各位置的
\(\phi\) 或 \(\phi^2\) 换成乘有固定 g 的 compact C² 窗。
这些窗的 derivative L¹ bounds 为 \(O_g(1)\)，Fourier L¹ 为
\(O_g(\log(2+\ell))\)，二阶 L¹ tail为 \(O_g(R^{-1})\)。
共同 Fourier 分离仍给四个原 sharp prefixes的 unit phases，
没有 moving arithmetic coefficients。原 near 的真实 composite energies、
整数并集 spacing、全部 repeated/distinct labels均不变。
原 far/alias 的 absolute overlap付款只增加 fixed sup norms。
middle-far 的共同 kernel和新增有限个 ghosts仍只产生 \(\ell^{O_g(1)}\)
费用，normalized canonical main仍是

\[
 X^{(5/2)a-9/4}\ell^{O_g(1)}=o(1).
 \tag{3}
\]

good 区所有 absolute heights仍在原 \([T/2,3T]\)；若某个新增 ghost离开主区，
某 Fourier coordinate有模至少 \(c_gT\)。其真实 C² L¹ tail给 \(T^{-1}\)，
原 four-prime absolute mass是 \(X^{5/4}\ell^{-4}\)，
finite kernel端点还有 \(d^{-1}\)，故整个坏区仍是
\(X^{-3/4}\ell^{O_g(1)}=o(1)\)。

finite-to-physical比较也逐个保留原 P。带内 prime operators有
\(y_H\le q_H,y_L\le q_L\)、双方向 leakage
\(l_i,l_i^*\ll_g\sqrt\ell\,y_i\)；新增乘法 factors 的 y 为 \(O_g(1)\)，
双 leakage为 \(O_g(\sqrt{\log(2d)})=O_g(\sqrt\ell)\)。
这里 standalone g 的两端值未必相接，须保留原圆周端点 jump；
若两端相接才可用较小的 \(\sqrt{\log(2+\ell)}\) 费用。
对有限长度 word逐个插入 P，每个 closed trace difference至少有两次 crossing；
其总费用不超过

\[
 C_g\ell\,q_Hq_L^3/d
 \ll_g X^{(5/2)a-9/4}\ell^{O_g(1)}=o(1).
 \tag{4}
\]

这是 HS–HS closed-word 展开，不假设 P 与 multiplication交换。
raw/good回到所有高度时，两个外 packet HS tails与 first-large-jump
HS kernel付款沿原13 bridge：新增窗只增加固定个 kernels，
near链长度仍为固定数，固定 numerical guards可相应取小。
normalized raw费用仍是 \(X^{-1/4}\ell^{O_g(1)}=o(1)\)。
若 word 中某相邻 marks合并，仍是同类 bounded C² 窗。
这证明引理，尤其支付下文两个带 smooth-J marks的 six-factor finite词。

## 3. sharp U 恢复与两个分别付款的正交

取 fixed odd contraction \(j_\varepsilon(u/\ell)\)，在
\(|u|\ge\varepsilon\ell\) 等于 sign u；记
\(S_\varepsilon=E^*M_{j_\varepsilon}E,D_\varepsilon=U-S_\varepsilon\)。
取 fixed smooth \(g_\varepsilon\ge|J-J_\varepsilon|^2\)，
支撑于 \(|u|\le2\varepsilon\ell\)，且 sup有固定界。
compression Schwarz 与 \((A+B)^2\le2A^2+2B^2\) 给

\[
 D_\varepsilon^2\le2(U-S)^2+2G_\varepsilon,
 \qquad G_\varepsilon=E^*M_{g_\varepsilon}E.
 \tag{5}
\]

原 low4 的 weighted版本保留全部 zero atoms和 offdiagonals，给
\(d^{-1}\operatorname{Tr}G_\varepsilon L^4=O(\varepsilon)+o_\varepsilon(1)\)。
具体是原 low4 proof中增加固定 C² 位置窗；near联合 Hilbert、entire far
support/alias和 low raw两cross均不变；zero atom只积分宽 \(O(\varepsilon)\)
strip。原 \(y_L\ll X^{1/4}/\ell\)、\(\|U-S\|_2^2=O(\log(2d))\) 又给

\[
 \operatorname{Tr}(U-S)^2L^4/d
 \le y_L^4\|U-S\|_2^2/d=O(\ell^{-4}).
 \tag{6}
\]

定义 normalized Schatten norm \(\|A\|_{p,d}=d^{-1/p}\|A\|_{S_p}\)。
对 A、B PSD，\(\operatorname{Tr}ABAB\le\operatorname{Tr}A^2B^2\)；
取 \(A=D_\varepsilon^2,B=L^2\)，严格有限式为

\[
 \|D_\varepsilon L\|_{4,d}^4
 \le\|D_\varepsilon\|^2\operatorname{Tr}D_\varepsilon^2L^4/d
 =O(\varepsilon)+o_\varepsilon(1).
 \tag{7}
\]

bounded-q给 H 的 normalized S4 bounded，原 low4给 L 的同界。
对下面(8)所需的两个 six-factor词，两个 U marks都直接邻接至少一个 L。
其 replacement telescoping中的每个 \(D_\varepsilon\)
都可挂到该相邻的 L；
其余 H,L,L用三个 normalized S4 Hölder，其他 marks op bounded。
因此 replacement费用为 \(O(\varepsilon^{1/4})+o_\varepsilon(1)\)。
先 fixed \(\varepsilon\)、再 T、最后 \(\varepsilon\downarrow0\)，
第2节证明以下两个实际有限词都是 o(d)：

\[
 \operatorname{Tr}L^2UHLU=o(d),\qquad
 \operatorname{Tr}L^2ULHU=o(d).
 \tag{8}
\]

原 \(UVU-V=o_{S_2}(\sqrt d)\)，而 bounded-q下
\(\|HL\|_2/\sqrt d=O(1)\)。有限循环迹及原 weighted2
\(\operatorname{Tr}VHL/d\to0\) 因而给
\(\operatorname{Tr}VUHLU/d,\operatorname{Tr}VULHU/d\to0\)。
所以新付款是

\[
 \langle\Delta,UZU\rangle=o(1).
 \tag{9}
\]

与已付 \(\langle\Delta,Z\rangle=o(1)\) 合并，真正推出

\[
 \boxed{\langle\Delta_{\rm e},Z_{\rm e}\rangle=o(1),\qquad
        \langle\Delta_{\rm o},Z_{\rm o}\rangle=o(1).}
 \tag{10}
\]

这是新 marked-word proof后得到的两个结论，不能只把原总正交拆写。
finite centering errors在下一节仍准确保留。

## 4. 两个严格 finite Gram，及 bounded-q联合极限

置 \(q_{\rm e}=q-r,q_{\rm o}=r\)，并记

\[
 \begin{gathered}
 \delta_j=\|\Delta_j\|_{2,d}^2,\quad z_j=\|Z_j\|_{2,d}^2,
 \quad p_j=\langle\Gamma_j,\Delta_j\rangle,\quad
 \beta_j=\langle\Gamma_j,Z_j\rangle,\quad
 \epsilon_j=\langle\Delta_j,Z_j\rangle,\qquad j\in\{{\rm e,o}\}.
 \end{gathered}
 \tag{11}
\]
原467的准确有限量 \(\chi_T,\tau_T,c_T,k_T,b_T\) 满足
\(p_{\rm e}+p_{\rm o}=c_T-\chi_T\)，
\(\beta_{\rm e}+\beta_{\rm o}=b_T-\tau_T\)，
\(z_{\rm e}+z_{\rm o}=c_T-k_T/4\)。
其中
\(\chi_T=\operatorname{Tr}(VH^2+WL^2-WV)/d\)，
\(\tau_T=\langle W,Z\rangle\)；
它们的已付极限为 \(\chi_T\to C,\tau_T\to0,\eta_T\to0\)。
每个 j 的三个实际向量 Gram PSD严格给

\[
 \left|\beta_j-p_j\epsilon_j/\delta_j\right|^2
 \le (q_j-p_j^2/\delta_j)(z_j-\epsilon_j^2/\delta_j).
 \tag{12}
\]
两个右因子非负；\(\delta_j=0\) 时改用 \(|\beta_j|^2\le q_jz_j\)，
且 \(p_j=\epsilon_j=0\)。所以 finite whole fourth上界为原467的
\(a_T+e_T+6c_T-k_T+4|\tau_T|+4|\eta_T|\)，再加

\[
 4\left|\sum_jp_j\epsilon_j/\delta_j\right|
 +4\sum_j\sqrt{(q_j-p_j^2/\delta_j)
                    (z_j-\epsilon_j^2/\delta_j)}.
 \tag{13}
\]
这是 finite式，不把未知增长乘 o(1)删掉。

在 bounded-q共同极限中，原 low parity常数为
\(\delta_{\rm e}=11/480,\delta_{\rm o}=13/480\)，两个 errors由(10)趋零。
记 \(p=p_{\rm e}+p_{\rm o}=c-C\)，有新的全词必要式

\[
 \boxed{|b|\le\sqrt{(q-r-p_{\rm e}^2/\delta_{\rm e})z_{\rm e}}
                   +\sqrt{(r-p_{\rm o}^2/\delta_{\rm o})z_{\rm o}}.}
 \tag{14}
\]
仍有 \(z_{\rm e}+z_{\rm o}=c-k/4\)，各因子非负。
尤其大 covariance不能继续把 \(p_{\rm o}=\delta_{\rm o}p/(\delta_{\rm e}+\delta_{\rm o})\)
免费放入 tiny odd variance；需 \(|p_{\rm o}|\le\sqrt{r\delta_{\rm o}}\)。
若舍去 z 的分配，(14)仍给更细惩罚
\(b^2\le[q-p_{\rm e}^2/\delta_{\rm e}-p_{\rm o}^2/\delta_{\rm o}](c-k/4)\)。
这比仅原总 Schur多真实已付信息，未假定任何算术前件可达。

## 5. 整个 low parity四矩与 odd-low diagonal的实际常数

本节独立复算供下面使用的最小 low子块，不需 high4或 [R]；
已 FULL READ表中本轮 root的完整16-label low源，下面与其 whole结论一致。
固定 smooth J marks按第2节同类方法插入原整个 low4 proof；
原 low raw op及两cross付款为
\(O(y_L^4\log(2d)/d)=O(\ell^{-4})=o(1)\)。
这里 standalone smooth-J 的两端是 \(-1,+1\)，故同样保留圆周 jump费用；
没有把它误算成 periodic matching weight。
每个原 nonzero-frequency项仍由完整 near/far/alias proof付款；
zero atoms仍是 A、A′、O 三配对，all-repeat correction趋零。
sharp恢复用(5)–(7)，此处四个原 L的 S4全已付；无需 high q。
因此以下是 actual \(L_{\rm e},L_{\rm o}\) 的整个四矩，非只配对诊断。

flat时记 normalized低步长 \(x,y\in[0,1/2]\)。all-even路径始终在
同一 half interval，width \(h=1/2\)。单half的三个配对全贡献为
\(4I_{\max}+8I_{\Sigma}\)，其中

\[
 I_{\max}=\int_0^h\!\int_0^hxy[h-\max(x,y)]\,dx\,dy=h^5/20,
 \quad I_{\Sigma}=\int_{x+y\le h}xy(h-x-y)\,dx\,dy=h^5/120.
 \tag{15}
\]
两half均保留，故 \(e_{\rm e}=2(4I_{\max}+8I_{\Sigma})=1/60\)。
all-odd路径每步过半轴。A与A′各有两种方向，crossing strip长度
\(\min(x,y)\)；O路径若第一、第三位置都过半轴，则 x、y同号而
middle位置不可能过回，故为空。所有原中间位置仍留在 I。
于是

\[
 \boxed{\lim\operatorname{Tr}L_{\rm e}^4/d
        =\lim\operatorname{Tr}L_{\rm o}^4/d=1/60,}
 \qquad 4\int_0^{1/2}\!\int_0^{1/2}xy\min(x,y)\,dx\,dy=1/60.
 \tag{16}
\]

原二矩的相同 bounded marks及 internal-P付款给 odd-low diagonal
\(v_{\rm o}(t)=1/8-t^2/2\)（\(0\le t\le1/2\)，even延拓）。
具体从正半轴到负半轴需要 \(x>t\)，积分
\(\int_t^{1/2}x\,dx\) 即该函数。记其真实压缩为 \(V_{\rm o,T}\)；
fixed smooth近似后 weighted2、Toeplitz两leak及 dominated convergence给

\[
 \begin{gathered}
 \|L_{\rm o}^2-V_{\rm o,T}\|_{2,d}^2\longrightarrow1/120,\qquad
 \langle W,L_{\rm o}^2\rangle\longrightarrow C_{\rm o}=19/1920,\\
 \langle\Gamma,V_{\rm o,T}\rangle=o(1),\quad
 \|(V_{\rm o,T})_{\rm o}\|_{2,d}=o(1).
 \end{gathered}
 \tag{17}
\]
常数来自 \(w(t)=t(t+1)/2\)：
\(2\int v_{\rm o}^2=1/120\)、
\(2\int wv_{\rm o}=19/1920\)；因此(16)减第一项是 \(1/120\)。
smooth-to-sharp各二矩用 bounded权与原 low leakage付款。
这里 \(V_{\rm o,T}\) 是原 finite-X same-prime zero-atom函数的压缩，
不能将它免费当任意 T-dependent C² weight。
表中 root源§6已经完整支付：先在离两个 endpoint strips宽度
delta的 compact部分作原 Mertens uniform逼近，再用 fixed smooth strip
majorant；正 weighted2主项在 strip中为 \(O(\delta)\)，其他原子仍o(1)。
原 exact function uniformly bounded，且 total variation有界；
先T后delta亦支付其与U的交换。用于本稿的额外
\(\Gamma\) 测试函数误差也可由 bounded-q HS Cauchy支付。
不需要把一般数域 raw合同移植到此原矩阵。

## 6. high even 的真实第四尾与 Z-even upper bound

对 fixed R，并取 \(R^2>M_T\)；渐近时先选固定
\(T_0,R\) 满足 \(R^2>\sup_{T\ge T_0}M_T\)。
置 \(H_R=\operatorname{clip}_R(H)\)，
\(D_R=H^2-H_R^2\succeq0,\Gamma_R=H_R^2-W,q_R=\|\Gamma_R\|_{2,d}^2\)。
原 parity证明给 \((H_R)_{\rm e}=o_{S_2}(\sqrt d)\)，op≤R，
故 normalized S4趋零。令 \(T_R=H-H_R\)，
parity conditional expectation的 PSD Jensen与谱逐点给
\((T_{R,\rm e})^2\preceq (T_R^2)_{\rm e}\preceq D_{R,\rm e}\)。
两个 PSD矩阵A≤B满足 \(\operatorname{Tr}A^2\le\operatorname{Tr}B^2\)，
因为 \(\operatorname{Tr}(B-A)(B+A)\ge0\)，无需交换。
所以 \(\|T_{R,\rm e}\|_{4,d}^4\le\|D_{R,\rm e}\|_{2,d}^2\)。
保留 core/tail cross后，准确有限展开是
\(q_T-r_T=q_{R,T}-e_{R,T}^2
 +2\langle\Gamma_{R,\rm e},D_{R,\rm e}\rangle
 +\|D_{R,\rm e}\|_{2,d}^2\)，
其中 \(e_{R,T}=\|\Gamma_{R,\rm o}\|_{2,d}\)。
原 PSD tail给 \(\langle\Gamma_R,D_R\rangle\ge0\)，而
\[
 \langle\Gamma_{R,\rm e},D_{R,\rm e}\rangle
 =\langle\Gamma_R,D_R\rangle
      -\langle\Gamma_{R,\rm o},D_{R,\rm o}\rangle
 \ge-e_{R,T}\sqrt{q_T}.
 \tag{18a}
\]
最后一步用 \(\|D_R\|_{2,d}^2\le q_T-q_{R,T}\le q_T\)。
因此新的严格有限成本为

\[
 \|T_{R,\rm e}\|_{4,d}^4
 \le\|D_{R,\rm e}\|_{2,d}^2
 \le q_T-r_T-q_{R,T}+e_{R,T}^2+2e_{R,T}\sqrt{q_T}.
 \tag{18}
\]
原实际 weighted commutator与 sharp finite \(4M\) 界，在 fixed R后 T、
再 R的顺序下给
\(\liminf_{R\to\infty}\liminf_{T\to\infty}q_{R,T}\ge
  \underline q=41/15120\)。
所以每个 bounded-q共同极限有

\[
 \boxed{\limsup\|H_{\rm e}\|_{4,d}^4
             \le q-r-\underline q=q_{\rm e}-\underline q.}
 \tag{19}
\]
这保留了可能非零的 high fourth tails；没有把 H 的二范数 even小量升级到S4小量。

同一 PSD tail在 bounded-q范围已给更细 odd预算：
\(\|D_{R,\rm o}\|_2^2\le\frac12\|D_R\|_2^2\)，因为
\(\operatorname{Tr}D_RUD_RU=\operatorname{Tr}(D_R^{1/2}UD_R^{1/2})^2\ge0\)。
再由 \(\Gamma_{R,\rm o}=o_R(\sqrt d)\)，先 fixed R后 T再 R，得到

\[
 \boxed{0\le r\le(q-\underline q)/2.}
 \tag{20}
\]
这是共同子列的界，不混合两个不同 limsup。
本轮 compression新源还完整保留正尾成本并消元，
已无任何q/a增长前件地证明
\(\liminf(q_T-2r_T)\ge\underline q\)。
其原有限式为
\[
 q_T-2r_T\ge\frac{K_T}{4M_T}
       \frac{2(R^2-M_T)}{2R^2-M_T}
       -2(R\alpha_T+\omega_T)^2-R^2\alpha_T^2
 \quad(R^2>M_T),
 \tag{20a}
\]
其中 \(K_T\to41/10080,M_T\to3/8,\alpha_T=O(\ell^{-1}),
\omega_T=O(\sqrt{\log(2d)/d})\) 均为原已付 finite量。
该源的 scalar clip平方恒等式、H谱基双随机求和、准确
\(-2\operatorname{Tr}WU D_RU\) cross与一元 tail消元已独立全文核准。
取 \(R^2=\ell\) 消除误差；本稿(20)现在也可直接由其 whole结论取共同极限。

准确有限 parity代数是
\[
 Z_{\rm e}=\{H_{\rm o},L_{\rm o}\}/2
              +\{H_{\rm e},L_{\rm e}\}/2.
 \tag{21}
\]
第一项不是小量。
由于 \(L_{\rm o}^2\) 精确 U-even，且 \(H_{\rm e}^2\succeq0\)，
\(\operatorname{Tr}H_{\rm o}^2L_{\rm o}^2\le\operatorname{Tr}H^2L_{\rm o}^2\)。
(17)与 parity HS Cauchy给

\[
 \limsup\operatorname{Tr}H^2L_{\rm o}^2/d
 \le C_{\rm o}+\sqrt{(q-r)/120}.
 \tag{22}
\]
第二项以 normalized S4 Hölder、(16)、(19)付款。因此

\[
 \boxed{\sqrt{z_{\rm e}}
 \le\sqrt{C_{\rm o}+\sqrt{(q-r)/120}}
                   +[(q-r-\underline q)/60]^{1/4}.}
 \tag{23}
\]
这是 actual even反交换子的必要上界，不是假设未知22只有重复主项。
第7节仅再将 \(q-r\) 放大到Q，下面原有理常数证书仍合法；
更细 even-tail信息不会使它变弱。

## 7. 同一既存 Q前件下的全连续有理证书

本节明确假设既存而未付的 \(\limsup q_T\le Q=1/350\)。
没有新增或声称已付款 high arithmetic上界。
由(20)，\(r\le\bar r=(Q-\underline q)/2=11/151200\)。
(23)的两个根号分别有如下有理上包：

\[
 \sqrt{19/1920+\sqrt{1/42000}}<76/625,\qquad
 (11/4536000)^{1/4}<79/2000.
 \tag{24}
\]
完整平方证书是

\[
 \begin{aligned}
 D&=(76/625)^2-19/1920=733609/150000000>0,\\
 D^2-1/42000&=17275154167/157500000000000000>0,\\
 (79/2000)^4-11/4536000&=84695927/9072000000000000>0,\\
 13/500-(76/625+79/2000)^2&=4679/100000000>0.
 \end{aligned}
 \tag{25}
\]
所以 entire actual \(z_{\rm e}<13/500\)。

取 fixed rational Young权 \(t_{\rm e}=16/3,t_{\rm o}=31\)。
(14)逐项使用 \(4\sqrt{AB}\le2tA+2B/t\)，并保留
\(z_{\rm o}=c-k/4-z_{\rm e}\)、\(p_{\rm e}+p_{\rm o}=c-C\)。
由于 \(t_{\rm o}>t_{\rm e}\) 与 \(1/t_{\rm e}>1/t_{\rm o}\)，
放大 q到Q、r到 \(\bar r\)、z-even到13/500后，全 fourth满足

\[
 \begin{aligned}
 F\le{}&S_H+Q+e+2t_{\rm e}Q+2(t_{\rm o}-t_{\rm e})\bar r
       +gC+2(1/t_{\rm e}-1/t_{\rm o})(13/500)\\
 &+gp_{\rm e}-2t_{\rm e}p_{\rm e}^2/\delta_{\rm e}
   +gp_{\rm o}-2t_{\rm o}p_{\rm o}^2/\delta_{\rm o}
   -(1+1/(2t_{\rm o}))k,
 \quad g=6+2/t_{\rm o}=188/31.
 \end{aligned}
 \tag{26}
\]
这里只扩大可行域，未假称原 p、z数据可任取。
对每个 real p分别完成平方，无需分段网格：
\(gp-2tp^2/\delta\le g^2\delta/(8t)\)。
flat的原 \(S_H=19/480,e=19/240,C=23/960\) 因而给

\[
 \boxed{F\le U-\frac{63}{62}k,\qquad
 U=\frac{25710335933}{77218272000}
   =\frac13-\frac{29088067}{77218272000}<\frac13.}
 \tag{27}
\]
所有全连续 q、r、c、两p、两z均覆盖，全部 root比较已用有理平方证书付款。
因此同一未付Q前件，结合已付 inputs，已足够整个原 prime fourth小于1/3；
无需额外假设 \(k\ge1/40\)。此常数只会条件地超过 flat 的 \(2/3\)；
它不会自动超过当前已知 \(0.672509329\ldots\)。
这仍不是当前已证实际四矩或比例改进。

若另外复用467原未付 \(\liminf k_T\ge1/40\)，则

\[
 U-63/2480=23748742733/77218272000<77/250,
 \quad 77/250-(U-63/2480)=34485043/77218272000>0.
 \tag{28}
\]
这里只加强同一旧joint前件的蕴含，不把它登记为新的 actual arithmetic付款。
得到 finite full fourth bounded后，原 proper-power/background与zero-side
稳定接口才可使用，保持全部条件量词；本稿不据此发布新比例。

## 8. 已付与仍开放的确切范围

新付款是原 marked entire13、两个分别证明的 residual正交、
原 low even/odd整个第四矩、high even真实尾的成本和全连续 Schur/Young证书。
没有构造 finite prime模型，也未声称467候选与全部实际transition数据相容或不相容。
Q上界本身仍未付；新(27)给更强的 whole31/22联合前向预算，
而不是把 scalar near-positivecore或 low配对积分冒充完整响应。
原 [R]仅在第2–3节 marked entire13使用；全部固定 profiles/marks/a先选，
再 T，sharp恢复最后 epsilon；high clip始终先固定R再T最后R。
实际 full high signed四素数余量、真实比例与 RH仍开放。
