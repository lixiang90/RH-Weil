# 2602.15941v1：真实截面、局部商及乘法的限定原件审查

2026-10-22。只审 Connes–Consani, *On the Jacobian of* \(\overline{\operatorname{Spec}\mathbf Z}\),
[v1 HTML](https://arxiv.org/html/2602.15941v1)，不串其他论文。
本稿是路线图B的来源准入材料，不是C036、独立容量定理或新数学迭代。
原件中的数学数据与下列本次推导分开；没有analytic source map的默示假设。

## 1. 范畴与原件定位

与路线图所指的是同一候选，没有发现另一个已给Weil正性的对象。
应分开四层：

| 层 | 原对象与定位 | 禁止的自动升级 |
|---|---|---|
| finite divisor | \(D=(n_p),\ n_p\in\mathbf Z\cup\{\infty\}\)，负项有限；\(L_D=\{q\in\mathbf Q:v_p(q)\ge-n_p\}\)；[§2.2](https://arxiv.org/html/2602.15941v1#S2.SS2) | 这是秩一无挠阿贝尔群，不是复测试函数空间 |
| metric divisor | \(\mathcal D=(L,\lambda|\cdot|),\lambda\ge0\)；[§3.1–3.2](https://arxiv.org/html/2602.15941v1#S3.SS1) | \(L\otimes\mathbf C\)的一维性不代表Weil primitive维数；非零metric不代表有限生成 |
| module sheaf | 有限处用\(H\mathcal L(U)\)，含∞处对有限pointed set \(X\)要求\(\sum_{x\ne *}\|\phi(x)\|\le1\)；[§5](https://arxiv.org/html/2602.15941v1#S5) | Γ-set／\(\mathbb S\)-module的单位球条件不使small sections成为阿贝尔群或复向量空间 |
| framed/rooted moduli | \((L,\xi,\tau)\)，\(\xi:L\to\widehat{\mathbf Z}\)为生成frame，\(\tau:L\to\mathbf R\)；[§8.1–8.2](https://arxiv.org/html/2602.15941v1#S8.SS1) | Thms8.5/8.6/8.15是moduli的monoid比较，不是解析源的faithful表示或正极化 |

在\(X=\{*,1\}\)层，small sections是\(\{x\in L:\lambda|x|\le1\}\)。
例如\(L=\mathbf Z,\lambda=1\)时为\(\{-1,0,1\}\)，加法不闭。
原文§4.2的“finite type”按metric非零划分，不能翻译成有限基／有限容量。

## 2. restriction处必须显式修补的歧义

[§5.2](https://arxiv.org/html/2602.15941v1#S5.SS2)把\(\mathcal L(V)\)描述为
\(L\)中在\(V\)正则的元素，并用分母约束解释。该字面定义不能直接消费为所需模层：
取\(L=\mathbf Z\)、\(V=\operatorname{Spec}\mathbf Z\setminus\{p\}\)，便得到
\(\mathcal L(V)=\mathbf Z\)，而结构层是\(H\mathbf Z[1/p]\)；\((1/p)\cdot1\)不闭合。
Prop5.1原证明只核smash乘法的norm不等式，没有排除此字面问题。
这限制的是这段表述的直接使用，不据此否定论文其余rank-one分类。

以下**本次采用的标准localization修补**须保持附加标记，公式用于非空Zariski开集\(V\)，另置\(\widetilde L_D(\varnothing)=0\)（其\(H\)为pointed零对象）：

\[
 \widetilde L_D(V)=L_D\otimes_{\mathbf Z}\mathbf Z[S^{-1}]
 =\{q\in\mathbf Q:v_p(q)\ge-n_p\ (p\in V)\},\qquad
 S=\operatorname{Spec}\mathbf Z\setminus V.
\]

集合等式的反向：对补集内有限多个prime乘足够幂即可回到\(L_D\)。
开集缩小时restriction为同一个\(q\)的包含映射；由各处valuation约束交汇而glue，
global恢复\(L_D\)。它给有限处真实模层，并可按Prop5.1的ℓ¹单位球公式接∞。
pointed-set映射合并坐标时用三角不等式；乘法用
\(\sum_{x,y}\|u_xv_y\|=(\sum_x\|u_x\|)(\sum_y\|v_y\|)\)。
这是可直接核算的修补，不声称原件已经明确写出该localization公式或完整解析比较。

## 3. 不依赖上述修补的真实有限商与kernel

这一项直接从[§8.1 Lem8.3](https://arxiv.org/html/2602.15941v1#S8.SS1)的frame得到。
固定\(L=L_D\subset\mathbf Q\)，\(a_p\ne0\)、\(v_p(a_p)=n_p<\infty\)，定义

\[
 e_{p,k}:L\longrightarrow\mathbf Z/p^k\mathbf Z,
 \qquad x\longmapsto a_px\pmod {p^k}.
\]

**本次直接推导**：

\[
 \ker e_{p,k}
 =\{x\in L:v_p(x)\ge k-n_p\}
 =p^kL=L(D-k[p]),\qquad L/p^kL\cong\mathbf Z/p^k\mathbf Z.
\]

第二个等号因\(x/p^k\)在其他prime不改变valuation约束。
存在\(x_0\in L\)达到最小\(p\)-valuation \(-n_p\)，故\(a_px_0\)为单位；
整数倍\(mx_0\)遍历有限商，证明surjectivity。这是原群上的reduction，非自由复jet。
对有限多regular prime，以CRT合并为\(e_m\)，kernel为\(mL\)。

若\(n_p=\infty\)，则\(pL=L\)、\(a_p=0\)、\(L/p^kL=0\)。
因此singular prime处的frame商没有非平凡jet，不能同时宣称全局允许任意pole、
而同一个frame又检测其有限消失阶。
尤其[§2.6](https://arxiv.org/html/2602.15941v1#S2.SS6)的\(\Theta(p)=\mathbf Z[1/p]\)
正是这一情形；在该对象上直接做本prime的reduction不会恢复全部prime-power迹。

原群全局到局部有限商有kernel，不等于“开集restriction的kernel”。
后者在上述localization模型中是injective；两者不能混作一个评价定理。
对small sections，\(e_{p,k}\)仍是set map，但小球未必覆盖整个商。

## 4. tensor、过滤与boundary的准确作用

[Prop2.9](https://arxiv.org/html/2602.15941v1#S2.SS4)给乘法
\(L(D_1)\otimes_{\mathbf Z}L(D_2)\cong L(D_1+D_2)\)。
对regular prime，前节kernel形成乘法消失过滤：

\[
 L(D_1-k[p])\,L(D_2-\ell[p])
 \subset L(D_1+D_2-(k+\ell)[p]).
\]

这是valuation可加的直接推导；若某项\(n_p=\infty\)，减有限阶仍为∞，
该divisor过滤本身失去有限阶分辨率。
metric与frame满足
\(\|x\otimes y\|=\|x\|_1\|y\|_2\)、
\(\xi(x\otimes y)=\xi_1(x)\xi_2(y)\)、
\(\tau(x\otimes y)=\tau_1(x)\tau_2(y)\)。

[Thm8.5](https://arxiv.org/html/2602.15941v1#S8.SS2)恢复
\(Y_{\mathbf Q}=\mathbf Q^\times\backslash\mathbb A\)的framed moduli；
[Thm8.6](https://arxiv.org/html/2602.15941v1#S8.SS2.SSS1)核上述tensor与adele乘法；
[Thm8.15](https://arxiv.org/html/2602.15941v1#S8.SS6)核frame/root对偶保该monoid。
root乘法在**每个有限环**\(\mathbf Z/m\mathbf Z\)计算：

\[
 \langle\rho(1/m),x\otimes y\rangle
 =\langle\rho_1(1/m),x\rangle
  \langle\rho_2(1/m),y\rangle\pmod m.
\]

兼容性是有限环投影保乘法，singular集合取并、支持取交。
不能把这个等式改为\(\mathbf Q/\mathbf Z\)上的普通双线性coproduct；
该群与自身的普通tensor为零。未消费Rem8.13的Ind-ring解释作为额外设施。

## 5. 独立前端与本轮准入结论

前节给真实加法群、局部商、kernel、乘法及消失过滤，强于任意插值标签；
不读ζ零点。这是可消费的**局部预算前端**，不是Weil正性的等价重述。
但是它还没有同一minor上的全位高度／容量不等式。

最廉价容量负测已在该原对象内部：
\(L=\mathbf Z[1/p],\lambda>0\)含任意小的非零\(p^{-j}\)，单位球有无限元素；
\(\lambda=0\)时约束更为空。对经典有限support、\(L=\ell\mathbf Z\)、\(\lambda>0\)，
小球计数只是\(2\lfloor(\lambda|\ell|)^{-1}\rfloor+1\)。
这两个本次直接计算说明：既不能从“rank one”取得一般有限容量，
也不能从这个单curve计数读出平方上的完整mixed Weil型。

尚欠：解析原源\(f\)／物理\(r=e^{u/2}f\)到此载体或对应的实际map；
合法principal关系与旧非根双测试；同一global对象的高阶评价非退化；
独立全位容量及其完整Γ、全部素数幂、pole/contact与全复源比较。
有限quotient不是带原\(du/D_{\log}\)费用的连续线性map。
没有这些输入，本paper候选不能晋级数学合同；不据此排除新复提升、相对载体或transverse动力学修复。
本稿没有构造一般g／连续／数域的对应物，也没有证明其不存在。

## 6. 实际核读与证明归属

本次只使用v1 HTML，没有下载PDF、调用zeros或重证全部论文。
实际核读：§2.1–2.5的定义及Props2.2/2.4/2.7/2.9/2.11的原证明；
§2.6的Abel–Jacobi定义及边界解释；§3定义/乘积与Thms3.4/3.6/3.11证明；
§4.1–4.4的定义／结构；§5.1–5.2及Prop5.1全部原证明；
§8.1–8.6中Lem8.3、Thms8.5/8.6、Prop8.9、Prop8.11、Lem8.14、Thm8.15原证明。
§8调用的Appendix A.6/A.7未在本次重读；涉及全部dual结构时仍保该来源依赖。
这里只独立补出所需有限商kernel及从有限level恢复frame的部分，不声称付清全部Pontryagin dual结论。

原证明另有可局部修正的表述失误：Prop2.4说任一固定prime的valuation有下界，
与\(L=\mathbf Z[1/p]\)不符；固定非零\(q\in L\)在几乎处\(v_p(q)=0\)，
只推出\(\inf v_p(L)\le0\)，并非所有\(x\in L\)均\(p\)-整。
结论可按Prop2.2证明修复：对\(q^{-1}L\supset\mathbf Z\)用已核的CRT分类，再缩回。
因此不把原证明的错误句当paid前件；rank-one分类、有限商及tensor结论保留。

实际瓶颈未变：真实局部restriction前端现在明确，经典同源source map与独立global容量仍未给出。
最强旧whole \(4/5\)、危险核心、完整Sonin低频及Ξ门均未受此来源审查改变。
