# 592. 正周期图的素数分离与返回通信费用

2026-10-29；C055一个完整数学迭代。两原件与不同数学fresh已terminal/root全文核，精确版本和结算见[根收据](../reviews/2026-10-29/positive-graph-prime-periods/root-consumption-scope.json)。不主张世界优先权；本结果是positive edge-additive周期模型的结构边界，不是RH证明或全部图逼近失败。

## 1. 同一实际周期测度

有限或可数有向multigraph的每条active边有strictly positive有限长度l(e)及activity a(e)。路径长度相加、activities相乘；primitive cyclic edge-word γ及全部repeats给

    ν_G=Σ_γ Σ_k≥1 lγ aγ^k δ_(k lγ)。

要求ν_G在(0,∞)Radon，不据可数性自动补局部有限。无需ordinary trace、自伴adjacency或normal/Schatten determinant极限。目标是原完整Weil分布的正prime部分

    νζ=Σ_p Σ_k≥1 logp p^(-k/2)δ_(klogp)，S={klogp}。

原physical源r=e^(u/2)bare、du/zero-extension Dlog及第一槽linear不改。图的正周期measure不自动给Weil正型、Hodge能量或独立算术primitive。

## 2. Exact结构与cofinal通信定理

**Exact。** 若supportν_G⊂S，每个有循环的strongly connected component只能含同一个prime基底的周期m logp。若ν_G=νζ，则每prime必有primitive长度logp的闭词，不同prime位于不同SCC。允许同prime内部复杂mixing、多个同标签SCC以及one-way/acyclic边；没有Hilbert block-diagonal结论。

核心反测是同SCC的prime闭词A/B及返回路径S/T。设lA=a=logp、lB=b=logq、p≠q、c=lS+lT，则实际closed words

    STA，STAA，SBTA
    lengths c+a，c+2a，c+a+b。

三者若全在S，N=e^(c+a)>1、pN、qN全为素数幂。前两者迫N为p的幂，第三者矛盾。对firstfixed C，取

    M=ceil[e^C p max(p,q)]，δ=1/(16M)，

全部c≤C的三个length至少一个距S>δ；近邻整数差≤4Mδ<1给出统一裕量。同证明容许a=m logp、b=n logq，不错误排有限域的同一logq时钟。

**Cofinal。** 两个marked闭词长度固定logp/logq（或趋近这两值）、activities均≥η∈(0,1]。令

    Z_(G,C)=sup{a(S)a(T):S:v→w，T:w→v，lS+lT≤C}，

空集取0，允许∞。对每firstfixed C有同一个非负h_C∈Cc∞((0,∞))，support不交S，且

    ν_G(h_C)≥(log2/32)η² min(1,Z_(G,C))。

因此ν_Gj→νζ于vague／D′((0,∞))必迫每fixed C的Z_(Gj,C)→0。路径可随层、图或非局部资料任意选择；Z是最佳单条roundtrip activity product的**sup**，不是sum、容量或operatornorm。

高重复没有漏掉：W=γ^k在ν中的系数为lγ a(W)，不是l(W)a(W)。若primitive period很短，其repeats在[d,2d]、d=log2/8的primefree区间留下统一正质量；否则原off-S atom已有统一lower。这给上述常数且不需要最小edge长度、rank或word长度上界。

## 3. 完整fixed源接口与接触修复

设每层确有共同W_j∈D′(R)，其off-origin限制为

    W_j=WΓ+H−(ν_j+ν_j^−)，H=2cosh(u/2)du，

WΓ保原完整Γ/contact规范，H在Weil平方上保indefinite双pole；所有proper powers仍按原logp权。允许W_j在origin有任意、逐层改变的接触修复，不假ν_j在0附近mass有限，也不由Radon(0,∞)反推全R延拓。

若全部fixed compact complex r满足W_j(r*r#)→Q_W(r)，则四平方极化给全部mixed pairs。对K=[u,v]⊂(0,∞)，用两个disjoint正bump的cross-convolution，可在K上严格正而支撑仍在positive半轴；所有origin contacts在此exact0。由此支付sup_jν_j(K)<∞，再用approxidentity得到ν_j→νζ vague。因此完整fixed源逼近也必须付上述通信费。

本桥不要求每层Q_j PSD，不给du→graph norm或principal/Hodge运输；改变off-origin背景、别处signed补偿或逐源另选图不在此同对象身份内。

## 4. 两个实际逃逸，防止过度判败

**长连接。** 素数≤N各取一条prime loop，以lengthN/activity1双向star连接。每层finite stronglyconnected、fixedprime活动权非零；含connector的闭路≥2N，故每fixed time窗最终exactνζ。同Γ/H的fullsigned fixed-source身份也最终exact，但未付PSD。

**扩散。** M态q块取每条q-edge activity q^(-1/2)/M，vertex0另加p-loop。以u=q^(-s-1/2)、v=p^(-s-1/2)，其有限transfer有

    det(I−B_M)=(1−u)(1−v)−uv/M。

Pure trace正确，fixed mixed-word系数O_T(1/M)。令M=N并用长star补其余prime≤N，即fullν_N→νζ及同Γ/H完整signed源收敛。p/q在vertex0的返回可为空、activity1，但每个individual q-loop activity→0，不满足marked lower。故新定理不控制整个q-sector的rankfree通信总量。

另有单q、2×2 rankone正mixing对照；不冒称非平凡曲线完整ζ。这些实例明确保留long/dilute/diffuse修复。Signed、非edge-additive／infinite-memory roof、一般flow/singular/higher/Hodge及非normal全局重整也未被本定理排除。

## 5. 强旧净值和停止

078同q图、079 prime-local normal-limit、565有限双向Markov、566jump域/heat、404真实周期及560/577完整目标先扣。新付款是countable正edge图的exact SCC分类、同一h_C下任意adaptive短返回的线性必要费，以及off0双源运输；不将原prime数据、旧正模型或两个局部bound拼成whole改善。

局部positivegraph如何承担跨prime耦合的判断改变；独立arithmetic primitive/Pan下降、principal/整截面/mixed、危险signedcore/cross及Ξ仍欠。Whole542+555→557 leading4/5仍仅负惯性UPPER。实际逃逸已可达fullsigned逼近，不能缩Goal第3门来完成目标。

C055一轮止；唯一cadence由root只一次1→2/history55→56/latest592，formal18保持。作者、辅助子审、fresh、源桥、逃逸例和发布不另计。未新读外部primary/query/PDF/下载/数值，manifest131保持。不续prime/graph/connector rate/capacity/source预算；长期Goal同实例active/open/noteligible。

原件：[主证明](../reviews/2026-10-29/positive-graph-prime-periods/three-word-and-cofinal-proof.md)、[强旧与实际修复](../reviews/2026-10-29/positive-graph-prime-periods/strongest-old-and-role-audit.md)、[不同数学fresh](../reviews/2026-10-29/positive-graph-prime-periods/fresh-positive-graph-prime-period-audit.md)。
