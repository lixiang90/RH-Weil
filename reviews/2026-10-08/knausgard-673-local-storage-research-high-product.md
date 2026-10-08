# 2610.08965v1：八点局部能量、storage 与严格小规模诊断

2026-10-08，high_product_joint。仅本研究源及忽略目录内的独立诊断；不改论文附件、旧审查、Git或当前其他作者源。
本稿解释67.35%方法并证明参数方向及有限诊断的限定命题；不重放完整Lean、大搜索或全核表，不登记新比例。

## 1. 版本、已读范围与真实不等式

固定 [arXiv v1](https://arxiv.org/abs/2610.08965v1)，本地根 tmp/pdfs/knausgard-2610-08965-v1/。
原 source.tar 为4746279字节，raw SHA256 60fb628fb12bdc1ca28d6e849ce9180e9fbcc8b482021bb62d2c92b7827ac3cb。
全文读Simple673的Defs/Spec、Local Checker/Model/Bridge/Spot/SpotChecks、Kernel Compute/Sound/Deriv/Table，
以及Transfer Tables/Potential/Sums/Main；Checker此前输出截断的430–515段另读补全。
另读论文八点local/Gram定理和line-ceiling命题的完整statement与proof；没有宣称本轮全文重读2584行论文。
以下个别原源身份是canonical UTF-8 LF，不裁trim或EOF：

| 原路径（以下Lean相对于anc/lean/Simple673/） | 行数 / LF字节 | SHA256 |
|---|---|---|
| Defs.lean | 141 / 6888 | 66fc20485be736401c9f735e993e284ed5f711b2ea5b488f02b109d95266c17c |
| Local/Checker.lean | 567 / 26866 | b01a26d0b2263757d22c473c51091d9d2a2781e95ce5067531d5453231a20cf6 |
| Local/Bridge.lean | 195 / 8250 | d42b955e389961540ed1d29ba2b0d7a5452588d377a3a1972d2ab4ae5a5e776e |
| Kernel/Compute.lean | 84 / 4151 | e0764a84182545ce3efa393c3552c27233e59ed8803d1e8c40a84615a43752e3 |
| Kernel/Sound.lean | 175 / 7631 | e883ff21ecbb6aa2f3fc3062f9252e6d25d7849571a62f615e84216d334ed294 |
| Transfer/Potential.lean | 118 / 4973 | f4194541090dd60985e5136fa54e1735faf4c1af435e597350f29263aeeb3196 |
| Transfer/Sums.lean | 321 / 15795 | cb2819690d6a0ecd78f8f8077fd0315df7885f696ed15563abfac227ade49c92 |
| Transfer/Main.lean | 391 / 20484 | 8e382b94b6c8452d837882151c57551530259e34aedaab40b448b63f6669bc0c |
| anc/certificate_line/build_kernel.py | 50 / 2717 | 7b4a1262c46c289c808e792d271f5a4e8b3350b733930c953d62370273b6eadc |
| anc/certificate_line/inputs.json | 499 / 6221 | 9f480bd9849cb083325a0ee64deda33faef421fb986a402c0d2206faf4a24ed9 |

原窗 f=1+Σ_(j=1..10)a_jcos(2πju) 在I=[−1/2,1/2]，外置零，∫f=1、f>0；
K=f̂实偶，K(t)=sinc(t)+Σa_j[sinc(t−j)+sinc(t+j)]/2，sinc(t)=sin(πt)/(πt)。
八点 y₀<…<y₇、七gap g_r≥θ=17/20，局部证书准确是
\[
 x\le\alpha\sum_{r=0}^6g_r+
       \sum_{0\le i<j\le7}W_{ij}K(y_j-y_i)^2+\sum_{r=0}^6B_r(g_r).
 \tag{1}
\]
α=627/10⁶、x=8722/10⁶。此673命题没有labels；general checker保留256编码和三类表，但三份完全相同。
不同κ_i分配在这里仅通过Σκ_i=x出现；改变奖励位置本身不是优化自由度。

## 2. 点对预算与storage为何有效

W≥0，按index distance s的预算 Σ_iW_(i,i+s)≤2；原七个整数预算为
1999996、1999998、1999998、1999998、1999999、2000000、2000000（单位10⁻⁶）。
把连续八点frame沿链滑动，固定真实点对在所有frame中的总权≤2，准确不超过两个ordered pair的能量。
因此不能统一放大W；可重分配其位置，但必须保留每个distance的完整预算。
B_r为14个等距knots上的分段线性函数，knots=3/4+k/8，外为0；逐k有Σ_rB_r(knot)=0，
共同hat插值故给所有实t的Σ_rB_r(t)=0。令 A_q=Σ_(r≤q)B_r，q=0,…,5，
\[
 \Phi(g_0,\ldots,g_5)=\sum_{q=0}^5A_q(g_q),\qquad
 \sum_{r=0}^6B_r(g_r)=\Phi(g_0,\ldots,g_5)-\Phi(g_1,\ldots,g_6).
 \tag{2}
\]
任意有限链的所有storage项准确为首状态减末状态，不要求周期或端点相同。
hat权非负且和≤1，partial knot maxima/minima为
(647,647,222,425,0,0)与(0,0,−425,−222,−647,−647)，所以状态oscillation≤Ω=3882/10⁶。
整链只付Ω，而非每frame付Ω；七个未奖励端点另付7x。pressure每gap至多出现7次。
若e_ij≥K²−ε且e≥0，至多14个range7 ordered邻居/点，准确得到
\[
 \sum_{i\ne j}e_{ij}\ge x m-7\alpha\,\operatorname{span}(Y)
          -(7x+\Omega)-14\varepsilon m,\qquad7x+\Omega=8117/125000.
 \tag{3}
\]
storage不是降低零侧能量常数C(f)的直接项，而是搬运各局部frame的正负余量，令更大x/更小pressure可能成立。
缩小Ω仅减少有限端点误差；在原固定证书下不会直接改渐近比例。

## 3. 全连续gap域如何由有限计算覆盖

H=16384、V=2²⁸、R=262143。u_r=Hg_r始终是实变量，不把真实gap舍入成整数样本。
root=[13926,R]⁷覆盖g≥17/20且Σu≤R，13926/H略小于θ；
Σu≥R由pressure单独付款：ΣB≥−1294/10⁶、W K²≥0，且
\[
 \frac{x+1294/10^6}{\alpha}=\frac{10016}{627}<R/H.
 \tag{4}
\]
大frame域没有截掉；clamp仅删除已付Σu>R部分，soundness逐实点证明每次clamp和两半split保覆盖。
核表每项是整个闭cell [k/H,(k+1)/H] 的lower bound，而非midpoint value。
在midpoint t₀=(2k+1)/(2H)，有精确有理Q(t₀)、Q′(t₀)和sin/cos外向Taylor包络，
K=(sinπt₀/π)Q、K′=cosπt₀Q+(sinπt₀/π)Q′；t₀非整数，分式没有整数pole。
f≥0、∫f=1给|K′|≤π、|K′′|≤π²。h=1/(2H)时，对整个cell，
\[
 |K(t)|\ge[\,\ell-h\min(\pi,D+\pi^2h)\,]_+,\quad
 \mathrm{tab}[k]=\lfloor V[\,\ell-h\min(\pi,D+\pi^2h)\,]_+^2\rfloor.
 \tag{5}
\]
因此整数endpoint、K的零点与cell内部都被包括。读越表为0仍安全；表到16已覆盖所有未由pressure支付的距离。
box第一test取28个pair-distance全cell range minima、7个potential endpoint/knot minima与lower-corner pressure；
第二test构造整个edge上的affine下支撑，将28条slope准确加到七gap系数，再按系数符号取box端点。
宽度≤1但未付不能默认为通过；它是fail。最终接受的是全连续七维域，不是成功搜索若干代表构型。
原全搜索的535m节点只是作者记录；本轮没有重跑。native计算信任边界沿用已冻结审查，不声称纯kernel或新数学公理。

## 4. 真正可优化的方向和可证明的无效方向

零侧C₀=6639737/5000000，局部证书经原separated Gram/clipping2桥给
\[
 q_0=\frac{2-C_0-7\alpha}{1-x}=\frac{1669159}{2478195}.
 \tag{6}
\]
这是通过提高Gram能量下界改进计数；新窗的plain bound 2−C₀=.6720526本身较弱。
相对旧.6734824的增量准确为34570933/619548750000≈.00005580018，即约.005580018个百分点。
固定window且新证书保持全域、close-pair x′≤β及1−x′>0时，有限参数变化准确满足
\[
 q'-q_0=\frac{q_0\delta x-7\delta\alpha-\delta C}{1-x-\delta x}.
 \tag{7}
\]
现点的∂q/∂x≈.67946449、∂q/∂α≈−7.0615912。提高reward/减少pressure须重新证全连续域，不能只看spot余量。
共同衰减(x,α,W,B)↦λ(x,α,W,B)，0≤λ≤1，继承(1)和pair budgets；但
q(λ)′=[x(2−C₀)−7α]/(1−λx)²>0，分子3681606943/2500000000000。
所以共同衰减不能超过原结果。另一个无须重搜索的方向δα≥0、δx=7θδα由Σg≥7θ保持局部式，
但(7)的gain numerator为δα(7θq₀−7)<0，因此也不能改进比例。
有意义的自由度是window与C、W位置分配、α/x联合、potential knots或多gap storage、interaction range及θ/majorant联合。
其中改变window必须同时重付kernel全cells、f正性/归一化、continuous majorant、close pairs、零侧C，而不只优化浮点LP。
论文line-ceiling对固定此window、所有range7 pair certificates证明上限<.67357；
当前.67353820已接近它。这个限制不是对其他window、range或ζ真实比例的上限。

## 5. 本轮独立小规模有理诊断：精确结论及限度

诊断位置：[script](../../tmp/pdfs/knausgard-673-local-storage-high-product/diagnostic.py)、
[output](../../tmp/pdfs/knausgard-673-local-storage-high-product/diagnostic.json)，均在既有忽略根tmp/pdfs。
script226行/9635 LF字节/SHA7bf456e2ed02039fd950514ae819a38011a756db865db8ef15ea16387d1cb77b；
JSON1317行/20941 LF字节/SHAa84505e1fc0259a57fb64116745d72544d3c5b7207748d35097691f1dae0ee13。
FULL READ最终script后实跑 C:\Python312\python.exe −B −X utf8：exit0，随后FULL READ完整JSON。
原50行build_kernel.py也全文读；因其顶层直接重建全表并写输入，未import或执行它。
独立Fraction实现只重算四box实际用的411个cells、389个trig midpoint，全部与原bin匹配；
Machinπ有理包络、10/11项sin/cos、2⁻⁷⁰外向rounding及(5)全保留，不以checksum代替这些cells的数学核验。
只读bin为1048576字节，SHAe32c430de69dd92adbfbdb9935a9983eb7e033113c2c87c2a763f549e4401e0a；
没有重算其余261733个cells，没有Lean重放、535m搜索或修改upstream。
由每个pair的全closed-cell lower bound和piecewise potential minima，四个原SpotChecks连续box的严格余量为：

| box | exact lower margin | 显示值 |
|---|---|---|
| trial | 510068977/67108864000000 | 7.60062005×10⁻⁶ |
| second_trial | 502341841/53687091200000 | 9.35684593×10⁻⁶ |
| corner | 44978824395589/268435456000000 | .167559178 |
| tightest | 225441149/268435456000000 | 8.39833725×10⁻⁷ |

这证明各box全连续域，不证明未覆盖域。最紧box的此range-min测试不能认证reward再增10⁻⁶；
这不是“不等式被反例推翻”，因为lower enclosure不足并不等于实际slack为负。
还以K(m)=a_m/2（1≤m≤10）、K(m)=0（integer m>10）精确算95个period≤5、gap∈{1,2,3}的range7周期能量。
任何同K证书必须有x n−bP≤e_period，storage在M-period链除M后严格消失，无zero-distribution假设。
两条period (1,2)、(1,1,2) 的(n,P,e)为
(2,3,17666086973/2000000000000)、(3,4,34707431173/2000000000000)。
令t=1/(1−x)、z=b/(1−x)，必要式是(n−e)t−Pz≤n；目标为(2−C₀)t−z。
将这两式以正权合成即可得upper1327688598573/1966542054373≈.675138676：
取λ₂=[3(2−C₀)−(2−e₁)]/[1+4e₁−3e₂]、λ₁=(1−4λ₂)/3，均正，目标≤2λ₁+3λ₂。
脚本Fraction vertex检查同一relaxation及其余93状态，得到这个值；不是可实现的local证书或新ζ下界。
它远弱于论文近整数rational periodic states的.67357限制，说明仅integer-grid构型会误判优化空间。
下一步应围绕真实near-integer周期构型联合优化window/pressure/storage并出全域证书，或研究更长range与lossless close-pair转移。
本稿可复用连续包络、storage有限端点和参数方向；不将局部PASS或必要条件LP变成新比例。
