# Barreto 三页截图的独立数学链核查

2026-10-20。独占数学审核输出；不修改 STATE、notes 或轮数。审核对象是用户附的三页完整截图，并比较 root 主稿 `goals/reviews/2026-10-20-landau-siegel-determinant-and-weil-facilities.md` §§1–3。本文不以 AI 归属、作者声誉或媒体报道替代证明检查。

## 结论与核查边界

**通过本次局部审核，未发现截图论证的实质性缺口。** 非零性、同一个整数 minor 的各素数高阶整除、与 q 一致的无穷位上界，以及 prime-sum 到实零点距离的链条均可闭合。普通导数、加权三角形单项式空间、两种代数共轭和全局整数乘积预算都是必要的具体设施。这里没有得到完整 Weil 正性、RH 或本仓新的全源正性结果。

root 主稿 §§1–3 的 ceil 端点、specialisations 数量、m! 费用、(11)–(13) 的符号及反演、有限小 q 的 L(1,χ) 非消失补充均正确。未发现需要修改的数学项。此结论只覆盖直接审查的截图链及主稿上述部分，不代表重跑 Lean、不代表审核整个 OpenAI 发布、不代表独立重证 Montgomery–Vaughan 中全部基础定理。

## 1. 对象、整数格和 q 一致参数

χ 必须是 primitive nonprincipal **real** Dirichlet character。取 squarefree d≠1、|d|≤q，使 odd p∤q 时 χ(p)=(d/p)。工作环仅需 O=Z[√d]，无需最大整数环。代数共轭 α'=u−v√d 在 d>0 时不是复共轭。

对 x≥max(e³,√q)，设 B=2√(2x)q^(1/4)。矩形 0≤u<B/2、0≤v<B/(2√q) 的整数点数为两个 ceil 的乘积，至少等于面积 2x。α_i 和 α'_i 各自两两不同，且两种共轭的绝对值均小于 B。这也适用于负 d。

k=ceil(log(x²B)) 满足 3≤k≤x；因为 q≤x²，所以 B≤2√2 x，k≤3log x+O(1)≤x（在 x≥e³ 的起点亦成立）。因此 log k=log log x+O(1)，全部常数可绝对取定，不依 q 或 χ。

令 T={(r,s)∈Z≥0²:r+ks<x}，J=ceil(2x/k)。评价所有普通 jets 0≤j<J，在 {1,√d} 上展开，得到一个真正的整数矩阵。不能在这一步换成除以 j! 的 jets。

## 2. Wronskian 的行独立证明

若整数矩阵的行不满秩，存在有理系数非零 F，deg_z F<x、deg_w F<x/k，其所有 specialisations F(z,α'_i) 在 α_i 处有至少 J 阶零。选取一个非零 z 系数作为 w 的多项式，说明恒零 specialisations 的个数至多 deg_w F<x/k。因此非零 specialisations 数量至少 2x−deg_w F>x。

这些一元多项式张成的空间维数 ℓ≤floor(deg_w F)+1≤ceil(x/k)。该空间可选具有不同次数的 monic 基 g_b。普通 Wronskian W=det(g_b^(a)) 的最高可能项系数是不同整数次数上 falling-factorial 多项式的评价行列式；这是特征 0 下的 Vandermonde 型非零数。因此 W≠0，deg W<ℓx。

任一非零 specialisation 可以经常数可逆换基放到一列。若其在 α_i 有 J 阶零，那么这列的前 ℓ 个导数分别仍有至少 J−ℓ+1 阶零。由于 2ℓ−2<2x/k，整数端点给 J−ℓ+1≥ℓ。因此 W 在超过 x 个不同 α_i 各有至少 ℓ 阶零，与 deg W<ℓx 矛盾。行满秩，确有使用全部行的非零整数 minor D。

## 3. 惰性素数的高阶整除发生在同一个 D

对 k≤p≤x、χ(p)=−1，p 为奇素数且 p∤d。二项式同余及 Euler criterion 给 α_i^p≡α'_i mod pO。

设 h=floor(r/p)，将 monomial z^rw^s 换成 z^(r−ph)(z^p−w)^h w^s。展开后领先项仍是原 monomial，其他项 z^(r−pj)w^(s+j) 的 z 次数下降；其权为 r+ks−j(p−k)≤r+ks<x，所以仍在原 T 中。按 r 排序所得整数行变换是 unitriangular，保留此前固定列集合上的同一个 D。不同 p 可以使用不同的行变换，不影响最终对原 D 汇总 valuations。

关键点是 z^p−w 的零阶值在各评价点被 p 整除；每个正阶普通 z 导数的系数也被 p 整除（阶数大于 p 时为零）。乘积法则对 h 个因子逐项保留至少 p^h；额外的 z^(r−ph) 和 w^s 及 Leibniz 整数系数不造成分母。因此变换后整行的两个整数坐标均被 p^h 整除，v_p(D)≥Σ_T floor(r/p)。没有要求 jet 阶数小于 p；也没有未经支付的 divided-power 分母。

## 4. 无穷位高度、阶乘和 floor 损失

记 m=|T|、U=Σ_T r。计数得 m≪x²/k，而 T 内 x/3≤r<2x/3、0≤ks<x/3 的矩形给 U≫x³/k≫xm。整数边界只改变绝对常数。

每个普通 jet 在两种代数共轭下模至多 x^(2x/k)B^(r+s)。由于 s<x/k，这不超过 B^r(x²B)^(x/k)≤B^r e^x。若 a+b√d 的两个共轭均被 M 控制，则 |a|≤M、|b|≤M/√|d|≤M，故转换到整数坐标不漏额外 q 费用。

行列式展开给 log|D|≤U log B+xm+log(m!)。m≪x² 且 x≥e³，故 log(m!)≪m log m≪xm≪U；于是 log|D|≤U log B+O(U)。

另一方面 floor(r/p)≥r/p−1，损失至多 mΣ_(p≤x)log p≪xm≪U。小于 k 的素数用 Mertens 付 log k+O(1)。同一个非零整数满足 Σ_p v_p(D)log p=log|D|，所以

    Aχ(x)=Σ_(p≤x,χ(p)=−1) log p/p
          ≤ (1/2)log x+(1/4)log q+log log(3x)+O(1).

若 x<√q，右边的前两项至少 log x；若 x<e³，所有残余量可吸收入绝对常数。因此全 x≥2 的一致结论成立。

## 5. 从 prime-sum 到实零点：符号和有限 q

对 0<η≤1，partial summation 给 Σ_(χ(p)=−1)log p/p^(1+η)≤1/(2η)+(1/4)log q+O(log(2/η))。其中 η∫_1∞ log t·t^(−1−η)dt=1/η，而 η∫_1∞log log(3t)t^(−1−η)dt 可由 Jensen 控制为 O(log(2/η))。

所有 k≥2 prime powers 的和在 η∈(0,1] 一致 O(1)。p|q 的一次项之和为 O(log log(3q))：在 p≤log q 用 Mertens，在 p>log q 用 1/p≤1/log q 和 Σ_(p|q)log p≤log q。故

    L'/L(1+η,χ)=2Σ_(χ(p)=−1)log p/p^(1+η)−1/η
                 +O(log log(3q))
               ≤(1/2)log q+O(log(2/η)+log log(3q)).

完成 L 的 Hadamard 实部公式给 Σ_ρ Re(σ−ρ)^(−1)=L'/L(σ,χ)+(1/2)log(q/π)+(1/2)ψ((σ+a)/2)。已知所有非平凡零点 Reρ≤1，所以 σ=1+η>1 时每项非负；留下一个 real β 并舍去其他项是正确的**上界方向**。Γ 项在这段实 σ 范围一致 O(1)，于是 1/(1−β+η)≤log q+O(log(2/η)+log log(3q))。

取 η=(log q)^(−2)，右边为 log q+O(log log(3q)) 且大 q 时正。先对实际正分母取倒数，再减 η，得到 (1−β)log q≥1−O(log log(3q)/log q)。这没有把上界倒数的方向写反。

大 q 给统一正下界；有限个小 q 还必须使用 L(1,χ)≠0 和解析零点孤立性，取得每个 L 的 1 邻域无零并取有限最小值。只说 character 有限而不排 β→1 不充分；root 主稿已明确付这一补充。截图结论是距离 1 的统一 c/log q 排除，不是 β=1/2。

## 6. 对一般 g-integer 的可移植与不可自动移植部分

可以抽象的是：实际 filtered sections/多项式及评价 jets、非退化评价预算、局部约束的非负 multiplicity、全局高度或 pole 容量，以及**同一对象**的全局 product formula。它们正好回应路线图中“真实截面—有效性—容量”的责任，且没有在定义中读取未知零点位置。

不可由正 P/Π、Euler 乘积或反射对偶自动得到的是：O 的加法格、有限位 reduction、Frobenius 交换二次共轭、普通导数的整性、整数 minor 的全球 valuations。一个自由乘法半群没有足够结构定义上述设施。χ=1 时不存在 χ(p)=−1 的惰性类；将 d 变成平方又破坏 α_i、α'_i 独立及 Wronskian 评价设计，故不能照搬成经典 ζ 的 RH 证明。

数域可以借 norm/product formula 及各 prime ideal 的 residue Frobenius，但全部嵌入、局部次数与 ramification 要重新结算，当前链没有任意 Dedekind ζ 的正性结论。函数域有主除子 degree 0 与 RR 容量，但正特征下普通 Wronskian 可能把 1、z^p 判为相关，必须重新使用合适的 separability/Hasse jets 设施。连续正例可以由独立 ODE/energy 实现容量证书；它们不需要字面的整数格。这些都是候选接口而非已建立的普遍推广。

本链约束特定 real-character prime bias 的一个标量。完整 Weil 正性需要全部 complex test、mixed terms、规范 Γ、prime powers、pole/contact 的同源带符号比较；正的 volume 或非零 D 本身不提供这些惯性信息。一般离线复零点造成振荡方向，尚无构造将其变成这里的非负局部 multiplicity。

## 来源与实际读取范围

- **直接数学审核对象**：用户三张图片中的 Kevin Barreto 三页稿，无稳定公开地址及版本信息；不冒认已取得原 PDF。未以不明地址补全任何关键步骤。
- **Banks**：`arXiv:2610.15483v1`，2026-10-11，https://arxiv.org/html/2610.15483v1 ，及记录 https://arxiv.org/abs/2610.15483 。浏览取得论文页面及完整 HTML，用于交叉确认二次/双二次评价格、Frobenius 整除与所陈述结论；未将其显式常数替换本截图常数。
- **Tao**：2026-10-19，https://terrytao.wordpress.com/2026/10/19/a-sketch-of-the-proof-of-non-existence-of-siegel-zeroes/ 。本 agent 实际检索取得分类页 https://terrytao.wordpress.com/category/mathematics/?iframe=true&preview=true%2Ffeed%2F 和搜索缓存长摘录，读到 adelic polynomial method、整数 product formula、评价格、Hadamard 与 valuation 机制及 Barretto sharpened bound 的记录；直接文章 URL 在本 agent 的 open 调用报不可访问。root 有独立直接文章读取，不将其范围冒记为本 agent 全文审核。
- **Green**：`hexagon:2610.00311v2`，https://hexagonmath.org/2610.00311v2 。本 agent 获检索记录显示初稿 2026-10-17、v2 解耦两参数；本地数学结论不依其全文审核。未把该 identifier 当作 arXiv ID。
- **基础外部输入**：Chebyshev、Mertens、real character 的二次域字典、Euler product、L(1,χ) 非消失、完成 L 的 Hadamard log derivative。本文核查其使用范围与符号，不声称重证所有基础来源。

本输出作为独立审核原稿交 root 消费；文件存在及本审核结论不自动构成新的数学研究轮、经典全源正性或宏观目标完成。
