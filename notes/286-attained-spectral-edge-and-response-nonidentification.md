# 286. 达到的最右零点实部与质量相对响应的非识别

日期：2026-09-06。主线：NCE-8 / B1z；论文归属：Vaughan--Brownian response。

状态：[C] 达到的有界最右零点实部下，新整数对角记录序列的完整四阶预算；
[T/N] 固定正整数源、正 Dirichlet 系数和单值亚纯模型的离线零点反例；
[O] 上确界未达到时的缺口及完整 Weil 接口。
本篇的实际 Riemann zeta 结论全部是条件性诊断，不标记为实际反例 [N]。
它不证明离线零点存在，不证明 RH/GRH，也不声称文献新颖性。

## 1. 最小条件定理与准确量词

固定 \(0<\sigma<\beta<1/2\)，置
\[
 \delta=\beta-\sigma>0,\qquad
 R(x)=\psi(x)-x,\qquad
 P_\beta(N)=\max_{1\le n\le N,\ n\in\mathbb Z}|R(n)|n^{-\beta}.
 \tag{1}
\]
\(\psi\) 右连续，所有原子取完整权，\(R(1)=-1\)。
记实际非平凡 zeta 零点的实部上确界为
\[
 \Theta=\sup_\rho\Re\rho .
 \tag{2}
\]
本篇只在下面明确的条件下工作：
\[
 \boxed{\quad \Theta<1,\qquad
       \text{存在实际零点 }\rho_*=\Theta+i\gamma_*
       \text{ 达到该上确界。}\quad}
 \tag{H}
\]
函数方程的零点反射对称性保证 \(\Theta\ge1/2\)，故
\(\Theta>\beta>\sigma\)。条件(H)不假设最大实部由有限个零点达到，
也不假设与其他实部之间存在正间隔。

令实际匹配的对角质量为
\[
 A_\sigma(Y)=M(Y,Y)
 =\sum_{2\le n\le Y}\Lambda(n)n^{-\sigma}e^{-n/Y}
          -\int_1^Yx^{-\sigma}e^{-x/Y}\,dx .
 \tag{3}
\]

### 定理286-A [C]

在(H)下，有共尾整数序列 \(Y_j=N_j\to\infty\)，满足
\[
 |M_j|\gg_{\sigma,\beta,\rho_*}N_j^{\Theta-\sigma},\qquad
 P_\beta(N_j)N_j^\delta<C_{\rm diag}|M_j|,\qquad
 M_j=A_\sigma(N_j),
 \tag{4}
\]
其中 \(C_{\rm diag}\) 是与尺度无关的固定有限常数。沿同一序列，
\[
 \boxed{\quad Q_{|\xi|\ge1}(r_j)\ll M_j^4,\qquad
 Q_{\mathbb R}(r_j)\ll M_j^4\log N_j,\qquad
 J_{4,j}=O(\mu_j^4).\quad}
 \tag{5}
\]
实际物理频率尾还满足
\[
 J_{4,j,|\xi|\ge1}=O(\mu_j^4/\log N_j).
 \tag{6}
\]
此处及下文常数允许依赖固定的 \(\sigma,\beta,\Theta,\rho_*\)，但不依赖 \(j\)。
\(Q,J_4,\mu\) 的原物理定义在第4节列明。

若 \(\Theta>1/2\)，(4)还自动给
\[
 |M_j|>N_j^{1/2-\sigma}\sqrt{\ell(N_j)}
 \quad\text{对充分大 }j,\qquad
 \ell(x)=\max(1,\log\log\log x).
 \tag{7}
\]
若 \(\Theta=1/2\)，(4)本身不提供 \(\sqrt\ell\) 因子；可另选284的强
\(\ell\) 对角序列，再使用本篇同样的端点估计得到(5)--(6)，详见第5节。
本篇不把这两种选择称为同一条预先指定序列。

## 2. 单个边缘零点的幅值与记录转移

### 2.1 独立幅值来源 [T/R]

[283的定量 Mellin 振荡引理](283-fixed-cutoff-abel-mass-oscillation.md)
适用于每个实部大于 \(\sigma\) 的实际零点，而不要求它是最右零点。
若 \(\rho_*\) 的重数为 \(m_*\)，实际 Mellin 变换在
\(s_*=\rho_*-\sigma\) 的留数为
\[
 -m_*\gamma(\rho_*-\sigma,1)\ne0.
 \tag{8}
\]
这里 \(\gamma(s,1)=\int_0^1t^{s-1}e^{-t}dt\) 在 \(\Re s>0\) 无零，
该复无零性已经独立证明，不能由正积分核直接默认。
283因此给
\[
 A_\sigma(Y)=\Omega_\pm(Y^{\Theta-\sigma}).
 \tag{9}
\]
同一整数单元内的求导误差为
\(A_\sigma(Y)-A_\sigma(\lfloor Y\rfloor)
=O_\sigma(Y^{-\sigma}\log Y)\)，所以(9)可以取整数 \(Y\)。
由此存在固定 \(c_*>0\) 及无界整数 \(Q\)，使
\[
 |A_\sigma(Q)|\ge c_*Q^{\Theta-\sigma}.
 \tag{10}
\]
这里使用的是实际 meromorphic 结构的已证条件推论，不是人为指定振荡模板。

### 2.2 归一化记录保留边缘幂次

令 \(b(n)=n^{-\delta}A_\sigma(n)\)。对每个满足(10)的整数 \(Q\)，
在 \(1\le n\le Q\) 中取 \(|b(n)|\) 的一个真正最大者 \(N\)。
则
\[
 B_N:=\max_{1\le n\le N}|b(n)|=|b(N)|=\max_{1\le n\le Q}|b(n)|,
\]
\[
 |b(N)|\ge c_*Q^{\Theta-\beta}\ge c_*N^{\Theta-\beta}.
 \tag{11}
\]
第二个不等式使用 \(\Theta-\beta>0\)。记录高度随所取 \(Q\) 无界，
故 \(N\) 无界，可抽出严格递增序列。乘以 \(N^\delta\) 得
\[
 |A_\sigma(N)|\ge c_*N^{\Theta-\sigma}.
 \tag{12}
\]
这是归一化质量记录，不是原始 \(A_\sigma(n)\) 的记录；也不保证所选记录
具有两种符号。主定理只要求非零绝对质量。

### 2.3 因果逆核控制整个历史

[284的因果逆核与整数历史桥梁](284-causal-abel-inverse-and-diagonal-record-selection.md)
无条件给
\[
 P_\beta(N)\le C_{\rm inv}(B_N+C_{\rm round})+1,\qquad
 C_{\rm inv}=e+\|l_\beta\|_1<\infty .
 \tag{13}
\]
其中 \(l_\beta\) 是已经证明因果且指数可积的实际 Abel 逆核；这一界
不要求零点位置、振荡假设或历史正性。
在上述记录 \(N\) 上，由 \(B_N=|b(N)|\to\infty\)，最终
\[
 P_\beta(N)\le2C_{\rm inv}|b(N)|
              <C_{\rm diag}|b(N)|,\qquad C_{\rm diag}=4C_{\rm inv}.
 \tag{14}
\]
乘以 \(N^\delta\)，与(12)合起来证明(4)。
所有 cutoff 仍精确是同一整数 \(Y=N\)，没有在记录点之后使用误差数据。
本篇只给存在性选择，不声称已实现认证算法，也不使用275原先指定的 guard 常数。

## 3. 保留真实端点的全体零点上界与高于固定频率的预算

以下固定一个所选整数 \(Y=N\)，写 \(L=\log N\)、\(M=A_\sigma(N)\)。
原中心化 discrepancy 的 Fourier 变换为
\[
 \widehat r(\xi)=
 \sum_{2\le n\le N}\Lambda(n)w_Y(n)(\cos(\xi\log n)-1)
 -\int_1^Nw_Y(x)(\cos(\xi\log x)-1)\,dx,
 \quad w_Y(x)=x^{-\sigma}e^{-x/Y}.
 \tag{15}
\]
其中的 \(-1\) 保留完整中心质量 \(-M\)。

条件(H)给全部零点的统一实部上界 \(\Re\rho\le\Theta\)。
[282定理C](282-rh-conditional-endpoint-preserving-response-bound.md)于是给
\[
 |\widehat r(\xi)|\ll_{\sigma,\Theta}
 1+w_Y(N)|R(N)|+
       N^{\Theta-\sigma}\log^2(2+|\xi|)
 \quad(|\xi|\ge1).
 \tag{16}
\]
这里引用的是282的一般 \(\vartheta=\Theta\) 版本，不是把它的 RH 应用
偷用于离线情形。该定理先固定 \(Y,N,\xi\)，只在 Stieltjes 普通积分中
令有限零点高度趋于无穷；积分后的 \(1/\rho\) 与 BV 衰减形成绝对可和级数。
真实的右连续 \(R(N)\) 端点始终没有被半权化，也没有被换成绝对求和的
端点零点级数。

本篇的 guard 直接给
\[
 w_Y(N)|R(N)|
 \le N^{-\sigma}P_\beta(N)N^\beta
 \le C_{\rm diag}|M|.
 \tag{17}
\]
又 \(|M|\gg N^{\Theta-\sigma}\to\infty\)，所以固定常数项也被吸收。
因此
\[
 |\widehat r(\xi)|\ll
 |M|+N^{\Theta-\sigma}\log^2(2+|\xi|),\qquad |\xi|\ge1.
 \tag{18}
\]
记
\[
 Q_E(r)=\frac1{2\pi}\int_E\frac{|\widehat r(\xi)|^4}{\xi^2}\,d\xi.
 \tag{19}
\]
由 \((x+y)^4\le8(x^4+y^4)\) 以及
\(\int_1^\infty\log^8(2+t)t^{-2}dt<\infty\)，
\[
 Q_{|\xi|\ge1}(r)\ll M^4+N^{4(\Theta-\sigma)}\ll M^4.
 \tag{20}
\]
最后一步是使用已经独立得到的质量下界(12)，而不是把所求预算作为记录条件。
这同时处理了整个无限频率尾，不需要274的 dyadic 高频定理。

## 4. 低频、两条实际正通道及完整归一化

### 4.1 历史路径的低频预算

令 \(H_Y(u)=M(Y,e^u)\)，\(0\le u\le L=\log N\)。
对 \(P=P_\beta(N)\ge1\)、\(1\le x\le N\)，右连续约定给
\[
 |R(x)|\le |R(\lfloor x\rfloor)|+1\le2Px^\beta.
 \tag{21}
\]
精确分部积分
\[
 M(Y,x)=w_Y(x)R(x)+w_Y(1)+\int_1^xR(t)(-w_Y'(t))\,dt
 \tag{22}
\]
保留来自 \(R(1)=-1\) 的下端常数。因 \(x/Y\le1\) 及 \(\delta>0\)，
\[
 |H_Y(u)|\le C_0Pe^{\delta u},\qquad
 C_0=3+\frac{2\sigma}{\delta}+\frac4{\delta+1}.
 \tag{23}
\]
例如积分的绝对值至多
\(2P\{\sigma x^\delta/\delta+x^{\delta+1}/(Y(\delta+1))\}\)，足以得到该常数。
积分指数及其平方，再用(14)，得
\[
 \|H_Y\|_1\ll PN^\delta\ll |M|,\qquad
 \|H_Y\|_2^2\ll P^2N^{2\delta}\ll M^2.
 \tag{24}
\]

原源的 Stieltjes Fourier 恒等式为
\[
 \widehat r(\xi)=M(\cos(L\xi)-1)
        +\xi\int_0^L H_Y(u)\sin(\xi u)\,du .
 \tag{25}
\]
将 \(H_Y/2\) 作奇延拓 \(h\)，有
\(\widehat h(\xi)=-i\int_0^L H_Y(u)\sin(\xi u)du\)，
\(\|h\|_1=\|H_Y\|_1\)、\(\|h\|_2^2=\|H_Y\|_2^2/2\)。
Plancherel 和 Young 给
\[
 \frac1{2\pi}\int_{\mathbb R}|\widehat h|^4
 =\|h*h\|_2^2\le\frac12\|H_Y\|_1^2\|H_Y\|_2^2.
 \tag{26}
\]
另有精确核恒等式
\[
 \frac1{2\pi}\int_{\mathbb R}
        \frac{(1-\cos(L\xi))^4}{\xi^2}\,d\xi=\frac54L.
 \tag{27}
\]
它可由 \(k_L*k_L\) 的四个长度 \(L\) 单元上的 primitive 值
\(1/4,-3/4,3/4,-1/4\) 直接平方积分得到。
对(25)用四次幂三角上界，因此
\[
 Q_{|\xi|\le T}(r)\le10M^4L+
       4T^2\|H_Y\|_1^2\|H_Y\|_2^2
       \ll M^4(L+T^2).
 \tag{28}
\]
特别 \(Q_{|\xi|<1}\ll M^4L\)。与(20)合并得到(5)的完整裸四阶预算。

### 4.2 物理正通道和分母不更换

设 \(\alpha,\nu\) 分别为正测度
\(\sum_{n\le N}\Lambda(n)w_Y(n)\delta_n\)、\(w_Y(x)dx|_{[1,N]}\)
在 \(\lambda=\log x\) 下的推前，质量为 \(A,B\)，置 \(S=A+B\)。
以 \(\nu\) 记连续源，避免与固定参数 \(\beta\) 混淆。
定义
\[
 k_\lambda=(\delta_\lambda+\delta_{-\lambda})/2-\delta_0,\qquad
 p=\int k_\lambda\,d\alpha(\lambda),\quad
 c=-\int k_\lambda\,d\nu(\lambda),\quad r=p+c .
 \tag{29}
\]
则 \(M=A-B\)，且(29)的 \(r\) 正是(15)中的真实中心化误差。
记 \(F_\eta(x)=\eta((-\infty,x])\)，原分母和原响应为
\[
 D=\|F_p\|_2^2+\|F_c\|_2^2,\qquad \mu=M/S,
\]
\[
 J_{4,E}=\frac1{S^4D}\frac1{2\pi}
       \int_E\frac{|\widehat r|^4
                (|\widehat p|^2+|\widehat c|^2)}{\xi^2}\,d\xi .
 \tag{30}
\]
没有因移除零点模式或改变选择而另换 \(p,c,S,D\)。

初等 Chebyshev 上界与分部积分给 \(A\ll_\sigma N^{1-\sigma}\)；
直接积分给 \(B\asymp_\sigma N^{1-\sigma}\)，故
\[
 S\asymp_\sigma N^{1-\sigma}.
 \tag{31}
\]
这里仅用定性的粗素数增长，不用 RH 或平方根误差。
正源的 Brownian 核恒等式为
\[
 \left\|F_{\int k_\lambda\,d\omega(\lambda)}\right\|_2^2
 =\frac12\iint\min(\lambda,\lambda')\,d\omega(\lambda)d\omega(\lambda').
 \tag{32}
\]
因为全部 lag 不超过 \(L\)，有 \(D\le L(A^2+B^2)/2\)。
连续源在 \([N/2,N]\) 中的质量为固定正倍数的 \(N^{1-\sigma}\)，该处
lag 至少 \(L-\log2\)。仅此部分在(32)中的自配对就给下界
\(D\gg_\sigma L N^{2-2\sigma}\)。于是
\[
 D\asymp_\sigma S^2L,\qquad
 |\widehat p|^2+|\widehat c|^2
 \le4(A^2+B^2)\le4S^2.
 \tag{33}
\]
因此对任意频带 \(E\)，在本篇非零质量序列上，
\[
 \frac{J_{4,E}}{\mu^4}
 \ll_\sigma\frac{Q_E(r)}{M^4L}.
 \tag{34}
\]
用(20)得(6)，用(20)、(28)得完整 \(J_4=O(\mu^4)\)，证明定理286-A。
各中间测度有限、零质量且紧支撑，primitive 的 Plancherel 恒等式合法；
零频的消失已在(25)--(28)中处理，没有积分发散的粗 majorant。\(\square\)

## 5. 中心线分支、未达到上确界及256接口

### 5.1 \(\Theta=1/2\) 的强质量选择

当 \(\Theta=1/2\) 时，全部零点实部至多 \(1/2\)，结合函数方程即为 RH。
第2节单个零点的(12)只给 \(|M|\gg N^{1/2-\sigma}\)，不能直接称作满足
275的 \(\sqrt\ell\) 门槛。若需要该门槛，可**另外取284定理D的对角序列**，
它由283的强振荡给
\[
 |M|\gg N^{1/2-\sigma}\ell(N),\qquad
 P_\beta(N)N^\delta<C_{\rm diag}|M|.
 \tag{35}
\]
同样使用(16)的 \(\Theta=1/2\) 版本和后续比较，即得(5)--(6)。
这是一项条件下的可选择性说明，不将不同记录构造混成同一预定序列。

当 \(\Theta>1/2\) 时，(12)除以
\(N^{1/2-\sigma}\sqrt{\ell(N)}\) 的比值趋于无穷，故原第2节序列已经满足(7)。
这一点不需要强 Littlewood 因子；它来自更大的假设零点实部。

### 5.2 上确界未达到的真实缺口

若 \(\Theta<1\) 但没有零点达到它，则任取满足
\(\beta<\Re\rho=\alpha<\Theta\) 的固定零点，283和记录转移只给
\(|M|\gg N^{\alpha-\sigma}\)，而(20)的上界仍含
\(N^{4(\Theta-\sigma)}\)。由这种信息得到的商还可能有
\[
 N^{4(\Theta-\sigma)}/|M|^4
 \ll_{\rho}N^{4(\Theta-\alpha)}
 \tag{36}
\]
这个不受控的增长上界，不能据此吸收余项。
选一列 \(\alpha\uparrow\Theta\) 也不能自动解决：振荡常数和取得大值的尺度
可能依赖所选零点，本篇没有所需的同时统一性。
若 \(\Theta=1\)，本篇(H)也不成立；它不覆盖所有 RH 失败的可能情形。

### 5.3 条件性非识别不是实际反例

(5)说明同一质量相对预算可在**假设的**
\(1/2<\Theta<1\) 且达到的情形下成立。其机制清楚：
边缘零点同时提高可选择的净质量尺度，而预算以这份实际 \(M^4\) 归一化。
因此本证明本身没有识别中心线的位置。

但这不是已经证明实际 zeta 存在离线零点，也不是实际意义下的
“\(J_4=O(\mu^4)\) 不蕴含 RH”反例。若日后有人独立证明该预算加上其他
真实桥梁可以推出 RH，本篇与该桥梁合用，将排除(H)中相应的离线情形；
在尚无实际离线模型时，不能把这样的条件推理误标成 [N]。

[256](256-quartic-discrepancy-capture-and-conditional-schur-gain.md)的准确接口
目前只从该预算推出 fixed-core capture 与 sign-pure prime--continuum Schur gain。
其第5--6节明确保留 Gamma block bridge，未声称这些两通道结论本身就是
完整 zeta response gain 或 RH。因此本篇没有发现256已证命题的矛盾；
它要求继续明确哪个独立附加结构真正具有中心线识别能力。

还有尺度量词限制：本篇物理 \(J_4\) 与256的四阶目标是同一积分对象，
但新选择是整数 \(Y=N\)，不是自动成为253--255文字定义的 dyadic
\(Y_m=2^m\) schedule。若另处完成一般尺度的重标度适配，应明确引用
该独立接口，而不是仅把整数记录重新编号就声称保持了原序列。
本篇的完整预算证明未调用274，故不依赖其高频尺度适配。

## 6. 固定正整数源与真正亚纯函数的反例 [T/N]

本节是独立、无条件的模型定理，不假设实际 zeta 存在离线零点。
它比281的非亚纯 chirp 模型多保留了单值亚纯函数、整数除数重数和正 Dirichlet
系数；但**不提供标准素数 Euler 乘积、完成函数方程或 Gamma 因子**。
因此只检验明确列出的部分配置，不是 RH、GRH 或完整 Weil 配置的反例。

### 定理286-B [T/N]

固定 \(0<\sigma<1/2\)，选
\[
 \frac{3+\sigma}{4}<\theta<1,\qquad \gamma>0,\qquad
 \rho=\theta+i\gamma,\qquad
 B=\left\lceil4^{1/(1-\theta)}\right\rceil .
 \tag{37}
\]
存在同一固定整数权序列 \(\lambda(n)\in[1/2,3/2]\)，使：

1. 在 \(\Re s>1\)，一个具有非负 Dirichlet 系数的函数 \(Z\) 满足
   \(-Z'/Z=\sum_{n\ge2}\lambda(n)n^{-s}\)。
2. \(Z\) 单值亚纯延拓到整个 \(\Re s>\theta-1\)，在其中恰有一个简单极点
   \(s=1\) 和两个简单零点 \(\rho,\bar\rho\)。两零点的实部为 \(\theta>1/2\)。
3. 对该源与原匹配连续背景，存在共尾整数对角 \(Y=N\)，同时有
   \(|M|\gg Y^{\theta-\sigma}\)、固定历史 guard 和完整 \(J_4=O(\mu^4)\)。
   正通道 \(p,c\)、中心化及分母 \(D\) 均由这个实际模型源计算，未换成连续模板。
   若 \(\gamma\log2\notin\pi\mathbb Z\)，还可取 dyadic 好子序列，
   但不将其称为同一记录算法或要求相同 guard 数值。

条件(37)是下述粗残差估计的一个充分范围，不声称为最优门槛。

### 6.1 同一固定整数源与有界格点残差

在实半轴上固定
\[
 F(x)=
 \begin{cases}
 0,&1\le x\le B,\\
 -2\Re\{(x^\rho-B^\rho)/\rho\},&x>B,
 \end{cases}
 \qquad
 \lambda(n)=1+F(n)-F(n-1)\quad(n\ge2).
 \tag{38}
\]
\(F\) 连续且局部绝对连续；在 \(x>B\)，
\[
 F'(x)=-2\Re x^{\rho-1},\qquad |F'(x)|\le2B^{\theta-1}\le1/2 .
\]
其余处导数为零。对单位区间积分，故每个 \(\lambda(n)\in[1/2,3/2]\)，
没有随 \(Y\) 重新定义源。写
\[
 R_\lambda(x)=\sum_{2\le n\le x}\lambda(n)-x,\qquad
 E(x)=R_\lambda(x)+1-F(x).
\]
由望远镜求和，
\[
 E(x)=F(\lfloor x\rfloor)-F(x)-\{x\},\qquad
 E(1)=0,\qquad |E(x)|\le3/2 .
 \tag{39}
\]
格点跳跃仍包含在 \(dE\) 内。不能用 \(|E|\) 有界就默认其响应的全部频率很小；
第6.4节将单独估算这一项。

### 6.2 整数留数、单值亚纯延拓及正系数

令 \(\mathcal D_\lambda(s)=\sum_{n\ge2}\lambda(n)n^{-s}\)，初始 \(\Re s>1\)。
对 \(n>B\)，Taylor 余项或导数积分给
\[
 \lambda(n)-1
 =-\frac{n^\rho-(n-1)^\rho}{\rho}
  -\frac{n^{\bar\rho}-(n-1)^{\bar\rho}}{\bar\rho}
 =-n^{\rho-1}-n^{\bar\rho-1}+O_\rho(n^{\theta-2}).
 \tag{40}
\]
所有 \(n\le B\) 的差异只是一个有限 Dirichlet 多项式。因此
\[
 \mathcal D_\lambda(s)=\zeta(s)-1
             -\zeta(s+1-\rho)-\zeta(s+1-\bar\rho)+H(s),
 \tag{41}
\]
其中 \(H\) 在 \(\mathcal H=\{\Re s>\theta-1\}\) 全纯。
余项级数在每个紧子集由 \(\sum n^{\theta-2-\Re s}\) 一致绝对收敛；
有限项及加回 \(n=1\) 的常数归入 \(H\)。
故 \(\mathcal D_\lambda\) 在 \(\mathcal H\) 的全部极点和留数恰为
\[
 (1,1),\qquad(\rho,-1),\qquad(\bar\rho,-1).
 \tag{42}
\]
这里(41)用的是普通 \(\zeta\)，不是 \(-\zeta'/\zeta\)，其零点不产生额外极点。

在 \(\Re s>1\) 定义
\[
 Z(s)=\exp\left(\sum_{n\ge2}
                 \frac{\lambda(n)}{\log n}n^{-s}\right).
 \tag{43}
\]
级数局部一致绝对收敛，逐项微分给 \(-Z'/Z=\mathcal D_\lambda\)。
若 \(b(n)=\lambda(n)/\log n\)（\(n\ge2\)、\(b(1)=0\)），其 Dirichlet 展开为
\[
 Z(s)=\sum_{n\ge1}a(n)n^{-s},\qquad
 a(n)=\sum_{k=0}^{\lfloor\log_2 n\rfloor}\frac{b^{*k}(n)}{k!}\ge0 .
 \tag{44}
\]
约定 \(b^{*0}\) 为 Dirichlet 卷积单位；对 \(n=1\) 有 \(a(1)=1\)。
绝对收敛的指数展开证明(44)，不是数值拟合的系数正性。

令
\[
 G(s)=\mathcal D_\lambda(s)-\frac1{s-1}
                         +\frac1{s-\rho}+\frac1{s-\bar\rho}.
 \tag{45}
\]
\(G\) 在单连通的 \(\mathcal H\) 全纯，故有全纯原函数 \(\mathcal G\)。
取适当非零常数 \(C\)，函数
\[
 Z_{\rm ext}(s)=
 C\frac{(s-\rho)(s-\bar\rho)}{s-1}\exp(-\mathcal G(s))
 \tag{46}
\]
在 \(\mathcal H\) 单值亚纯，且其负对数导数恰为 \(\mathcal D_\lambda\)。
在实点 \(s=2\) 匹配(43)，两函数的商在 \(\Re s>1\) 为常数1，
所以(46)是 \(Z\) 的延拓。指数因子没有零极点，故除数恰如定理所列。
实际整数留数在这里必不可少；若只构造任意复留数后形式积分，
不能保证得到单值亚纯函数。共轭对称性也由实系数和唯一延拓保持。

### 6.3 固定 cutoff 质量及共尾选择

取 \(Y=N\ge B\)。由 \(dR_\lambda=dF+dE\)，
\[
 M_\lambda(Y,Y)=M_F(Y)+M_E(Y),\qquad
 M_F(Y)=-2\Re\int_B^Y x^{\rho-\sigma-1}e^{-x/Y}\,dx .
\]
对 \(E(1)=0\) 使用正递减权的完整 Stieltjes 分部积分，
\[
 |M_E(Y)|\le\frac32\left(w_Y(Y)+\int_1^Y(-w_Y')\right)
              =\frac32e^{-1/Y}.
 \tag{47}
\]
令 \(g=\gamma(\rho-\sigma,1)\ne0\)，无零性由283-B给出。换元即有
\[
 M_\lambda(Y,Y)=-2\Re\{gY^{\rho-\sigma}\}+O_{\rho,\sigma,B}(1).
 \tag{48}
\]
从 \([0,B]\) 减去的固定前缀积分是该常数的一部分，可很大；在有限实验中
不得误删它。相位 \(\gamma\log Y+\arg g\) 在正、负余弦固定子区间内
各有无界实区间，其长度趋于无穷，故包含整数；(48)给两侧
\(\Omega(Y^{\theta-\sigma})\) 及共尾好相位整数。

如需与本轮完全同型的 history guard，固定任意 \(0<\sigma<\beta<1/2\)，
对这些整数取 \(n^{-(\beta-\sigma)}M_\lambda(n,n)\) 的过去绝对值记录。
\(\theta-\beta>0\) 使第2.2节的证明逐字保留 \(N^{\theta-\sigma}\) 强度。
284的 Volterra/因果逆适用于这里的右连续源；整数化只用
\(\lambda(n)\le3/2\)，仍有统一的 \(C_{\rm round}\)。
因此同一记录最终满足
\[
 P_{\lambda,\beta}(N)N^{\beta-\sigma}
       <4C_{\rm inv}|M_\lambda(N,N)|,\qquad
 |M_\lambda(N,N)|\gg N^{\theta-\sigma}.
 \tag{49}
\]
该论证不调用实际 zeta 的零点或 RH；模型振荡已经由(48)显式证明。

还有一个精确的 dyadic 版本。若 \(\omega=\gamma\log2\notin\pi\mathbb Z\)，
有限几何和给
\[
 \frac1K\sum_{m=1}^K\cos^2(\omega m+\arg g)
           =\frac12+O_\omega(K^{-1}).
 \tag{49a}
\]
因此有无界整数 \(m\) 满足 \(|\cos(\omega m+\arg g)|\ge1/2\)；
否则均值最终至多 \(1/4+o(1)\)，矛盾。
取 \(Y=N=2^m\)，(48)在足够大时给 \(|M_\lambda|\ge(|g|/2)Y^{\theta-\sigma}\)。
整数端点有 \(R_\lambda(n)=F(n)-1\)，且
\(|F(n)|\le(2/\theta)n^\theta\)，故
\[
 P_{\lambda,\beta}(N)\le(2/\theta+1)N^{\theta-\beta}.
 \tag{49b}
\]
这些 dyadic 好点也满足固定模型 guard，例如常数 \(4(2/\theta+1)/|g|\)；
下面全频证明仍适用。所用数值参数 \(\gamma=2\) 满足
\(0<2\log2<2<\pi\)，无须任何无理性断言。
这里只证明一条 dyadic 好子序列，未审定256全部附加假设，
也不将其冒称为275或284的原记录算法。

### 6.4 完整整数响应：不能只计算连续模板

令 \(r_F,r_E\) 分别为 \(w_YdF,w_YdE\) 推前到原 lag、
对称化并减去各自中心质量后的零质量测度。精确有
\(r_\lambda=r_F+r_E\)，全部测度仍取共同 cutoff \(Y=N\)。
连续模板满足
\[
 \|w_YdF\|_{\rm TV}\ll_{\rho,\sigma}Y^{\theta-\sigma}.
\]
其中心化测度 \(r_F*r_F\) 支撑在 \([-2L,2L]\)，总变差至多
\(4\|w_YdF\|_{\rm TV}^2\)。用 primitive 的平方积分恒等式，得到
\[
 Q_{\mathbb R}(r_F)
       \ll_{\rho,\sigma}Y^{4(\theta-\sigma)}L .
 \tag{50}
\]

以下单独处理格点误差。置 \(f_\xi(x)=w_Y(x)(\cos(\xi\log x)-1)\)。
完整 Stieltjes 恒等式为
\[
 \widehat r_E(\xi)=f_\xi(Y)E(Y)-\int_1^Y E(x)f_\xi'(x)\,dx .
 \tag{51}
\]
下端 \(f_\xi(1)=0\)，但右端没有删除。对 \(q=|\xi|\le1\)，
\(|1-\cos(\xi\log x)|\le q^2(\log x)^2/2\)、
\(|\sin(\xi\log x)|\le q\log x\)。
在 \(x\le Y\) 上 \(|w_Y'|\le(\sigma+1)x^{-\sigma-1}\)，而
\(\int_1^\infty x^{-\sigma-1}(\log x)^jdx<\infty\) 对 \(j=1,2\) 成立。
端点 \(Y^{-\sigma}(\log Y)^2\) 也一致有界，故(51)给
\[
 |\widehat r_E(\xi)|\ll_\sigma q^2\quad(q\le1).
\]
用 \(|1-\cos|\le2,|\sin|\le1\) 代入同式，且
\(\int_1^Yw_Y(x)dx/x\le1/\sigma\)，给全频界 \(O_\sigma(1+q)\)。
另一方面，正权、\(\lambda(n)\le3/2\) 和 \(|F'|\le1/2\) 给
\[
 \|w_YdE\|_{\rm TV}
 \le\sum_{n\le Y}\lambda(n)w_Y(n)
       +\int_1^Yw_Y(x)(1+|F'(x)|)dx
 \ll_\sigma Y^{1-\sigma}.
\]
所以又有 \(|\widehat r_E|\ll_\sigma Y^{1-\sigma}\)。对任意 \(V\ge1\)，
分别积分 \(q\le1\)、\(1<q\le V\)、\(q>V\)：
\[
 Q_{\mathbb R}(r_E)
 \ll_\sigma1+V^3+\frac{Y^{4(1-\sigma)}}V
 \ll_\sigma Y^{3(1-\sigma)}
 \quad\text{取 }V=Y^{1-\sigma}.
 \tag{52}
\]
由(37)，\(3(1-\sigma)<4(\theta-\sigma)\)，故(52)在(49)序列上
为 \(o(M_\lambda^4L)\)。这控制了整数原子的整个无限高频尾，
不是从有限频带复算外推。

由加权 \(L^4\) 三角不等式、(49)--(52)，
\[
 Q_{\mathbb R}(r_\lambda)\ll M_\lambda^4L .
 \tag{53}
\]
真实模型正源满足 \(A\ll_\sigma Y^{1-\sigma}\)，匹配连续 bulk 给
\(S\asymp Y^{1-\sigma},D\asymp S^2L\)，与第4.2节同证。
原两个正通道仍有 \(|\widehat p|^2+|\widehat c|^2\le4S^2\)，
所以 \(J_4/\mu^4\ll Q_{\mathbb R}(r_\lambda)/(M_\lambda^4L)=O(1)\)。
这证明定理286-B的全部断言。\(\square\)

### 6.5 障碍的精确范围

反例排除的是：仅从固定正整数源、匹配连续背景、单值亚纯延拓、
整数除数留数及上述共尾质量相对预算，就推出所有目标零点位于
\(\Re s=1/2\) 的一般推理。甚至加入同型的历史 guard 仍不够。
这里的零点是(46)中真正的函数零点，不只是任意复留数形式产生的“模式”。

但 \(\lambda(n)\) 在一般整数上非零，不是 \(\Lambda(n)\)，不是标准素数幂支撑；
\(Z\) 也没有本篇证明的完成函数方程、Euler 乘积或 Weil 显式公式正性。
因此它不排除同时利用这些缺失结构的路线，不是对完整广义 Weil 配置的反例。
它说明281的“非亚纯”缺陷被补上后，单独的质量相对预算仍不能普遍识别中心线。
实际286-A仍只标[C]，不得把这个模型[N]转移给 Riemann zeta。

这些模型差异可以直接定位。首先 \(\lambda(6)=1\)，而一个在某右半平面
绝对收敛、各局部因子只依赖 \(p^{-s}\) 的标准素数 Euler 乘积，其负对数导数
的 Dirichlet 支撑只能在素数幂上；绝对收敛 Dirichlet 级数的系数唯一性排除两者相等。
其次，(46)在整个开临界带只在 \(\rho,\bar\rho\) 有零点，却在
\(1-\rho,1-\bar\rho\) 非零。因此乘以任何在开临界带全纯无零的完成因子，
都不能得到要求关于 \(1/2\) 反射的函数方程；否则反射零点立即产生矛盾。
这涵盖在该带无零无极点的通常 Gamma 完成因子及只在 \(0,1\) 消去极点的因子。
本篇没有把缺失的 Euler/对偶性结构隐藏在“zeta 型”名称中。

### 6.6 可复现有限模型检查 [E]

主代理读并独立运行
`python -B scripts/meromorphic_response_model_probe.py --max-m 18`。
固定 \(\sigma=1/4,\theta=17/20,\gamma=2,B=10322\)，
计算完整整数源及反射频带 \(|\xi|\le2L\)，保留原 \(p,c,S,D\)。
连续模式只取 \((B,N]\)，并另行展示忽略固定前缀的渐近主项。

| \(Y=N\) | 实际 \(M\) | 有限模式 \(M_F\) | 不含固定前缀的主项 | \(J_{4,|\xi|\le2L}/\mu^4\) |
|---:|---:|---:|---:|---:|
| \(2^{14}\) | -117.764830 | -117.305902 | -74.116914 | 7.293612 |
| \(2^{16}\) | 18.126853 | 18.593518 | 45.352560 | 15962.47743 |
| \(2^{18}\) | 175.891272 | 176.362096 | 196.832822 | 106.464235 |

这些预选窗口不是已认证的质量记录，第二行有很小的质量分母。
不能据此表的比值大小或变化判断渐近预算成立/失败。
固定前缀在本批数值中明显不可忽略，实际 \(M-M_F\) 则全部符合(47)的界。

脚本在原物理权中保留
\((\widehat r_F+\widehat r_E)^4\) 的五个有符号项，求和相对误差小于
\(7.97\cdot10^{-16}\)。两级高斯求积结果的最大相对差为
\(1.24\cdot10^{-10}\)；初试的粗面板未达预定门槛后，缩小面板重跑，
没有放宽门槛或删掉交叉项。MP50独立模式/连续变换、首窗口全原子求和
的误差分别不超过 \(3.85\cdot10^{-13},1.20\cdot10^{-15},5.62\cdot10^{-17}\)。
单个系数和(40)的 Taylor 余项界也独立复算通过。

这些是有限一致性实验，不是区间认证；未采样的频率尾没有数值结论。
完整模型预算来自(50)--(53)的独立解析证明，亚纯性来自(40)--(46)，
不由数值图形或拟合产生。本轮没有改动持续集成依赖或 PDF。

## 7. 依赖与结果边界

- (H)是明确的条件输入，不是未经解释的广义 Weil 结构公理。
- 实际净质量的边缘幂次来自283定量 Landau 结论；因果逆核和记录选择本身
  不产生振荡。
- 历史 guard 来自284的完整稳定逆，而不是由端点质量大自动推断。
- 全部零点的统一响应上界来自282的一般实部版本；保留真实端点与中心质量。
- 物理比较只用同一套实际正通道、Brownian 分母和粗素数增长。
- 本篇不证明实际 zeta 的上确界必然达到、不证明 \(\Theta<1\)，也不产生其离线零点。
- 模型[N]有独立完整构造；原 Weil 存在性、Gamma gluing 和统一算术正性仍开放，
  实际[C]不得升级为实际[N]。

主代理独立审查第1--5节，并完整构造、证明第6节；
gap_exception_audit 独立逆向复核全文，carrier_audit 独立复核第6节，
midband_compute 另核算模型、写并运行脚本；主代理全文读并独立复跑三窗口。
特别核验了实际[C]/模型[N]边界、单位整数留数、固定前缀及完整整数高频残差。
dyadic 几何和与固定 guard 推论亦经 gap_exception_audit 独立核算。
完整内部证明不等于文献新颖性、外部同行评审或完整 Goal 的阶段验收。
