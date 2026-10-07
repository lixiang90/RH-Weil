# 442. 新边界上的同源 high 身份、共享轮廓与主信号

2026-10-07。状态 [T/R]：以下解析扩展相对于明确列出的原通用 [R] 输入成立。
不直接调用 statement 限定 sigma0>=7/8 的旧轮廓定理；逐步重放其证明。
本稿支付解析与外行前件，不单独宣称新的无零半平面、比例记录或 Lean 验收。

## 1. 固定来源、对象和输入

来源为 [OpenAI/math September-30 paper.tex](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex)，
提交 adc7f1241b42e322a6451854ab7e4b4c146bf78a，canonical LF SHA256
42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3。
下文行号绑定该文件。

保留原 physical finite compensated probe I_modified、S,T,xi、Gaussian、ray calibration、
原 completed-index 限制和 zero-on-nonunit masks。X、Y 与固定 slot 长度按441改变；
每个 Z 的 finite compensation 仍是原 completed sums 的有限线性组合。
主信号、完整局部校正及两侧估计均使用同一个最终 S。

确切外部 [R] 输入为原 coefficientwise probe/Poisson 与局部算术身份，
4013–4047的局部表及其defect恒等式，固定ray素数渐近，
buffered bins、global/buffered reciprocal与Hecke增长，
以及5672–5728的 external-contour-tails。
这些是原稿明确声明的通用结果；本项目没有重新证明全部原稿。
新参数前件及它们导出的解析扩展在下面逐项支付。

固定

\[
 b=1/8,\quad \ell=10003/60000,\quad
 l_x=42497/120000,\quad l_y=57497/120000,\quad
 h=32503/40000,
 \qquad \sigma_1=69999/80000.
 \tag{1}
\]

取固定有限个 disjoint annular slots，ell_i>0、sum ell_i=ell、P_i=Z^{ell_i}。
槽窗 W_i、norm-ratio 紧区间、ray 系统均在 Z 和目标角色前固定。
令 beta_* 为原全集 primitive finite-order Hecke characters 的零实部共同上确界，
在反证条件 beta_*>sigma1 下工作。Global reciprocal 只用于 Re s>beta_*；
没有假定待证的新半平面已经无零。

固定主留数来自 w=1,z=1/6，因此

\[
 C(s)=s+l_x/2-1+h/6=s-11/16.
 \tag{2}
\]

## 2. 新 Euler 域与完整无商 tuple

保留原域

\[
 D_1(\epsilon_0):\quad
 \Re s\ge51/100,\ \Re z\ge17/50,\ \Re w\ge-1/100,
 \ \Re(s+w)\ge1+\epsilon_0,
\]

并将原 D2 的 s 下界改为固定 sigma1：

\[
 D_2^*:\quad \Re s\ge\sigma_1,\quad
 \Re z\ge33/200,\quad\Re w\ge19/20.
 \tag{3}
\]

令Q=Np，D,V,W,R及 P_p^*、G_p 为原局部符号。
保留完整校正的精确式

\[
 H_p-1=
 \frac{D(V+W-VW)-VW+(1-V)(1-W)\mathcal E_p}{1-D},
 \qquad \mathcal E_p=P_p^*+D.
 \tag{4}
\]

它没有 1-W 分母。p|u 时原零延拓给 D=W=0，必须保留这一特化。
原 j=0 表在 p不整除u 上给
|mathcal E_p|<<Q^{4-6Re s-6Re z}+Q^{1-Re s-Re w-6Re z}。
因此440的逐项估计在 (3) 上成为

\[
 |H_p-1|\ll Q^{-1-c_b}\ (p\nmid u),\quad
 c_b=\min\{6\sigma_1-401/100,\sigma_1-3/50,47/50\}
     =65199/80000>0,
\]
\[
 |H_p-1|\ll Q^{-c_r}\ (p\mid u),\quad
 c_r=\min\{\sigma_1-1/20,3\sigma_1-3/2\}
     =65999/80000>0.
 \tag{5}
\]

分母 1-R、1-V、1-D 在此域一致离零；所有高度和单位模目标相位的常数一致。
严格正 c_b,c_r 允许实部下界稍向外移动，故不是只有闭轮廓上的点态收敛。
Good-prime 正乘积收敛，ramified divisor product 为 (Nu)^epsilon；
基础校正在 D2* 每点邻域全纯，并有 |mathcal H_{eta,u}|<<epsilon(Nu)^epsilon。
D1 上则用原同类正常收敛估计，epsilon_H=min(epsilon0,1/50)>0。

必须用原8707–8711的完整 tuple，而不在一般行除以 H_p：

\[
 \mathfrak H_{\eta,u,Z}(s,w,z)=
 \sum_{(p_i)\in\prod_i\mathcal P_i(Z)}
 \prod_i[W_i(Q_i/P_i)Q_i^{z-1}G_{p_i}]
 \prod_{\substack{p\notin S\\p\notin\{p_i\}}}H_p.
 \tag{6}
\]

有限 selected 因子和正常收敛的 unselected 乘积在两域全纯。
删 selected primes 是从正 majorant 中删若干 >=1 因子，所得界独立于 tuple；
不要求一般 H_p 非零。在任意固定 real box，|G_p|<<Q^B 对全部虚部一致。
每槽 O(P_i) 个理想、Q_i~P_i，所以

\[
 |\mathfrak H_{\eta,u,Z}|
 \ll (Nu)^\epsilon\prod_iP_i^{\Re z+B}
 \ll (Nu)^\epsilon Z^{B'}.
 \tag{7}
\]

B′只依赖已经固定的box与槽系统。对Nu<=Z^D，(7)支付
`eq:stage-all-height-majorant`，可取 J=0；B′在任何后续积分分部阶数之前固定。
这不是 central numerator 联合界或行数界。

## 3. 同一个物理表达式的准确 high 身份

原8717–8719的 selected local operation 是

\[
 \overline{\eta(p)}Q^{s+z-1}P_p^*-Q^{z-w-1}P_p
 =\frac{1-D}{(1-V)(1-W)}Q^{z-1}G_p.
 \tag{8}
\]

它不含固定 ell=1/6 或旧 X,Y 的数值。
Disjoint slots 保证每个 selected prime 只操作一次。
在绝对起始线 (Re s,Re w,Re z)=(3,3,2)，
将原基础probe身份的有限 compensated 线性组合按 (8)整理，得到

\[
 I_{\eta,\mathrm{modified}}(Z)=\frac1{(2\pi i)^3}
 \int_{(3)}\int_{(3)}\int_{(2)}\mathcal W
 \sum_u^{(6)}q_u^{-z}\overline{\xi(u)}
 \frac{\zeta_F^S(6z)L^S(w,\chi_\bullet(u))}
 {L^S(s,\eta\overline{\chi_\bullet(u)})}
 \mathfrak H_{\eta,u,Z}\,dz\,dw\,ds,
 \tag{9}
\]

其中物理 u 限制与原Poisson式完全相同，
mathcal W=X^{1/2-z}Z^{s+z-1}Y^{w-1}e^{(s+z-1)^2}M(z)hat W_1(w)。
绝对收敛及基础算术身份是明确 [R] 输入；有限操作的重放不改变它。
(9)是原独立 physical expression 的恒等式，不是重新定义一个容易估计的 high 函数。

## 4. 主行校准与实际 normalizer

原唯一 principal numerator row 是 u=1。
在 D2*，选固定 P0 使乘积误差的正majorant
exp(C sum_{Q>P0}Q^{-1-c_b})-1<=1/2。
于是主行每个H_p及完整H_{eta,1}均非零，且 |H_{eta,1}-1|<=1/2。
P0 对目标单位相位一致，可在目标前选；目标确定后扩大S仍缩小同一正majorant。
440的闭式另外给 H_eta(s)=mathcal H_{eta,1}(s,1,1/6)
在 Re s>2/3 全纯；本稿只用固定 Re s>=sigma1 的非零性。

仅在这条已保证非零的主行，可令 B_p=G_p/H_p。
原主局部抵消的四错误指数为

\[
 -\Re s,\quad -6\Re z,\quad
 4-5\Re s-6\Re z,\quad1-\Re w-6\Re z.
\]

在 D2* 的最大值分别是
-69999/80000、-99/100、-21839/16000、-47/50。
因此正确扩域版本是 B_p=-1+O(Q^{-sigma1})，不能照搬旧 -7/8 指数。
整个principal box的tuple界为
|mathfrak H_{eta,1,Z}|<<Z^{ell Re z}，所有高度一致。

令

\[
 S_i(Z)=\sum_{p\in\mathcal P_i(Z)}W_i(Q/P_i)Q^{-5/6}
 \sim c_iP_i^{1/6}/\log P_i,\quad c_i>0,
 \qquad A_T(Z)=(-1)^K Z^{-\ell/6}\prod_i S_i(Z).
 \tag{10}
\]

固定ray素数渐近是 [R] 输入。各ell_i>0固定，故 A_T 最终非零，
|A_T|~(log Z)^{-K}，逆为任意小幂。阈值可以依赖目标的最终有限S。
固定任意 0<mu<sigma1 min_i ell_i。在 w=1,z=1/6 上有限槽的相对误差为
rho_i=O(P_i^{-sigma1})，非负窗使逐槽相对估计合法；于是

\[
 \mathfrak H_{\eta,1,Z}(s,1,1/6)
 =H_\eta(s)Z^{\ell/6}A_T(Z)(1+\mathcal R_{\eta,Z}(s)),
 \qquad|\mathcal R_{\eta,Z}|\ll Z^{-\mu}
 \tag{11}
\]

在整条global线 Re s=beta_*+e 成立。Mu 在目标前指定。
原 c_S=hat W_1(1)M(1/6)(Res_{v=1}zeta_F^S(v))²/6>0，
使用同一 S 和 A_T 正规化所有物理贡献。

## 5. Principal 轮廓的实际误差

保留global s=beta_*+e；先移 w,z 至1+e、1/6+e，
再移 w 至19/20跨w=1，在其留数中移 z 至33/200跨z=1/6。
这些路径在D2*，1/L始终在global线，未跨任何目标零点。
主双留数的 s 积分最后仅向右移至2。
三维本体与取留数后的二维核分别按原外尾引理处理，不能用单轴控制代替整核控制。
令mathscr P_eta为(9)的u=1项，且

\[
 f_\eta(Z)=\frac1{2\pi i}\int_{(2)}
 Z^{C(s)}e^{(s-5/6)^2}\frac{H_\eta(s)}{L_F^S(s,\eta)}\,ds.
 \tag{12}
\]

Raw Mellin幂为 l_x/2+s-1+h z+l_y(w-1)。重放原主留数证明和(11)给

\[
 \frac{\mathscr P_\eta}{c_SA_T}-f_\eta
 \ll Z^{C(\beta_*)+(1+h)e-m_w+\epsilon}
 +Z^{C(\beta_*)+e-m_z+\epsilon}
 +Z^{C(\beta_*)+e-\mu+\epsilon},
\]
\[
 m_w=l_y/20=57497/2400000>0,\qquad
 m_z=h/600=32503/24000000>0.
 \tag{13}
\]

逆normalizer的小幂在此epsilon内计一次。
选小e及real损失可保留每项固定正saving；轮廓扩域本身不能代替这些误差预算。

## 6. Whole-bin 中央轮廓的新版本

原buffered bins的floor为a=51/100；非floor a<=beta_*。
先固定整个bin及原physical rows，不按Mellin点的detector集合预切。
沿D1将 z 移至 z0=17/50、s 移至 beta_*+20e、w 移至1-a-6e。
此时 Re(s+w)>=1+14e。
在global s线上移除同一个高度box外部尾后，才将retained s段移至a+16e。
此时 Re(s+w)>=1+10e，Re s>a+6e，故 buffered reciprocal 与
D1(10e)均适用；w>=-6e>-1/100。没有额外 sigma0>=7/8 门槛。
完整 (7) 的B′及各global bound的固定height阶在外尾阶N之前确定。
Discarded pieces和joins为 O_{eta,N}(Z^{B_eta}T1^{-N})。

原bin-contour-accounting由(9)的幂直接计算，给新参考幂C(sigma1)的指数

\[
 E_{\sigma_1}(d;R,g)=a-\sigma_1+h(z_0-1/6)-a l_y-\ell/2+g
   +d(R+\delta/2-z_0),\qquad\delta=2a-1.
 \tag{14}
\]

附加real损失为(16-6l_y)e+(1+d)epsilon_c+d epsilon_d+epsilon_p，
高度成本为已固定有限(1+T1)^{A_eta}。
必须另证实际 pointwise error-slot×numerator 联合界及行数R、gain g，
本节不把439的nominal R_*当成已成立的计数。

## 7. 原外小行与外大行

小行在 (Re s,Re w,Re z)=(beta_*+e,1/2,17/50) 估计。
原D1(3/8)在beta_*<7/8时不保证成立；改用固定D1(1/3)，因为
sigma1+1/2>1+1/3。Epsilon_H仍可取1/50。
Off-row selected errors的四指数为
-Re s、-51/25、49/25-5Re s、-77/50，全部严格负，故G_p=O(1)。
Ramified D=W=0后，原j=1,…,5表的边界指数为
-1/2、3/2-2Re s、(3/2-2Re s,2-3Re s)、2-3Re s、3-5Re s，
在Re s>=1/2上均<=1/2；原strict项为1-w=1/2。因此G_p<<Q^{1/2}，
无需任何H_p非零性。
每槽正和由原divisor-many计数给

\[
 \sum_p|W_i(Q/P_i)|Q^{z_0-1}|G_p|
 \ll P_i^{z_0}+U^\epsilon P_i^{z_0-1/2}
 \ll U^\epsilon P_i^{z_0}.
 \tag{15}
\]

故完整tuple<<U^epsilon Z^{ell z0}，全部高度一致。
固定宽条带numerator增长为U^{3/5+epsilon}乘固定height幂，
行数O(U)及q_u^{-z0}给总幂63/50。
取d_min=1/100，相对C(beta_*)的小行误差自由指数准确为

\[
 h(13/75)-l_y/2+(63/50)d_{\min}
 =-172249/2000000<0.
 \tag{16}
\]

用较粗63/50<2也有-157449/2000000。
这是对d<d_min的独立证明；439的中间行margin不覆盖这些行。
若额外使用beta_*<=7/8，则改参考幂C(sigma1)最多增1/80000，仍为严格负。

大行 U>Z^{h+zeta} 使用固定(2,2,z_infty)，z_infty>2。
原完整selected G_p=O(1)与unselected正乘积给全高度tuple界
U^epsilon Z^{ell z_infty}，并有

\[
 \sum_{U>Z^{h+\zeta}}|\mathscr R_\eta(U;Z)|
 \ll Z^{B_0+(h+\zeta)(1+\epsilon)-\zeta z_\infty+\epsilon},
 \quad B_0=l_x/2+1+l_y=264994/160000.
 \tag{17}
\]

先固定zeta>0，再在目标前取足够大的z_infty，最后选epsilon和height/tail阶，
可以达到指定负幂。不能令z_infty随Z或moving row变化。

## 8. 准确边界

本稿证明同一physical probe的新stage-high身份、完整tuple的全纯与全高度majorant、
主校正非零和实际normalizer、principal residues、whole-bin轮廓及两类外行接口。
中央 joint error slots、actual capacity/counts、全d严格saving及最后continuation
须由443及后续稿另行支付。未使用正在证明的sigma1零自由性作为前件。

逐源详细读稿：[独立解析推导](../reviews/2026-10-07/hybrid-shared-contour-extension-derivation.md)。
441已支付low；440已给主校正更大域。完整原来源仍为外部[R]，
本项目没有将这一纸面分析称作新的Lean核验结果。
