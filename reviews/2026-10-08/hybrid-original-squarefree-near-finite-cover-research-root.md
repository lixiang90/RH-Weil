# 原平方自由近相关：固定系数的八平移覆盖桥

2026-10-08，root。研究轮4，基线 main da5f0df。
只新增本研究源；不改冻结来源、数域或原完整观察量。
状态：证明一个有限覆盖充分合同，待不同作者全文复核。

单个原ν的第四矩上界不能反推canonical J第四矩。
本稿保持同一真实R和同一X、Y，以八个辅助平移ν正覆盖J，
将canonical增长目标还原到一个完整signed近相关和的一侧上界。
没有证明这一算术上界，也没有新的完整增长、中心常数、比例或无零边界。

## 1. 原始合同与固定系数

本轮 FULL READ 以下四份冻结源；canonical UTF-8 LF只转换CRLF/lone CR，不trim。

| 来源 | 行数 | SHA256 |
| --- | --- | --- |
| [原载体425](hybrid-whole-fourth-unit-unit-actual-research-whole.md) | 425 | b3f14cf4ee5659f8e23bd51dc9bf71e853e783bd2d55e42ee8846d6e8d1e41dc |
| [原ν平方自由四阶188](hybrid-original-squarefree-carrier-fourth-near-research-perron.md) | 188 | 2142645eed724da49a3e6faae7068adb2c8ca907c196a691f09a2b7a7fd6f3ae |
| [490完整函数差](../../notes/490-original-weighted-mobius-squarefree-conditional-remainder.md) | 118 | a5bf40493c864774da5f8fbecce8d257bc21176a78b16ff1841c89843d4924ef |
| [453固定零点包](hybrid-original-squarefree-signed-zero-gram-research-perron.md) | 453 | 0b126138c7bf42e9be3c4352b099a6ab37d88cef93af20593593c8e849aa2a17 |

固定X=T/(2π)、L=logX、d=floor(XL)、η=2π/L、s_T=T/√L，
χ仍是原固定正概率密度，支撑[3/8,5/8]，含原Γ衰减合同。
原ν与J准确为
\[
 \nu_T(t)=\frac1{ds_T}\sum_{k=0}^{d-1}
       \chi((t-T-k\eta)/s_T),\qquad J=[T/4,4T].
 \tag{1}
\]
大T时dη≤T且dη≍T。其原支撑两端保持425的floor。

取490的同一真实
\[
 R(t)=\sum_{Y<n\le X}r_n n^{it},\qquad
 R(t)^2=\sum_\ell g_\ell\ell^{it}.
 \tag{2}
\]
r_n是188(3)的负prime/squarefree系数，含全部方面比和截断。
整个证明中X、Y、U、V、r_n及g_\ell不随平移改变。
已有准确系数界为
\[
 \sum_\ell|g_\ell|\ll XL^2,\qquad
 D=\sum_\ell g_\ell^2\ll L^{16}.
 \tag{3}
\]
系数为实数；没有新增零点假设或素数相关估计。

## 2. 八平移正覆盖

188已证明原ν在[6T/5,9T/5]上为T^(-1)量级。
这里明确下界常数：令h=η/s_T→0，对任何相位a，整条lattice
Riemann和有
\[
 h\sum_{k\in\mathbb Z}\chi(a-kh)=1+O_\chi(h\|\chi'\|_1).
 \tag{4}
\]
可在每个长度h的小区间以积分均值估计误差，再对|χ′|积分；
该界对平移a一致。对t∈[6T/5,9T/5]，χ支撑内所有k均落在
0≤k<d中：距两端为固定T比例，s_T=o(T)、dη=T+O(η)。
因此大T时
\[
 \nu_T(t)=\frac{1+O_\chi(h\|\chi'\|_1)}{d\eta}
          \ge\frac1{2T}\quad(6T/5\le t\le9T/5).
 \tag{5}
\]

定义固定的八个辅助平移及其平均：
\[
 h_m=(-1+m/2)T,\quad
 \nu_m(t)=\nu_T(t-h_m)\quad(0\le m\le7),\qquad
 W_T(t)=\frac18\sum_{m=0}^7\nu_m(t).
 \tag{6}
\]
每份仍为正概率测度。各正core为
[(1/5+m/2)T,(4/5+m/2)T]；相邻core重叠T/10，
总覆盖[\,T/5,43T/10\,]，故覆盖整个J。
由(5)严格得到
\[
 \boxed{W_T(t)\ge \frac1{16T}\mathbf1_J(t),\qquad \int W_T=1.}
 \tag{7}
\]
所以对任意可测f，按非负积分解释，
\[
 \boxed{\mathcal M_J(f):=\frac1T\int_J|f(t)|^4dt
       \le16\int_{\mathbb R}W_T(t)|f(t)|^4dt.}
 \tag{8}
\]
这是新证明的有限覆盖，不是将188的ν≤C/T单向不等式倒用。
W只用于给原J作正majorant；不替换原physical载体或重选空间profile。

## 3. 固定真实系数的准确覆盖核

保留188的准确原核
\[
 \Psi_T(u)=e^{iTu}\Gamma(s_Tu)\frac1d\sum_{k=0}^{d-1}e^{ik\eta u}.
 \tag{9}
\]
平移(6)的核准确为e^(ih_m u)Ψ_T(u)，故
\[
 \Psi_{\rm cov}(u)=\Psi_T(u)\frac18\sum_{m=0}^7e^{ih_m u}
  =\Gamma(s_Tu)\left(\frac1d\sum_{k=0}^{d-1}e^{ik\eta u}\right)
                 \left(\frac18\sum_{m=0}^7e^{imTu/2}\right).
 \tag{10}
\]
两个有限几何因子与所有floor均保留，模长分别至多1。
Ψ_cov(0)=1，且Ψ_cov(−u)=conj(Ψ_cov(u))。
有限系数和与概率积分交换准确给
\[
 M_{\rm cov,R}:=\int W_T|R|^4
 =\sum_{\ell,\ell'}g_\ell g_{\ell'}
                   \Psi_{\rm cov}(\log(\ell/\ell')).
 \tag{11}
\]
没有在八个高度尺度重新定义R，也没有换成八个不同截断主项。

## 4. 完整近相关的canonical充分合同

使用原Δ=1024L^(5/2)/X、κ=√(8π)。
由s_TΔ=2048πL²和原Γ合同，(10)给
\[
 |u|\ge\Delta\ \Longrightarrow
 |\Psi_{\rm cov}(u)|\le X^{-\kappa}.
 \tag{12}
\]
按全部实际系数对定义far与非对角near，准确地
\[
 M_{\rm cov,R}=D+C_{\rm cov,near}+F_{\rm cov},\qquad
 |F_{\rm cov}|\ll X^{2-\kappa}L^4.
 \tag{13}
\]
C_cov,near是ℓ≠ℓ′、|log(ℓ/ℓ′)|<Δ的完整实数和。
它也准确等于八份平移载体near和的平均，但无需每份分别有好上界。
不得把Gram半正定当成near各项实部非负。

由(8)、(13)，对任何固定B≥0，下列一个完整一侧算术合同足够：
\[
 C_{\rm cov,near}\ll_{\epsilon,\phi,\chi}X^{B+\epsilon}
 \quad\Longrightarrow\quad
 \boxed{\mathcal M_J(R)\ll_{\epsilon,\phi,\chi}X^{B+\epsilon}.}
 \tag{14}
\]
对角的polylog及far负幂均可被任意ε吸收。
顶端near仍允许|ℓ−ℓ′|≪XL^(5/2)；覆盖本身不支付这些真实相关。
该合同比要求八份near各自小更弱，是充分条件而非必要条件。
特别地，原未平移ν的一份near上界不足以推出(14)。

## 5. 回到原完整函数及严格边界

只有先得到(14)的canonical R上界，才在同一个J消费490的
完整差P_H=R+E_θ和已付M_J(E_θ)≪X^(c_θ+ε)。
在原全高度[R_θ]及全部准入合同下，c_θ=1−1/(2θ)。
由L⁴三角不等式令b=max(B,c_θ)，严格得到
\[
 \mathcal M_J(P_H)\ll X^{b+\epsilon},\qquad
 |\mathcal M_J(P_H)-\mathcal M_J(R)|
       \ll X^{(3b+c_\theta)/4+\epsilon}.
 \tag{15}
\]
后一式逐项展开完整|R+E|⁴差并用Hölder；若B<c_θ则费用c_θ占优。
名义θ=7/8下，任何真正证明的B<5/7都会降低这里的完整增长上界，
但本稿尚未证明这样的B。单纯覆盖不会改善既有5/7或3/7、9/14。

辅助W的支撑伸出J；最左平移下沿约为3T/(8√L)，
最右上沿约为9T/2+5T/(8√L)。
453的固定零点包表达和旧J误差合同没有因此扩大到W全部支撑。
本稿没有在W上免费运输Z_T、A或E_θ；(15)只在J内消费旧完整差。
即使(14)改善增长幂，也不直接给实际中心四阶常数：
16的覆盖常数、中心化、配置误差和实际计数桥仍须按各自合同支付。

新增的是(7)–(14)的准确有限覆盖与真实近相关充分输入；
其算术前件仍未付。没有新whole增长定理、简单比例或无零边界。
