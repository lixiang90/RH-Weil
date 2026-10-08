# 原Kdev：两条mixed prime／continuous腿的完整polylog付款

2026-10-08，checkpoint_audit。研究轮4，基线main da5f0df。
只新增本研究源，不修改冻结输入、检查器、输出或Git。
状态：完整解析证明，待不同作者全文审查。

本稿对493的同一实际主频带证明：一条内腿是原actual prime measure，
另一条是μ0连续measure时，全部端点、bulk、共同频率mask与same-u union
只有O_(φ,χ,g)(L^C)费用。因此两个Δμ／μ0 mixed项也已付polylog；
未付对象可准确缩为两条内腿都是Δμ的完整signed项。
没有实际double-deviation省幂、whole四矩或中心常数的新界。

## 1. 固定输入与scope

本轮FULL READ actual425和493；原scalar370、337与195源在连续研究中
已完整读取，且本轮重核实际所用合同及全部canonical UTF-8 LF身份：

| 输入 | SHA256 |
| --- | --- |
| [原C²与prime系数](hybrid-short-carrier-canonical-scalar-fourth-admission-research-radial.md) | f04279a9de54303d772859b2ee5e05010567404c53143c928a14e905eb51a0d7 |
| [actual425、两个profiles与ν](hybrid-whole-fourth-unit-unit-actual-research-whole.md) | b3f14cf4ee5659f8e23bd51dc9bf71e853e783bd2d55e42ee8846d6e8d1e41dc |
| [337共同J与参数分离](hybrid-original-high-product-minor-rational-slice-research-high-product.md) | 56219e9f136c0f0666c5b1ce028ec4d7d93ad33f5ebd43d5e4a5e34c399677a8 |
| [195双连续reference与deviation](hybrid-original-product-cell-continuous-main-and-prime-deviation-research-checkpoint-audit.md) | f55667a3d84405eb183e94a1a3e03ccda127bbe075e920744d0262dfcfea10e9 |
| [493准确剩余](../../notes/493-original-reference-subtraction-and-carrier-near-correlations.md) | efbefb73a457e1bda079fdb9c003ec4bcf9c50d89a1f1c2053b548153371a67a |

保持X=T/(2π)、L=logX、N_L=a_LL、a_L≥cφ>0和
b_p=log p/(N_L√p)。φ是原zero-extended even C² taper，0≤φ≤1，
∥φ′∥1+∥φ″∥1≤Cφ、∥φ∥1≤CL，故∥φ′∥∞≤Cφ。
χ、ν、d的floor、正height、g、四种最大标签位置与同一个u均保留。

q,s仍是实际genuine primes，√X<s<q≤X；q为实际最大者。
固定q∈(Q,2Q]、s∈(S,2S]，全部interior与实际产品cap给真实s区间。
固定内腿dyads(P,2P]、(R,2R]，严格q-prefix保留，P,R≤q且PR≍QS。
频率先用ν零支撑写在337的共同J_q内；原删弧、unit限制、fullperiod／edge
及任何已有产品分块，只保留对应的准确(q,n,S)共同mask。
本证明直接逐mask做正范数估计，不截取某旧signed总量的上界。

## 2. mixed函数与一次连续分部积分

先让p为连续腿，r为实际prime腿。将425的profile写为
Φ(p,r;q,s,u)=A(p;q,s,u)B(r;q,s,u)，其中A与B分别只含p与r变量。
从425(4)、(5)可直接得
|A|≤1、|∂_pA|≤Cφ/P，|B|≤1。
定义完整mixed内腿（先不删r=s，以第7节的正估计准确修正）
\[
 G_{0,\mathrm{pr}}=
 \frac1{N_L}\int_{I_p}p^{-1/2}A(p)
 \sum_{r\in I_r\cap\mathbb P}b_r B(r)g(pr/(qs))
                  e(-npr/q^2)\,dp,
 \tag{1}
\]
I_p=(P,2P]∩(√X,q)，I_r=(R,2R]∩(√X,q)。空区间为零。
令f(p,r;s)=p^(-1/2)A(p)g(pr/(qs))。因为n>0、r>√X，精确有
\[
 G_{0,\mathrm{pr}}=-\frac{q^2}{2\pi i nN_L}
 \sum_r\frac{b_rB(r)}r
 \left\{[f(p,r;s)e(-npr/q^2)]_{\partial I_p}
       -\int_{I_p}\partial_pf(p,r;s)e(-npr/q^2)\,dp\right\}.
 \tag{2}
\]
全部continuous lower／upper endpoints、dyadic endpoints与q-clipped endpoint
均在(2)，无需它们是整数。没有丢掉p=q的alias或其他dyadic alias。
bulk的三项分别来自p^(-1/2)、A和g；
\[
 \partial_pf=p^{-3/2}\left[-\tfrac12 A g+(p\partial_pA)g+
                                A\,(xg'(x))\right],\quad x=pr/(qs).
 \tag{3}
\]
p∂pA有uniform sup，g和xg′是固定smooth产品窗。

## 3. ν／n的精确共同分离；不对φ′索取weighted矩

置y=sn/(qX)、V(y)=Xν(2πXy)、V1(y)=V(y)/y。
V及V1支撑在同一固定正紧区间，后者没有y=0问题。
原prefactor乘(2)的q²/(2πnN_L)准确为
\[
 \frac{2\pi s}{q}\nu(2\pi sn/q)\frac{q^2}{2\pi nN_L}
       =\frac{s^2}{N_LX^2}V_1(sn/(qX)).
 \tag{4}
\]
V1的前两阶对数导数只损失L^C；其共同Mellin包络的L1质量为L^C。
Mellin中的真实n外相位n^(itν)(qX)^(-itν)完整保留，模长1。
它将在每个j的residue Cauchy–Schwarz中作为diagonal unit乘子。
没有对它求导，也没有删掉原ν、floor或公共参数尾。

在(2)之后才分离仍跨actual r／s的未求导φ因子、g与xg′。
原φ的Fourier绝对积分由
|φhat(t)|≲min(L,Cφ|t|^(-2))给L^C；固定g窗的Mellin绝对积分为常数。
所以全部这些公共参数有同一个L1正包络，其质量为L^C，
不随q、n、p或某个私有prime tuple改变。

关键顺序是：连续腿已经求导，固定当前连续坐标p之后，
p∂pA(p;q,s,u)仍可直接留作F的bounded s系数。
它不依赖n或actual r，因此对每个q,p的完整residue Parseval合法。
本稿不需要F系数在不同p之间相同；bulk用Minkowski后取uniform界。
无需把φ′ Fourier分离，不要求∫|t φhat(t)|dt或φ″uniform sup。
例如第二位置φ′(u+log(s/p))正是这样的s系数；
也可用φ′(v)=∫_(−∞)^v φ″(w)dw作阈值区间分解，总variation≤Cφ，
但这里直接bounded coefficient的Parseval已经足够。

## 4. 所有continuous endpoints的actual prime平方能量

写n=a+qj，0≤a<q。固定q、p∈I_p的闭包、j及所有公共参数。
实际r<q，频率ξ_r=pr/q²落在(0,1)；相邻不同整数r的距离至少p/q²。
整族跨度≤p(q−1)/q²，故圆上的wrapgap也≥p/q²。
于是δ=p/q²是真实circle spacing，包括p=q边界。

自足的平方能量界如下。几何和给Gram entry
|Σ_(a=0)^(q−1)e(a(ξ_r−ξ_r′))|≤min(q,(2∥ξ_r−ξ_r′∥)^(-1))。
按δ-spacing排列每一行的正负circle距离，Schur行和≤C(q+δ^(-1)log(2q))。
因此任意真实r系数c_r均有
\[
 \sum_{a=0}^{q-1}\left|\sum_rc_re(-apr/q^2)\right|^2
 \le C\left(q+\frac{q^2}{p}L\right)\sum_r|c_r|^2
 \ll\frac{q^2}{P}L\sum_r|c_r|^2.
 \tag{5}
\]
这只是单q完整residue能量；没有假设Dirichlet-L全族RH，
也没有借用一个要求跨q固定系数的联合大筛。
j相位e(−jpr/q)只改变c_r的模1 twist，故(5)对全部真实j统一成立。
原prime norm为Σ_r b_r²≲φ1；r/R及所有normalized prime weights有界。
一个endpoint的实际r-leg含p^(-1/2)b_r/r，因此
\[
 \|H_{q,p,j}\|_{\ell^2(a)}
 \ll\frac{qL^{1/2}}{PR}\ll\frac{L^{1/2}}S.
 \tag{6}
\]
任何实际a-mask只缩小这个正能量。q endpoint中j相位确实消失，
但(5)同样支付其他全部alias；证明未将前一种特殊相位套给其他端点。

bulk的(3)多一个1/P，且其continuous积分长度≤P。
对每个p先用(5)–(6)，再Minkowski积分，仍得(6)；
被q截得很短的区间不产生反长度损失。
所有端点与bulk仅有固定多个此类项。

## 5. 保留F相消后的完整box与union付款

固定p与公共参数，外F为
F_(q,p)(a)=Σ_(s∈S_q)b_s(s/S)²β_s(q,p,u,λ)e(as/q)，|β_s|≤Cφ。
这里S_q是原准确s支持，含产品cap、interior、sharp endpoints；
β可以随q,p变化，但与a、j无关。实际s<q给不同modq残类，故
\[
 \|F_{q,p}\|_{\ell^2(a)}^2=q\sum_{s\in S_q}
       |b_s(s/S)^2\beta_s|^2\ll_\phi q.
 \tag{7}
\]
原同u的s-only profiles直接留在β里；已经分离的twists均模1。
每个q,j的实际mask（含unit与至多两端partial period）作为正投影保留。
联合n外twist与(6)、(7)一起Cauchy–Schwarz，不取F的逐点绝对L1质量。

共同J_q只含0<n≲qX/S。j的准确个数≤C(X/S+1)，
其中+1保留；由于S≤X，X/S≥1。不存在丢掉j=0的步骤。
若j=0，n=0仅可在扩大的正平方范数内添加；实际mask仍n>0，
n^(itν)只在实际非零n上取值，不定义0^(itν)。
Chebyshev给Σ_(q∼Q)b_q≲√Q/N_L。
用(4)、(6)、(7)及全部j，固定(Q,S,P,R)的费用为
\[
 \frac{S^2}{N_LX^2}\left(\frac XS+1\right)
 \frac{\sqrt Q}{N_L}\frac{\sqrt Q}S L^C
 \ll_\phi\frac{Q}{N_L^2X}\left(1+\frac SX\right)L^C
 \ll_\phi L^C.
 \tag{8}
\]
公共参数正包络已含在L^C中，没有τ未付款的尾。
再对全部O(L^C)个实际dyadic boxes求和，恢复原
L^(-1)∫_(I+)φ(u)²du≤1/2及四种最大标签位置，只增加polylog。
因此全部一连续、一actual-prime腿的同mask union有
\[
 \boxed{|K_{0,\mathrm{pr}}|\ll_{\phi,\chi,g}L^C.}
 \tag{9}
\]
这里是原χ-carrier signed函数，不是某个canonical任意子块的norm。

## 6. 交换两条内腿的合同

把r作为连续腿、p作为actual prime时，相位与(2)完全对称。
原profiles虽不对称，但仍是p-only乘r-only。
求导只施于continuous profile；其r／s ratio derivative在固定r后
成为F的bounded s系数，actual p／s的未求导ratio仍用原C² L1包络。
所以(4)–(8)以P、R交换后原样成立，得到
\[
 \boxed{|K_{\mathrm{pr},0}|\ll_{\phi,\chi,g}L^C.}
 \tag{10}
\]
同一个u、全部q-prefix、all aliases及n外twist继续保留。

## 7. actual s点删除的直接正付款

连续p=s的删除是measure-zero。actual r=s必须另付，不能让其s依赖
隐藏在分离后的r系数里。直接对单点r=s的连续积分用(2)：
g支撑强制P≍q，且n≍qX/s，端点与bulk的绝对界为
\[
 |G_{0,r=s}|\ll_{\phi,g}\frac{b_s\sqrt q}{N_LX}.
 \tag{11}
\]
原ν的正n质量准确有Σ_n(2πs/q)ν(2πsn/q)≤Cχ，含整数count的+1。
所以任何准确mask的删除费用为
\[
 \sum_{q\sim Q}b_q\frac{\sqrt q}{N_LX}\sum_{s<q}b_s^2
 \ll_\phi\frac{Q}{N_L^2X}\ll_\phi L^C.
 \tag{12}
\]
产品窗使相关continuous dyad仅固定多个；即使再按全部boxes求和也只有polylog。
continuous r、actual p=s的删除完全同样。actual p=r graph已有的完整付款
保持旧范围；连续reference中的该等式集合为measure-zero。
没有将原discrete repair估计机械套到continuous积分。

## 8. 对493实际deviation的准确消费

定义μ_pr,s为原actual内prime measure并删除s原子，Δμ_s=μ_pr,s−μ0。
两条腿的共同kernel保留全部原q,s,u、产品窗、q-prefix与频率mask。
按测度的准确bilinear identity，
\[
 K_{\mathrm{pr}}=K_{0,0}+K_{\Delta,0}+K_{0,\Delta}+K_{\Delta,\Delta},
 \qquad K_{\mathrm{dev}}=K_{\Delta,0}+K_{0,\Delta}+K_{\Delta,\Delta}.
 \tag{13}
\]
195源已付K_(0,0)=O(L^(-3))；(9)、(10)、(12)付两个raw mixed项，
因此K_(Δ,0)=K_(pr,0)−K_(0,0)、K_(0,Δ)=K_(0,pr)−K_(0,0)均为O(L^C)。
严格得到
\[
 \boxed{K_{\mathrm{dev}}=K_{\Delta,\Delta}+O_{\phi,\chi,g}(L^C).}
 \tag{14}
\]
所有等式消费的是同一实际χ-carrier合同。旧nn、graph、chirp和physical桥的
已付误差继续按原完整范围保存，不转成逐tuple或任意canonical子集结论。
两条Δμ腿的真实signed预算仍未证明；(14)不是新whole／比例／无零边界。
本稿没有有限数值实验或新checker；mixed付款不使用[Rθ]或任何无零前件。
