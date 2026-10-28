# Inclusion-cone实际boundary检验：先原eη，再同norm精确因子化

2026-10-28；G20261027/runtime1793085111/原0c4f。执行STATE唯一 [next](../independent-mixed-formation/next-canonical-inclusion-cone-admission.md) 的实际completed-projective存活test。恢复README/STATE、check→show、Goal/C049/D20261028AA/frontier/summary/currentnext及573必要原前件。只检这一固定pair/norm/source，不web、新source、数值、STATE/Git/cadence或数学合同；本稿待root另行核验。

**结果：原eη给出有界primitive费的actual boundaries趋近z_r，故reduced类为0；更强的同一闭C*理想内显式因子化还给一个精确primitive，故这份source类在unreduced同调也已为0。** 后一句使用实际exact boundary，不是从closure推unreduced零，也不借excision。

## 1. 冻结对象、chain degree及范数

保原unital C*代数Abar=C*(A_src)、闭双侧理想Jbar=closure(D_src)。573已经支付Jbar含全部raw F_r；对r∈L¹的延拓由‖F_r‖≤2‖r‖₁给出。u是原幺正，设a=u*、B=B_r=uF_r∈Jbar，‖a‖=1。

连续Hochschild链C_n(E)=E的(n+1)重完成projective tensor，C_(−1)=0。其低阶边界为

\[
 b_1(x\otimes y)=xy-yx,
\]
\[
 b_2(x\otimes y\otimes z)
       =xy\otimes z-x\otimes yz+zx\otimes y.
\]

固定理想包含i:Jbar→Abar的cone

\[
 S_n=C_n(\overline A)\oplus C_{n-1}(\overline J),\quad
 D_n(x,y)=(b_nx+i_{n-1}y,-b_{n-1}y),
\]

用原projective norm的ℓ¹直和，不改trace norm或source拓扑。已给闭源是

\[
 z(B)=(a\otimes B,-[a,B])\in S_1,
 \qquad\|z(B)\|\le3\|a\|\|B\|\le6\|r\|_1.
\]

这是本次的输入，不重计raw闭性或其费用。它不同于573原quotient-fiber cone；本稿不把另一方向的−4电荷挪来消费。

## 2. 一个明确tensor恒等式：不使用excision

对任意e,c∈Jbar，取实际degree2元素

\[
 P(e,c)=-a\otimes e\otimes c\in C_2(\overline A),
 \quad Q(e,c)=ae\otimes c+ca\otimes e\in C_1(\overline J).
\]

后一个确在Jbar的二重tensor，因为ae、ca、e、c都在同一双侧理想。逐项算得

\[
 b_2P=-ae\otimes c+a\otimes ec-ca\otimes e,
\]
\[
 b_1Q= aec-cae+cae-eca=[a,ec].
\]

所以在原cone里精确有

\[
 \boxed{D_2(P(e,c),Q(e,c))=z(ec).}                         \tag{1}
\]

同一projective norm直接给

\[
 \|(P(e,c),Q(e,c))\|\le3\|a\|\|e\|\|c\|.                 \tag{2}
\]

没有用“B在J中，所以quotient为0”跳过实际boundary；(1)保原符号、degree及两分量。

## 3. 原eη实际检验：误差及primitive费用

令T=BB*∈Jbar正，η>0，按next固定

\[
 e_\eta=T(T+\eta1)^{-1}.
\]

连续C*函数演算的f(0)=0给eη∈Jbar，0≤eη≤1。这是source-adapted的实际元素，不假存在一个free approximate unit。

将e=eη、c=B代入(1)，得到actual boundary

\[
 D_2(-a\otimes e_\eta\otimes B,
          ae_\eta\otimes B+Ba\otimes e_\eta)=z(e_\eta B).   \tag{3}
\]

其primitive费用由(2)为≤3‖a‖‖B‖，不随η发散。实际C*范数误差可直接计算：

\[
 \|(1-e_\eta)B\|^2
  =\sup_{t\in\operatorname{spec}T}\frac{\eta^2t}{(t+\eta)^2}
  \le\eta/4.
\]

因而在原cone projective sum norm中

\[
 \boxed{\|z(B)-D_2(P(e_\eta,B),Q(e_\eta,B))\|
       \le\tfrac32\|a\|\sqrt\eta.}                         \tag{4}
\]

这实际证明z(B)∈closure(imD₂)，故reduced HH₁类为0。单凭(3)–(4)及有界primitive序列，尚不能推出primitive收敛或imD₂闭；本稿不作这个错误推断。原eη test已完成，不能只保下一更强结果而抹掉它。

## 4. 同一pair/norm内更强的exact因子化

本对象还允许标准C*因子化，足以不经closure解决同一z(B)。若B=0取e=c=0。否则设

\[
 E=T^{1/4}\in\overline J,\qquad
 C_\eta=(T+\eta1)^{-1/4}B\in\overline J.
\]

不把未有界的T^(−1/4)写作代数元素。对t≥0定义gη(t)=√t/(t+η)^(1/4)，g₀(t)=t^(1/4)。在0≤t≤η时|gη−g₀|≤η^(1/4)；t≥η时用

\[
 0\le1-(1+\eta/t)^{-1/4}\le\eta/(4t)
\]

得同样upper。实际乘B的C*范数于是给

\[
 \|C_\eta-C_\delta\|
 \le\eta^{1/4}+\delta^{1/4}.
\]

故Cη在原C* norm中收敛到C∈Jbar，‖Cη−C‖≤η^(1/4)。每个Cη在闭理想内，极限没有改域。另有

\[
 \|B-EC_\eta\|
 =\sup_{t\in\operatorname{spec}T}
    \sqrt t\,[1-(t/(t+\eta))^{1/4}]
 \le\sqrt\eta\longrightarrow0.
\]

于是**实际exact** EC=B。函数演算还给

\[
 \|E\|=\|C\|=\|B\|^{1/2}.
\]

现在再次使用同一链恒等式(1)，而不是假设(3)的primitive序列收敛：

\[
 \boxed{D_2(-a\otimes E\otimes C,
                    aE\otimes C+Ca\otimes E)=z(B).}       \tag{5}
\]

(5)是完成后同一代数／理想中由有限纯tensor组成的一个exact primitive。因此z(B)∈imD₂，**unreduced类也为0**，无需imD₂闭、H-unitality或excision。

## 5. 原source量词、费用与不得升级的结论

这些公式对每个原complex r∈L¹(R)合法，特别覆盖全部S_exp与Cc∞；B_r来自原已付raw map，包含全部物理关系源及537非根。没有按未知ζ零点、Q号或目标primitive选择B。

原同norm的exact primitive费用由(2)、EC=B及‖a‖=1给

\[
 \|(P(E,C),Q(E,C))\|\le3\|B_r\|\le6\|r\|_1.              \tag{6}
\]

先fixed支撑I_L时，它≤6√(2L)‖r‖du，亦≤6√(2L/log2)‖r‖Dlog；全线L¹／强源费不换成global L²/Hlog uniform费。η误差(4)为absolute bound；若希望对每个B用relative容差，可选η=ε²‖B‖²，但这不是更换pair、source域或regulator。

因子E、C依B非线性，(6)只给每个source的有界primitive，**不宣称**已经构造一个bounded linear chain contraction、全S_*同调为0或一套functorial source乘法。也不将C*函数演算因子免费放回较小A_src／D_src、trace-class子代数或更强源链完成化。

只要读出真正因子化这份固定cone的同调，(5)就使其在全部z_r上为0；reduced连续读出由(4)已零，unreduced同调读出则由(5)零，后者不靠连续性。特别不能从这些source类取得537的非零完整Weil值。若另有只在更小强域定义的无界regulator，它须另给actual域／费用／coupling，不能用本次预算自动延伸或恢复旧432电荷。

## 6. 强旧比较、范围和停止

573支付的是实际Jbar包含raw ideal及L¹费用；(1)是普通Hochschild边界展开，(3)–(5)是同一C*函数演算／因子化的直接应用。原先next要求的reduced test已由这条标准链决定，并且同norm更强exact后果也一并恢复。这里不以新文件／source-adapted标签领数学轮，不宣称外部首创或新的算术正性。

它不与573原quotient-fiber cone的非零−4 relative类矛盾：pair、方向、source代表和目标不同。也不能拿(5)否定原411轴trace、432电荷或较强trace-norm的实际代数；本测试始终在已冻结的Abar/Jbar、completed-projective范数及这份z_r上。

准确建议为：按强旧／标准直接消费0止此pair/norm下的source-survival路线；不调norm、改pair、缩source域、加metric或换regulator续预算，不预C050/587。未给新的两sourcemixed、Hodge primitive或整过滤／sections／RR容量，也未提供完整Γ/contact、proper powers、双pole下的独立Weil正型。Whole4/5负惯性UPPER及长期关键瓶颈不变，Goal门open；本稿不修改cadence或自行结算。
