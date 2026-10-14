# Canonical cosh deflation：signed有限秩修复及准确费用

2026-10-14；`/root/principal_final_reverse`，短独审。没有spawn；只写本owned稿，
不改已final cosh raw、公共STATE/cadence/Git，不建C024。
恢复AGENTS/README/STATE/check后show、同Goal/frontier、C023 stopped、D20261014AC/战略。
入口HEAD `43d4b0af7fe57cbf672d85fc82e7b690fa45e7ed`；root正在保存STATE及来源目录。
强旧whole对照557 leading4/5，当前审查不把形式修复当新算术输入。

**结论：** root指定构造合法。修复算子V的norm精确为||w||，不是2||w||；
w不必在DomH。deflated补空间D是合法selfadjoint restriction，非未核域的formal compression。
原actualQ仍保signedpole，可得安全count

    n_−(Q_L)≤2+n_−(D_L−||w_L||I)。                       (1)

该源定义signed有限秩/deflation逃逸必须保留；旧GT/无pole热门或某个修复失败不能排它。
但D的gap、负惯性/trace共同算术费用、Ξ仍open。本稿旧024/555及当前原domain费用的直接消费0。

## 1. 实际对象与已付canonical operator前件

ALL fixed L≥1，原H_L=L²((-L,L),du；C)、zeroextension Dlog；
H=Γ_I−A_L，actualΓ=2θ′，A_L保全部strictq<exp(2L) properpowers。
Γ_I selfadjoint semibounded，A_L bounded selfadjoint，所以H selfadjoint，DomH=DomΓ_I。
规范内积第一变量线性。

取c=cosh(u/2)/sqrt(L+sinhL)，||c||=1、P=|c〉〈c|、R=I−P。
已final原件 `cosh-full-operator-and-residual-domain.md` rawSHA256
`ff475dc3d87737f64135d5a511b9b396b15041a7f5cfc054cc8ea82e7fe39c7f`
付c∈DomΓ_I=DomH及uniform ||Γ_Ic||；endpoint jumps/Γ² Fourier尾完整付款。
actualPole_even=κP，κ=2(L+sinhL)，oddvector s(u)=sinh(u/2)∈R。
完整Q=H+κP−2|s〉〈s|。

定义actual source coefficients

    a=〈Hc,c〉∈R，w=RHc=Hc−ac∈H_L，w⊥c。

source c、H和全row均已明确，没有使用未知true eigenvector、零点位置或metric反造。
fullQ c=Hc+κc，故w=RQc。原cosh残差费用给

    ||w_L||≤||Q_Lc_L||=o(exp L)，a_L+κ_L=o(exp L)。

旧PNT只付这个relative leading费，未给absolute o(1)、Γrelative小费或未知补空间正性。
由于κ/exp L→1，另有a/exp L→−1；这仅是intermediateH的头槽，非actualQ负性。

## 2. V的确切norm、sign和bounded perturbation域

定义

    V=−|w〉〈c|−|c〉〈w|，
    Vx=−〈x,c〉w−〈x,w〉c，ALL x∈H_L。

二项互为adjoint，V bounded selfadjoint、rank≤2。若w=0则V=0。
若σ=||w||>0，在orthonormal basis {c,w/σ}上它的matrix为

    [ 0  −σ ]
    [−σ   0 ]。

在其正交补上V为0，eigenvalues±σ，所以

    ||V||=σ=||w||，−σI≤V≤σI。                          (2)

它是signed修复，不是PSD majorant。直接将两个rank-one norm相加给2σ只会丢掉已知
w⊥c的几何；此处没有该多余factor2。
w∈H_L足够定义V，完全不需要w∈DomH。即便V(DomH)不包含在DomH内，
bounded selfadjoint perturbation仍给H'=H+V selfadjoint，DomH'=DomH，form domain仍Dlog。
不能把“修复输出不在原operator域”扩大成此direct boundedpert定义非法。

## 3. 真正block diagonalization及补空间D域

V c=−w，所以H'c=ac。Pc映射DomH到DomH，因为c∈DomH；
Rx也在DomH（x∈DomH）。对r∈DomH∩R H_L，selfadjointness给

    〈H'r,c〉=〈r,H'c〉=a〈r,c〉=0。

因此span{c}和R H_L是H'的reducing subspaces；
DomH'=span{c}⊕(DomH∩R H_L)。restriction

    D=H'|_(R H_L)，DomD=DomH∩R H_L

是真selfadjoint，且对上述r有

    Dr=RHr=RHRr。

因为Vr只沿c，R V r=0。这里RHR这个符号是在已经证明domain/reduction后消费，
不是假定任意unbounded compression自伴。D对应原q_H在R∩Dlog上的closed restriction，
since q_V(r,r)=0；也保持原compact resolvent（H' boundedpert，restriction减一个头）。
没有因deflation声称D≥γ或谱位置已知。

parity全部合法：Γ even multiplier/对称支持、完整±prime shifts给H commute反射；
c even，Hc/w even，V kills所有odd向量并保even。s odd且s⊥c，负oddpole保在R。
complex源没有被压成real测试或单一parity；此block只用原H正交分解。

## 4. ActualE/Q的符号、lower和+2安全惯性数

以H'=diag(a,D)记，真实保正evenpole的中间E是

    E=H+κP=diag(a+κ,D)−V，
    Q=E−2|s〉〈s|。

没有把修复后的H'冒充原H，也没有丢掉−V的费用。
由(2)，原wholeQ form在同一Dlog上满足

    Q≥diag(a+κ,D)−σI−2|s〉〈s|。                       (3)

严格负Q子空间交ker〈·,s〉至多少一complex维；其上diag(a+κ−σ,D−σ)亦严格负。
directsum head只可能贡献一维，故

    n_−Q≤1+1_{a+κ<σ}+n_−(D−σI)
          ≤2+n_−(D−σI)。

head恰零时不贡献strict negative；式(1)是无需判head sign的安全版本。
+2分别来自一个canonical头槽和一个negativeoddpole，不按rankV再多加两维，
也不因complex dimension翻倍。修复费σ已经作为massshift支付，不能同时重复rank罚。

## 5. 已付逃逸与仍未付的箭头

该构造是actualsource-defined finite-rank signed修复/deflation，fee σ=o(exp L)。
它使原大negative H头槽与真实positiveevenpole合并为a+κ=o(exp L)，
不使用unknown eigenvector，因此必须保留在合法修复清单中。
旧024的抽象residual/block消费加555 actualrow与当前Γoperator域即可闭合，0新数学轮。

原cosh稿的actualprincipal smooth counter仍在R中，双pole0且Q(r_L)→0。
其q_D与q_H/完整Q相同；因而canonical一维deflation仍不提供fixed positive cofinalgap。
但该counter不排γ_L→0、growingcore、σ付款后的不同joint/source/domain修复，更不证明Q负。
没有D的same-source Γ/pp/trace/net费用，式(1)不能变成优于557的whole budget或Ξ结论。

root可消费的准确范围：原operator domain完整；ALL L≥1/allcomplex；actualΓ/strictpp/signedpole；
σ精确norm/relative old费；头/complement/coupling角色明确；remainingD谱隙与fulltrace/netopen。
不据purefinite-rank或无poleGT失败排该paidescape，不建C024，不结束宏观Goal。
