# 换域的特殊 Möbius 下一步：principal 幂次子族与未付 primitive joint

2026-10-07。twisted_research；有针对性的只读分析，只新增本报告。
未改冻结前件或Git。结论：有一个具体的特殊 Möbius 子族改进，但
Gaussian 全实际 raw 在 U接近D^(1+c)的线性合同仍未闭合，无新sigma。

## 1. 绑定与关键判断

- [457](../../notes/457-number-field-choice-and-relative-amplification.md)：
  `75079970955602644a9290709f66e2be331ad6116d2a637ed8fc97fb0dde5791`。
- [458](../../notes/458-gaussian-all-row-large-sieve-comparison.md)：
  `3ee821601d6e1d5da38c8235586981b28d7ebee5a5f28691a98d869834dcc8ac`。
- [460](../../notes/460-generic-power-row-obstruction-and-field-choice.md)：
  `9625c0d618854769de90edfb3ee3b8d8b89e1d3b2b83d676dffccb927e09d85f`。
- [459](../../notes/459-natural-inverse-and-primitive-zero-joint-reduction.md)：
  `fe6046154965fb8e833e0a96adf0801f9aa4fd4b2ea8b27397748c79193477b6`。

核对结果：457的order4条件放大仅在特殊raw前件成立后获准；458实际
unmarked全行界在U=D^(1+c)、0<c<1仍有相对损失D^((1-c)/3)；460的
第四幂行下界是任意列系数算子范数，不能给固定Möbius列下界。
普通Gaussian Hecke FE、quartic Gauss/theta completed反射必须分开。
本报告没有把已付 sign-adapted finite probe当作arbitrary-eta完成。

保持458的同一固定eta、同一W（annulus[1,2]）、同一原height和全部零值：

\[
 M_u(D')=\sum_{n\ {\rm odd,sf}}\mu(n)\eta(n)(Nn)^{-1/2}
 W(Nn/D')\left(\frac un\right)_4^\epsilon,
 \qquad\epsilon=\pm1.                                  \tag{1}
\]

原norm twist如存在仍在同一列系数中，绝不变成另一个target。

## 2. 特殊第四幂子族的实际估计

只取**odd primary u=r^4**（不扩大为所有unit/lambda sectors）。准确有

\[
 M_{r^4}(D')=\sum_n\frac{\mu(n)\eta(n)}{\sqrt{Nn}}
                  W(Nn/D')1_{(n,r)=1}.                   \tag{2}
\]

自然mask保留在(2)。现在明确增加一个作用于**同一个已固定eta**的前件
[Z_eta]：其primitive普通L在Re s>theta_0无零，并有fixed-gap uniform
reciprocal control，原height<=U^A，A先固定。它不是全Gaussian家族前件。
取 \(1/2\le\theta_0<1\)；若已有更强的线，可在这里使用 \(\theta_0=1/2\)。
于是所选 \(a>\theta_0\) 自动大于 \(1/2\)，(3) 的 scale-sup 幂是递增的。
这里 control 明确指每个固定 \(\delta,\varepsilon>0\) 均有
\(\left|1/L_\eta^*(\sigma+it)\right|\ll_{\delta,\varepsilon,\eta}(1+|t|)^\varepsilon\)
uniform于 \(\sigma\ge\theta_0+\delta\)；任意固定次数的 polynomial bound
不足以直接支付 (3) 的 \(U^\varepsilon\)。原长 height 的固定 A 先选，
再缩小此 \(\varepsilon\)。
若原eta已经是Dirichlet角色的norm base-change（包括eta=1），既有[R]
Dirichlet全族输入通过 `L_Q(i)(s,chi∘N)=L(s,chi)L(s,chi chi_-4)`给
theta_0=7/8；没有为达到此条件更换原eta。任意Gaussian eta不自动满足它。

在固定a>theta_0、a<1上，r产生的deleted Euler inverse product仅为
(Nr)^epsilon。对同一个W的Mellin inversion，保留原height shift而不
微分norm phase，得到

\[
 \sup_{0<D'\le D}|M_{r^4}(D')|
 \ll_{a,W,\varepsilon}D^{a-1/2}U^\varepsilon.             \tag{3}
\]

这里D>=1；D'小尺度为空或有限项亦被右侧控制。principal普通L的s=1
pole在1/L中是zero，没有新增residue。固定eta的primitive坏素数与r的
附加零值全由真实finite Euler factors保留，(3)不是删除它们。
按Nr<=U^(1/4)实际计数，遂有

\[
 \sum_{Nr\le U^{1/4}}\sup_{D'\le D}|M_{r^4}(D')|^2
 \ll U^{1/4+\varepsilon}D^{2a-1}.                        \tag{4}
\]

若U>=D^(1+c)、c>0固定且theta_0<=7/8，选择固定
`0<a-theta_0<=min(3c/16,(1-theta_0)/2)`，则

\[
 (4)\ll U^{1-\chi+\varepsilon},\qquad
 \chi=\frac34-\frac{2a-1}{1+c}\ge\frac{3c}{8(1+c)}>0.    \tag{5}
\]

这个真实Möbius子族的上界说明460的generic D U^(1/4)/logD峰不能
照搬为(1)的实际下界。并未证明whole Gaussian raw线性：其余quartic
primitive角色随a,b,c变化，正线(3)所需前件没有被固定eta控制所覆盖。
unit/lambda sectors可在各自固定twisted-target具有[Z_eta-sector]时
同样处理；不能假称Dirichlet norm base-change自动覆盖所有这些sectors。

## 3. 同一原始逆列的具体primitive联合条件

对一般u，quartic reciprocity在固定有限sector内给实际natural Hecke
presentation `L_u=L(s,psi_u*)D_Ru(s)`；finite-order psi_u*仍包含原eta
与原sign，原norm height留在同一profile的Mellin shift，不伪装为新的
finite-order角色。其primitiveconductor和redundant radical为U的固定幂。
普通虚二次FE的Gamma比值阶为1；Gaussian只改变固定conductor常数。
459的代数恢复与其负线kernel因此适用于这同一普通L，不要求新quartic
theta完成。primitiveprincipal同样使用meromorphic FE，1/L的s=1zero
不给新pole；Gamma(s)的s=0pole在该情形抵消。

固定1/2<vartheta<1，保留同一W及原cutoff，有限恢复给

\[
 M_u(D)=Z_{u,\vartheta}(D)
       +O(D^{1/2-\vartheta+\varepsilon}U^\varepsilon)
       +O(U^{-A_0}),                                     \tag{6}
\]

Z是该row的primitive reciprocal residues与horizontal joins乘有限
`G_u(s)=sum_{h|R_u^infty,Nh<=D^vartheta}psi_u*(h)(Nh)^-s`。
若原列含 `(Nn)^{i omega}`，其Mellin表示中的 `D^{i omega}` 全局因子
仍精确保留，f(y)=y^(-1/2+i omega)W(y)；原height在fhat的shift中。
各短尺度D/Nh使用原D-cutoff/profile，**不改为短尺度新test**；同row全部
尺度使用同一primitivezero rectangle与原长列height。multiple zeros、
trivial zeros、h/R phases与joins全保留，没有跨row分离measure。

Gaussian实际rows数O(U)。于是固定scale得到明确的新接口

\[
 \sum_{Nu\le U}|M_u(D)-Z_{u,\vartheta}(D)|^2
 \ll U^{1+\varepsilon}D^{1-2\vartheta+\varepsilon}.        \tag{7}
\]

当U=D^(1+c)时，取vartheta=3/4，该替换误差相对U为D^(-1/2+epsilon)。
所以它不会阻止linear raw；线性均方合同严格转成**同rows的实际
primitive residues/joins联合能量**是否为O(U(UD)^epsilon)。
对row-scale supremum同样如此：先把D'<固定常数的有限项并入O(U)，
余尺度(6)uniform且误差平方至多U^epsilon；三角不等式直接比较两个
sup能量，误差O(U(UD)^epsilon)。不能从逐scale大筛免费交换sup。
本归约没有给Z的joint estimate，也没有改善458的(UD)^(2/3)项。

## 4. whole scale-sup本来不应要求小于U

还有一个关于**固定Möbius列本身**的基线，区别于460任意系数反例。
若W非零，取y0∈[1,2]使W(y0)!=0，D0=1/y0。Gaussian odd ideals在
`[D0,2D0] subset[1/2,2]` 中只有单位理想1，所以(1)准确为
`M_u(D0)=W(y0)`，对所有u；原eta(1)=1和mask(1,u)=1。
因此对于458定义的包含全部D'<=D、D>=1的sup，有

\[
 \sum_{Nu\le U}\sup_{D'\le D}|M_u(D')|^2\gg_W U.         \tag{8}
\]

这是特殊真实profile的small-scale观测，不是通过更换列系数制造的峰。
它只说明whole scale-sup linear U是合理目标，不能要求其strict U-power
saving；并不阻止固定大scale或真正marked峰集的节省。若其他原test
明确删去单位项或只允许大scale，(8)不适用，不能擅改其test再引用本例。

具体下一输入仍是(7)的primitive联合能量，尤其相同eta下变化的quartic
conductors、R/h phase、不等plain heights以及horizontal joins。principal
幂次子族(4)可先另付，但不会推出这一joint bound。没有quartic marked
reflection、全raw线性合同或新的sigma；换域收益仍是带明确未付前件的
研究候选。
