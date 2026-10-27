# 全整数阶乘—整除耦合尝试：实际公式及强旧去重

2026-10-28；G20261027／runtime1793085111／原0c4f。本次仅自主尝试一个整数／prime共同signed规则，不重开rank2、wind、ξ纵投影、clipping、theta参数或Sonin投影。已恢复README／STATE、check→show、Goal、宏观前沿、D20261028O及O结算；C048已耗尽。只写本稿，无web、PDF、下载、数值、STATE、cadence或Git变更；支持稿不代root消费。

**结果：本次没有形成独立新input。** 尝试用全整数的阶乘计数，把全部prime powers共同搬入一个实际signed reader；最便宜的逐整数系数门便将它精确还原为原prime-shift腿。接回原Γ及双pole后恰是已有完整Weil型，没有新增共同正号或原norm费用。下面保留实际公式与失败链，而不将“经典算术确实出现”冒充数学准入。建议构造自筛／强旧0止，不另立合同、编号或轮次。

## 1. 唯一尝试：阶乘计数经全整数整除反演的signed reader

动机是全整数有一个不选择未知ζ根的实际prime耦合：对每个实x≥1，
\[
 \mathcal L(x):=\log(\lfloor x\rfloor!)
 =\sum_{n\le x}\log n
 =\sum_{q=p^k\le x}\Lambda(q)\lfloor x/q\rfloor.
 \tag{1}
\]
它同时含整数通常次序、任意多个素因子的整除结构及全部proper powers，不是先假定PNT或正H。最后一式由每个整数的完整因子分解
\(\sum_{q\mid n}\Lambda(q)=\log n\)给出；不能只留prime k=1。

冻结原physical r=e^(u/2)f、全complex源和\(\tau_a r(u)=r(u-a)\)。拟从整数count而不是从给定的prime腿出发，定义有限、按同一product cutoff的源reader
\[
 \boxed{\mathcal J_N r
 =\sum_{mn\le N}\frac{\mu(m)\log n}{\sqrt{mn}}
                   \tau_{\log(mn)}r},\qquad N\ge2.
 \tag{2}
\]
μ来自实际整数的整除反演。这里的mn≤N不能改成两个独立rectangular cutoffs；后者产生另一批未付边界／cofactor项。本次不作该改变。

候选的signed mixed读出是在I_L=(−L,L)、原zero-extension上，将(2)与原arch和两个endpoint共同配对：
\[
 \mathcal B_{N,L}(r,s)=q_{\Gamma,I_L}(r,s)
 -\langle\mathcal J_Nr,s\rangle-\langle r,\mathcal J_Ns\rangle
 +2C_L(r)\overline{C_L(s)}-2S_L(r)\overline{S_L(s)},
 \tag{3}
\]
\[
 C_L(r)=\int r(u)\cosh(u/2)du,\qquad
 S_L(r)=\int r(u)\sinh(u/2)du.
\]
内积以第一变量线性；Γ保完整\(\Re\psi(1/4+it/2)-\log\pi\)、FP与指定contact，Fourier hat r(t)=∫r(u)e^(−itu)du、dt/(2π)。先固定N、L，r,s在原Dlog型域；并没有另选physical权、删除负pole或声称(3)非负。这是本次唯一尝试，不再另造平方修补。

## 2. 最便宜的系数门已经决定：它只是原prime腿

在(2)按同一实际整数k=mn合并，
\[
 \sum_{m\mid k}\mu(m)\log(k/m)=\Lambda(k),\qquad
 \mathcal J_N=\sum_{k\le N}\frac{\Lambda(k)}{\sqrt k}
                                      \tau_{\log k}.
 \tag{4}
\]
这个合并保全部exact cofactor碰撞，不是只看对角或把cross设零。最小检查就能区分两种错误：k=6时log6−log3−log2=0；k=p^j时jlogp−(j−1)logp=logp，故proper power的系数不是jlogp。任取更大N也不会改变这一系数事实。

因此只要N≥e^(2L)，所有与I_L有正长度overlap的原pp位移都已经出现；k=e^(2L)的endpoint overlap为零。式(3)于是**恰等于**555／578已付完整经典Weil mixed型。没有较小的signed误差、额外Γ协同项、特殊正子空间或actual corecross估计从反演中留下。这里不是“不知如何证明新比较”：这个拟用信息差已被精确恒等式消去，原目标只换了一次整数标签。

若将(2)称为primitive源，还缺同对象关系／商和mixed身份；本稿不作该称呼。它在当前尝试里只是prime腿的reader，不要求单腿独自消405，也不因单腿不消Pan宣布完整Weil型失败。

## 3. 实际域、原费及fixed／cofinal界限

式(2)有限，因此覆盖全S_exp及全L²(R,du)。由(4)及平移酉性，令
\[
 s_N=\sum_{k\le N}\frac{\Lambda(k)}{\sqrt k},\quad
 \|\mathcal J_Nr\|_2\le s_N\|r\|_2.
 \tag{5}
\]
全线Fourier multiplier的绝对值≤s_N，故同样支付原zero-extension的log Fourier范数。对强源半范数\(p_{M,j}(r)=\sup e^{M|u|}|r^{(j)}(u)|\)，
\[
 p_{M,j}(\mathcal J_Nr)
 \le\Big(\sum_{k\le N}\Lambda(k)k^{M-1/2}\Big)p_{M,j}(r).
 \tag{6}
\]
这是每先fixed N的真实费用，不给N成长时uniform原费。Γ型域仍由(3)原闭型与bounded pp／finite-rank pole扰动承担，不需要声称每个硬截断reader输出都自动保持压缩后的强域。

粗PNT／Abel已给s_N~2√N；在N≈e^(2L)时由此只能得到O(e^L)粗费。更强的555已对**实际压缩两向总行**、ALL原complex源和ALL L证明\(\|A_L\|=(1+o(1))e^L\)，并付后续whole预算。不能拿本稿较弱的逐项Young界当新source费或whole改进。

fixed窗时取N足够大仅使(3)稳定为原Q；cofinal L↑∞需相应N↑∞，没有新相消。频高t、源窗L和整数N仍为不同量词；全线N∞算子界及moving源统一极限均未付，也不靠无穷Dirichlet乘积作形式交换。

## 4. 阶乘中的Γ没有支付arch Γ

式(1)在整数端可写\(\log\Gamma(\lfloor x\rfloor+1)\)。这不是完成函数中的\(\Gamma(s/2)\)，也不是其log导数的原Fourier FP/contact。不能把floor删去，再用Γ的凸性／Binet正性代替原arch有符号型。

只在绝对收敛域Re s>1作必要Mellin核查便看清角色：
\[
 \int_1^\infty\mathcal L(x)x^{-s-1}dx
 =-\frac{\zeta'(s)}s
 =\left(-\frac{\zeta'}\zeta(s)\right)\frac{\zeta(s)}s.
 \tag{7}
\]
全整数floor count提供的是额外ζ(s)/s乘子。把它反演，得到的正是已有−ζ′/ζ，而非一个独立Γ补偿。有限N的(4)已无条件完成系数反演；若改走无穷Mellin division到临界域，还须支付080／081已有的闭值域、inverse增长及除子责任，不能由Re s>1的式(7)跨域免费取得。这里不提出该额外合同。

## 5. 扣最强旧后的净值与停止

* **036：** 次序max核的prime-square能量与临界membership、Selberg乘积平方的区别早已付。对阶乘／prefix reader再取正Gram，不会自动给原完整signed净号；本次未把这种平方另立候选。
* **080／081、549及550补正：** 整除inverse、Mellin division和完整cofactor fiber合并本来已付。549中\(\sum_{m\mid\kappa}\Lambda(m)=\log\kappa\)正是(4)的逆向；本稿没有新的raw抵消、实际α=1合成费用或强于550已付topband原norm O(1)的结果。
* **555及557：** ALL L／ALL complex完整行sharp原norm和whole leading4/5负惯性UPPER均强于本稿粗界；(4)只恢复同一A_L，不改actual负惯性、coverage或coupling。
* **576–578：** 正生成、membership、clipping等价及完整Γ＋prime／双pole signed表达已经存在。(3)与原Q完全同型，没有付实际q_R负部或其逐源消失，也不把普通PNT／Toeplitz／Selberg预算改名使用。
* **585：** actual Sonin fixed源t、K必要同阶成长和旧safehigh保持；本稿既没有同源Sonin新身份，也没有改变t−K净差，不能把另一个合法reader的费代入。

本次自主构造确实使用了全体整数因子分解，并保所有proper powers；但实质算术作用是**精确再生已知prime算子**，不是新的独立约束。完成域和系数门后，没有剩余可准数学的input／test／强旧净后果。原Γ、contact、双pole、ALLcomplex和原du／Dlog责任完整保留；原目标的正号及corecross仍未付，而非产生了一个可暂名的未知Ω上界。

故止此阶乘—整除反演recipe，不换cutoff、平方、权或Mellin域继续试参数，不另串来源。没有提出新的RH证明、方法类边界或经典成长后果；也不从这一旧重编码失败推断所有全整数／prime耦合都失败。后续自主构造授权持续，但本稿不伪装已经形成另一候选或数学合同。
