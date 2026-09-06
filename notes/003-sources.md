# 文献与证据边界（本轮增补核对日期：2026-09-06；历史条目保留各自核验范围）

## 一手与权威来源

1. Pierre Deligne, *La conjecture de Weil I*, Publ. Math. IHES 43 (1974), 273–307. 证明有限域上 Weil 猜想的 RH 部分；本文的权重结论应以此为历史/数学基准。  
   https://publications.ias.edu/node/368

2. A. Grothendieck, *Standard Conjectures on Algebraic Cycles* (Bombay Colloquium, 1968/1969). 原文把所需内容概括成 Lefschetz 型存在性与 Hodge/Weil 型正性，并解释它们如何导向 Weil 猜想。  
   https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/StandardConjs.pdf

3. Steven L. Kleiman, *Algebraic Cycles and the Weil Conjectures*. 系统整理 Weil cohomology、standard conjectures 与 Weil 猜想之间的形式蕴含。  
   https://agrothendieck.github.io/divers/kleimanweil.pdf

4. André Weil, *Sur les “formules explicites” de la théorie des nombres premiers* (1952). 数域显式公式与正性判据的原始来源。  
   https://cds.cern.ch/record/471308

5. Christopher Deninger, *Some analogies between number theory and dynamical systems on foliated spaces* (ICM 1998). 明确描述数域算术 scheme 所期待的上同调/动力系统形式，并指出对 `Spec Z` 尚无这类完整理论。  
   https://ems.press/books/dms/246/4682

6. Alain Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function* (1998/2000). adele 类空间、吸收谱/共振以及显式公式的迹解释。  
   https://arxiv.org/abs/math/9811068

7. Alain Connes, Caterina Consani, Henri Moscovici, *Zeta Spectral Triples* (2025 preprint). 构造有限 Euler 截断的自伴谱模型；原摘要明确说，若能严格证明谱及正规化行列式的极限收敛，就会得到 RH。  
   https://arxiv.org/abs/2511.22755

8. Alain Connes, Caterina Consani, *Spectral Triples and Zeta-Cycles* (2021 preprint; 2023 journal version). 给出 prolate 向量的原始构造，明确要求 `f(0)=hat f(0)=0`，说明压缩 Fourier 特征值只近似为 `+/-1`，并把 prolate 向量表述为 Weil 型的 near-radical，而非精确有限区间 radical。  
   https://arxiv.org/abs/2106.01715

9. Alain Connes, Caterina Consani, Henri Moscovici, *Zeta Zeros and Prolate Wave Operators* (2024). 说明 `E(S_0^ev)` 位于全局 Weil radical、prolate 正谱产生有限支撑 near-radical，以及向半局部 prolate 结构推广的算子框架；这些结果解释极小 residual，但没有给出本仓库定理 AM 所需的 uniform residual/gap 率。  
   https://arxiv.org/abs/2310.18423

10. Alain Connes, *The Riemann Hypothesis: Past, Present and a Letter Through Time* (2026 survey/preprint). 给出 Weil 二次型的有限素数逼近与中心线零点，并把有限到无限 Euler 乘积的收敛列为潜在证明路线。  
   https://arxiv.org/abs/2602.04022

11. Alain Connes, Caterina Consani, *On the Absolute Geometry of Spec Z* (2026 preprint). 构造 `Spec Z` 的绝对/F1 几何及局部 Weil 群/周期轨道结构；它提供几何候选，但其摘要不声称已建立 G1–G4 或证明 RH。  
   https://arxiv.org/abs/2606.06604

12. Hyman Bass, *The Ihara--Selberg Zeta Function of a Tree Lattice*, International Journal of Mathematics 3 (1992), 717--797. Bass determinant formula 的一手来源；文档 078 使用其有限正则图 specialization。  
   https://doi.org/10.1142/S0129167X92000357

13. Toshikazu Sunada, *L-functions in Geometry and Some Applications*, Lecture Notes in Mathematics 1201 (1986), 266--284. 图 zeta 的谱解释以及 Ihara RH 与 Ramanujan 条件联系的一手来源。  
   https://doi.org/10.1007/BFb0075662

14. Alexander Lubotzky, Ralph Phillips, Peter Sarnak, *Ramanujan Graphs*, Combinatorica 8 (1988), 261--277. 显式 Ramanujan 图族与最优邻接谱界的一手来源。  
   https://doi.org/10.1007/BF02126799

15. Adam W. Marcus, Daniel A. Spielman, Nikhil Srivastava, *Interlacing Families I: Bipartite Ramanujan Graphs of All Degrees*, Annals of Mathematics 182 (2015), 307--325. 证明每个 degree `>2` 都存在无限二分 Ramanujan 图族。  
   https://annals.math.princeton.edu/2015/182-1/p07

16. Barry Simon, *Trace Ideals and Their Applications*, 2nd ed., Mathematical Surveys and Monographs 120, AMS (2005). Schatten ideals、Fredholm determinants 及 higher regularized determinants 的标准权威参考；文档 079 的 diagonal prime model 另给出所需公式的直接证明。  
   https://bookstore.ams.org/SURV/120

17. E. C. Titchmarsh, revised by D. R. Heath-Brown, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford University Press (1986/1987), especially Theorem 14.25(c) for the Mertens-function RH equivalence. 文档 080 的 zeta specialization 采用这一标准 Perron 等价；finite incidence/Hodge factorization 则在文档中直接证明。  
   https://old.maa.org/press/maa-reviews/the-theory-of-the-riemann-zeta-function

18. Michel Balazard, Éric Saias, *The Nyman--Beurling Equivalent Form for the Riemann Hypothesis* (1998 preprint). 给出 fractional-part Mellin identity，并整理 Bercovici--Foias 的精确 division-range characterization；文档 081 的 Mellin division package 以此为解析背景。  
   https://www.esi.ac.at/preprints/esi623.pdf

19. Luis Báez-Duarte, *A Strengthening of the Nyman--Beurling Criterion for the Riemann Hypothesis*, Rendiconti Lincei 14 (2003), 5--11. 证明只用 integer dilations 已足够，并给 constructive approximants。  
   https://arxiv.org/abs/math/0202141

20. Anne de Roton, *Généralisation du critère de Beurling--Nyman pour l'hypothèse de Riemann*, Transactions of the AMS 359 (2007). 把 density/zero-free equivalence 推广到广泛 Dirichlet series / Selberg-class data。  
   https://doi.org/10.1090/S0002-9947-07-04261-4

21. Jean-François Burnol, *A Lower Bound in an Approximation Problem Involving the Zeros of the Riemann Zeta Function*, Advances in Mathematics 170 (2002), 56--70. 证明 Nyman--Beurling finite distance 的 critical-zero lower bound，并构造相关 Hilbert--Pólya vectors。  
   https://doi.org/10.1006/aima.2001.2066

22. Sandro Bettin, J. Brian Conrey, David W. Farmer, *An Optimal Choice of Dirichlet Polynomials for the Nyman--Beurling Criterion*, Proceedings of the Steklov Institute of Mathematics 280 (2013), S30--S36. 在 RH 与 reciprocal-derivative moment hypothesis 下达到 Burnol constant，说明 `1/log N` 是 conjecturally sharp 的 Hodge-distance scale。  
   https://arxiv.org/abs/1211.5191

23. Hugh L. Montgomery, Robert C. Vaughan, *Hilbert's Inequality*, Journal of the London Mathematical Society (2) 8 (1974), 73--82. 给 separated frequencies 的 weighted Hilbert/large-sieve bilinear bound；文档 085 用其 continuous approximate-Plancherel consequence控制 Farey boundary 的 `y>=N^2` 部分，文档 150 用 `lambda_n=logn`, `delta_n asymp1/n` 的 mean-value consequence把 Abel polynomial off-diagonal从粗 `NlogN` 降为 `N`；文档 205 用其圆周版本逐 Toeplitz diagonal 闭合 adjacent product family；文档 208 用 Dirichlet-polynomial mean-value 版本证明首个 boundary entry 的 normalized height mean square 具有正极限；文档 209 用圆周版本把所有 sub-square-root primitive ratio boxes 渐近对角化；文档 210 结合 dyadic von Mangoldt 能量把单-box 范围推进到 `AB<=XL^(2-epsilon)`；文档 212 用圆周 mean square 闭合 fixed-aperture 双曲 radial chain，并将 non-seam aperture crosses 排除到 `o(N)`。文档 223 将 Dirichlet-polynomial mean-value 逐 Hilbert--Schmidt 坐标相加，在每个长度 `X/sqrt(log X)` 的区间内闭合 actual supercritical adjacent aggregate；dimension-free 扩张在笔记中重证。
   https://doi.org/10.1112/jlms/s2-8.1.73

24. Ethan S. Lee, Nicol Leong, *New Explicit Bounds for Mertens Function and the Reciprocal of the Riemann Zeta-Function* (2024 version). 给 classical 与 Korobov--Vinogradov 形状的显式 Mertens bounds；文档 085 只使用存在某个正常数的 stretched-exponential 渐近形状。  
   https://arxiv.org/abs/2208.06141

25. W. Duke, J. Friedlander, H. Iwaniec, *Bilinear Forms with Kloosterman Fractions*, Inventiones Mathematicae 128 (1997), 23--43. 给 arbitrary coefficients 的 bilinear modular-inverse exponential sums 的无条件 bounds，并讨论 incomplete Kloosterman completion；文档 092 精确引用其 Theorems 1--2。  
   https://doi.org/10.1007/s002220050135

26. Sandro Bettin, Vorrapan Chandee, *Trilinear Forms with Kloosterman Fractions*, Advances in Mathematics 328 (2018), 1234--1262. 给 arbitrary coefficients 的 trilinear modular-inverse bounds，并应用于 determinant equations；文档 092 引用其 Theorem 1，同时审计其与 paired cotangent kernel 之间尚需完成的 dyadic bookkeeping；文档 220 审计 Corollary 1 的 fixed-determinant hypotheses，明确其两个 smooth weights 不能直接替换为 von Mangoldt weights；文档 221 改用二维 Selberg 外筛，并逐式推出 divisibility main term 的 exact gcd density 与 level error；文档 222 将同一 formula 推广到 moderate unbalanced aspect，并在 extreme aspect 改用两线性形式直接筛。
   https://arxiv.org/abs/1502.00769

27. J. Barkley Rosser, Lowell Schoenfeld, *Approximate Formulas for Some Functions of Prime Numbers*, Illinois Journal of Mathematics 6 (1962), 64--94. 给 `n/phi(n)` 等经典显式估计；文档 093 只使用其推论 `max_(n<=N)n/phi(n)<<loglog(3N)`。  
   https://doi.org/10.1215/ijm/1255631807

28. Luis Báez-Duarte, Michel Balazard, Bernard Landreau, Eric Saias, *Sur l'autocorrélation multiplicative de la fonction « partie fractionnaire »* (2003), 后发表于 Ramanujan Journal 9 (2005), 215--240。系统研究 Nyman--Beurling fractional-part features 的 multiplicative autocorrelation 与 rational cotangent formulas；文档 095 只把它作为 actual Gram geometry 的背景，不调用未经重证的渐近结论。  
   https://arxiv.org/abs/math/0306251

29. Edvinas Goldštein, Andrius Grigutis, *On a Positivity Property of the Real Part of the Logarithmic Derivative of the Riemann Xi-function* (2022 preprint; 2024 journal version). 研究 `1/2<sigma<1` 中 `Re xi'/xi` 的局部正性与假想 off-line zeros 的影响；文档 131 用它说明 scalar 局部正性不同于全右半平面 Pick-kernel 正性，不调用其估计证明结构定理。  
   https://arxiv.org/abs/2201.08599

30. Andrius Grigutis, Lukas Turčinskas, *Note on the Positivity of the Real Part of the Log-derivative of the Riemann Xi-function Near the Critical Line* (2025). 给出离中心线约 `1/sqrt(log t)` 区域内已知 critical-line zero contribution 的显式下界；同样不声称全局 passive continuation或 RH。  
   https://arxiv.org/abs/2509.18963

31. NIST Digital Library of Mathematical Functions, §5.9.19 与 §5.11.9。前者给 Gamma derivatives的 Euler integral representation，后者给 bounded real part上一致的 vertical Stirling decay。文档 144 用它们控制 single-wave derivative与 countable Gamma-packet tails；carrier、compactness及 distribution uniqueness论证在文档中给出。  
   https://dlmf.nist.gov/5.9.E19  
   https://dlmf.nist.gov/5.11.E9

32. Patrick X. Gallagher, *A Large Sieve Density Estimate Near sigma=1*, Inventiones Mathematicae 11 (1970), 329--339. Lemma 1把 exponential sum在有限 frequency band上的 mean square控制为 coefficients在短 frequency intervals内的 sliding sums；文档 151先作 frequency translation，再将其用于 modulated arithmetic lag measures。  
   https://doi.org/10.1007/BF01403187

33. Larry Guth, James Maynard, *New Large Value Estimates for Dirichlet Polynomials*, Annals of Mathematics 203 (2026), 623--675. 证明新的 Dirichlet-polynomial large-value bounds、zero-density exponent `30/13`，并推出长度 `x^(17/30+o(1))` 的 primes-in-short-interval asymptotics。其主定理针对 `|b_n|<=1` 的 dyadic polynomial及 `1`-separated large-value points；文档 151 与 168只把它列为 layer-cake/superlevel 的潜在输入，不把它冒充 continuous balanced `L2` Selberg profile。
   https://doi.org/10.4007/annals.2026.203.2.6

34. R. C. Vaughan, *Sommes trigonométriques sur les nombres premiers*, C. R. Acad. Sci. Paris, Série A 285 (1977), 981--983；以及 *On the distribution of alpha p modulo 1*, Mathematika 24 (1977), 135--141。Vaughan identity及其把 prime sums分解为 Type I/II sums的原始语境。文档 153所用的 centered全整数形式不依赖引用，而由 `log=Lambda*1` 与 `mu*1=epsilon` 逐行重证。  
   https://www.cambridge.org/core/journals/mathematika/article/abs/on-the-distribution-of-p-modulo-1/98751083E04CE57F16D94FCF4D3B94E2

35. B. Saffari, R. C. Vaughan, *On the fractional parts of x/n and related sequences. II*, Annales de l'Institut Fourier 27 no. 2 (1977), 1--30，尤其 Lemma 5。其式 (6.4) 在 RH 假设下给 uniform multiplicative Selberg variance；同一引理另列基于 zero-density hypothesis 的 unconditional long-interval版本。文档 169 使用前者证明 RH `=>` polylogarithmic profile，并明确禁止把 conditional estimate冒充无条件输入。
   https://doi.org/10.5802/aif.649

36. Levent Alpöge, Raphael Furman, *More than two thirds of the zeros of the Riemann zeta function are simple and on the critical line* (arXiv:2608.13637v2, 2026)。其主结果无条件给 zeta 及固定本原 Dirichlet L 函数至少 0.6725007... 的简单中心线零点比例；第 7 节说明四矩 sine-kernel 假设给 Christoffel 层级 13/18，而全部矩假设在该机制中给比例 1。文档 197 把其二矩证明抽象为 partial Weil configuration，文档 198 只把四矩讨论作为条件性算术目标；文档 226 逐式使用其显式公式中的 `mu`、pole-absorption 项与临界 Gabor 矩阵定义，并另用 Stirling 和窗口衰减证明 Archimedean 背景的零频归约，不从原文外推未证明的四矩估计。文档 228 逐式使用 §§2.2--2.3、Propositions 4.1--4.3、Corollary 4.5、Theorem 5.7 与 §6，证明 relative-dense grid starts 的 moving zero blocks 与固定 dyadic block 只差 `o(N)`；该桥梁不把本项目的 fourth-trace upper bound 归因于原文。
   https://arxiv.org/abs/2608.13637

37. Sabine Burgdorf, Igor Klep, *The truncated tracial moment problem*（arXiv:1001.3679；J. Operator Theory 68 (2012), 141--163）。给出非交换 tracial moment matrices、有限秩表示与 flat extension 的标准框架。文档 202 的 Archimedean finite-satisfiability completion 使用更直接的乘积紧致性证明，不把 flatness 当作 zeta 的已知输入。
   https://arxiv.org/abs/1001.3679

38. Bernard Mourrain, Konrad Schmüdgen, *Flat extensions in star-algebras*（论文原题使用星号；arXiv:1406.4975；Proc. Amer. Math. Soc. 144 (2016), 4873--4885）。提供一般 star-algebra 中正泛函 flat extension 的背景。文档 202 的 65 维 no-go 说明固定 degree-four scalar data 并无所需 flatness，故必须增长 localizer 层次。
   https://arxiv.org/abs/1406.4975

39. Esther Notik, *A sharp four-moment inertia bound for the zeros of the Riemann zeta function* (working paper, August 2026)。该稿提出在相同四矩数据下保留 rank--trace--inertia 账本可得 16/21 与 37/42。这是尚未同行评议的近期 working paper；文档 197 与独立论文逐式重证其有限维 quartic dual、闭式比例和匹配极端谱测度，但不据此认定 zeta 的四矩算术假设已成立。
   https://www.academia.edu/171780663/

40. Natalie Evans, *Correlations of almost primes*, Mathematical Proceedings of the Cambridge Philosophical Society 174 (2023), 301--344. Theorem 1.1 对受限类 \(E_2'(P)\)（一个素因子位于 \((P,P^{1+\delta}]\)）在 \(H\ge (\log X)^{19+\varepsilon}\) 时给出 almost-all shift 渐近，例外数为 \(O(H\log^{-\eta}X)\)，其中 \(P\) 由 \(H\) 所处区间指定；Theorem 1.3 对一般 \(E_2\) numbers 给出 \(\exp((\log X)^{1-\varepsilon})\le H\le X\log^{-A}X\) 范围内除 \(O(H\log^{-B}X)\) 个 shifts 外的 Hardy--Littlewood 型渐近；Lemma 2.1 记录 singular series 的平均上界。文档 214 只使用 Theorem 1.3 的 almost-all upper-bound 后果，并用独立 Cauchy budget 处理 exceptional shifts；文档 216 同时审计 Theorems 1.1、1.3 的精确范围，证明它们均不覆盖 polylog shift 下的 balanced-factor transition core，不作范围外外推，也不调用逐 fixed-shift 猜想。
   https://doi.org/10.1017/S0305004122000251

41. Kevin Henriot, *Nair--Tenenbaum bounds uniform with respect to the discriminant*, Mathematical Proceedings of the Cambridge Philosophical Society 152 (2012), 405--424；及 *Erratum*, ibid. 157 (2014), 375--377。原论文 Introduction, Theorem 2 记录对受 divisor-function 控制的两个 multiplicative functions 的 uniform shifted upper bound；Theorem 3/5 给出精细 discriminant factor。勘误明确说明上界仍有效，但把 congruence factor `rho-hat_R` 修正为 `rho-check_R`，并把一般多项式的坏素数因子从 `D*` 扩大为 leading coefficient `a*` 乘 `D*`；主要失效的是原 Theorem 6 的 lower bound 与 sharpness。文档 229 对 `Q_1=X,Q_2=X+h` 的 primitive monic 情形逐项核验：`a*=1` 且 `rho-check<=rho-hat`，所以文档 217、224、227 使用的上界不削弱；`f_z(n)=z^{Omega(n)}` 在固定函数类中随 `z->0` 仍有统一隐常数。文档 224 以分别匹配 `Omega=1,3` 的两个参数得到 one-prime/three-prime support correlation，并只使用统一 discriminant majorant 的 bounded mean，不把 upper bound 外推为渐近式；文档 225 仅复用该上界处理 finite `3+1` boundary 的 comparable ranges，其新增输入是仓库内证明的 Toeplitz crossing trace estimate。
文档 227 在同一统一参数类中取 `Omega=1,2`，重证 one-prime/two-prime 与 prime-pair upper bounds，并只使用 discriminant factor 的 bounded mean；不把 upper bound 称为 Hardy--Littlewood 渐近。
   https://doi.org/10.1017/S0305004111000752
   https://doi.org/10.1017/S0305004114000280

42. Roman Holowinsky, *A sieve method for shifted convolution sums*, Duke Mathematical Journal 146 (2009), 401--448。建立 shifted multiplicative correlations 的 upper-bound sieve；文档 217 使用 Henriot 所记录的 discriminant-uniform general formulation，不从该论文外推任何 asymptotic。
   https://doi.org/10.1215/00127094-2009-002

43. Hugh L. Montgomery, Robert C. Vaughan, *The Large Sieve*, Mathematika 20 (1973), 119--134。给 classical analytic large-sieve 与 Hilbert-inequality方法的一手背景；文档 218 的 cone-valued clustered Fejér版本在笔记内完整重证，不从 separated-frequency theorem 外推聚类结论。
   https://doi.org/10.1112/S0025579300004708

44. Gérald Tenenbaum, *Introduction to Analytic and Probabilistic Number Theory*, 3rd ed., Graduate Studies in Mathematics 163, American Mathematical Society (2015), Chapter I.4。给出 Selberg upper-bound sieve 及其 remainder-form 基础；文档 221--222 只调用固定二维 sieve dimension、fixed positive level 下的上界筛；文档 222 另逐行验证两线性形式的 residue counts，不调用 lower sieve 或 prime-tuple asymptotic。
   https://www.ams.org/bookstore/pspdf/gsm-163-prev.pdf

45. Harold Davenport, revised by Hugh L. Montgomery, *Multiplicative Number Theory*, 3rd ed., Graduate Texts in Mathematics 74, Springer (2000)。作为素数定理 `psi(x)=x+o(x)` 的权威参考；文档 252--253 只使用这一无条件渐近来控制 Mangoldt interval mass 与 matched Stieltjes discrepancy，不使用 RH 级误差项。
   https://link.springer.com/book/9780387950976

46. Shashi Chourasiya, Aleksander Simonič, *An explicit form of Ingham's zero density estimate*, arXiv:2507.15184v2（2025-09-30），Corollary 1 与 Table 1。[R] 正式预印本，非本项目新零密度定理。对全部 \(1/2\le b\le1\)、\(H\ge3\cdot10^{12}\)，16个闭区间覆盖给统一常数的
   \(N(b,H)\ll H^{3(1-b)/(2-b)}(\log H)^{(7-5b)/(2-b)}+\log^2H\)。
   本轮直接核对 v2 的完整表；三个系数的最大值分别为 \(46.06,9.461,167.8\)。
   对数指数在 \([2,3]\)，因而可弱化为统一 \(H^{3(1-b)}\log^3(2H)\)；
   文档287另保留靠近 \(b=1\) 时的对数指数，通过自行证明的加权 layer-cake 和 dyadic 求和压缩响应的高谱尾。
   只用有限区间零点总数补足小 \(H\)，不从有限高度 RH 验证推断全体零点，也不把零密度计数冒充剩余带符号四阶预算。
   https://arxiv.org/html/2507.15184v2

47. Kiran S. Kedlaya, *Notes on analytic number theory*, Chapter 9, Lemma 9.4 与 Theorem 9.9（作者公开书稿，本轮2026-09-06再次核验）。[R] 使用经典单位高度零点计数及半权截断 von Mangoldt 显式公式；282、285、289只在普通积分内取截断高度极限，实际整数端点另完整保留。289的增长阶 resolvent 系数、统一Cauchy估计及多对数谱局部化均由本项目自行证明，不归因于书稿。原文9.1的 \(\psi\) 是半权约定，与仓库右连续 \(\psi\) 在非原子处一致；采用Theorem9.9所列的正确常数 \(-\zeta'(0)/\zeta(0)\)，不照抄Lemma9.2个别显示中的分母笔误。
   https://kskedlaya.org/ant/chap-von-mangoldt.html

48. Alexander Weiße, Gerhard Wellein, Andreas Alvermann, Holger Fehske, *The Kernel Polynomial Method*, Reviews of Modern Physics 78 (2006), 275--306；作者预印本 arXiv:cond-mat/0504627v2，§II.3.2--II.3.3。[R] 作为正核保正、Chebyshev展开和经典Jackson分辨率的文献定位。本轮已阅读相应正文；式(71)的优化KPM核不是291采用的正弦四次卷积核，不能混用系数。291的具体加权平方迹误差、常数及次数下界均独立重证，不归为该文的新结果，也不据此声称本项目论文新颖性。
   https://arxiv.org/html/cond-mat/0504627v2

49. NIST Digital Library of Mathematical Functions，§5.7(ii)，公式5.7.6。[R] 292仅使用digamma部分分式展开，并自行按 \(n\asymp |t|\) 分段证明固定 \(\sigma>0\) 的 \(\psi((\sigma+it)/2)=O_\sigma(\log(2+|t|))\) 及Cauchy可积性。不把固定Gamma估计外推到变化参数或未截断Abel尾。
   https://dlmf.nist.gov/5.7.E6

50. Kiran S. Kedlaya，*Notes on analytic number theory*，第5章§5.1的完成函数方程及第9章Remark9.7的临界带零点计数。[R] 292的全尺度定性障碍只需要“有一个非平凡零点”和中心线反射，不使用计数速率、RH、离线零点假设或数值零点。292定量记录部分仍使用283--284中已独立核验的输入，不能用此弱零点存在性取代强质量记录。298另在RH分支中以此选取孤立的实际临界零点；固定有限模式减法的扩展使用零点高度无穷多。298的共同载波消去及299的Mellin--Volterra/一侧Landau链条均由本项目独立重建，不归因于书稿；298主要障碍不需要强质量记录。
   https://kskedlaya.org/ant/chap-funceq.html
   https://kskedlaya.org/ant/chap-von-mangoldt.html

   300继续只取上述经典输入：非实极点用于弱Landau反证，RH分支的计数用于全谱尾。
   本轮再次阅读第9章Lemma9.4、Remark9.7和Theorem9.9；补偿差的一致复模界、
   有限包到全谱的临界常数及小端点整数选择均在300独立重建，不归因于书稿。
   300的小端点共尾性不调用Littlewood强振荡幅度；其临界渐近明确以RH为条件。

51. Andrew Fiori, Habiba Kadiri, Joshua Swidinsky, *Sharper bounds for the Chebyshev function \(\psi(x)\)*，arXiv:2204.02588v3（2023-05-17）。[R] 263/265已经调用该文的Corollary1.4；本轮再次核验作者预印本摘要所列的无条件全 \(x>2\) 误差界，并补入统一文献表。294只使用其弱后果：存在固定 \(c>0\)，\(|\psi(x)-x+1|\ll x e^{-c\sqrt{\log x}}\)。不优化或认证数值常数，不宣称本轮重新审读其完整证明或出版版本。相同弱输入亦由Kedlaya书稿第7章Theorem7.7给出；从半权到完整原子的 \(O(\log x)\) 差可吸收。294的匹配Abel前缀、记录交点及295的固定正源饱和构造均独立重证，不归因于上述来源。
   https://arxiv.org/abs/2204.02588v3
   https://kskedlaya.org/ant/part-2-4.html

52. Elchin Hasanalizade, Quanli Shen, Peng-Jie Wong, *Counting zeros of the Riemann zeta function*, arXiv:2107.06506v1（2021-07-14），Corollary 1.2。[R] 本轮核对作者预印本第2页的计数陈述；297只使用其蕴含的经典 \(N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi e}+O(\log T)\) 和单位高度 \(O(\log T)\) 上界，不使用数值常数，不声称当前前沿纪录，也未重建该文完整证明。原始复核的端点下界、Cauchy参数界及其求和后果在297内独立证明；不能把复模结论改为实际共轭配对实部的发散。
   https://arxiv.org/abs/2107.06506v1
   https://arxiv.org/pdf/2107.06506

53. Fredric J. Harris, *On the Use of Windows for Harmonic Analysis with the Discrete Fourier Transform*, Proceedings of the IEEE 66(1) (1978), 51--83。[R] 本轮阅读原文§III p.52、§V.C p.60及pp.60--62的端点平滑、cosine-lobe窗与移位谱核相消讨论，定位301的经典机制，不采用旁瓣最优数值。301的正Poisson背景分离、Cauchy负部上界、相位主项和同解析germ非一致性均独立重建；有限上端尾的改进不等于整个单边复变换均有二次衰减。本文具体结果的优先权仍[O]，不能从检索未命中推断新颖性。
   https://doi.org/10.1109/PROC.1978.10837
   https://web.mit.edu/xiphmont/Public/windows.pdf

54. Siegfred Alan C. Baluyot, Daniel Alan Goldston, Ade Irma Suriajaya, Caroline L. Turnage-Butterbaugh, *Pair Correlation of Zeros of the Riemann Zeta Function I: Proportions of Simple Zeros and Critical Zeros*，arXiv:2501.14545v3（2026-09-01），§3。[R] 本轮核验无条件MT的修正版、全谱resolvent范数和适用范围1≤x≤H；误差含O(H sqrt(log H))，不沿用原始较小误差。初读v2链接后，收尾明确复核v3并固定引用。289§11只代入当前参数，证明现成公式不直接覆盖x约Y、H约log²Y；不把全谱正性移植为深右子集或增长权的四阶估计。
   https://arxiv.org/html/2501.14545v3

55. Kevin Ford, Alexandru Zaharescu, *On the Distribution of Imaginary Parts of Zeros of the Riemann Zeta Function*，作者公开PDF，§3 Lemma1及相邻Selberg密度陈述。[R] 主代理已阅读Landau--Gonek型公式与最近素数幂主项的处理；289只使用其全零点和余项上界核验保证尺度，没有审读或声称重证Gonek原证明。该全谱公式不能直接代替实际深右加权子和；密度代入只说明当前上界未提供所需节省，不构造实际离线零点。
   https://www.ford126.web.illinois.edu/wwwpapers/fz.pdf

56. Youness Lamzouri, *A new proof that more than 2/3 of the zeros of the Riemann zeta function are simple and on the critical line*，arXiv:2609.02882v1（2026-09-02）。[R] 本轮阅读§§2--3主要证明，包括Proposition2.1、固定测试函数去除相关权及先固定epsilon取高度极限的次序。197§10独立重建其有限Hilbert不等式与本项目原二阶部分配置的精确算子接口；这不是新纪录、四阶算术节省或Gabor四迹同一性。未运行附录Lean工程，不把作者形式证书声明当成本地复核。
   https://arxiv.org/html/2609.02882v1

## 使用这些来源时的边界

- Deligne 已无条件证明有限域结论，但不是通过证明全部 standard conjectures；不能把 standard conjectures 的一般成立当成已知事实。
- Deninger/Connes 提供的是严肃且部分已实现的研究纲领；截至核对日期，没有上述来源声称完成经典 RH 的证明。
- 2025–2026 的有限截断数值逼近即使极高精度，也不替代局部一致收敛或等价强度的严格极限定理。
- Academia 的 zeros-of-Riemann-zeta-function 专题只作为线索聚合页，不提供质量背书。Notik working paper 的有限维证书已独立复核；其四矩 zeta 输入仍是条件性的，不能把 16/21 当作当前无条件纪录。
- `arXiv:1009.6121` 曾声称 von Mangoldt symmetry/Selberg integral 的 log-power interval估计，但已由作者撤回；其撤稿说明指向 `arXiv:1103.4451v2`，后者明确记录 Lemma 2 所用 Lemma A 有关键错误。该 claim 不作为本文证据。
- Saffari--Vaughan Lemma 5 的 Selberg-order estimate (6.4) 明确以 RH 为假设；文档 169 又从 Mellin continuation证明所需 polylog profile反向蕴含 RH。因此该 profile 标为 `[E]`，不能列作已知无条件 short-interval input。
- 本仓库的定理/引理 A–ACJ 的形式蕴含均给出证明；使用的外部 Weil/prolate/Ihara/trace-ideal/Perron/Nyman--Beurling/large-sieve/Kloosterman-fraction/totient/Hardy outer-factorization/Paley--Wiener/Bochner/Gamma-integral/Stirling/Carathéodory/Montel/Gallagher/Vaughan 定理与渐近输入在相应笔记中明确标注。开放性在于把这些假设无循环、以所需统一速率实现到经典 zeta/一般 L 函数上。文档 136--162 的数值 Cauchy-defect/variance表、finite correlation Grams、Loewner spectra、quadrature values、zero-wave samples、quadratic energies、sampled Laplacian margins、finite-trace、block、modulated-energy、Vaughan-component、background-gauge、multiscale-cutoff、matrix-channel、common-basis Feshbach、out-of-sample、Laurent-channel、incidence-cone、tilted-channel与 compression-obstruction diagnostics只用于区分可行与失配的估计结构；scalar integrals、eigenvalues、stationarity groups与 sampled moments尚非 interval/symbolic enclosures，不作为 bounded `J_Y` 或 RH 的证据。文档 149--157逐步把 Cauchy negative index定位到公共二维 Vaughan channels；文档 158--161依次冻结经验与algebraic tilted channels；文档 162给出其exact Type I/II formulas并证明tail/coupling-only compression的rank-one no-free-lunch。尚未证明的是禁止core amplification的数域Hodge--Riemann relation，以及定理 ACG的 noncircular core/coupling/tail uniform dyadic bound。
