# 固定未平均Petersson覆盖塔：独立fresh逆审

2026-10-28；/root/pet_fresh独占。恢复同G20261027／原0c4f、STATE／D20261028A及唯一[准入公式](../../2026-10-27/raw-theta-mean/next-cofinal-petersson-local-norm-admission.md)。本稿仅核固定κ=3/2、restricted unitary automorphy、Γ_n=Γ(N0 n!)、原未平均Petersson范数的Gram族；不改STATE/cadence/Git，不预C048/585，不执行其他路线或新增外部来源。

**最终有限PASS：两原稿的实际终版已完整核读、逐式对齐并绑定；固定原规范的局部统一du费及完整Q高频反测闭合，建议标准强旧合成0数学轮。** 下文不代root消费，不完成长期Goal。

## 1. 几何域、halfweight与原Pet局部费用

N0=4D(B)≥4。Γ(N0)中γ=I+N0 A的det=1给trγ=2−N0²det A；有限阶SL2(R)元素的trace在[−2,2]，遂trγ=2，有限阶时γ=I。−I不在Γ(N0)中，因此原矩阵群到PSL2的作用无中心kernel且无torsion。半整数automorphy可以有phase或metaplectic lift；本门只用已定义scalar f的holomorphic性及

\[
 |f(\gamma z)|^2(\Im\gamma z)^{3/2}
       =|f(z)|^2(\Im z)^{3/2}.
\]

restricted unitary multiplier正好给此模长身份。若中心/automorphy相容性使S_n为零，空和本身通过估计，不能用未知非零性延长门。没有将κ=3/2当weight2或trivial multiplier。

在compact ray K={ie^t:|t|≤17/16}，Γ(N0)的自由properly discontinuous作用给统一正的局部注入半径；每个Γ_n为subgroup，同一小圆盘在全部quotient中嵌入。也可直接由矩阵得到uniform位移，原稿须付实际常数，不能把quotient整体当compact。

独立地取固定η∈(0,1/2)，使D(z,η Im z)在上述嵌入圆盘内。holomorphic均值及y∈[(1−η)y0,(1+η)y0]给每个f∈S_n

\[
 |f(iy_0)|^2\le\frac1{\pi\eta^2y_0^2}\int_D|f|^2dxdy
 \le\frac{\sqrt{1+\eta}}{\pi\eta^2}y_0^{-3/2}
             \|f\|_{\rm Pet,n}^2.
\]

第二个不等式确实使用原Pet密度y^(κ−2)=y^−1/2和未平均quotient积分，没有vol/index因子。局部积分≤全Pet积由disk嵌入及非负性付清；不需要覆盖塔总面积有界。

## 2. Riesz总evaluation与原du上界

上界对任意unit f成立。Riesz evaluation的squared norm正是Σ_j|f_(nj)(iy)|²；若用基变换写，这是sup_(Σ|a_j|²=1)|Σa_j f_(nj)(iy)|²。必须在整个unit球取sup一次，不能单独估每个基函数后乘dim S_n。

因此沿冻结W_(nj)(t)=e^(3t/4)f_(nj)(ie^t)，有Σ_j|W_(nj)(t)|²≤Cη，独立n,t∈I*。对全部complex r∈Cc∞(I*)，有限基上的Hilbert空间Cauchy–Schwarz给

\[
 G_n(r,r)=\sum_j\left|\int r\overline{W_{nj}}\right|^2
       \le\left(\int_{I_*}\sum_j|W_{nj}|^2dt\right)\|r\|_{du}^2
       \le |I_*|C_\eta\|r\|_{du}^2.
\]

这不是全线level统一费用、sharp norm或necessary lower。原physical r=e^(t/2)f_phys不改；没有在未付的全线Hlog/Dlog上另作claim。Gram的kernel方向为Σbar W(t)W(u)，第一腿r线性，与原Pet约定一致。

## 3. 完整Γ高频与极限量词

旧552§5已经给固定ψ≠0∈Cc∞(I*)、r_R(t)=ψ(t)e^(iRt)的完整型Qζ(r_R)=log|R| ||ψ||²+O(1)。537恢复的actual Γ multiplier为Re digamma(1/4+iξ/2)−logπ，含contact规范；它在|ξ|→∞为log|ξ|+O(1)。Plancherel和ψ的Schwartz Fourier尾直接给leading系数1。

支持差在(−17/8,17/8)，故全部properpowers仅留下有限Λ(n) shift；各相关项由原du的Cauchy–Schwarz一致有界，随R可振荡但不长出log R。完整双pole矩是smooth compact函数的Fourier值，反复分部积分快速衰减；并未删除pole或假设RH。无需双polezero修正即可反测全compact源极限；若另声明该子域，须实际付固定dual templates及原form混合费。

若对每个固定r∈Cc∞都有G_n(r,r)→Qζ(r)，上节统一上界传给每个这样的r。先据Cη选一个充分大但固定的R，使Qζ(r_R)>|I*|Cη||r_R||du²，再只对这一个r_R令n→∞，即得矛盾。不依n换测试源，不交换n和R双极限，不用负Q或RH。

G_n是源上的PSD Gram；B_n(t,u)一般尚未证明只依t−u，不将每层自动称为单变量Weil正分布。该区别不妨碍当前逐源Gram极限的必要门。

## 4. 消费范围、最强旧与计轮

本门至多停止当前固定**原未平均Pet**、固定weight/ray的cofinal Gram逐compact源极限recipe。逐层无需消noncompact405，旧fixed A的精确Pan同像不能直接用于本量词；这里另付局部统一norm与旧全Γ频率比较。没有泛排vol归一化、发散level权、非局部/源适应/不同域的positiveapprox或额外实际arithheight；这些仍须各自公式、原费和完整signed误差，不能事后默改当前family。

local holomorphic均值/Riesz是标准估计，高频log已由更强旧552明确支付，二者直接合成建议0数学轮。source/具体候选选择改变，不是新的经典独立primitive、整过滤/截面/mixedRR、signedgrowth/actualq/core/coupling/Ξ或whole后果。542＋555→557 wholeleading4/5仍为负惯性UPPER。原literalR/K与整体arithmeticTheta/7.4冻结保持；长期Goal门open，不因本次候选止门完成。

## 5. 两原稿终版核查与绑定

实际核读local稿时，复核其明确δ=min{log16−17/8,2arsinh(2e^−17/16)}>0。c≠0时原c∈N0 Z给height ratio≥16e^−17/8；c=0时a=d=1、|b|≥4给第二支位移。ε=1−exp(−δ/4)的Euclidean盘由直线段积分落在hyperbolic δ/4盘内；若平移相交便给中心位移<δ/2，实际注入前件成立。κ−2=−1/2的权不等式方向、原未平均Pet积分、(10)的Riesz总和及kernel bar方向都逐项核过；(11)的明确常数为C_(I*)=(17/8)sqrt(1+ε)/(πε²)。没有只核相同结论标签。

实际核读frequency稿时，逐项对齐537/552的Fourier规范、leading系数1、全部六个非零properpower/prime shifts、完整不定双pole及固定bump量词。原稿已补明可选polezero修正的固定dual templates和Hlog极化连续性，不因L²修正小就误用未有界的Q。§4先选fixed R0，再对所有n取得同一源的严格signed缺陷，顺序准确。仅发现公式(2)一处TeX排版错误，作者已将`\!left[`修为`\!\left[`；修正没有改变数学内容，已核实际新版本。

最终绑定均为UTF-8字节、LF规范化SHA256：

* local-evaluation-and-original-fees.md：c92db289a522e161dac945c67c6129d57c5dc477910a3b56badba85d2f62c3a3（8113 bytes）。
* full-weil-frequency-and-limit-scope.md：fcd873faa4f7ca363258a54abbb18dcb3dff9137ac438b4593f7f9f6b3cb7410（7933 bytes）；旧7932-byte／c794f75e…稿不作最终绑定。

只有以上版本获本次有限PASS。对象/automorphy、Pet归一化、源map、局部费用、全Γ/pp/pole规范或极限量词改变，须重闭对应依赖；hash本身仅认版本，不证明结论。当前仅止已冻结family，不泛排正D′路线。root仍须消费实际前件链、strongest-old净后果与准确范围。本稿没有外部PDF／网页／原proof新读或下载，没有执行下一候选，也没有修改其他文件、STATE、cadence或Git。
