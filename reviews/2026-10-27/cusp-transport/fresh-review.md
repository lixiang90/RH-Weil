# C046 独立 fresh 审查

2026-10-27；审查者 `/root/cusp_fresh_review`。本稿只记录独立核查，不改 STATE、合同、cadence 或文献库；root 拥有前件消费与统一结算。已恢复 README／STATE、check→show、G20261027、C046、D20261027C 和宏观前沿，并核实际工作树。

**最终结论：限定 PASS。** 三份原稿、root583 和实际 root 消费收据均已全文核查；本结论只覆盖下列对象与量词。支持 root 将 C046 统一结算一数学轮，不支持完成长期 Goal 或声称经典独立正性／primitive RR 已获得。

## 1. 已核解析源与模截断

实际全文核读 `fourier-kernels-and-faber-tails.md`。允许全部复源 S_exp，F_r=L_r(j) 的指数是 u·j，任一目标 compact 仅需有限线性指数矩，不重新引入此前 height-transport 的双指数源尾。

轮廓核 K_n 的符号为 q^(−n−1)，故 b_m=a_(−m) 的界确为 s^m p_(A_s)，不是 s^(−m)。Cauchy 估计、微分和 Fubini 均由同一固定 q 圈的指数矩支付；源窗 du 精确 dual norm 与粗 upper 分开。原 Dlog 平方权 log(2+|t|)≥log2，使其 upper 额外乘 (log2)^(−1/2)；这不把 Dlog 与 du 等同，也不声称全线 du 连续。

Faber 生成式 −qj′/(j−z) 的导数是 q 导数。双半径重构可直接复核：取 j(q) 在小 q 圈的反向大曲线，对 entire L_r 使用 Cauchy；换元所得积分恰为 ∮F_r(q)G(q,z)dq/q，其常数项为 a0+Σ_(m≥1)b_mP_m。该式的方向、常数项和几何尾一致。整数基 J_m=q^(−m)+O(q) 的 constant 为0；真正模截断保 a0，普通负 Laurent 多项式不能代替。

固定源窗／目标 compact／两圈后有真正 operator tail；源窗、cusp height 与算术 height 成长时各常数另变，原稿没有无声交换极限。全负系数注入由重构、虚轴 Fourier 衰减和唯一性成立；有限 N 的 finite-rank 核仍是旧机制。

## 2. 已核真实关系与非根

实际全文核读 `principal-relations-and-nonroot-test.md`。A(u)=CT exp(uj)，V=A″−A/4。j=q^(−1)+744+Σc_nq^n 的非负系数给 u≥0 时 V≥(744²−1/4)e^(744u)。这仅用于正半线，负半线另以真实 H∈S_exp 的尾支付。

对405实际 p=(D²−1/4)H，a0(τ_bp)=∫H(v)V(v+b)dv 的分部积分合法。v∈[0,1] 给正项 c_H e^(744b)，v<−b 的绝对负尾给 C_N e^(−Nb)；所以全部充分大正 b 上确有严格非零和发散下界。原 du／Hlog／Dlog 平移不变，而该实际读出发散，故这里必要的全线不统一费用不是将粗 upper 反用为 lower。

537 奇源 r_*=(D²−1/4)(uφ) 的双 pole moment 精确为零。V′(0)=744³+6·744c1+3c2−186>0，足够小偶非负 φ 给 a0(r_*)>0；完整 Weil 正号只是继承原537的 fixed 窗结论，没有由新模型推得。

扣 a0 后所有负系数仍注入，故解析层保 Pan 和537。该修复移除 weight 数据，不等于处理 character／边界，也不等于在 native principal 类中保非根；原稿对此分层正确。

## 3. 已核 native 特殊身份、尺度与全尾

实际全文核读 `native-products-and-green-tail.md`；并从已存 Borcherds 作者 PDF 印刷47–50页独立核原13.3、product prefactor、log规范和split cusp例外。II_(2,2) 的 Ψ_(J_m)=C_mR_m 特殊身份可闭合：weight0在有序 SL2×SL2 上使乘子成为实际 character，两因子各 abelianization exponent12；12次方消 character。原 product 在 y1>m·y2、固定第二变量的紧集上给有限第一 cusp 阶，反向同理；generic boundary 延拓后的剩余 corner 为 codimension2，meromorphic Hartogs 适用。所得 rational ratio 在 A² 无零极除子，UFD迫它为常数；原unimodular前因子模1和monic q1^(−D_m) leading再迫 Weyl指数(−D_m,0)与|C_m|=1。此证明没有调用原 Problem16.5 的一般 Hecke 等变。椭圆点由有限商不变函数下降，不引入新的divisor重数。

Poincaré–Lelong 的顺序与尺度正确：dd^c=(i/2π)∂bar∂，dd^c log|f|²=[div f]，g_m=−log|R_m|²而native Φ_m=2g_m；principal pair 的cycle须同时乘2。R_m 在两个变量的pole degree同为D_m=σ1(m)，第二方向block的leading sign为−1，总符号为(−1)^τ(m)，不误将其总degree改成τ(m)。因此完整Z_m=Tbar_m−D_m(B1+B2)与dd^cΦ_m=−2[Z_m]一致。

原稿另付的global费用实际成立，消除了初审提出的cusp偷渡风险。|Y|=1可取共同compact reduced j-preimages，Hecke root的reduced height≤Cm；在|X|=|Y|=1上得sup|R_m|≤exp(CmD_m)，Cauchy给全部系数同界。product FS体积下正log部由系数bound和可积log^+|X|、log^+|Y|支付；负log部使用monic X逐root分解以及FS density≤1/π，给每root≤1/2的uniform积分。因此global L1≤C_XmD_m是独立已付界，包含boundary，未从interior bound直接外推。

positive Tbar_m 的FS mass为2D_m，B1+B2 mass为2，故Z_m totalvariation≤4D_m；与|b_m|≤s^m p_(A_s)合并后，在任意fixed0<s<t<1上有全global mass与balanced G的L1几何尾。dd^c只按L1→distributions连续性取极限，不声称L1→mass的一般有界算子；mass收敛是上述独立positive-cycle估计付的。fixed窗du上界与全S_exp强源上界仍分开。

完整Hecke norm的matrix gcd分解给T_m=Σ_(k²|m)T_(m/k²)^prim，原Borcherds divisor中的positive scalar倍数给同一重复，符合逐m身份。absolute mass和Σ_h d(h)s^(Nh²)<∞允许重排及平方Möbius反演。虽支持并可稠密，不同primitive curves仅在离散点相交，各自divisor trace measure对其他curve为零；绝对质量和保持这一互奇异性，所以measure restriction可以识别A_N。这里仅识别raw current；不是从dense support直接读取普通divisor系数。

有限principal pair的复span在L1×mass拓扑下的闭包商会杀掉实际极限；这在指定连续quotient中成立，未将无限pair本身称为ordinary principal divisor或单值rational function。balanced解析/current保源与这个quotient全零不冲突。仅保Tbar时剩下2D(r)B边界腿，不能默删；a0Φ0则另保weight／metric／character。**已付global L1目标严格为balanced G；固定Φ0的global L1尚未估，不并入同一norm目标。** 不同relative/higher读出没有被本特例排除。

## 4. 初步净值与结算限制

三原稿已超出上一轮 essential／Baire 的标准资格复述：有实际源核、全模尾、真实 Pan constant 下界和必要费用，并新增该整数基native lift的special normalization、global balanced Green／mass全尾及完整边界身份。新完成化设施支持root统一记一数学轮；分支数、文件数、标准finite-rank部分和恢复均不单独增轮。

强旧 whole leading4/5 仍为542+555→557的负惯性 UPPER；537 fixed 窗、552高频、553旧稠密及579–582源设施均为输入。本轮不改善 actual q／core／coupling／Ξ，不自行完成长期 Goal。

## 5. root583 与消费闭合的最终核验

实际全文核读 `notes/583-completed-modular-faber-source-and-native-green-transport.md` 及 `root-consumption-scope.json`。root 主稿保留了所有关键分层：全complex物理源和fixed源窗；fixed FS geometry 与cofinal算术height；a0Φ0独立line标签与balanced global L1目标；原整数基lift和后续复化；raw注入和continuous principal闭商；正cycle的mass估计和signed组合；A_N方向及Nk²别名；Φ=2g尺度与两条cusp边界。

root 收据逐项保 object／norm／源成长量词／paid依赖与全部误差／系数方向／关系与商角色／coverage-coupling／strongest-old净值，未把若干局部结论自动提升为完整Bζ身份。完整Γ/contact、properpowers和双pole仍是未匹配的经典责任；新m项没有被换成经典p^k。原主瓶颈未改和局部设施改变分别报告，停止本recipe的范围也未泛化到所有relative／higher／非闭或更强拓扑修复。

初审提出的两项范围风险已修复：native 全X尾另给coefficient-height及FS log积分，而非由interior compact自动外推；native和root均将未估global norm的固定Φ0留作独立标签腿。native另补了product整体趋1的normal-convergence majorant，避免逐项极限替代乘积极限。没有剩余必须阻止本范围结算的修正项。

本审查核对了 root 收据中的实际 LF SHA256，四项均相符：

| 原件 | SHA256（LF） |
|---|---|
| root583 | `babe212467d5c41d14a20ba2d0d99b1f49722f2388bfea9dc13c6334ef3fadab` |
| Fourier／Faber原稿 | `e46cd697ef3b496e44a1c922793ef6f15d323582e60c6be6fb548b3bf850ab58` |
| native产品／Green原稿 | `1368aa94eb460554e5f78aaaeca06bede02ff6ea735c3d4e7fac0eb994f10adf` |
| 关系／非根原稿 | `9b61e33b5a7a6df9f7d0a59c23cbfa9ad2a842c248273a74357ad6591096eea7` |

哈希只固定审查版本，不替代证明。适用验证 `git diff --check` 通过；本审查未修改 STATE、cadence、合同或库。本稿最终 PASS 也不是 root 的结算动作，亦不验收 GitHub 同步是否完成。
