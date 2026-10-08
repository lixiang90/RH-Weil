# 原product-cell：完整连续主项付款与真实素数偏差

2026-10-08，checkpoint_audit。研究轮3，基线 main cd95587。
只新增本研究源，不修改冻结输入、输出、检查器或Git。
状态：完整连续参考项证明，待不同作者全文审查。

本稿定义同一实际mask上的双连续腿reference，并严格支付其完整signed值
至O_(φ,χ)(L^(−3))。这不是实际prime主项的界。
真实函数减去该reference的偏差仍保留全部actual primes和同一u，尚未支付。
另明确product-cell的h=1端点主项，不能将每个Taylor阶都当作mean为零。

## 1. 固定输入与原对象

本轮 FULL READ 原scalar源370行；actual425、slice337和上一轮191行
沿连续研究已完整读取。canonical UTF-8 LF只转CRLF/lone CR，不trim：

| 输入 | SHA256 |
| --- | --- |
| [原scalar及φ导数合同](hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md) | f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7 |
| [actual425与同u](hybrid-whole-fourth-unit-unit-actual-research-whole.md) | b3f14cf4ee5659f8e23bd51dc9bf71e853e783bd2d55e42ee8846d6e8d1e41dc |
| [337共同J及准确mask](hybrid-original-high-product-minor-rational-slice-research-high-product.md) | 56219e9f136c0f0666c5b1ce028ec4d7d93ad33f5ebd43d5e4a5e34c399677a8 |
| [191完整coherent能量](hybrid-original-coherent-period-energy-research-checkpoint-audit.md) | fe19e50f955c47b7abb22933d0b406a9bc339ac68056d8d115d1f7277be22c5f |

保持X=T/(2π)、L=logX、N_L=a_LL、b_p=log p/(N_L√p)。
原φ zero extension为even C²、0≤φ≤1、a_L≥c_φ>0。
scalar源21–30给∥φ′∥1+∥φ″∥1≤C_φ，故∥φ′∥∞≤C_φ。
本稿不要求φ″的uniform sup，也不升级φ光滑性。

q,s仍是实际外genuine primes，√X<s<q≤X，q是真实最大者。
全部原interior、qs产品cap、Ω(q,n,S)频率mask与两个最大标签profiles保留。
原ν仍是425(11)的正概率密度，含全部d floor、χ与正height。
先用ν零支撑写337共同J_q，再恢复ν、g和φ的共同参数积分。
本稿连续项的估计在恢复后直接进行；没有为φ Fourier参数要求额外moments。

## 2. 正确continuous-density的定义

实际prime measure为Σ_p b_p δ_p；连续reference定义为
\[
 d\mu_0(p)=\frac{dp}{N_L\sqrt p}.
 \tag{1}
\]
它来自形式mean measure dp/log p乘原log p权。
这是参考项的定义，不是断言实际prime measure与它的误差已小。
连续腿的sharp intervals是
I_p=(P,2P]∩(√X,q)、I_r=(R,2R]∩(√X,q)，保留所有真实dyadic endpoints。
空区间给零，不要求非空区间长度与P或R可比。

令Φ_ℓ(p,r;q,s,u)为425(4)或(5)的两套profile乘积，去掉b_p,b_r。
两者只含原p-only、r-only φ因子，始终是同一个u。
固定g为已准入产品窗，定义完整连续双腿
\[
 G_0^{(\ell)}(q,s,n,u;P,R)
 =\frac1{N_L^2}\int_{I_p}\int_{I_r}
  \frac{\Phi_\ell(p,r;q,s,u)g(pr/(qs))}{\sqrt{pr}}
  e(-npr/q^2)\,dr\,dp.
 \tag{2}
\]
g支撑令PR≍qs；没有将它的s依赖作为私有系数塞入联合大筛。
实际p=s、r=s的删除点在连续measure中为零；原p=r原子也不由reference冒充。

固定共同Mellin参数时，保留两连续腿的twistsτ_p,τ_r，
其正确product pushforward density为
\[
 c_{q,\lambda}(k)=\frac{k^{-1/2+i\tau_r}}{N_L^2}
    \int_{\substack{p\in I_p\\k/p\in I_r}}
           p^{i(\tau_p-\tau_r)}\frac{dp}{p}.
 \tag{3}
\]
Jacobian为dr=dk/p。恢复全部公共参数后得到相应c_(q,s,u)(k)，
含原Φ和g；(2)准确等于∫c_(q,s,u)(k)e(−nk/q²)dk。
这是一份连续k-measure，不是将c(k)采样成整数原子。
尤其不把v=0的模型值当成实际q|pr项。

## 3. 两次分部积分：所有sharp角与边均付

实际ν支撑给n≍qX/s，置α=n/q²、A=PR；则αA≍X。
p=P x、r=R y后，(2)为
\[
 \frac{\sqrt A}{N_L^2}\int_a^b\int_c^d
   W(x,y)e^{-i\Lambda xy}\,dy\,dx,
 \quad \Lambda=2\pi\alpha A\asymp X,
 \tag{4}
\]
其中1≤a≤b≤2、1≤c≤d≤2，q-clipping仍严格保留。
W=(xy)^(-1/2)Φ_ℓ(Px,Ry;q,s,u)g(Axy/(qs))。
由φ′ uniform sup与固定g，有
\[
 \|W\|_\infty+\|W_x\|_\infty+
 \|W_y\|_\infty+\|W_{xy}\|_\infty\le C_{\phi,g}.
 \tag{5}
\]
mixed导数只对每个独立φ腿求一次导数；g最多求二阶。
u仅作为同一固定参数，没有对它求导。

先对x用e^(−iΛxy)=(−iΛy)^(-1)∂_x e^(−iΛxy)。
它给x两端的∫W/y及bulk的∫W_x/y，各有Λ^(-1)。
再对每个y积分用(−iΛx)^(-1)∂_y。
结果含四个corner、两条fixed-x edge、两条fixed-y edge和bulk。
振幅分别是W/(xy)、∂_y(W/y)/x、W_x/(xy)、∂_y(W_x/y)/x，
全由(5)支付，x,y都≥1，interval长度≤1。
没有漏掉sharp q-prefix boundary，也没有用短interval长度作分母。
严格得到
\[
 \boxed{|G_0^{(\ell)}|\le
  C_{\phi,g}\frac{\sqrt{PR}}{N_L^2X^2}.}
 \tag{6}
\]
这给完整两连续腿的真实振荡相消。若在Fourier参数上逐项取derivative界，
会引入未付φ weighted moments；本稿没有采用那个顺序。

## 4. 同一mask与ν质量下的完整reference预算

用(2)替换当前主频带中两内prime腿，外q,s及same-u保持原样，
定义K_0；对当前K的两个rational complement及任何其子mask均同样定义。
这是新定义的reference，下面的upper直接逐n证明，未限制某旧signed总界。
原正prefactor的n质量有准确界
\[
 \sum_{n\in\mathbb Z}\frac{2\pi s}{q}\nu(2\pi sn/q)\le C_\chi.
 \tag{7}
\]
ν支撑长度O(X)、sup≤Cχ/X，步长2πs/q≤2π，
整数count为O(qX/s+1)；其中+1项仍付O((s/q)/X)。
ν支撑外严格为零，原floors和正height均未丢弃。

固定q,s时PR≍qs的dyadic pairs数O(L)，各pair的(6)一致。
Chebyshev的Σ_(p≤X)log p≤CX给
\[
 \sum_{\sqrt X<s<q\le X} b_qb_s\sqrt{qs}
 \le \frac{CX^2}{N_L^2}.
 \tag{8}
\]
外L^(-1)∫_(I+)φ(u)²du≤1/2；四种最大标签位置只付固定倍数。
(6)–(8)直接给完整signed reference
\[
 \boxed{|K_0|\le C_{\phi,\chi,g}\frac{L}{N_L^4}
                 \ll_{\phi,\chi,g}L^{-3}.}
 \tag{9}
\]
这是整个实际高产品mask的连续主项付款，包含edge和fullperiod。
没有把恢复ν之前的individual(s,n) mask重新塞入分离后的两腿。

## 5. cell mean cancellation与h=1端点项

固定公共参数的连续product-cell必须定义为
\[
 B^0_{q,z,h,I}=\int_0^q c_{q,\lambda}(qz+v)
                  D_I(v)(v/q)^h\,dv,
 \quad D_I(v)=\sum_{j\in I}e(-jv/q).
 \tag{10}
\]
这里v是连续变量。k=qz+v及slow相位Taylor仍是准确变换，
它还原连续G_0；无需Euler–Maclaurin或凭空插入lattice aliases。

原正height使非空完整j窗在正整数上。若一个cell的density为常数c_z，
则h=0严格有B^0_(z,0)=0，因为∫_0^1e(−jy)dy=0，对每j≥1成立。
但
\[
 \int_0^1 y e(-jy)dy=-\frac1{2\pi i j},\qquad
 B^0_{q,z,1,I}=-\frac{q c_z}{2\pi i}\sum_{j\in I}\frac1j.
 \tag{11}
\]
这是明确endpoint项。j≍M、|I|≍M时harmonic和为常数量级。
在(3)的τ_p=τ_r=0、overlap loglength有固定正下界且避开product corners的bulk，
c在宽q cell上的变化为相对O(q/(PR))=O(1/S)，且|c′|≤Cc/(PR)。
对y c(q(z+y))分部积分并用常数的整周期积分为零，得到
B^0_(q,z,1,I)=−qc(q(z+1))/(2πi)Σ_(j∈I)1/j+O(qc(q(z+1))/S)。
这条bulk尺度比较只用于上述无twist的正连续density；
它不是全部实际prime或公共参数的额外估计。

所以未减mean的逐h cell能量目标可能要求额外消去这些endpoint项。
它不是完整H的必要条件：全部slow相位、相邻cells及公共参数联合恢复后，
这些model边界按第3–4节已付款。没有从(11)断言真实prime估计不可能。

## 6. 真实偏差的精确归属

令K_pr为当前已冻结实际prime主频带，含同u、准确q-prefix、s排除和Ω。
按定义严格有K_pr=K_0+K_dev，K_dev=K_pr−K_0。
连续删除p=s、r=s是measure-zero；实际删除仍由K_pr自己的原tuple规则保留。
旧nn、graph、chirp及physical桥的signed误差保持旧完整付款范围，不被重切。

在固定公共参数的product-cell上，准确deviation为
\[
 B^{\rm dev}_{q,z,h,I}=
 \sum_{v=0}^{q-1}C_{q,qz+v}D_I(v)(v/q)^h-B^0_{q,z,h,I}.
 \tag{12}
\]
第一项仍是实际prime乘积，第二项是连续integral，不是同一类measure的采样差。
另一等价写法是每腿实际measure减μ0后的mixed与double-deviation三项；
每个实际s删除点和sharp区间必须一并包含，不能只保留double项。
本稿没有支付这些三项的全signed预算，也未引用Dirichlet-L全族前件。
普通[Rθ]的prefix上界本身不能把(12)当作已小的短cell covariance。

本轮严格新增的是(6)、(9)的完整连续reference付款与(11)的mean endpoint核。
真实K_dev仍承载原高产品prime covariance问题；其省幂尚未证明。
没有新whole、中心常数预算、比例或无零边界，没有数值采样或新checker。
