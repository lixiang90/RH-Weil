# 586 固定theta基态谱与完整Gamma热缺陷

2026-10-28；C049，G20261027/runtime1793085111/原0c4f。两独占最终证明经本轮独立逆审限定PASS，root已将谱前件与热稿(C)对齐闭合，按本范围正式消费并统一一数学轮结算。不声称外部优先权、经典RH反例或一般confining方法类不可能。

## 固定对象和严格结果

采用405已付的全整数正theta源
\[
 H_\theta(x)=2e^{x/2}\sum_{n\ge1}
 \pi n^2e^{2x}(\pi n^2e^{2x}-3/2)e^{-\pi n^2e^{2x}}.
\]
算子坐标x∈(0,∞)，固定Dirichlet边界。令w=Hθ′/Hθ，由core平方型qθ[f]=∫|f′−wf|²取闭包，表示算子
\[
 A_\theta=-D_x^2+H_\theta''/H_\theta,
 \quad\mathcal D(q_\theta)=H_0^1(0,\infty)
          \cap L^2(e^{4x}dx).
\]
它是非负自伴、有compact resolvent，且λ₁>0。按半线本征值的完整重数、每个只计一次，有
\[
 \boxed{N_\theta(T^2)=\frac{T}{2\pi}[\log(T/\pi)-1]
       +O_\theta(\sqrt T(1+\log T)).}                 \tag{1}
\]

固定正谱生成规则νθ,T=Σ_{√λj≤T}(δ√λj+δ−√λj)，Wθ,T(u)=∫e^(−iτu)dνθ,T(τ)。物理源是另一变量u上的r=e^(u/2)f，保全complex。Wθ,T对全部compact complex卷积平方正，随T→∞有唯一温和分布极限Wθ，全部fixed Cc∞/S_exp源逐一收敛。此处不把x能量与physical du/Dlog认作同一范数。

该规则的普通热量满足
\[
 \Theta_\theta(t)=2\operatorname{Tr}e^{-tA_\theta}
 =\frac{\log(1/t)-\gamma_E-\log(4\pi^2)}{4\sqrt{\pi t}}
  +O_\theta(t^{-1/4}\log(2+1/t)).                     \tag{2}
\]
旧566完整显式公式已给
\[
 \Theta_\zeta(t)=W_\zeta(k_t)
 =\frac{\log(1/t)-\gamma_E-\log(16\pi^2)}{4\sqrt{\pi t}}+O(1),
 \quad k_t(u)=(4\pi t)^{-1/2}e^{-u^2/(4t)}.
\]
因而同一完整目标下
\[
 \boxed{\Theta_\theta(t)-\Theta_\zeta(t)
 =\frac{\log2}{2\sqrt{\pi t}}
  +O_\theta(t^{-1/4}\log(2+1/t)),\quad t\downarrow0.} \tag{3}
\]
这给实际正谱规则的非零归一化热缺陷；Wθ,T不能趋于完整Wζ的D′分布，也不能在全部compact complex卷积平方上给目标极限。所有cofinal原cutoff序列有同一Wθ，选择cutoff子列不能消除此缺陷。

## 原证明的短链

[谱证明](../reviews/2026-10-28/theta-ground-state/spectral-domain-and-two-term-count.md)令z=πe²ˣ，将全和写为H₁(1+ρ)。n≥2的可和majorant对j≤3给ρ^(j)=O(z^j e^(−3z))。由此
\[
 V=4z^2+O(z),\quad V'=16z^2+O(z),
 \quad |V-4\pi^2e^{4x}|\le C_\theta e^{2x}.
\]
旧10-14已付H/V leading；这里实际补齐导数与终单调，未把n=1模型冒作原算子。平方型与Schr能量在原core相等，闭包的准确weighted-H¹域给紧嵌入。q核局部仅cHθ，而Dirichlet与Hθ(0)>0排零模。

对Schr能量作D/N分割，不能逐段切平方而漏边界项、变为Robin。终单调转折点a_T=½logT+Oθ(1)，网格δ=T^(−1/2)只产生O(√TlogT)个cell；每格常势计数取整误差≤1，单调Riemann上下和差≤δT。初始compact段计数为x₀T/π+O(1)、相位积分为x₀T+O(T^(−1))，所以该段比较误差为O(1)。Neumann尾有V≥T²且几乎处处V>T²，无≤T²态。于是Nθ(T²)=π⁻¹∫√((T²−V)_+)dx+O(√TlogT)。

用|√(a_+)−√(b_+)|≤√|a−b|，实际势与4π²e⁴ˣ的phase积分之差O(√T)。纯指数积分准确为
\[
 \frac T2\int_{2\pi/T}^1\frac{\sqrt{1-y^2}}{y}\,dy
 =\frac T2[\log(T/\pi)-1]+O(T^{-1}),
\]
故得(1)，不调用未付WKB余项。

[热与源证明](../reviews/2026-10-28/theta-ground-state/heat-source-and-gaussian-transport.md)按±各一次给
\[
 \Theta_\theta(t)=4t\int_0^\infty T e^{-tT^2}N_\theta(T^2)dT.
\]
ψ(½)=−γ_E−2log2，ψ(3/2)=ψ(½)+2，严格给(2)及余项。完整Θζ保持Γ/FP-contact、全部Λ(p^k)=logp的proper powers和两个pole，不假RH把它换成实频率平方和。旧目标两项不重报新结果；(3)的新责任仅实际Aθ的同对象谱比较。

## 原源费用与真正compact反测

M_T=2Nθ(T²)，每层|B_T(r,s)|≤M_T||r||₁||s||₁。fixed支撑(−L,L)时Q_T(r)≤4LNθ(T²)||r||²_du，再由||r||²_du≤E_log(r)/log2付原zero-extension Dlog。S_exp由p_a,j付L1及全部频尾。没有globaldu统一费用或moving源／成长窗统一误差；每层不必exact消noncompact405。

D′本身不允许直接测试非compact k_t。这里用同一compact crop闭桥：χ_Rk_t→k_t于Schwartz/S_exp；θ侧由多项式谱计数延续，完整ζ侧由Γ的log multiplier、pole指数权和全部pp可和指数尾延续。因此D′身份若成立，必给全部t>0的热身份，与(3)矛盾。

还可直接给合法卷积平方的差：先固定足够小t使δ_t=Θθ(t)−Θζ(t)>0，取r_{t,R}=χ_Rk_(t/2)。加权卷积连续性使Qθ(r_{t,R})−Qζ(r_{t,R})→δ_t。再选一个有限R并固定r，随后T→∞，最终
\[
 Q_{\theta,T}(r)-Q_\zeta(r)>\delta_t/4>0.              \tag{4}
\]
这是一个真正fixed compact physical源，不用非法Gaussian测试、移动源或compact Pan交零。它不声称r在旧17/16窗内，也不推出Qζ(r)<0；两种正型可以数值不同。

## 扣旧、停止与净后果

405/10-14的正源和尾、565基态selector、566完整目标及旧图反测均是输入。它们未给实际Aθ的两项计数／热缺陷，旧非局部E_g亦无同对象谱等价可传此结论。本次新完整反测不从“第一次打印常数”或“正平方”取得资格，而由独立准入、实际原域／严格余项与完整目标运输闭合。

停止原半线Dirichlet/x尺度/H幂/倍数及cutoff规则；不调参数拟合Γ或续谱优化。不同confining、relative、非局部、有补偿的规则没有被整体排除。两份另行整数theta采样／阶乘反演尝试只回到旧582与μ*log=Λ，按0另存，不合并成新增独立输入。

本结果把这一实际候选的目标身份从未付变为确定失败；全局独立signed/corecross、同一非零primitive/mixed容量及Ξ仍未付。Whole542+555→557 leading4/5仍仅负惯性UPPER，585必要费和safehigh保持。它既无whole预算改善，也不移除长期Goal关键瓶颈，更不满足广泛方法类边界完成门。

[根结算](../goals/reviews/2026-10-28-theta-ground-state-586-settlement.md)、[最终逆审](../reviews/2026-10-28/theta-ground-state/fresh-spectrum-heat-source-audit.md)与[前件绑定](../reviews/2026-10-28/theta-ground-state/root-consumption-scope.json)保实际版本、norm/符号/量词及最强旧范围。fresh附核的是6098bytes/417da833…消费草稿；最终版仅更新消费状态并增加这些链接，数学内容不改。
