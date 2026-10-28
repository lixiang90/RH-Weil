# Möbius Green 响应：独立定义域与强旧范围审查

2026-10-29；限定 **PASS**，无必须修项。审查者不同于两原稿作者；本稿仅核当前已经形成的响应、普通临界L²域比较及消费范围，不创建数学合同／计轮／改原件，不代替root最终消费。

## 1. 当前冻结版本

均按UTF-8规范LF计字节及SHA256，同目录文件如下。

| 原件 | LF bytes | SHA256 |
|---|---:|---|
| root-formula-and-admission-test.md | 3037 | d78e03dff73ee0eee6132b87eb2f1cf502c9e2ca898a816d6da3c188cba4539e |
| root-critical-domain-and-role-draft.md | 5845 | c99d6da97e5fbd00ef6c5138d7973864cfcea2ba140cd5aeab6764e86d54a970 |
| domain-and-critical-energy-test.md | 10389 | 292706a8ada9b4aed8960cd1003c0bfd0980446c958a8b958262a24acb028ac1 |
| strongest-old-and-principal-scope.md | 13383 | 764717bf80a2d7e491fe074526169eb962a7cc7cc77133dc7e2d5812097bbc11 |

已读四件全文并独立重算下列核心链；来源接口核405的E／次数／完整B、518§§4–6、519闭像与源作用、520实际Jordan、522增长合同、525原响应／临界量词／pole及Gaussian端点、526忠实多权与退化，另核080–082所用对象和NB residual角色。这里不重新认证上述旧文所有无关证明或外部原论文。

## 2. 源、因子、域和范数：PASS

固定bare f∈S_exp,C及physical r(u)=e^(u/2)f(u)。给定实际μ系数的响应为

    V_r(t)=Σ μ(n)n^(−1/2)r(log n−t)
          =2e^(−t/2)θ_f(e^(−t))
          =2e^(−t/2)W_f(e^t)。

前一逆就是518(11)，后一W就是525(1)，不是新算术源。S_exp的全部固定指数半范数保证各紧t区间上各导数绝对一致收敛；对compact r局部有限。负t端任意指数衰减、正t端粗界O(e^(t/2))可由n在e^t两侧分开求和直接取得。乘e^(u/2)是Fréchet自同构，不提供原du／Dlog共同有界范数。

405真实Eη=2Ση(ne^u)含正负整数；按mn分组时Σd(k)k^(−N)<∞支付固定t的双和，得到

    V_(e^(u/2)Eη)(t)=2e^(−t/2)η(e^(−t))，
    ||V||²_(L²(dt))=4∫₀∞|η(x)|²dx=2||η||²_(L²(R))。

后一式仅用x=e^(−t)及η偶性。η(0)=0和偶性给正时间O(e^(−5t/2))，Schwartz给负时间尾；不把源零积分误作目标两个次数零。519的实际闭像I=E(S_even,0)及逆连续性使此结论覆盖整个I，不只是原像稠密部分，也不只是P_an。

物理平移严格为V_(τ_a r)(t)=V_r(t+a)；bare τ_a f的physical化则多e^(a/2)。两种平移及精确范数相容，全部真实P_an及其平移均消于模L²类。对数卷积a*b=δ₀、a*V_r=check r也由实际除数消去成立，但仅在所列源域上有绝对换序，不能拿作整个L²上的有界Hilbert复形。

## 3. 非零compact源的临界L²排除：PASS

这项标准域推论的量词是每个非零r∈C_c∞,C、原始全时间未加权响应；不是RH断言。独立核算如下。

取supp r⊂[−L,L]。V_r在t<−L为0。对Re z=σ>1/2，绝对费

    (∫|r(u)|e^(σu)du) Σ n^(−σ−1/2)<∞

支付Fubini，所以F(z)=∫V_r(t)e^(−zt)dt=M_r(z)/ζ(1/2+z)，M_r(z)=∫r(u)e^(zu)du。

若V_r∈L²，因果支撑与Cauchy–Schwarz给Re z>0内全纯以及

    |F(σ+iτ)|≤||V_r||₂ e^(σL)/sqrt(2σ)，σ>0。

紧子半面上的导数也有指数余量支配。亚纯唯一性把原商身份延到右半面；ζ在s=1的极只要求F的相应零，未被当成零点障碍。开右半面内未消分母零点会给真pole，违反全纯性。边界z=iγ若有k≥1阶未消pole，则径向模下界cσ^(−k)违反上式O(σ^(−1/2))；这里没有预设H²函数在该点已有边界值。

因此L²假设要求M_r在所有z=ρ−1/2、Reρ≥1/2处消掉完整mρ重数。非零r的M_r不恒为零；compact支撑给|M_r(z)|≤||r||₁e^(L|Re z|)。在任意M_r(z*)≠0处，以2R盘的最大模控制R盘、用Jensen，零数按重数是O_r(R)。另一方面RvM的N(T)~TlogT/(2π)和保持正高度的对称ρ↦1−conjρ，给Reρ≥1/2的零点至少占N(T)/2，仍计重数。它们的z位于半径O(T)盘内，不可能全被O_r(T)个零点覆盖。故至少一个真pole未消，产生前述矛盾。

此链无需RH、简单性、零间距或中心线正比例定理；RH允许的边界poles本身仍阻止裸能量。它不否定允许增长／截断／不同norm或signed比较，更不反驳081的NB residual closure。该lemma虽不是旧文逐字命题，却是同一旧pole接口加标准Jensen/RvM/Laplace的直接组合，不付未知临界算术增长。

## 4. 商、次数及条件Jordan：PASS

ambient L²_loc/L²、或C∞/(C∞∩L²)在局部拓扑下均有稠密分母，截断给Hausdorff化为0。原稿正确限定为ambient：χV_r未被证明还在响应range，所以没有偷推restricted response商也退化。compact源映到非零代数类，不自动给Hausdorff正Hilbert primitive。

405的h=Eη₀满足c(h)=d(h)=1/4、B(h,h)=1/16，却被本模L²类消掉；故仅凭此类不能承载全部源的完整B。这个B数值属于405 bare归一化，原稿没有无换算冒作另一个physical Q的数值。外加d/c只能补回旧次数信息，405(14)的C²×(S_exp/I)已有这个解析分裂，并未因此得到principal、section或mixed RR。

条件左Jordan警告也成立。若存在Reρ₀<1/2的真实非平凡零点，520的actual u₁∈S_exp,C有M_(u₁)=H₀/(s−ρ₀)、[u₁]_I≠0。H₀=ξ/2=s(s−1)π^(−s/2)Γ(s/2)ζ(s)/4，故

    M_(u₁)(s)/ζ(s)=s(s−1)π^(−s/2)Γ(s/2)/(4(s−ρ₀))。

初始Re s>1线移到Re s=1/2不跨pole；s=1不是pole，Gamma负偶pole亦在左边。固定条带上的Gamma指数衰减支付水平边，临界线上的该函数是Schwartz，逆Fourier（z=s−1/2）给V_(e^(u/2)u₁)∈L²。它与u₁∉I相容。此为条件对照，不断言离线零点存在；故不能免费认定整个响应核等于I或Pan，也没有全kernel充分性定理。

## 5. 消费方向与结算范围：PASS

最短旧链是518实际逆→525同W响应→physical半密度运输；519全像／逆连续与405次数反测已决定关系及degree角色。522原商次指数的RH强度、526忠实多权但非等价酉化／critical fixed-class退化已是更强旧设施，不能用本ambient类重新领取carrier／metric／增长预算。080实际finite Green仍保inverse内容，081/082求非compact feature/target的Schur residual与相位对齐，不是本bare compact inverse的有限能量要求。

同意限定standard old0／恢复同域停止，不建C056/593、不新增独立算术正性或关键瓶颈移除，不把标准端点推论标作新的whole定理。完整Γ/contact、proper powers、indefinite双pole仍留原完整Weil型；逆ζ公式未给完整正平方身份，537非根可见也未给新metric。Principal／整过滤／sections乘法／mixed RR、危险signed corecross及成长Ξ仍欠。Whole4/5负惯性UPPER按现前沿保持，本审未重验该旧预算。

截断／换权／非local／有费强完成／relative或higher几何及正D′逼近均不由本门否定；未排不等于已付或可自动续预算。Goal完成门没有通过，当前应由root闭合前件、保存准确old0范围并按既有授权同步，不延长本μ增长／damping／metric／source队列。

只写本审稿，无外部query/primary/PDF/下载/数值。观察唯一cadence SHA256仍为ea44d838ee01c575b03fab5a1aa3986134ee5f8e55e7fd55d7b5cbbe2eef714d，manifest仍为e0c1343bcfdb60db617aa2a84d10f7b0501fb3a16fcfc521f75299b2469fe039；未修改STATE、cadence、原稿或Git。结构check通过不充当本审数学证明。
