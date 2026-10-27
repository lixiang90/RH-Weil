# 冻结五源的原 norm／完整 Weil 矩阵及可认证求积输入

2026-10-27；`/root/tf_source_matrix`独占分支。已恢复README／STATE、check→show、G20261027、C046停止状态、D20261027E、宏观前沿及next-input-admission。只建设源侧输入，不改STATE／cadence／文献库，不建C047，不运算浮点矩阵或提前检验Hfin。actual t_F 的独立reader由另外两分支付款，本稿不能用Q反定义T。

本稿的有限算法及粗显式常数足以使源侧Ndu／NDlog／完整Q的每项误差趋零；这不是新Weil正性、成长uniform预算或未消费的actual投影误差证书。

## 1. 冻结对象和全部系数方向

固定L=3/2，I=(-L,L)，j=-2,-1,0,1,2，α_j=πj/L，

\[
 \chi(u)=e^{-1/(1-(u/L)^2)}1_{|u|<L},\qquad
 g_j(u)=\chi(u)e^{i\alpha_ju},\qquad r_j=g_j''-g_j/4.
 \tag{1}
\]

源在R上Cc∞，support=[-L,L]且端点flat；它是560已付zero-extension Dlog(I)的元素，非离端点有正距离的严格Cc∞(I)。原physical r=e^(u/2)f，Fourier为 rhat(s)=∫r(u)e^(-isu)du。

一个独立可核的源公式是rhat_j(s)=−(s²+1/4)·chihat(s−α_j)。因为χ实偶，实s上的chihat及这五个rhat_j均为实数。因此本冻结族的Ndu／NDlog／Γ和prime两号总和矩阵实际为real symmetric；若actualT采用同一scalar实密度ρ_F，它也如此。这是该源族的解析对称性，不能在一般complex源表中任意删掉imaginary部分。

采用任务的线性first表：N_ij=∫r_i overline(r_j)。若实际源r_c=Σc_jr_j，则其norm²为c^T N overline(c)，不是未说明地写成c* N c。实现可将**所有**N／Q／T／E同时转置成标准column Gram，记mathsfN=N^T等，才有c*mathsfN c。Hermitian谱／符号不受统一转置影响，但crossblock相位与source map必须同步，不能只转某一张表。

每个μ_±(r_j)=∫r_j e^(±u/2)=0由两次分部积分精确成立。若Σc_jr_j=0，则compact smooth函数Σc_jg_j解(D²-1/4)g=0，故g=0；χ在I严格正，互异指数的线性独立给全部c_j=0。因此Ndu严格正定，且NDlog≥log2·Ndu也严格正定。此证明没有给已计算的conditioning数字。

## 2. 全导数的明确常数：有限模式不是bandlimited

对标准bump b(x)=e^(-1/(1-x²))，令a=1-x²，取complex Cauchy圈半径a/8。有

\[
 |(1-z^2)-a|\le a/4+a^2/64<a/3,\qquad
 \Re\frac1{1-z^2}\ge\frac3{8a}.
\]

于是|b^(n)(x)|≤n!(8/a)^n e^(-3/(8a))。最大化a^(-n)e^(-3/(8a))，再用(n/e)^n≤n!，得到可用的全局粗界

\[
 \|\chi^{(n)}\|_\infty\le\beta_n,
 \quad\beta_0=1,\quad
 \beta_n=\left(\frac{64}{3L}\right)^n(n!)^2\quad(n\ge1).
 \tag{2}
\]

因为|α_j|<5，定义完全显式的正数

\[
 G_n=\sum_{k=0}^n\binom nk5^{n-k}\beta_k,
 \quad R_n=G_{n+2}+G_n/4,
 \quad C_n=2LR_n.
 \tag{3}
\]

则全部五源满足||r_j^(n)||∞≤R_n、||r_j^(n)||1≤C_n。端点flat使任意次数分部积分没有边界项，故

\[
 |\widehat r_j(s)|\le\min(C_0,C_n|s|^{-n}).
 \tag{4}
\]

这是真实全frequency尾，不把小j当作bandlimit。若求Fourier在s方向的ℓ阶导，直接有B_ℓ=2L·L^ℓR_0的uniform界；积分分部还给

\[
 |\widehat r_j^{(\ell)}(s)|
 \le2L|s|^{-n}\sum_{k=0}^{\min(n,\ell)}
 \binom nk\frac{\ell!}{(\ell-k)!}L^{\ell-k}R_{n-k}.
 \tag{5}
\]

后续只需固定n=4已足，毋须随参数提高源模式或换源。

## 3. actual Γ的全尾及有限节点求值

Γ(s)=Reψ(1/4+is/2)-logπ。重核既有[NIST DLMF5.7.6](https://dlmf.nist.gov/5.7.E6)及[5.15.1](https://dlmf.nist.gov/5.15.E1)的partial fractions／trigamma式；本节从它们直接推粗常数，不依赖ζ零点或渐近代定义。

取a=1/4、b=s/2，partial fractions给

\[
 \Re\psi(a+ib)=\psi(a)+
 \sum_{n\ge0}\frac{b^2}{(n+a)((n+a)^2+b^2)}.
\]

有|ψ(a)|≤5。以N=ceil|b|+1分和，前段≤4+log(4N+1)，尾段≤2；结合logπ<2与4N+1≤2|s|+9，得到

\[
 |\Gamma(s)|\le16+\log(2+|s|),\qquad
 |\Gamma'(s)|\le10,\qquad |\Gamma''(s)|\le36.
 \tag{6}
\]

导数界来自Σ(n+a)^(-2)≤20及2Σ(n+a)^(-3)≤144，再乘s导数的1/2、1/4。没有略去Γ/contact的常数。

在|s|≤S上，可用

\[
 \psi(z)=-\gamma-1/z+\sum_{k=1}^{M}\frac{z}{k(k+z)}+\mathcal R_M,
 \quad |\mathcal R_M|\le |z|/M\le(1/4+S/2)/M.
 \tag{7}
\]

γ可用H_m-logm的区间，宽度≤1/m，π／log等用向外舍入。于是Γ各节点的统一误差δΓ可显式由(7)、γ区间及有限arithmetic误差给出。只调用未认证的floating digamma不算完成该项。

## 4. Dlog与Γ积分的全frequency尾

S≥2、n≥1。由(4)定义

\[
 \mathcal T_{n,A}(S)=\frac{C_n^2}{\pi}S^{1-2n}
 \left(\frac{A+\log(2S)}{2n-1}+\frac1{(2n-1)^2}\right).
 \tag{8}
\]

若|w(s)|≤A+log(2+|s|)，则

\[
 \left|\frac1{2\pi}\int_{|s|>S}
 w(s)\widehat r_i(s)\overline{\widehat r_j(s)}ds\right|
 \le\mathcal T_{n,A}(S).
\]

这里用log(2+t)≤log(2t)并准确积出t^(-2n)与logt。NDlog取A=0，Q的Γ部分取A=16。每个固定n≥1时右边趋零；本稿建议固定n=4。该式不能自动支付actual ρ_F的高频尾：它还需要其他分支独立给ρ_F的明确增长常数。

## 5. 有限积分的中点规则与节点误差

对长度ℓ区间上的complex C²函数f，以M个等长中点求积，误差≤ℓ³ sup|f''|/(24M²)；对complex值直接用积分余项可得同一常数，无需把实虚误差再错误相加。

### 5.1 物理源与全部shift

令U₂=2R₀R₂+2R₁²。du Gram integrand及任意a的相关

\[
 R_{ij}(a)=\int_{-L}^{L}r_i(u+a)\overline{r_j(u)}du
\]

的二阶导均≤U₂，故各自物理中点误差≤(2L)³U₂/(24M_x²)。在全[-L,L]积分即可，因zero-extension在shift support端点仍flat，不必把跳动的overlap边界当硬截断。

若source节点absolute evaluation error≤τ_r，积分另付2L(2R₀τ_r+τ_r²)。若a=logq只有区间半宽δa，额外相关误差≤2LR₀R₁δa；全部shift两号均保。可直接用interval source evaluator合并该费，避免重复计。

source节点有明确closed expression：t=u/L、h=1-t²、|u|<L时

\[
 r_j(u)=e^{i\alpha_ju}\chi(u)
 \left[L^{-2}(4t^2h^{-4}-2h^{-2}-8t^2h^{-3})
       -4i\alpha_jt/(Lh^2)-(\alpha_j^2+1/4)\right].
 \tag{9}
\]

区间跨support端点时不直接把h的除法用于含0的区间；使用flat zero-extension与全局R₀／R₁界包住节点，或split interval。每个三角／exp／log节点的向外舍入也必须进入τ_r。

### 5.2 Fourier节点

在|s|≤S上，用M_u个中点计算rhat_j(s)，有统一解析误差

\[
 \tau_{\rm hat,quad}=
 \frac{(2L)^3}{24M_u^2}(R_2+2SR_1+S^2R_0).
 \tag{10}
\]

另加所有source／phase节点误差的积分总量，记最终τ_hat。相应product误差≤2B₀τ_hat+τ_hat²，B_ℓ=2L·L^ℓR₀。

### 5.3 有限frequency中点积分

令D₀=B₀²、D₁=2B₀B₁、D₂=2B₀B₂+2B₁²。g_ij(s)=rhat_i(s)overline(rhat_j(s))分别满足|g|≤D₀、|g'|≤D₁、|g''|≤D₂。

对NDlog，必须把[-S,S]分成[-S,0]与[0,S]，因为log(2+|s|)在0有一阶折点。各半区用M_s个中点，定义

\[
 M_D(S)=D_0/4+D_1+\log(2+S)D_2,
 \quad M_\Gamma(S)=36D_0+20D_1+(16+\log(2+S))D_2.
\]

两种积分的解析frequency求积误差分别≤S³M_D/(24πM_s²)、S³M_Γ/(24πM_s²)，均已含1/(2π)。

Γ节点误差δΓ与Fourier节点误差τ_hat再贡献

\[
 \frac S\pi\left[\delta\Gamma D_0+
 (16+\log(2+S)+\delta\Gamma)(2B_0\tau_{\rm hat}+\tau_{\rm hat}^2)\right].
 \tag{11}
\]

Dlog同式以其log节点误差δw及wmax=log(2+S)替换。有限加权和本身的rounding费独立加上；不能只付解析中点余项而漏掉nested Fourier／digamma节点误差。

## 6. 完整Weil矩阵：所有proper powers与双pole

全部base primes是F={2,3,5,7,11,13,17,19}。在q<e³的完整primepower表中，

| q | Λ(q) |
|---|---|
| 2,4,8,16 | log2 |
| 3,9 | log3 |
| 5,7,11,13,17,19 | 相应logq |

所以完整矩阵仍为

\[
 Q_{ij}=\frac1{2\pi}\int\Gamma(s)\widehat r_i(s)
 \overline{\widehat r_j(s)}ds
 -\sum_{q<e^3}\frac{\Lambda(q)}{\sqrt q}
 [R_{ij}(\log q)+R_{ij}(-\log q)]
 +2C_i\overline C_j-2S_i\overline S_j.
 \tag{12}
\]

C_i=∫r_i cosh(u/2)、S_i=∫r_i sinh(u/2)，对(1)两者解析上精确0；这是该输入的取值，非删掉目标定义。q≥e³的相关因support精确0；有限endpoint等号也无测度贡献。不得用logq代proper-power的Λ(q)，也不得只保primes。

每个相关按§5.1认证；权与位移的log／sqrt区间也付款。例如W_q包住Λ(q)/sqrtq，若其半宽δw_q、|R_ij|≤2LR₀²，则权误差每个两号合计≤4LR₀²δw_q；相关误差再乘2 supW_q并求全部12个q之和。由于q表有限，不存在未付primepower尾；这不消除t_F inverse中独立存在的全部Euler returns尾。

Hermitian化只能用(M+M*)/2减少已认证误差，不能用它掩盖相位或原norm转置错误。

## 7. 一个真正有限且可按任意容差选择的输入方案

给定每entry的目标η>0，以下步骤只定义可执行的integer参数选择，尚未运行：

1. 固定n=4，取integer S≥2并倍增，直到T_(4,0)(S)、T_(4,16)(S)各≤η/8。两项显式趋零，故必有限结束。
2. 选M_s，使S³ max(M_D,M_Γ)/(24πM_s²)≤η/8。把(11)的Fourier节点项和weight节点项分别压到η/8：先选τ_hat≤1，再按(10)选M_u和有限向外舍入精度；按(7)选M与γ区间长度。所有上界只含已显示常数。
3. 选M_x与source／shift／weight精度，使du积分误差≤η，且12个两号primepower项的总误差≤η/4。其余Γ费与(8)合并，不把某个被压到η的子费称为完整Q误差。
4. 给其余有限加权和arithmetic另留η/4预算；每entry最终区间是各项Minkowski和，以上可使完整Q误差≤η。以5×5 dimension把entry误差ε转operator误差≤5ε，分别保存Ndu／NDlog／Q的账本；不能只报告打印小数精度。

该粗方案可能很昂贵；这里只证明明确有限的构造与收敛，不声称推荐的具体精度已在本机可快算，也不使用算法未运行的成功状态。

## 8. Gram conditioning、真正crossblock和Hfin的有限意义

精确N正定不代当前rounding下的conditioning。对计算的标准column Gram mathsfNhat，entry误差≤ε_N给||mathsfN-mathsfNhat||≤5ε_N。可用rational／interval LDL或一份explicit inverse factor残差证书验证λmin(mathsfNhat)>5ε_N；未通过则提高精度，不可直接使用floating Cholesky失败／成功作定理。

实际orthogonalization先固定core C=span{r₀}，再把另外四个源对C投影并在其4维测试补空间内正交化。保存完整source coordinate map A，使A*mathsfN A=I；Ndu和NDlog用不同A，不能混为一个Euclidean basis。raw非正交r₀与r_(±1,±2)的block不自动叫原norm正交core／complement；这里的补空间也不是全Dlog补空间。

若Ahat*mathsfNhat Ahat=I而真实Gram残差范数≤δ<1，令E₀=Ahat*mathsfEhat Ahat、η_E=||Ahat||²δ_E，真实norm-normalizedE距E₀至多

\[
 \frac{\eta_E+\delta\|E_0\|}{1-\delta},
 \tag{13}
\]

另加Ahat数值实现误差。该式使用(I+R_N)^(-1/2)的真实congruence，不把finite矩阵逆残差冒称Hilbert G_F inverse残差。

反驳Hfin可更便宜：给一个明确原坐标rational coefficient向量c，若c*mathsfEhat c-δ_E||c||²>0，即得到真实E正Rayleigh值；不必先对整个E求floating eigenvalues。归一化幅度再用经认证的c*mathsfN c区间。这里δ_E必须包含另外分支的actualT全部误差；源侧Q／N已付不能代T。

有限Hfin只在这5个冻结源上说E≤0，非全源、成长窗、全补空间、RH或whole leading4/5的新结论。pass也不自动准入数学合同；反驳只停止这个冻结无费比较ansatz，不推出Q有负方向。

## 9. root消费范围

对象／domain：fixed五源、原du与zero-extension Dlog，完整实际Bζ；不改变L／j／F。paid：全源导数、nested physical／frequency／digamma误差与全部primepowers/poles的明确账本；无数值矩阵输出。方向：source-first表或统一transpose后的column Gram，全部相位同步。未付：actualP／k_s／G_F独立reader、其Hilbert残差、ρ_F高频和全部returns尾仍须由其他分支闭合。

这是标准求积／旧full-Weil身份对当前actual源的设施落实，不能单凭本稿文件或收敛公式计新数学轮。535／560已付的trace／Gram存在性不重计；独立primitive RR、成长signed core／coupling、actualq／Ξ及strongest-old whole4/5UPPER未改。最终root对三稿共同前件审查后决定是否存在可运行的有限输入门。
