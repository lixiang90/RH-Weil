# C016：完整双尾 physical packet、原范数与同对象准入

2026-10-14；独立代理 `/root/c016_packet_norm`。
本稿是指定候选的全频 source 审查，不修改 STATE、cadence、Goal 或 Git，
不自行结算数学轮。结论不使用 RH、零点拟合、有限矩阵或无零区域优化。

## 1. 恢复与责任范围

已读 AGENTS、README、STATE，先运行 research_state.py check，再 show，
再读 Goal、MACRO_FRONTIER、C016、D20261014Q 及所需原件。
结构 check 通过；初始 Git clean，HEAD
`d924d2cae53c19c3ee99e8a1ace550072c4b4683`。
子代理 get_goal 返回 null，只说明子代理运行域，不认证 root Goal 的状态。
本稿无科学 producer 或待续 exec session。

Goal 固定基线为 `0c4f3a3eb609bb1d9564138fa4a35701f05605f2`、全部≤538。
当前最新数学结算543，原cadence2。543的 cofinal 全复源负惯性上预算
`1+C exp(S_L)` 不支付成长 PSD 或 Ξ 识别；本稿也不能用新的正 Gram 命名
代替这两项责任。

必要原件是 Zagier §2 (2.2)–(2.8)、Garrett 四项 Maaß–Selberg proof，
及 actual Q 的016/028/543消费规范。Zagier PDF和text的现场hash与来源收据一致：

- PDF `a7ad2a85f9a90de14ac0b4affd723393b7ab61e16dd749dd6c4c0db881767b94`；
- text `82a4e9799d6c3d6fe3a71dc726a2cfc887244826ad7232a28861b34ff9212a29`。

原扫描PDF第12页已按像素核(2.6)/(2.7)，不把OCR损坏的公式消费成原件。
来源：[Zagier作者原PDF](https://people.mpim-bonn.mpg.de/zagier/files/scanned/EisensteinSelberg/eisenstein-selberg-I-978-3-662-00734-1_11.pdf)、
[Garrett作者原PDF](https://www-users.cse.umn.edu/~garrett/m/v/maass_selberg.pdf)，
本地冻结版本见[c015来源收据](../c015-admission/sources/macro-primary-source-receipt.json)。
Γ双尾使用[NIST DLMF 5.11.9](https://dlmf.nist.gov/5.11.E9)，
而下面ζ的粗界直接证明，不借临界线零点位置。

## 2. 冻结实际变量与 Hilbert 空间

取 `M=PSL₂(Z)\H`、`dμ=dxdy/y²`，`H=L²(M,dμ)`，
标准 fundamental domain 的 cusp 是 `−1/2≤x≤1/2,y>1`。
定义

    Λζ(w)=π^(−w/2)Γ(w/2)ζ(w),
    a(s)=Λζ(2s),       b(s)=Λζ(2s−1),       p(s)=s(s−1),
    α(s)=p(s)a(s),     β(s)=p(s)b(s),
    E*(z,s)=a(s)E(z,s),      F(z,s)=p(s)E*(z,s),
    c*_s(y)=α(s)y^s+β(s)y^(1−s),
    F_Y=F−1_(y>Y)c*_s,       Y≥2,
    s_t=1/4+it/2,            v_Y(t)=F_Y(·,s_t).

这里 s_t 的 `2s_t=1/2+it` 是 actual ζ 变量，
`Γ_actual(t)=Reψ(s_t)−logπ=2θ′(t)`。
原 source 是全部 complex `f∈L²(I_L)`，`I_L=(−L,L)`，零延拓，
`hat f(t)=∫ f(u)e^(−itu)du`，Plancherel因子为`1/(2π)`。
原型域

    Dlog={f∈L²(I_L): ∫ log(2+|t|)|hat f(t)|²dt<∞}。

不以单侧频率、有限频窗、偶实源或不同 Hilbert norm 代替这些对象。

Zagier原Bessel式是

    E*(z,s)=a(s)y^s+b(s)y^(1−s)
      +2√y Σ_(n≠0) τ_(s−1/2)(n)K_(s−1/2)(2π|n|y)e^(2πinx),
    τ_ν(n)=Σ_(ad=|n|,a,d>0)(a/d)^ν。

在任意compact s集上，τ有统一多项式n界；
原`K_ν(x)=∫₀∞ e^(−x cosh r)cosh(νr)dr`给compact ν集、`x≥x₀>0`
的`|K_ν(x)|≤C e^(−x)/√x`，因为`cosh r≥1+r²/2`。
故非零mode在cusp上有参数compact-uniform指数y尾，
有限Y以下的fundamental domain也是compact。
因此regular参数上的F_Y是真正H向量，且沿当前整条s_t线连续。
0/1 pole-clearing及s=1/2相消须用原件的参数延拓核验；
当前s_t线不穿这三点，下面不靠跳过频率点去掩盖source奇性。

## 3. 直接 classical norm 与完整 t=0 head

以下对角式可以独立由 classical hyperbolic Green identity 推出。
E*与F仍满足`ΔF=s(1−s)F`，其中`Δ=−y²(∂x²+∂y²)`。
在fundamental domain的水平边y=Y应用Green，配对的竖边按automorphy相消。
把y>Y的非零Fourier modes补回：它们在Y处的Wronskian恰与该区域的
Green边界项相消，∞端为0。余下只是constant modes的Wronskian。
除以

    s(1−s)−bar w(1−bar w)=(s−bar w)(1−s−bar w)

得到原四项的完成形式

    H_Y(s,w)
    =[α(s)barα(w)Y^(s+barw−1)−β(s)barβ(w)Y^(1−s−barw)]/(s+barw−1)
     +[α(s)barβ(w)Y^(s−barw)−β(s)barα(w)Y^(barw−s)]/(s−barw)。       (1)

分母相消处按removable limit消费，不增加未付scalar因子；
x周期宽度1与`dμ=dxdy/y²`正是这里的classical norm规范。
这也核对了Garrett general公式到当前Haar规范的消费范围。

令w=s=s_t、t≠0，(1)给

    ||v_Y(t)||²
      =2Y^(1/2)|β(s_t)|²−2Y^(−1/2)|α(s_t)|²
        +2 Im(α(s_t)barβ(s_t)Y^(it))/t。                         (2)

尤其最后项是完整mixed响应，不能删去，也不能换成对角`2logY`。
当t=0，α、β实值，mixed numerator为0；其除以t的极限是对应导数。
对`|t|≤1`，α、β及其t导数有固定compact上界。
利用`|sin(t logY)|≤|t|logY`和其余系数的Lipschitz界可得

    ||v_Y(t)||²≤C(√Y+Y^(−1/2)+1+logY)≤C₀√Y,
       |t|≤1, Y≥2。                                               (3)

常数不依赖Y或source；head和coalescence确实支付。
这里的C₀可取上述compact系数/导数sup及有限几何常数，
不包含未知ζ zero-free下界。此线没有Λζ的0/1极点。

## 4. 不借RH的ζ粗界及实际双尾

对`Re w>0,w≠1`和整数N≥1，Euler积分恒等式为

    ζ(w)=Σ_(n≤N)n^(−w)+N^(1−w)/(w−1)
                  −w∫_N^∞ {x}x^(−w−1)dx。                      (4)

从`Re w>1`的逐段积分证明，再由右边的绝对收敛积分延拓即可；
这是原ζ函数的恒等式，不假设RH。取`w=1/2+it`、`T=|t|`、
`N=ceil(1+T)`。三个绝对费用依次不超过`2√N,2√N,2√N`，
故对全部t

    |ζ(1/2+it)|≤6√N≤9√(1+T)。                                  (5)

Λζ功能方程还给

    b(s_t)=Λζ(2−2s_t)=Λζ(3/2−it),
    |ζ(3/2−it)|≤ζ(3/2)≤3。                                      (6)

NIST的Γ双尾式给固定实部1/4、3/4上的全局界

    |Γ(σ+it/2)|≤K_σ(1+T)^(σ−1/2)e^(−πT/4)，
        σ∈{1/4,3/4}。                                            (7)

K_σ由双尾渐近的有限阈值及剩余compact的sup合并选取；
负尾由conjugation完全保留，既不减半规范也不删一尾。
于是(5)–(7)给

    |a(s_t)|+|b(s_t)|≤C(1+T)^(1/4)e^(−πT/4)，
    |α(s_t)|+|β(s_t)|≤C(1+T)^(9/4)e^(−πT/4)。                    (8)

把(8)代入(2)，对T≥1付完整mixed项，舍去负的α对角项只用于上界。
连同(3)，得到一个对全部`Y≥2,t∈R`的绝对包络

    ||v_Y(t)||²≤C₁√Y(1+|t|)^5e^(−π|t|/2)。                       (9)

幂5只是把严格可得的9/2向上取整，未声称最优。
它给全部双尾矩及误差：对T≥1

    ∫_(|t|>T)||v_Y(t)||²dt
       ≤C₂√Y(1+T)^5e^(−πT/2)。                                 (10)

用五次分部积分即可取C₂；head不藏在这项tail误差内。
同样`∫(1+|t|)^k||v_Y(t)||dt<∞`对每个固定k成立。

## 5. 真正全源 Bochner、双频极化与HS运输

对整个`L²(R)`而不仅原Cc∞源，定义

    A_Y f=(2π)^(-1)∫_R hat f(t)v_Y(t)dt。                         (11)

由(9)和Cauchy–Schwarz，`∫|hat f| ||v_Y||<∞`；
因此(11)是绝对Bochner integral，且

    ||A_Y f||≤(2π)^(-1/2)||v_Y||_(L²_t(H)) ||f||_(L²_R)。         (12)

Fourier单位化`U f=hat f/√(2π)`后，(11)的向量核是`v_Y/√(2π)`。
故它在整个L²(R)上已经Hilbert–Schmidt，严格费用为

    ||A_Y||_HS²=(2π)^(-1)∫ ||v_Y(t)||²dt≤C₃√Y。                 (13)

限制到零延拓L²(I_L)不会增大HS范数；Dlog上的波包就是这个同一延拓，
不需要增加source正则性，也不以Cc∞的有限频率近似替代全轴。
这是一项**原norm上的有界运输**，不是原norm上的可逆运输。

由`|H_Y(s_t,s_r)|≤||v_Y(t)|| ||v_Y(r)||`，
对所有complex f,g∈L²(I_L)双积分绝对可积，Fubini给

    <A_Y f,A_Y g>
       =(2π)^(-2)∫∫ hat f(t)bar(hat g(r)) H_Y(s_t,s_r) dt dr。    (14)

内积取第一变量线性；正Gram是这一个双频能量，而不是单频multiplier。
物理核

    K_Y(u)=(2π)^(-1)∫ e^(−itu)v_Y(t)dt,
    A_Y f=∫ f(u)K_Y(u)du                                      (15)

具有全部实变量导数，并在`|Im u|<π/4`为H值holomorphic。
这从(8)/(9)的L¹双尾直接得出，是具体completed smoothing，
不只是一项有限matrix事实。
若(11)只取`|t|≤T`，全源误差由(10)支付：

    ||A_Y−A_(Y,≤T)||≤||A_Y−A_(Y,≤T)||_HS
       ≤C₄Y^(1/4)(1+T)^(5/2)e^(−πT/4)。                        (16)

这些常数不依赖L；Y增长时明示`Y^(1/4)`费用。
HS与紧性不推出A_Y无核、不推出实际谱的可见性或任何ζ零点约束。

## 6. 完整 cusp 扣除对全部物理源的确切效果

令

    C_(2,Y) f(y)=(2π)^(-1)∫ hat f(t)c*_(s_t)(y)dt， 2<y≤Y。

每个finiteY有同样Bochner和L² band延拓，可直接由
`F_Y−F₂=1_(2<y≤Y)c*`与(13)获得。
F₂在该band只有非零x modes，c*是constant mode，二者正交。
所以所有complex f,g∈L²(I_L)，不用频窗、偶实限制或Y→∞，均有

    <A_Y f,A_Y g>−∫_2^Y C_(2,Y)f(y)bar(C_(2,Y)g(y))dy/y²
           =<A₂ f,A₂ g>。                                      (17)

对角余项非负，但正是`A₂* A₂`这一个trace-class smoothing。
所以任何有限`Y=Y(L)≥2`的完整费用扣除后，净source算子仍为A₂；
仅增长Y不能恢复原norm底。即使每个source另选有限Y(f)，
只要扣的是同一完整cusp mode，对角净值仍为`||A₂ f||²`。
这是exact单source恒等式，不把source-adaptive选择伪装成一个线性Gram。

若Y(f)同时改变频权/参数或保留不同cusp余项，(17)不再自动认证这种新对象；
须另付共同source、范数和全频费用。有限Y费用大并不构成RH错误反例，
而完整扣除余项与Y无关也不排别的subleading/signed几何机制。

## 7. 不能无费升格为原norm或actual Q

对任意fixed L>0、finite Y≥2，A_Y在无限维L²(I_L)上紧。
因此不存在`c>0`使`||A_Y f||²≥c||f||²`对全部合法源成立。
更具体地，取非零`g∈Cc∞(I_L)`并令

    f_ω(u)=e^(iωu)g(u)/||g||，      ω→+∞。

这些是原complex Dlog合法源，L²范数1，且弱趋0。
由紧性`||A_Y f_ω||→0`，完整扣除后的`||A₂ f_ω||`也趋0。
若要求任意有限个连续L²线性条件，可把每个代表向量用Cc∞有限dual矩阵实现，
减去趋0的有限个smooth correction；得到同norm极限的合法条件源，紧性仍消费。
所以固定有限条件或有限秩修复不付source norm底。

实际完整Weil型则是

    Q_L(f)=(2π)^(-1)∫ Γ_actual(t)|hat f(t)|²dt
       −2Σ_(n<e^(2L)) Λ(n)n^(−1/2) Re∫ f(u+logn)bar f(u)du
       +2|∫f cosh(u/2)du|²−2|∫f sinh(u/2)du|²。                 (18)

保留全部strict primepowers和双pole。对上述carrier，
`Γ_actual(t)=log(|t|/(2π))+O(1/|t|)`给第一项`logω+O_g(1)`；
全部prime项fixed L上有界，pole functionals由smooth积分分部而趋0。
分解频率近ω与Schwartz尾即可严格支付渐近。因此

    Q_L(f_ω)=logω+O_(L,g)(1)，   ||A_Y f_ω||²→0。              (19)

这是源范数/能量scope检验，**不是Q负反例**。
它排除把completed Gram等同于Q或用任何fixed bounded原L²残差修成等式，
也排除completed Gram无费替代原Dlog/Γ能量。
它没有排除方向`Q≥c A₂* A₂−εI`，也不凭高频正性完成这种direction；
真正signed/core比较仍需独立新输入，不能从Gram≥0推出。

对每个fixed L，任意有界频权m_L(t)、有界输入算子或有界几何输出权B_L，
均保持相应A_Y的紧性；`A_Y* B_L A_Y`仍紧。
加入任意fixed finite-rank bounded修复仍紧，不能给原L²无限维底。
这允许权的norm/rank随L增长，但每个fixed L的全源门已失败。
它不排无界权、无限秩非紧的新输入或专门危险core上的有费比较。

## 8. Undo completion 的实际费用与两套pole不可混同

### 8.1 无零β系数的严格 inverse-domain 门

先用完整constant mode的第二系数，而不用临界ζ的除法：

    β(t)=β(s_t)=s_t(s_t−1)Λζ(3/2−it)。

`Re(3/2−it)>1`上ζ及其Möbius逆级数均绝对收敛。
由`μ*1=δ₁`及绝对Cauchy乘积，`1/ζ(w)=Σ μ(n)n^(−w)`；
两级数的绝对值都≤`ζ(3/2)≤3`，所以

    1/3≤|ζ(3/2−it)|≤3，所有实t。                              (20)

Γ在`3/4−it/2`无零，由双尾渐近及compact最小值给全实t两侧界
`|Γ(3/4−it/2)|≍(1+|t|)^(1/4)e^(−π|t|/4)`。
这里的Γ无零性质见[NIST DLMF 5.2(i)](https://dlmf.nist.gov/5.2#i)。
`s_t(s_t−1)`沿实t无零且绝对值≍`(1+|t|)²`，故

    0<c(1+|t|)^(9/4)e^(−π|t|/4)
      ≤|β(t)|≤C(1+|t|)^(9/4)e^(−π|t|/4)，所有实t。             (21)

所有head常数有有限正下界，没有未知zero-free假设。
在L²(R)用原单位化Fourier定义有界乘子β(D)，其最大inverse域是

    Dom β(D)^(-1)={f∈L²(R): hat f/β∈L²(R)}。

则对**每个finite L>0**，严格有

    Dom β(D)^(-1) ∩ {f∈L²(R): supp f⊂[−L,L]}={0}。          (22)

证明：若`h=hat f/β∈L²`，(21)上界使对任意`0<a<π/4`

    e^(a|t|)|hat f(t)|
       ≤C(1+|t|)^(9/4)e^(−(π/4−a)|t|)|h(t)|

属于L²。对`|Im z|<a`，`(2π)^(-1)∫hat f(t)e^(itz)dt`
在每个严格更小strip绝对局部一致收敛，所有导数由相同指数余量控制；
所以定义holomorphic函数，其实轴值等于f的连续代表。
compact support令其在外部开实区间为0，identity theorem令其在整个strip为0。
因此f=0。这对全部complex L²成立，包含原Dlog全部合法compact源；
不只排一个smooth carrier或一个fixed频窗。由每个L的同一结论，
允许finite L成长仍没有非零原source可以直接使用该inverse coefficient。

量词限于**把原hat f直接除β作为同packet的L²频系数**。
β(D)在自己的range上有合法inverse：因为β无零，它是injective，
range稠密且包含大量非零analytic source；其inverse就是最大域上的闭无界算子。
例如任意h∈L²取`hat f=βh`，就在inverse域里；此f通常不compact-supported。
不能把(22)读成inverse在已知analytic range上不存在，
也不能排直接以h为新coefficient构造另一个非紧振荡packet。
后者改变了原physical source，须重新支付sameobject actualQ桥。

### 8.2 第一系数、原norm费用与actual dual poles

若只把source权改成`1/[p(s_t)a(s_t)]`去还原E，
(8)已给不借zero-free的双尾费用

    |p(s_t)a(s_t)|≤C(1+|t|)^(9/4)e^(−π|t|/4)。

除去该因子的频乘子因而至少指数增长，不能是原L²的bounded权。
ζ的孤立零点还会使该表达式出现未付pole；本稿无需假设它们在哪条线上。
事实上对任何非零compact-supported L² f，
`hat f/[p(s_t)a(s_t)]`不可能属于L²(R)：否则上面的下费用给
某个`0<a<π/4`的`e^(a|t|)hat f∈L²`，逆Fourier定义strip内holomorphic函数，
它在compact support之外的开实区间为0，identity theorem强迫f=0。
孤立零点测度0不破坏这一下费用论证。

这里只说明“同一completed有界source运输+inverse multiplier”的原norm费用。
不能由向量pointwise增大就推断所有直接uncompleted振荡packet均无定义，
也不能排除另有一项直接非紧运输定理；那需要新common-source分析。
即便只去Γ、保ζ所付的逆权也是指数的，不能沿用(11)的bounded原norm证明。

还须区分两套pole：F的`p(s)=s(s−1)`清除的是几何E*在s=0,1的极点，
沿`w=2s=1/2+it`对应w=0,2，即`t=i/2,−3i/2`。
实际ζ的dual poles w=0,1对应`t=±i/2`，ξ的多项式因子是`w(w−1)`，
换到s为常数倍`s(2s−1)`，不是`s(s−1)`。
s=1/2处E*两个constant poles内部相消，不自动支付(18)的两项pole型。

在regular点completion log-derivative虽含

    d_s log a(s)=−logπ+ψ(s)+2ζ′(2s)/ζ(2s)，

其实部的Γ部分对齐actual2θ′，但这不是(14)双频Gram到(18)单频Γ、
全部strict pp与dual pole的正型运输。
对临界变量的log-derivative、Fourier展开及零点处division所需费用也不能
以`Re w>1`的Euler绝对收敛无声搬到`Re w=1/2`。

## 9. Direct 剥β的真实逃逸：原norm有界、非紧且有cusp核

### 9.1 必须改正“inverse空域排整个补偿”的推断

由原functional equation `E*(s)=E*(1−s)`、`p(s)=p(1−s)`，
常数项截断也同样相消，严格有

    U_Y(t)=F_Y(s_t)/β(t)=Λ^Y E(1−s_t)，
    1−s_t=3/4−it/2，
    m(t)=α(s_t)/β(s_t)=a(s_t)/b(s_t)，   sup_R|m(t)|=M₀<∞。     (23)

(5)、(20)与Γ ratio付m的双尾和head，`m(−t)=bar m(t)`。
故从(2)直接除`|β|²`得`||U_Y(t)||²≤C√Y`，包括t=0的mixed limit。
对Cc∞原源，hat f∈L¹，因此

    D_Y f=(2π)^(-1)∫hat f(t)U_Y(t)dt                           (24)

是真正Bochner integral。它不是先把`hat f/β`放进A_Y的L²系数域，
所以(22)不能否决(24)。这里的U_Y恰是原uncompleted Eisenstein系列的
`Re s=3/4`同对象kernel，并非仅因norm缺失而虚构的逆映射。

### 9.2 完整双频公式给全部L²的有界延拓

把(1)除`β(t)barβ(r)`，a=logY/2，得到

    J_Y(t,r)
      =[m(t)bar m(r)Y^(−1/2)e^(ia(t−r))
                         −Y^(1/2)e^(−ia(t−r))]/[−1/2+i(t−r)/2]
       +[m(t)e^(ia(t+r))−bar m(r)e^(−ia(t+r))]/[i(t+r)/2]。      (25)

第二行在r=−t因m共轭关系removable；不能独立删mixed项。
第一行是两项Cauchy convolution的bounded乘子/phase夹心。
`PV 1/t`的卷积Fourier multiplier为`−iπ sgn`，norm为π；
`1/[−1/2+it/2]=−2/(1−it)`的卷积multiplier是一个指数半线函数，
其L∞ norm为4π。这两个事实也可由`∫₀∞e^(−x)e^(itx)dx=1/(1−it)`
及symmetric principal-value Fourier积分直接支付。
具体地，后一核的Fourier transform为`−4πe^(−ξ)1_(ξ>0)`；
前者可用Abel核`e^(−ε|t|)/t`：半线sin积分的x导数为
`ε/(ε²+x²)`，从x=0积分得`arctan(x/ε)`，ε↓0得所述sgn乘子。
因而这些是整个L²的费用，而不是仅compact频段的上界。
第二行的每项是reflection后的Hilbert transform与bounded m/phase夹心，
两项总norm≤4πM₀。于是(25)在全L²频率上的operator norm≤

    4π[√Y+Y^(−1/2)M₀²+M₀]。

先对smooth compact频系数使用原Gram和上述PV分解。
令`x=t+r`，mixed numerator N满足`N(t,−t)=m(t)−bar m(−t)=0`；
因此`N·PV(1/x)`是原removable quotient的普通函数。
若用同一boundary-value正则化，可能的δ(x)项也乘这个零系数相消；
不能对两项各选不同prescription再保留一个伪δ响应。
phase、reflection、bounded m的norm夹心无需m导数的全局上界。
由密度延拓，完整Gram算子在整个L²仍bounded且positive。
原单位化频系数`u=hat f/√(2π)`给能量factor`1/(2π)`，
所以上述`4π`费用须再除`2π`，严格得

    ||D_Y f||²≤B_Y²||f||²，
    B_Y²=2[√Y+Y^(−1/2)M₀²+M₀]，  f∈L²(R)。                 (26)

故频率cutoff由Cauchy性在H中定义全L²的强极限；
Cc∞源的该极限与(24)Bochner相同，再限制到所有原L²(I_L)/Dlog。
这是真正原norm运输，fixedY常数不依赖L；它没有inverse频权的空域障碍。
此处不能要求对每个L²源绝对Bochner收敛，但强L²延拓合法。
全频误差也明示：

    ||D_Y f−D_(Y,≤T)f||
       ≤B_Y[(2π)^(-1)∫_(|t|>T)|hat f(t)|²dt]^(1/2)，
       ≤B_Y[ (2π log(2+T))^(-1)
                   ∫log(2+|t|)|hat f(t)|²dt ]^(1/2)， f∈Dlog。 (27)

这是source-dependent尾及Dlog图norm误差，不是L² unit ball的uniform小误差。
有限频率D_(Y,≤T)为HS；下文D₂非紧，因此此近似不可能在L² operator norm趋0。

### 9.3 不同组织：incomplete Eisenstein与exact polar rank one

令

    g_f(y)=y^(3/4)f(−logy/2)，
    P(g_f)(z)=Σ_(Γ∞\Γ) g_f(Im γz)，
    G_f(w)=∫₀∞g_f(y)y^(−w)dy/y
           =2∫ f(u)e^(2(w−3/4)u)du。

对smooth compact f，G在vertical strip上Schwartz。
在`Re w=c>1`的Mellin inversion可逐项unfold；
移到`Re w=3/4`只跨`Res_(w=1)E(z,w)=3/π`。
该strip其他位置regular，因为ζ(2w)的实部>1，无需RH。
沿`w=3/4−it/2`向上方向对应t从+∞到−∞；
`G(w)=2hat f(t)`，dw和方向产生factor1/(4π)，不是1/(2π)。
结合G的2因子，得到准确原(24)系数：

    D_∞ f=P(g_f)−k(f)·1，
    k(f)=(3/π)G_f(1)=(6/π)∫ f(u)e^(u/2)du。                  (28)

移线可先在任意compact-height fundamental domain的L²进行。
该strip的classical norm及Euler/Γ比值给vertical polynomial界，
乘G的Schwartz尾使水平边趋0；再用下一段H界延拓。
并未把untruncated单个E(w)误当H向量。

g支持`[e^(−2L),e^(2L)]`。标准fundamental domain有`y≥y₀=√3/2`。
height进入该band时，`|c|≤e^L/√y₀`且在`y≤e^(2L)`上
`|d|≤e^(2L)+e^L/(2√y₀)`；忽略coprime及±同一类只增大计数。
因此finite overlap可取

    N_L=[2ceil(e^L/√y₀)+1]
        [2ceil(e^(2L)+e^L/(2√y₀))+1]。

若`y>e^(2L)`，identity height大于上界，非identity的
`Imγz≤1/(c²y)<e^(−2L)`，故P(g)=0。
按Cauchy及unfolding，全部complex f的原norm费用为

    ||P(g_f)||²≤N_L∫₀∞|g_f(y)|²dy/y²
              =2N_L∫_(−L)^L e^(−u)|f(u)|²du
              ≤2N_L e^L||f||²。                                (29)

constant函数的H范数为`√(π/3)`，所以(28)也给一个独立的有限固定窗界

    ||D_∞f||≤[√(2N_L e^L)
                   +(6/π)√(π/3)√(2sinhL)]||f||。             (30)

(30)粗费随L增长，不能宣称成长uniform；(26)对fixedY的更强界来自完整mixed Gram，
不与此粗全cusp式矛盾，且不能把(30)非最优粗费读成source norm的必要成长损失。
令P_Y在H中正交删除y>Y的constant x模式，它是contraction。
逐参数截断与Bochner/polar移线给

    D_Y f=P_Y D_∞ f，                                         (31)

先smooth compact，后用(26)/(29)–(30)密度延拓到全原L²。
原rank-one k正是几何w=1 residue来源；它不自动等于actual Weil的dual pole型。

U的完整cusp constant packet为

    c_(D,f)(y)=y^(3/4)f(−logy/2)
                    +y^(1/4)[m(D)f](logy/2)。                 (32)

m(D)为原L²上bounded Fourier multiplier；(32)与(28)的constant mode一致。
故完整扣除依旧严格给全部physical source

    ||D_Y f||²−∫₂^Y|c_(D,f)(y)|²dy/y²=||D₂ f||²。             (33)

但是此D₂与completed A₂不同，不能把A₂的trace-class结论偷移过来。

### 9.4 Direct base2确非紧，但成长窗有无穷源核

标准fundamental domain中所有orbit height≤y。
若seed仅支持y>1，则在domain的y≤1部分为0，在y>1 cusp只identity能贡献，
因为任何c≠0的height≤1/y<1。因此P(g)=g(y)的rectangular cusp函数。

对任意L>0，取非零source支持
`u∈(−min(L,log2/2),0)`且`k(f)=0`。
其seed支持`1<y<2`，(28)/(31)直接给

    D₂f=P(g_f)，  ||D₂f||²=2∫e^(−u)|f(u)|²du≥2||f||²。      (34)

这一subspace infinite-dimensional，正交序列的image有正norm底；
因此D₂不是compact。这是实际escape：directβ剥除确能恢复非紧几何响应，
先逆权source空域不能把它排掉。

另一方面，当`L>log2/2`，取source支持`u∈(−L,−log2/2)`且`k(f)=0`。
其seed全部支持y>2，P(g)全部是y>2的constant mode，
故base2完整扣除给

    D₂f=0。                                                    (35)

这也是无穷维全部complex合法source空间，可取其中Cc∞/Dlog源。
因此direct fullcusp余项在成长窗上仍不是whole-source frame，
finite rank bounded修复或有限个L²条件不能删除这一个无穷维source核。
它不由(35)推出Q负，也不排在实际危险core上D₂可能提供新信息。
若保Y≥e^(2L)，此特定高cusp源的P(g)可以留在截断Gram中；
但按(33)扣完整band费用后又回D₂，所以保留它的费用不能无声删去。

## 10. 准入净状态与停止/重新准入

已支付的是：samephysical complex L²/Dlog的完整双尾Bochner/极化、
hyperbolic原norm规范、HS/compact smoothing费用、全部cusp扣除后的exact A₂余项，
及无临界零点除法的actualβ双尾两侧界和(22)全source inverse-domain费用。
同时必须消费其真实direct逃逸：(23)–(33)支付剥β的full-frequency原L²有界运输，
(34)证其非紧，(35)只排成长窗fullcusp base2的whole frame。
不是 finite matrix PASS，也不是whole Weil正性。
全源norm底、actualQ signed/core桥、成长正性和Ξ识别仍未付。
特别是(26)已经给fixedY的全L²、uniform L上norm运输，
不再将其upper source norm标记为成长前件；未付的是whole frame与actualQ joint箭头。

最强旧016 graph/profile、028 negative trace及543 cofinal `1+C e^S`
没有被(11)–(17)改善。新source存在不等于净whole谱输入。
这里的compactness/inverse及direct cusp-kernel门属于明确候选的source范围，
不作完整几何方法类边界。不能以inverse空域否决已由direct kernel支付的同norm运输。
原件恢复、标准HS推导与generic strip-uncertainty工具是零轮输入；
actualβ全source费用若在最强旧资产扣除后仍是新完整准入结果，
由root决定是否结算一次合同研究轮，本代理不从文件/证明数量消费cadence。

建议C016若另两审没有找到新的actual joint comparison，对该正Gram到actualQ的准入停止，
不盲增频率/N/精度、不再借等价Hilbert酉化或源修正恢复norm。
重新准入须在已支付direct非紧运输上另给新的signed/core sameobject比较，
同样保fullΓ、全部pp、两套pole的明确比较与joint成长误差；
单纯换Y或finite rank不付(35)与joint桥；普通bounded频权的适用对象须明示，
不得把completed A的紧性套到direct D的非紧source上。
瓶颈改变在于两种运输的source norm都已付并区分，direct非紧逃逸确实存在；
整体成长signed/PSD/Ξ瓶颈没有缩小，宏观Goal仍须由root现场保持其真实active状态。
