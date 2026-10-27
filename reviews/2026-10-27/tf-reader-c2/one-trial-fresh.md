# 一次相关trial预算：独立审查

2026-10-27；`/root/one_trial_fresh`独占稿。已读README/STATE，check→show、G20261027、已结算C046、D20261027H、宏观前沿及next-one-trial-budget-admission；核现场工作树。只审本次固定h0/F8/v的有理预算及停止范围，不重跑旧c2/scalar/G，不改STATE、cadence、看板或库。root本轮已核同runtime Goal；本文不创建或完成Goal。

## 1. 强旧source后果和方向

physical H=L²(R+,dx)，P为Sonin正交投影，v=PBh0，h0=1_[1,2]、norm1，G=P B*B P在RanP上；n=||v||²、a=<v,Gv>、b=||Gv||²。有限Euler B是相交换unitary dilations的多项式，所以B normal。线性在第一腿的内积准确给

\[
 n=\langle v,PBh_0\rangle=\langle B^*v,h_0\rangle,
 \qquad a=\|Bv\|^2=\|B^*v\|^2\ge n^2.
\]

这是旧source输入的直接Cauchy后果（也由q0≤1及n²≤a q0得），不能以改好弱dn或p2 lower计新whole后果。

W2=(3/2)I−(U_log2+U_-log2)/sqrt2。当前v为real physical输入，c2=<v,U_log2v>实，故a2=<v,W2v>=(3/2)n−sqrt2*c2。Wrest为其余七prime的正因子乘积，且与W2交换；因此drest*a2≤a≤urest*a2。只需v∈RanP来把G二次型转成W二次型；不假定G或P与每个dilation交换。

正G的全谱上界G≤u_hi给G²≤u_hi G，故b≤u_hi a。冻结z=t v，

\[
 r^2=n-2ta+t^2b\le n+(u_{hi}t^2-2t)a.
\]

0≤t≤2/u_hi时系数非正，应使用a_lo；其最优t=1/u_hi。该相关包络最小值n−a/u_hi，使用区间付款得r²_hi=n_hi−a_lo/u_hi。这里没有把a/b拆成无关rectangle，也没有将包络的正值升级为actual r²的下界。

## 2. 独立有理重算

我直接用Python Fraction读取原n、真实c2和既存prime inverse-sqrt/d/u记录，独立逐prime求rest七因子，而非调用本次producer代码。sqrt2直接取2/sqrt2的原有向包围，负c2的乘法端点按符号运输；a_lo取max(n_lo²,d_lo*n_lo,drest_lo*a2_lo)，a_hi取min(u_hi*n_hi,urest_hi*a2_hi)。所有下列显示小数只作摘要，正式接受来自有理比较：

| 量 | 独立计算显示 |
|---|---:|
| a2 | 约0.281813617517250 |
| p2/rest lower | 0.00051666323928845 |
| 旧source lower n_lo² | 0.02266102783295458 |
| 新a_hi | 17.984178804052817 |
| 旧u_hi*n_hi | 27.995602216216067 |
| 冻结t的J区间 | [0.0010989143883674542,0.0016182439069201465] |
| 相关residual包络hi | 0.15041395135671254 |
| 原d_lo/32目标 | 0.000004914894986912351 |
| free exacta时该包络最优值的有理下端 | 0.05383265720924377 |

精确比较已核：a_lo=n_lo²；residual包络hi>目标；n_lo−a_hi/u_hi>目标。因此新的p2 lower没有改变当前残差包络所用强旧lower。新upper仍可能有fixed scalar作用：Cauchy q0≥n²/a给可认证lower约0.00126005352148，比旧n/u约0.00080944955775高；不得反向声称c2毫无数值作用。它仍远不付原宽1/16，也不改变classic成长／whole／primitiveRR瓶颈。

## 3. 消费范围与停止

即使免费知道actual a，仅保b≤u_hi*a的本scalar包络也不能付原残差门；所缺是更紧的同向b/a或actual residual信息。该结论不是actual residual的必要lower，不排其他trial、真正b费用、非局部/源适应/压缩或有费远尾修复，不建立实质方法类边界。必须停止此输入/包络的自动t/prime/Chebyshev/Krylov续算；fixedc2不重跑。

一个标准解释是：若actual a,b将来都已给，same-v scalar trial的最佳残差为n−a²/b。付ε=d_lo/32须nb/a²≤1/(1−ε/n)，即G谱测度的相对方差nb/a²−1至多ε/(n−ε)，本固定输入约3.265·10^−5。它说明“更紧b/a”仍是需要实际支付的强信息；这里未计算actual方差，也未提供新的输入或自动准入，不因这个标准重述续调t。

标准旧算子不等式加已产固定数值的预算比较，0数学轮，无C047/584。最强经典后果542+555→557 whole leading4/5负惯性UPPER及完整Γ/contact/properpowers/双pole、allcomplex原du/zero-extensionDlog／五源T/E/cross和成长core责任均不变。长期Goal完成门open。

## 4. 实际producer执行审查

已全文核实际`tf_reader_one_trial_budget.py`与`one-trial-budget.json`。独立执行build_record，除elapsed_seconds外全部JSON字段exact match；另用不调用producer interval helpers的direct Fraction prime-product／sign-aware计算，重构a2、rest七prime产品、强旧max／upper min、冻结t/J、residual包络、free-a包络诊断和新旧Cauchy q0 lower，关键字段全部exact相等。所有prime inverse-sqrt包围另逐个核p·lo²≤1≤p·hi²及0<lo≤hi<1，原d/u全产品的保守包围亦exact通过。

实际结果是合法非零trial z=t v、J的有理区间和true-H residual的**充分上界**已经给出；不能继续沿用旧“完全没有trial/J”的描述。没有执行的是Gv action、actual residual value或更紧b/a、窄q0验收与五源表。脚本trial指同一exact v，未无声替换为存储的v*；若未来执行t v*的J／残差，需另外运输δv，本次并未作该替代或预填其结果。

冻结trial的J半宽约0.000259665<1/128，但residual包络约为d_lo/32目标的30603.70倍；free exacta时该包络最优值的有理下端仍约为目标10952.96倍。独立精确比较确认两个预算门皆不足。variational interval上端与投影旧界相交后仍为1；新Cauchy lower交入仅得到约[0.00126005,1]，宽约0.99873995>1/16。该q0区间是实际有理证书，仍无原窄门结果。

当前script/JSON数学范围限定PASS；producer说明稿与root结算/前件最终实际版待出现后再补版本绑定，不用未出现的稿件代消费。


## 5. producer最终实际版：限定PASS

已全文核最终one-trial-budget.md；其exact v／stored v*角色、strongest-old lower、upper的fixed q0作用、相关残差包络及停止范围与以上独立推导一致。全部numeric执行terminal，未重跑旧c2/scalar/G。脚本implementation hash和四个source hashes均与现场LF版本一致，最终三个执行原件如下：

| 文件 | 规范LF SHA256 |
|---|---|
| scripts/tf_reader_one_trial_budget.py | 64a5f1177f103b5c5db5b3a29106d111b028f6620f16aa5c58c6f55af0ade2a6 |
| reviews/2026-10-27/tf-reader-c2/one-trial-budget.json | b8f6f53386ccde0a0632195254071747fcc5d8e73b8da88cc3f365c390489499 |
| reviews/2026-10-27/tf-reader-c2/one-trial-budget.md | 79c7c085788dd95e5f3255794f805fcef7c22c20cbc160f2570c1c6a4ca14cb4 |

**限定结论PASS**：本次标准固定有理预算与明确不足结果可消费；已经有合法非零t v、J和真实H残差上界。原q0宽门不通过，当前相关scalar包络即使免费知a也不足；后一句只诊断该包络，不是actual residual下界或所有trial不可能。新的fixed q0 lower改善和残差瓶颈不变分开；无classic whole/core/growth/primitive后果，0数学轮，停止自动t/prime/Chebyshev/Krylov续算。

root结算及前件收据仍待实际版；本PASS只审以上实际producer输入／数学／运行和停止，不预消费未出现的root结算。

## 6. 下一输入审视稿§7与本次停止的分离

已读`reviews/2026-10-27/after-reader/next-input-audit.md`的稳定版（LF SHA `436a1013afed62fa688de28b75ed1e83a9c0b169d936641d8ac5d9986fc70dca`）。其II2,2/BY同载体零shadow来源门已执行停止，不能再当未执行下一动作；root另给固定marked pair X0(11),{∞,0}，在∞保旧主部、在0给零主部。这是一腿cut的具体source操作，与此前完整pullback/principal像有别，不能把它当已给native shadow／relative类／height。

作为纯q解析定义，g11=q∏(1−q^n)²(1−q^(11n))²在|q|<1局部一致收敛；K11(u)=CT[e^(u j)g11]在0<|q|<1的contour取CT，ℓ11(r)=∫rK11=Σa_−m(r)c_g(m)。s<R的两Cauchy界给绝对换序和C_R·s/(R−s)·p_As(r)强源费用，且K(0)=0、K'(0)=1、K''(0)=1486的局部系数核对正确。fixed support的原du费用也直接由C_s exp(AsL)√(2L)||r||得；它不是全线du统一界、几何height或Petersson费用。

因此可**限定准入一次functional构造及Pan/537首门**，没有重启本次预算包络或自动G／prime／Krylov。实际门仍须明示每个405非compact Pan真在该p_As有限的强源域；若有输入出域，先标未定义并给扩张／尾运输，不可无声缩域让全关系测试变空。modular/cusp型、Γ0(11)/Weilρ和所有cusp规范仍需原定理或证明，不能由上面的纯q定义预领。

ℓ11目前只是C值rank1 functional，不代全源coverage或full Gram；native ξ反线性、Petersson约定、无限主部完成化及Green尾未付。Pan反例若成立只停止当前shadow-only下降recipe，保独立实际边界补偿／不同relative map的合法修复。下一门的全量词新结果须按实际范围另结算，不预保证其也为0数学轮。以上只审准入边界，尚未执行下一functional/Pan测试，也未审BY原文证明。


## 7. root实际结算／前件及单泛函下一门：最终限定PASS

已全文核`goals/reviews/2026-10-27-reader-budget-stop-and-marked-source-admission.md`、`after-reader/root-consumption-scope.json` draft、`next-marked-cusp-functional-admission.md`及文献source-scope记录。root收据的12个规范LF版本全部与现场一致，两份PDF的raw-byte SHA亦与实际本地文件一致；这只绑定原件，不替任何PDF证明审计。root指定作者更正版p1/19/25–26的目视／statement/domain范围、v1仅元数据/首页和未审整篇proof的限制有明确记录，本fresh不冒称自行重审BY原文证明。

root当前预算消费与独立重算一致：exact-v的合法非零trial/J/true-H residual充分上界已经给出，强旧a≥n²仍胜、新upper对fixedq0lower有作用，但原残差和宽门不通过。免费exacta的正下端只约束同一symbol包络最优值，不是actual residual下界或一般方法边界；停止自动t/prime/Chebyshev/Krylov/旧c2续算的范围准确，真正有费globalmixed/远尾/不同trial保持合法。

下一单泛函门严格与reader止门分离：fixed marked X0(11),{∞,0}只保∞配对而0主部取零，source/boundary操作确有变化；直接q解析K11/ℓ11及s<R Cauchy费用不是native harmonic shadow或算术lift。全S_exp源泛函与BY的有限principal-part H_k域已分开。实际next稿要求逐个Pan核p_As有限，出域须标未定义/未覆盖或另付运输，不能以compact-only空测试充当全Pan通过；原537指定源和额外control也明确分开。Γ0(11)/cusp/character、原ρ、ξ反线性/Petersson、无限主部Green尾／relativePic／mixedRR仍未付，不自动领取新primitive或wholecoverage。

同原II2,2的零shadow类型来源门已止，不留作未执行下一动作。一次新marked-cusp functional/Pan首门有实际公式/input、费用及可否决recipe的test，可限定准入；失败止本一腿cut，不换N/cusp/补偿参数/paper，合法不同relative修复仍须独立公式。新严格全量词结果要按实际范围重新计轮，root没有预保证后续全为construction0。当前预算/来源类型对照和准入组织0数学轮、cadence1/历史47/cycle16及strongest-old whole4/5UPPER/主瓶颈不变的结算相容。

审到的root三个关键LF版本如下；收据状态为root-draft-awaiting-final-fresh：

| 文件 | SHA256 |
|---|---|
| goals/reviews/2026-10-27-reader-budget-stop-and-marked-source-admission.md | 36240c4064edcc1d59febff7460a22dab093d4225a10e19c88e545d4b78958e2 |
| reviews/2026-10-27/after-reader/next-marked-cusp-functional-admission.md | 91570b2c3b0e6dfd0f08667a8e8c70329923d1e3a07a1c6205f6f5432deeb5d4 |
| reviews\2026-10-27\after-reader\root-consumption-scope.json | 1d6313ef3736103c6fdaf68f66325480f994fcd82b718921f77eab053af7c8cc |

**最终限定PASS**：root可消费本次实际预算不足及保存的标准来源止门，并仅准入所写的下一单泛函构造/关系首门。下一functional/Pan测试尚未执行，不预填其结果。此审查不认证actual Gv/tight b/a、一般trial不可能性、完整BY证明／算术height、classic全源／成长signed、primitiveRR或长期Goal完成门。root仅填最终receipt status／fresh metadata而不改变上述数学/依赖内容时，本PASS继续适用；如语义/依赖改变须重闭前件。
