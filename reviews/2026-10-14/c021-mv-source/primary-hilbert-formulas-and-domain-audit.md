# MV1974 原 Hilbert 公式、域与实际 sinc 前件审查

2026-10-14；C021 stopped 后的一项来源门，**零数学轮**，不重开合同。
已按 AGENTS 恢复 README/STATE、check/show、当前 Goal/frontier/C021/D20261014Y，
读实际 carry/G1/下一来源定位。check 通过不认证数学。
入口 HEAD `36810d109e184787027656c31fb636e880036d7f`；现场 root 的
git属性/ignore与本来源目录有进行中改动。子 get_goal=null，不代root同epoch运行观察。
只编辑本稿，不改 STATE/cadence/Git，不以来源恢复完成Goal。

## 1. 原件身份与视觉核验

H. L. Montgomery、R. C. Vaughan，*Hilbert's Inequality*，JLMS (2) 8 (1974),73–82。
一级[作者托管PDF](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)，
本地固定PDF 538953 bytes、10页，SHA256
`0dbcddf24bc41c65d1920c59aafe7fe85f13a7519b0edf9be9164c84d1cc6db4`。
配套text SHA256
`7857f725cf16975b6408f23dfbe040a82e2161f6fb6ac20a69323666f30fd7aa`，现场均重新核一致。
使用PDF技能只读核印刷73、74、75页（PDF1、2、3），原公式以PNG视觉为准。
text的关键公式OCR不完整，不能凭它补常数。原proof §3、§4文字仅用于定位证明组织；
下面对Cor2/sinc接口另写有限和直接推导，不声称重建作者全部lemma证明。

这是仓库003/085等已使用的旧MV工具，一级原件恢复不构成新独立算术成果。

## 2. §1 的精确公式与常数

所有系数 complex；默认有限 r=1,…,R。Σ′排除无穷summand，
在distinct假设下恰排 diagonal；min₊ 是有限集合的最小正值。

**Theorem 1，印刷73页，(1.2)/(1.3)。** x_r 是 real 且 distinct modulo1，
δ=min₊||x_r−x_s||。则

    |Σ′ u_r overline(u_s)cscπ(x_r−x_s)|≤δ^−1Σ_r|u_r|²。

若0<δ_r≤min₊,s||x_r−x_s||，同一左侧≤(3/2)Σ_r|u_r|²/δ_r。
这里cscπ已有π在argument中，外部常数是1和3/2，不能再乘π。

**Theorem 2，印刷74页，(1.6)/(1.7)。** λ_r 是 distinct real，
δ=min₊|λ_r−λ_s|、δ_r=min₊,s|λ_r−λ_s|。则

    |Σ′ u_r overline(u_s)/(λ_r−λ_s)|≤πδ^−1Σ_r|u_r|²，
    同一左侧≤(3π/2)Σ_r|u_r|²/δ_r。                 (H)

原local δ_r定义为该最小值；若下游只有较小的正lower spacing，替代它只增右侧，仍合法。
不能把mod1距离和real距离混用。

**Corollary 2，印刷74–75页，(1.8)/(1.9)。** 相同real-frequency前件、T≥0，

    ∫_0^T|Σ a_r e^(iλ_rt)|²dt
      =(T+2πθ₁δ^−1)Σ|a_r|²，|θ₁|≤1；
    ∫_0^T|Σ a_r e^(iλ_rt)|²dt
      =Σ|a_r|²(T+3πθ₂δ_r^−1)，|θ₂|≤1。             (M)

第二式中的δ_r仍在r求和内；θ₂可为控制总real误差的一个共同数。
特别local Hilbert的3π/2进入mean-square后是3π，不是3π/2。
这些θ不是已知算术signed节省，只把error压在给定区间。

## 3. 无限域与碰撞：不能只删奇异项

印刷73页指出local/infinite版本把min₊换成inf₊；74页说明无限mod1点集的globalδ=0，
所以该global界vacuous。75页对(M)明确要求相应右侧有限，并按finite partial sums的
mean-square limit解释左侧，不声称任意双重级数绝对收敛。

安全消费条件为：real频率逐个distinct，有δ>0时Σ|a_r|²<∞；
local版每点d_r=inf_(s≠r)|λ_r−λ_s|>0且
Σ|a_r|²(1+d_r^−1)<∞。选择对所有有限subset都合法的同一spacing，
(M)上界使partial sums在L²(0,T) Cauchy，再取极限。
(H)用weightedℓ²域的有界skew-Hermitian型极限；不支付绝对double-sum收敛。
若某d_r=0，不能把1/d_r付作有限费。单频率情形直接给T|a|²，不使用空spacing集合。

actual矩阵的重复label若有同一real频率，必须先合并

    c_λ=Σ_(labels with frequency λ)c_label。

新的diagonal质量是|c_λ|²，包含全部coherent cross；原Σ|c_label|²不能代它。
Σ′在(H)排奇异pair，是定理对已distinct对象的约定，不授权把actual exact collisions删掉。

模1精确碰撞也是Theorem1的前件问题，但actual连续sinc并非csc/cot kernel。
λ和λ+n在unitinterval是不同real modes，n∈Z\{0}时仍正交；
不能通过mod1合并把它们当相同source。若另改用csc kernel，须支付具体phase/sign运输。

## 4. 为什么原证明适用于sinc；2π转换与mean subtraction

对distinct angular频率 λ_r，finite和逐项积分给

    ∫_0^T|Σ a_r e^(iλ_rt)|²dt−TΣ|a_r|²
      =(1/i)[H(a_r e^(iλ_rT))−H(a_r)]，
    H(z)=Σ_(r≠s) z_r overline(z_s)/(λ_r−λ_s)。

两次(H)上界分别产生2πδ^−1和3πΣ|a_r|²/δ_r，正是(M)。
不要求spacing比1/T大才能有upper bound；当spacing很小时费用很大。
general起点t₀只给系数乘e^(iλ_rt₀)，不改质量/spacing。
原§4实线limit用εx的mod1距离最终等于ε|x|及πεcsc(πεx)→1/x；
这需要先固定有限frequency集合，再ε→0，不直接制服成长族的spacing质量。

现在用actual cycles-frequency ρ_r（例如m/q），angular频率是λ_r=2πρ_r。
记 d=min|ρ_r−ρ_s|、d_r=min_(s≠r)|ρ_r−ρ_s|，
h(z)=∫_0^1e^(2πizv)dv=e^(πiz)sinc(πz)，h(0)=1。
(M)、T=1于是精确给

    ∫_0^1|Σ c_r e^(2πiρ_rv)|²dv
      ≤(1+d^−1)Σ|c_r|²，
    ≤Σ_r[1+(3/2)d_r^−1]|c_r|²。                  (S)

3/2来自3π/(2π)，不是丢掉π；它与(H)的3π/2是不同规范下的不同界。
linear-first原Gram为h(ρ_r−ρ_s)。child mean projection后的profile

    ψ_ρ(v)=e^(2πiρv)−h(ρ)

有exact Gram h(ρ−σ)−h(ρ)overline(h(σ))。
该rank-one subtraction是同一L²(0,1)正交mean projection，故

    ||Σ c_r ψ_(ρ_r)||²≤||Σ c_r e^(2πiρ_rv)||²，      (S′)

(S)可合法给其upper。不能由unprojected lower bound继承centred lower；
也不能忽略mean subtraction后说它就是Hilbert奇异kernel。

## 5. 实际carry接口及此来源尚未付的运输

从550/C021原du等距因子r=a_Nφ、||r||²=N^−1/2||φ||²开始，
detail adjoint是R_flat U_q*(I−P_q)，q<N且Λ保全部proper prime powers。
对某actual完整child cell n∈{1,…,N−1}，j=floor(n/q)≥1、s=n−qj，
full arithmetic adjoint输出的flat profile准确为

    Σ_(2≤q≤n) Σ_(m≠0,q∤m)
      [Λ(q)/q ·e^(2πim s/q) f_(floor(n/q),m)]
      ·[e^(2πi(m/q)v)−h(m/q)]。                     (A)

(A)每个child的v确实在整个(0,1)，因为N为整数且原cutoff不切半个child；
不存在凭一个共同profile替换所有cell的操作。q|m部分已是另付D-part，
q∤m的real ρ=m/q一般非integer。重复real ρ的全部coefficient/phase先合并，
然后才能把每个child的完整(A)作为(S′)输入。
这个**形式级接口合法**，并非直接宣称(S′)的右侧足够小。

每个fixed N的全部m无限集，合并后仍是分母≤N−1的distinct rationals；
real spacing≥(N−1)^−2。有限q的coeff映射在ℓ²上有fixed-N有界质量，
所以(S′)的infinite mean-square域可进入，不必把有限Fourier诊断当full-source结论。
但source-blind global费为O(N²)，不是目标polylogN；localspacing及coherent
collision质量是否抵消此损失，必须从(A)另付。一个upper过大不是必要增长或反例。

原fullcarry二次型是2N^−1/2Re〈Σ_qw_q C_qφ,φ〉，
而(S′)控制的是相应adjoint合成norm。要从后者回到前者，必须保同一φ、
原du系数N^−1/2、全部q/cell/m/cross与Γ价格；不能把positive Gram本身当signed Weillower。
已经付的G1 E_cell≤4JΓ+56logNnorm²，不自动控制collision/spacing加权的(A)质量。
单fixedm、某个finiteband或仅Cor3旧Dirichlet均值仍不是ALL Dlog的G2。

消费记录：原定理是旧 Hilbert/mean-square工具；有限或合法weighted无限complex域已核，
π/3π/2/3π及cycle conversion全付，无浮点误差。actual sinc/centred Gram对象精确，
但成长localspacing、碰撞合并质量和原Γ-relative transport仍open。
本稿不预付G2/conditionalwholecount，不新建合同、不计轮、不完成Goal。
下一只由root合并actual collision原审与强旧净值后决定该来源是否入口停止。
