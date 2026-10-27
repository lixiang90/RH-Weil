# Raum§5：Chow值模性量词、native系数与前提运输

2026-10-28；/root/unit_modularity独占稿。执行STATE唯一[来源门](../causal-strategy/next-unitary-modularity-premise-gate.md)，同G20261027／原0c4f。完整核读并目视固定Raum v2的§5 PDF52–56；只定位必要的先前定理/定义陈述及Li–Liu v5 Hyp4.5，不审§1–4深层证明，不追引文，不改STATE/cadence/Git。出稿不代root消费。

## 1. 固定原件与证明层级

Raum原PDF58页、644075 bytes，raw SHA256 `8a92b4cac23ed6a26e70575919f2a13377715e0e8e5ad38c339f771bc5d2c7eb`；Li–Liu v5原PDF66页、1263440 bytes，raw SHA256 `b3705e15817c142a2319660f12b07bf3871e13389d6d5557397c776809cec289`。原件本地路径沿上一来源记录，不改原PDF。

§5的实际依赖链为：cycles与Hodge补次数(5.2)–(5.5)；Prop5.1给symmetry；Liu的genus1模性作为Th5.2被引用；Prop5.4用finite gluing和cycle pushforward组织Fourier–Jacobi系数；再调用作者Theorem C的automatic convergence，最后证明Theorem A及Corollary B。Theorem C的陈述见PDF4，深层证明本次**cited而非重新认证**。Th5.2和旧pullback来源也保cited。本稿另核两个native系数问题，不能把“来源有定理”说成本次已逐式证明其全部规范。

## 2. 对象、签名、level与系数空间

Raum§5固定CM域E/F、Hermitian整数格L。其一个实place的复Hermitian签名为(p,1)，其余无穷place正定；Γ为neat、stable congruence subgroup，特别逐元素固定disc(L)=L∨/L。X=Γ\Gr⁻(L_R⁻)为相应unitary Shimura variety的一个复连通分支。作者说明经有限cover可处理neat compact level的分支，并以(5.1)的有理Chow pullback注入传递结果；这不是stack上的无条件等距规范。

特殊cycle的原始codimension是rank(t)，不是一律genus g。(5.4)的native系数为

\[
 Z_L(\mu;t)\,\omega_X^{g-\operatorname{rk}(t)},
 \qquad t=\tfrac12\langle\lambda,\lambda\rangle,
\]

ω为dual Hodge bundle的第一Chern类，所以系数确在CH^g(X)_C。其Weil type不是任意新选的positive representation，而是固定nearby totally positive incoherent Hermitian space所给的type，限制到lattice-coset指标后为C[disc(L)^g]上的\(\widetilde\rho_L^{(g)}\)。作者特别区分它与coherent Weil representation及某些SU/U限制后才相同的情形（Remark5.3）。

Li–Liu Hyp4.5（PDF24）的对象为每个compact open K⊂H(A_f)、每个K不变有限Bruhat–Schwartz φ_f，以及**每个复代数线性泛函**l:CH^m(X_K)_C→C。结论是l作用后的生成函数绝对收敛且属于规定weight的automorphic空间。不是只测试连续对偶、有限选定coordinate、height functional或cohomology quotient。这里的CH^m尚不自动为homologically trivial CH^m,0；后者的投影/lift构造由后续设施另付。

两文moment字母也不能直接混同：Li–Liu Notation2.2(H1)（PDF10，必要陈述）用T_LL(x)=((x_i,x_j)_V)，Raum用½⟨λ,λ⟩。若逐项同一索引，须明示( , )_LL=½⟨ , ⟩_Raum的form字典，再相应运输dual lattice、additive character、Weil type和selfdual measure；不能一边缩form一边保所有dual/measure不变。Corollary B给qualitative模性前提的cited运输，本稿没有由它领取精确height/Petersson系数或原物理费用。

## 3. 为什么“所有代数泛函”能给有限张量

作者在PDF56先对每个l∈CH^g(X)_C^∨调用Theorem C，得到l(θ_L)∈M=M_(p+1)(\widetildeρ_L^(g))。M在固定weight/type/level下有限维。这个量词很强，足以推出一个**共同的有限cycle span**，不必假定整个Chow群有限维。

标准有限维核对如下。取M的基f_1,…,f_d，并选有限组Fourier指标t_1,…,t_d，使系数矩阵(c(f_j;t_i))可逆；存在性来自Fourier展开的注入。用θ_L在这些指标的Chow系数a_(t_i)解出固定Z_1,…,Z_d。对任意l，l(θ_L)由这d个值唯一决定，故全部指标t有

\[
 l\bigl(a_t-\sum_j c(f_j;t)Z_j\bigr)=0.
\]

全部代数泛函分离向量，遂a_t=Σ_j c(f_j;t)Z_j。因而θ_L=Σ_j f_j⊗Z_j∈M⊗CH^g(X)_C，是代数有限张量，不是未定义的Chow级无限和。每个l作用后是有限个真实holomorphic modular forms之和，其Fourier展开有通常的绝对/局部正常收敛。无需给CH任何Hilbert/Banach范数，也没有得到对l、level、genus或物理源统一的operator norm。

这一核对直接支付所声明的代数泛函量词；它不使所有代数线性泛函在某个外加Chow完成化上连续，也不容许把无限物理source尾直接塞入有限张量。

## 4. 半正定Jacobi指标的Hodge次数补注

以下是本项目对native系数的明确重闭，**不是原PDF已经逐字写出的乘子**。PDF54的Prop5.4允许m半正定，令k=rank(m)=rank(\widetilde L)≤g−1，Y为正定span \widetilde L的正交补对应的Shimura subvariety，i:Y→X。

PDF55将genus1的θ_Y^Kudla直接置于CH^(g−k)(Y)，但按(5.4)，native genus1 θ_Y的系数属于CH¹(Y)。当k<g−1时，必须先乘固定

\[
             \omega_Y^{g-k-1}
\]

再push，才能取得codimension g。对单个upper-block正交分量u，记e=rank(u)∈{0,1}；rank(t)=k+e。native genus1系数是Z_Y(u)ω_Y^(1−e)，并且i*ω_X=ω_Y。因此projection formula给

\[
 i_*\!\left(Z_Y(u)\omega_Y^{1-e}\omega_Y^{g-k-1}\right)
 =i_*Z_Y(u)\,\omega_X^{g-k-e},
\]

恰为目标(5.4)的native次数。固定Chow乘子不改τ的模性。Y上genus1权为p+1−k，positive rank-k Jacobi theta的权为k，合成仍p+1；不要求k=g−1。退化m须在真正正定的rank-k lattice上构造theta并沿原tuple关系pullback，不能把正定index定义(2.17)原样套给退化size-(g−1)矩阵。

特别地，m=0给ω_X^(g−1)乘genus1系列；若k=g−1，额外固定乘子为1，但u=0的native genus1系数**仍有ω_Y**。所以PDF55–56只写raw Z_Y(u)的展开不能在零指标处被当作已保全部Hodge次数。只有k=g−1且e=1时，该raw项的次数直接相符。

本次不无条件消费原印(5.6)对所有rank的字面等式。标准补注后的native次数和modular weight可重闭；Theorem A的独立cited地位与这段局部规范审查分开，不由此宣告整篇定理失效。

## 5. Gluing的sum-map与averaged projection不是同一个map

另一个独立规范点见PDF55：M=\widetilde L^⊥⊕\widetilde L⊂L，d=[L:M]，原文π^ρ在可glue的basis element上给e_(ν+L)/d。PDF56的系数比较未显式解释这个1/d如何抵消；必要定义(2.17)的positive Jacobi theta是裸指数和，无相应d前因子。

标准finite gluing中，I=L/M为A_M中的isotropic subgroup，A_L=I^⊥/I。固定μ∈A_L及lift ν_0∈I^⊥，L-coset中的每个λ按正交投影唯一写成λ=x+y；其M-coset数据属于ν_0+I。这个fiber是不同向量的分割，并不是每个λ被重复d次。故恢复native系数1的map应是quotient **sum-map**

\[
 \Sigma^\rho(e_\nu)=e_{\nu+I}\quad(\nu\in I^\perp),
 \qquad\Sigma^\rho=d\pi^\rho,
\]

非image处为0。d为每个固定\widetilde L的常数，Σ^ρ仍是intertwiner；若用原π^ρ，就须在该项明确乘d。它不能因π是合法projection而被自动省略。neat Γ与cycle inclusion也没有在§5中给出可免费抵消d的统一stack/degree规范。

一个仅核map normalization的标准负对照：取Z²的标准点积，Q(x)=|x|²/2，M=2Z²，L={(a,b)∈Z²:a≡b mod2}。L是even overlattice，d=2，I={0,(1,1)}在A_M中isotropic。positive theta向量的constant term在M侧只有e_0；原averaged map送成e_0/2，而native θ_L constant term为e_0。Σ^ρ给正确的1。此toy只核finite gluing map的系数方向，不是unitary Theorem A/B的反例，也没有获得任何height或Pet范数。

于是可把本项目消费用的FJ式明确组织为：对每个固定正定span，先将native genus1 θ_Y乘ω_Y^(g−k−1)，作i_*，再tensor positive rank-k theta并施Σ^ρ；对各有限orbit项求和。前述唯一正交分解和projection formula给其native系数。这样重闭的是模性成员性所需的标准有限组织；不把原(5.6)的未解释单位系数/所有rank字面运输当成无条件已审，也不保留averaged map的任何等距解释。

## 6. Corollary B的Schwartz与level量词

PDF56明确从所有Hermitian lattice及其dual-coset indicator扩到**全部有限adelic Bruhat–Schwartz函数**。其实际代数内容是有限张成：compact support和local constancy允许把一个φ_f写成有限个coset indicators；取共同足够小的integral lattice，并用有限adelic弱逼近选rational coset代表，再缩lattice使代表落在dual，便落入作者所用lattice-coset类。没有φ_f的无限lattice展开、截断极限或跨lattice uniform bound。

作者还使用O_E^×/O_F^×有限，使其SU_(g,g)(O_F)框架包含U_(g,g)(O_F)的某congruence subgroup；有限phase/central-character条件必须按原representation保存，不能将SU上的type与U上的type直接视作同一个trivial type。对给定compact level，取共同neat/stable细化并分解有限多个Shimura分支；在原开放Γ\D及适用的compact模型上，(5.1)与标准finite étale push–pull在Q/C系数下给下降/唯一性。若在细层的生成函数是有限tensor，trace/d的有限线性作用仍是有限tensor，从而对目标level的每个代数l都得到规定的modular函数。这里没有把一般F=Q的toroidal边界cover自动当作étale；若另用compactification，其boundary pullback/正则化须按原模型另付，不能借这一句省去。这只恢复作者Corollary B的每个fixed input/level qualitative运输，不给level成长、height规范或原source费用。

因此在作者cited Theorem C/Th5.2及上述明确native补注的消费下，Hyp4.5的“任意代数l、任意finite φ_f、任意fixed compact level”有具体来源，不再只保formal modular坐标陈述。仍不包括582的S0/A1强完成输入、一般noncompact physical r或任何Chow-norm连续延拓。Hyp4.5的解除也不自动解除Li–Liu其他假设。

## 7. 净值、范围与实际阅读记录

已核的是新unitary来源设施的代数量词和有限运输；native Hodge次数及sum/average归一化作为明确补注与原文分开。没有新的经典Weil source、405 principal身份、537非根/whole coverage、原du/zero-extensionDlog或强源成长费。primitive/mixed与完整Γ/contact/powers/双pole比较仍由root/height稿另核，不能从模性或finite tensor倒填。

建议按来源审查/标准前件恢复0数学轮结算；没有新classic whole/core/coupling/Ξ后果。原literal/整体Theta/7.4冻结保持，不用unitary结果回填旧orthogonal定义；不续rank/level/weight、后章或paper。

实际范围：Raum PDF52–56全文提取并全部目视；PDF4 Theorem C陈述定位，PDF6引言roadmap目视；PDF29 (2.17)定义块文字核读，不审其深层证明。Li–Liu PDF24 Hyp4.5/Remark4.6/Prop4.7陈述块完整目视，PDF10–11 moment/Gaussian/Fourier必要定义由本稿及height分支对齐。一次locator误选Raum PDF26的首600字符输出，未据该§2 proof片段消费任何命题或执行其证明。无新网页、PDF下载或引文读取。

本稿生成的private render缓存为`unit-modularity-raum-52.png`至`-56.png`、`unit-modularity-raum-p06.png`、`unit-modularity-li-liu-p24.png`，均在既有本地ignored文献目录；原PDF不变。root还须按实际终版及fresh重闭本稿所列补注，文件/hash不代语义审查。
