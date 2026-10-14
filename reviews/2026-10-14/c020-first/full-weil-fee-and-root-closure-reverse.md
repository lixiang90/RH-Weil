# 549 §3：完整Weil源费与root前件闭合短逆审

2026-10-14，`/root/c017_gamma_cross`，只读逆核，不进行新研究，不改root文件或计轮。
按 AGENTS 读 README/STATE 并运行 check/show；两者现场报告
“Goal version changed; inspect scope before rebinding state”。
已告知root并读实际Goal：新增前件闭合/停滞准入组织条款，完整数学门、G20261014及0c4f/≤538基线不变。
本代理不修改STATE指纹，不把这个并发结构状态宣称为数学通过或数学失败。
继续恢复当前frontier/C020/D20261014U和原证据；HEAD
bc2a891e885f5cb4412c44c5f10df049cfc9127f，root组织/549稿等尚在工作树。
子get_goal=null不代root运行态。

所读 [549](../../../notes/549-mobius-window-norm-full-cofactor-gram-and-physical-synthesis-gap.md)
raw SHA256：`8d5c9eb9490ce949b6636b1792b051e43c7e4c8f2f42c50f5f796fa6a2d074c5`。
读完整cofactor原稿及[537](../../../notes/537-source-exact-weil-window-positive-tail-admission.md)第100–101行的
原平移/真实overlap消费范围；没有重做已通过的来源及variable-window证明。

## 1. 同一source的共同支持及平移

所有真实columns Fκ使用 n=κd∈(Y,2Y] 和 E_n=1_[logn−h,logn]，
故共同支持包含于 [logY−h,log(2Y)]，与κ、μ符号或cofactor clipping无关。
T≥sqrtY、h=1/T；对大Y，宽 Δ=log2+h<2。
置 c_Y=[logY−h+log(2Y)]/2，g(v)=f(v+c_Y)，则支持⊂[-Δ/2,Δ/2]⊂I₁=(-1,1)。
这是一个共同平移作用于所有columns/labels，没有分别平移而改变cross。

原du norm和Dlog域保持，hat g(t)=e^(itc_Y)hat f(t)，完整actualΓ=2θ′的型不变。
所有 lag autocorrelation 满足

    ∫g(v+logq)overline(g(v))dv
      =∫f(u+logq)overline(f(u))du。

原 dual pole functionals A±=∫f(u)e^(±u/2)du 则精确变为

    A_+(g)=e^(−c_Y/2)A_+(f)，
    A_−(g)=e^(c_Y/2)A_−(f)。

c_Y为实数，所以完整 signed 2Re[A_+overline(A_−)] 不变。
这正是537的原对象平移消费，不是把两个原moment逐项假设不变。
偶/奇 C,S 单独会混合，但2|C|²−2|S|²这个完整pole型保持，odd负pole没有删除。
因此 complete Q(g)=Q(f)，并保共同全complex标签的所有cross。

## 2. fixed I₁上的全部pp/双pole bounded费用

零延拓 g 支撑I₁。lag≥2时两个支撑仅可能零测交，实际相关为0；
所以完整primepower和只按真实overlap缩到 strict q<e²。
实际全部pp是2、3、4、5、7，properpower4仍保Λ(4)=log2；不凭prime-only截断。
对每一个q，full-line unitary translation及Cauchy给

    |∫g(u+logq)overline(g(u))du|≤||g||²。

故 absolute prime费用≤2Σ_(q<e²)Λ(q)/sqrtq·||g||²。
在I₁，||e^(u/2)||²=||e^(−u/2)||²=e−e^−1，
所以整个 signed pole绝对值≤2(e−e^−1)||g||²=4sinh1||g||²。
actual qΓ=Γ₀||g||²+JΓ(g)，JΓ≥0，因此

    |Q(g)|≤JΓ(g)+C₁||g||²，
    C₁=|Γ₀|+2Σ_(q<e²)Λ(q)/sqrtq+4sinh1。             (1)

这是absolute定值、原norm、全部complex Dlog源的fixed-window bounded perturbation。
finite BV columns及它们的finite label组合属于Dlog甚至actualΓ operator域；
(1)也可按原闭型域直接消费，没有smooth-only门、频率截断或未付pole-error。

## 3. normalized完整Q的flat-label推论

令 Aα=Σ_(2≤κ≤M)ακFκ，为原 shared physical map。
已审fullmask raw positiveGram给 ||Aα||²≤η(Y)||α||²、η(Y)→0。
全 Γ/Dlog positive form Gram的trace/β趋0，给

    JΓ(Aα)/β≤δ(Y)||α||²，δ(Y)→0，β≥c log(e+T)。

这些positiveGram界保所有exact/near-product cross，不是逐column丢cross。
§1共同平移不改这两个Gram，联(1)得

    |Q(Aα)|/β≤[δ(Y)+C₁η(Y)/β]||α||²=o(1)||α||²。     (2)

这里调用的是fullmask JΓ form/beta，而非operator-square/beta。
原Γ operator-square预算只有/beta²那一项，未偷换归一化。
source-free tail和每fixed-aspect MR由root消费到fullpositiveGram后，(2)是严格的直接推论；
没有把MR字符范围扩到所有Fourier tau+t。

## 4. root闭合范围及宏观判定

549表中“每fixedlabel→全部flat单位labels→实际α=1”明确区分，消费范围正确。
source MR前件、原du variable-window、可和fullcofactor raw/Γ tail共同付款后，(2)是新的源费用。
它不提供新fixed-window positive定理：537已对包含I₁的窗口支付全complex正性。
更不支付成长全Weil域、actualακ=1的质量M−1、TypeI/continuum或谱core净后果。
对实际方向，右端仍乘M−1；无rate不能胜最强旧actual II 的 O(log⁶Y)范数费用。
old016/028及543的whole惯性预算也未因此改进。

scope准确：可以消费normalized完整Q fee；不能把“费小”改成独立正性来源，
也不能从flat label trace小改成actual fullphysical synthesis小。
本逆审不独立计轮；C020由root统一结算一次，组织完善不计数学轮，长期Goal仍open。
未发现§3符号、domain、primepower、dual-pole或前件闭合数学错误。
