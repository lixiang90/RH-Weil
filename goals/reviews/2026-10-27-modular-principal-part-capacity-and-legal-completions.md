# 有限主部模输入的全源容量与合法完成化

2026-10-27；执行STATE唯一下一比较，同G20261027／原0c4f冻结基线。上一Goal启动和同步已实际完成，本轮root get_goal仍为同createdAt1793085111的active实例；工作树起点0359653 clean。三独占稿为[实际模过滤](../../reviews/2026-10-27/modular-capacity/modular-filtration.md)、[Baire／Gram与原费](../../reviews/2026-10-27/modular-capacity/baire-factorization.md)、[最强旧与逃逸](../../reviews/2026-10-27/modular-capacity/old-net-and-escapes.md)。

## 1. 结论与本次实际信息差

固定格、weight和Weil表示的honest weakly holomorphic输入，确为闭有限维pole层的可数并。整个fixed-window Fréchet源若连续线性地映入这个目标，其像必须落在同一个有限pole层。更强的是：精确恢复537窗全部正Gram甚至不需要Baire；源的Hamel维数不可数、目标至多可数，任意复线性map已有非零核。

这定位了**直接把任意平滑源送入一个honest有限主部输入，再只经该输入恢复完整Weil型**的类型限制。它不是经典独立正性，也不是Borcherds／Weil几何总体失败。真函数域本来用连续y-family；逐层正逼近和完成化同样可合法绕过。

本轮新增的是实际目标类型与已知障碍的对齐和选择信息。标准维数/Baire、537正定和552高频是旧输入；无新独立算术、费用或whole净后果，按0数学轮消费，不建C046，不把一次输入接口诊断升级为宏观完成。

## 2. 实际目标：不先假设LF拓扑

唯一原始论文仍为[Borcherds作者稿](https://math.berkeley.edu/~reb/papers/aut/aut.pdf)，本地SHA为93618b64a0c07f68a085b0b520079b1062a98ff7672159f34f77b1463e0724d2。实际核§2、§4有限表示及§13输入；没有串新论文。§4的ρ_M经有限群／其double cover分解，half-integral weight保原Mp automorphy。

先把整数principal-part输入放入复线性包络H=M_k^!(ρ)。这只放大容量，不把任意complex输入说成原乘积定理已许可的整输入。F在H内必须全纯，只在cusps亚纯；输出Ψ的内部divisor不能反向搬成输入可移动pole。

对ρ(T)的有限个特征指数0≤α<1，写Fλ=q^αλΣ_n aλ(n)q^n，令H_N为全部n<−N系数零的子空间。则H=∪_N H_N。乘Δ^N将H_N单射入固定weight k+12N的holomorphic-cusp空间。后者的fundamental-domain sup由有限height横截线和cusp最大模控制；Montel紧开收敛与同一最大模控制给supnorm单位球紧，标准Riesz结论遂给有限维。详细证明保所有分量、半权和多cusp，见原稿。

给H以Hol(上半平面,V)的紧开子空间拓扑，它已是Hausdorff，有限维H_N因此闭。不需额外假设H完整／Baire，也不需先将更强的inductive-limit拓扑与紧开拓扑等同。标量II_(2,2)、k0控制为H_N=span{1,J,…,J^N}、dim=N+1、H=C[j]；用J的简单cusp pole逐阶消主部，余项在紧化上全纯而为常数即可。

同SHA作者PDF内部含2018补注，因此首页1997日期只能称首页标注，不可当整个文件最后修订日。此处§4表示及§13 p=1输入消费不受该内部补注影响；文献元数据追加说明，不静默改动数学结论。

## 3. 源与两级容量限制

固定具有非空内部的K⊂(−17/16,17/16)，源E=C_K∞(R;C)取固定支持Fréchet拓扑；双pole矩零子空间E0为其中闭子空间，两者均Baire。537已给完整Qζ(r)≥τ||r||du²，τ=2^−49162；此处不外推成长窗。

若复线性J:E→H连续，则E=∪_N J^−1(H_N)是闭线性子空间的可数并。Baire给一层有内点，该层因此等于E，于是J(E)⊂H_N0。N0可依赖J、K；不是所有map的共同N，不是成长费用估计。只给逐负Fourier系数连续也可直接核闭逆像，但不能由map名称领取连续性。

精确全Gram的代数门更早出现：取χ在K内某开区间非零，χ(u)e^(tu)、t∈R不可数线性独立，有限组由Vandermonde即可核。Hamel维E不可数、H至多可数，任意复线性J均非单射；对E0可先施compact上单射的D²−1/4，结论相同。若Bζ(r,s)=G(Jr,Js)，或仅Qζ(r)=q(Jr)且q(0)=0，非零kerJ源与537严格正定矛盾。目标G不必正，也不必连续。

因此取消连续性只可能逃过“统一有限pole层”，不能救完整analytic源到该可数Hamel目标的精确线性因子化。可数稠密整数／有理源与其全源完成是不同对象，不能合并。

## 4. 原norm与系数方向

仅由Q≥τdu²和每个J的非零核，不能推出所有J共有的Hlog误差下限，du／Hlog并不等价。本项目另有552的完整Γ高频主项，才能得到更强的旧合成。

对rank d的任意线性J，选d+1个互不交支持的光滑profiles，以−t^−2(D²−1/4)(e^(itu)φ_j)归一化。它们支撑不变、du正交、精确双polezero。每个t在d+1维span内选J核的单位向量r_t。有限profile空间的Schwartz半范数一致可控，actualΓ渐近和全部fixed窗prime-shift给

\[
 Jr_t=0,\quad\|r_t\|_{du}=1,\quad
 Q_\zeta(r_t)=\log|t|+O_J(1),\quad
 \|r_t\|_{H_{\log}}^2=\log|t|+O_J(1).
\]

Hlog仍为原zero-extension规范，Fourier因子1/(2π)、weight 1+log(2+|ξ|)。prime powers不删；pole在本源上实际为零。故只读J且零数据给0的q满足

\[
 \sup_{r\ne0}\frac{|Q_\zeta(r)-q(Jr)|}{\|r\|_{H_{\log}}^2}\ge1.
\]

这是552高频机制与有限核的标准消费，不是新Γ费用。它否定精确身份、统一双侧Hlog小误差或上侧Qζ≤q(Jr)+δ||r||Hlog²、δ<1；**不否定**正性证明可使用的下侧Qζ≥q(Jr)−ε||r||Hlog²。下侧仍须独立证明signed残差的符号，核论证既未付款，也未排除它。

## 5. 实际合法修复与未付箭头

**真函数域。** 旧567给B_y(r)=Σ_j r(y+jℓ)E_(j+j0)，Q_C(r)=ℓ∫_0^ℓ||B_y(r)||²dy。每个fiber只有有限组合，whole目标却是连续y-family／L²完成，Hamel维不可数。有限H1、可数正交基、separable与可数Hamel维不能混同。所有aliases、returns和H0/H2身份仍保留。

**有限秩逐源逼近。** 在537已付正窗Q-Hilbert完成中取源内正交基和前N维投影P_N，G_N(r,s)=Bζ(P_Nr,P_Ns)正且对每个r,s趋Bζ，但每层相对Q的uniform误差=1。它可用complexified多项式坐标表示，却未给Borcherds整输入或nativeheight。该例仅证明逐源逼近合法；构造使用已知fixed窗B，不是经典全域独立正来源。P_N也不自动给平移不变分布W_N。

**正分布弱极限。** 旧576／577的独立正Γ背景可用对称正中点cos求积在S′／D′逼近；finite-rank与逐层Radon不妨碍该极限。它不是完整Wζ。正D′路线中间层不须精确消noncompact405；完整signed缺陷消失仍须独立支付。

**不读Q的完成化实物。** 对compact源令

\[
 L_r(z)=\int r(u)e^{zu}du,\qquad F_r(\tau)=L_r(j(\tau)).
\]

Laplace唯一性与j的非恒定开映射给连续注入，且对compact A有

\[
 \sup_{z\in A}|L_r(z)|\le\sqrt{2L}
 e^{L\sup_A|\Re z|}\|r\|_{du},\qquad\operatorname{supp}r\subset[-L,L].
\]

非零compact r的L_r(it)为Schwartz衰减，故L_r不能是非零多项式，F_r在cusp为essential，离开honest有限主部域。它真实绕过rank门并保源；现有compact-open原du费用upper含exp(L|Re j|)，尚未支付uniform height费，不能单凭这个upper宣称必要增长。原Thm13.3的product／principal／Green延拓尚无。这个标准修复不是独立Weil正性，也不证明noncompactPan和完整mixed预算已闭。

先整／有理几何再完成、移动载体／表示、真正非线性源map与不同relative配对仍须按实际对象另核，不能被本门一并否定。

## 6. 与最强旧结果的净比较

580已经核指定finite通道的全Pan张满与537正盲源；本轮把任意固定honest模目标的连续map化为有限rank，末端仍是旧核机制。553的全线bounded消Pan迫零是另一原域，不能直接替代fixed-K容量门。552完整Γ高频支付本轮统一Hlog误差方向；有限截断、强源和成长量词保持其原范围。

本次没有实际r→合法几何primitive、principal／Green transgression、独立mixedRR或新的signed下界。最强whole仍542+555→557 leading4/5负惯性UPPER；actualq/core/coupling/Ξ及宏观完成门未改变。类型纠正有价值，但不能因“任意poleorder”措辞重新计旧机制。

## 7. 停止与接下来的准入

停止本single-input/Baire/poleorder容量诊断，不开C046，不继续换weight、level或paper。下一只使用已给的具体完成化F_r=L_r(j)做最便宜截断／lift比较：由cusp轮廓积分求其Fourier常数与各负系数的source核、原费用及有限主部截断，检这些截断的实际Green／relative输出和全尾能否运输405真实Pan／537。非零compact源已被证明不属原Thm13.3 honest域，不再重查该membership；若只是再次得出essential／原域不合法，立即按旧推论止，只有新的截断尾／relative接入信息才可晋级。若仍只有保源而无actualprincipal／Green运输，原recipe止，不把essential完成化名称当新独立容量。

此动作有实际公式、可判的常数／输入门，区别于重复CR或未知J；尚未执行，不能当已证结果。更高优先级的新signed残差或同对象family/transgression实物若出现，先按宏观复盘改策。

## 8. Root消费范围

实际object/norm/domain为fixed-K physical E／E0及完整Bζ、原du／Hlog，和fixed-data复包络H而非原整输入本身。映射J是被测试的假设，不是已构造的算术资产；其缺失不妨碍条件容量命题，但不能据此领取principal/coverage。各误差、极限、符号与合法逃逸见上述段及三原稿；source投影不代geometric乘法，正Γ背景不代全Wζ。

root已实际核读三稿及[fresh修后限定PASS](../../reviews/2026-10-27/modular-capacity/fresh-review.md)，height-upper与下一准入guard修订后前件范围闭合。按标准接口／旧推论0轮结算，未新增notes/583或数学合同。既有5完整轮578–582和连续来源停止触发提前cycle16宏观审视，复盘本身0轮，仅在完成后消费原cadence5→0一次；不再新增轮数。
