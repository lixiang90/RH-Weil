# 571. 真实receiver上的双边界signed比较与成长费用

2026-10-20，C034，同G20261014／0c4f≤538固定基线。
执行570保存且用户本轮明确要求的真实receiver门，不重跑窄源η或全空间norm下界。
三份原证明、primary核读和独立终审统一一完整研究迭代，原稿出稿不代root消费。

**结论：同一真实receiver pair给出完整双边界Gram差；正向upper可避开坏gap分母，
但没有自动有利符号。固定单prime在严格T=Γ(R)下有趋∞的两号载波序列。
cofinal时另得m²归一的真实receiver同步高度平均趋零；还原原norm、乘实际|b|²、
运输到Sonin k_R及全部Weil源的费用仍未付，故没有独立容量或whole4/5改善。**

## 1. 原物理对象与三个不同角色

在H=L²(R,dy)、U_a f(y)=f(y−a)，先固定任意有限F。定义

\[
 B=\prod_{p\in F}(1-q_pU_{a_p}),\quad q_p=p^{-1/2},\ a_p=\log p,
 \quad D=B^{-1},\quad W=B^*B,\quad Z=W^{-1}=DD^*=D^*D.             \tag{1}
\]

m=∏(1−q_p)>0，M=∏(1+q_p)，m²I≤W≤M²I。设P=1_(0,T)、L=1_(-∞,0)、H_+=1_(T,∞)，
G_T=PWP作用在PH；双边界模型始终是

\[
 S_T=P(Z-DLD^*-D^*H_+D)P,\qquad
 w_{R,T}=\frac{e^{iRy}1_{(0,T)}}{\sqrt{2\pi}},\quad
 T=\Gamma(R)=\Re\psi(1/4+iR/2)-\log\pi>0.                         \tag{2}
\]

Γ是完整actual2θ′，不把log渐近当定义。一般operator身份可对任意T成立，实际carrier消费锁定(2)。
模型G_T不同于Sonin空间M上的G_F；w_R、裸求值k_R、log-Weil源r也是三个不同角色。
本篇模型差记δ_F(R)=〈w,(G_T^−1−S_T)w〉，不记作570的actual E_F，也不直接改名ε_F。

## 2. 完整逆恰落在真实receiver pair上

对任意w∈PH，令v=LD*Pw、u=H_+DPw。半线因子D_L=LDL、D_H=H_+DH_+可逆。
因果性及D normal给

\[
 LZL=D_LD_L^*,\quad H_+ZH_+=D_H^*D_H,\qquad
 K=D_L^{-1}(LZH_+)D_H^{-1}=LBD^*H_+=LD^*BH_+.                    \tag{3}
\]

BD*=B(B*)^−1为整线酉all-pass，K是它的真实远端block。令A=D_L⊕D_H*、Q=L+H_+，则

\[
 J=\begin{pmatrix}I&K\\K^*&I\end{pmatrix},\quad
 QZQ=AJA^*,\quad QZPw=A\binom vu,\quad
 J\ge(m/M)^2I,\quad\kappa=\|K\|\le1-(m/M)^2<1.                 \tag{4}
\]

最后两个身份把外域Gram接到同一个真实receiver，不能用任意低输入替代v。
Schur补给G_T^−1=PZP−PZQ(QZQ)^−1QZP，所以精确有

\[
 \boxed{\delta(w)=\|v\|^2+\|u\|^2-
       \left\langle\binom vu,J^{-1}\binom vu\right\rangle.}       \tag{5}
\]

它也等于560的−〈w,G_T^−1(G_TS_T−I)w〉；原双残差两项均在，没有换成近似inverse。
正平方根归一的外域C与本K只差半线polar unitary，receiver也作同一酉运输；
两种归一具有同一个二次型和κ，不能把其坐标字面认作相同。

展开完整block inverse得到

\[
\begin{split}
 \delta(w)={}&2\Re\langle v,K(I-K^*K)^{-1}u\rangle\\
 &-\langle v,KK^*(I-KK^*)^{-1}v\rangle
  -\langle u,K^*K(I-K^*K)^{-1}u\rangle.                           \tag{6}
\end{split}
\]

完整returns仍在两个inverse中；cross减去两侧非负self-return，不自动取号。
完成平方及谱界进一步给

\[
 \delta(w)=\|u\|^2-\|(I-K^*K)^{-1/2}(u-K^*v)\|^2,
 \quad\delta(w)\le\min(\|u\|^2,\|v\|^2),                       \tag{7}
\]
\[
 -\frac\kappa{1-\kappa}\mathcal B\le\delta(w)
 \le\frac\kappa{1+\kappa}\mathcal B,\qquad
 \mathcal B=\|u\|^2+\|v\|^2.                                   \tag{8}
\]

正向upper没有坏gap分母；receiver自身的原norm和实际b权尚须支付。
若只取首个cross，则余下全部returns费用≤κ²/(1−κ)·B，不把它们删除。
J正仅来自一般正W，不能由被减Gram正性宣称δ正或Weil正。

## 3. 真实carrier的相位、原norm与fixed-F费用

实系数使反射共轭R_T f(y)=overline(f(T−y))满足

\[
 u=e^{iRT}R_Tv,\qquad\|u\|=\|v\|,\qquad
 v(-t)=\frac{e^{-iRt}}{\sqrt{2\pi}}
       \sum_{t<x<t+T}c_xe^{iRx},\quad
 x=\log n,\ c_x=n^{-1/2}.                                      \tag{9}
\]

n遍历F-smooth，包括1；phase不能通过酉共轭消失，只会进入D的全部系数。
精确原norm是带实际相位的双和

\[
 \|v\|^2=\frac1{2\pi}\sum_{x,z}c_xc_ze^{iR(x-z)}\ell_T(x,z),
 \quad\ell_T=\min\{\min(x,z),(T-|x-z|)_+\}.                     \tag{10}
\]

令D0=m^−1、J0=Σxc_x，绝对上界D0J0/(2π)支付换序；它不含粗carrier的T因子。
旧第一矩及(3)给κ≤min(1−m²/M²,Mτ_F(T))，τ_F(T)≤A_(F,γ)e^−γT。
所以每fixed F、0<γ<1/2，δ=O_(F,γ)(e^−γT)，代完整Γ为O_(F,γ)(R^−γ)。
这省旧粗upper的T，但由560旧exact/firstmoment直接合成，不计新的whole容量。
绝对常数、m/M/A/J不能在成长F时吞进O1，actual Sonin运输仍须另加。

## 4. 单prime精确反测：T=Γ(R)下两号确实存在

固定p，a=logp、q=p^−1/2，T=Na+τ、0≤τ<a。原dy空间酉分解为x∈[0,a)的ℓ²(Z) fibres。
x≥τ的window有N点、x<τ有N+1点。每个n点fibre上

\[
 (G_n)_{ij}=(1+q^2)\delta_{ij}-q\delta_{|i-j|,1},\quad
 (S_n)_{ij}=\frac{q^{|i-j|}-q^{i+j+2}-q^{2n-i-j}}{1-q^2},        \tag{11}
\]
\[
 (G_n^{-1})_{ij}=
 \frac{q^{|i-j|}-q^{i+j+2}-q^{2n-i-j}+q^{2n+2-|i-j|}}
 {(1-q^2)(1-q^{2n+2})}.                                        \tag{12}
\]

这是完整inverse的闭式，不是有限N近似。设u_i=q^(i+1)、v_i=q^(n−i)、c=q^(n+1)，则

\[
 \Delta_n=G_n^{-1}-S_n=
 \frac{c(uv^*+vu^*)-c^2(uu^*+vv^*)}{(1-q^2)(1-c^2)}.           \tag{13}
\]

n≥2每fibre恰有一正一负；整个连续直积分不能称有限秩2。
实际carrier相位θ=aR，不是任意eigenvector。令ζ=qe^(iθ)、C_n=(1−ζ^n)/(1−ζ)，
负fibre的真实receiver是v_(-ℓ)=e^(iRx)q^ℓC_n/√(2π)，ℓ≥1。故整个窗口严格有

\[
 |b_p(R)|^2\|v\|^2=\frac{q^2}{2\pi(1-q^2)}
 \{(a-\tau)|1-\zeta^N|^2+\tau|1-\zeta^{N+1}|^2\}.              \tag{14}
\]

每n点fibre上跨到右边界的原norm比是q^(n+1)/(1−q²)；原receiver为几何尾，未用全H自由bump。
固定p时加权receiver能量趋a q²/[2π(1−q²)]，相对||w||²=T/(2π)为O1/T。

取R_N^0=Γ^−1(Na)=2πe^(Na)(1+O_p(e^−2Na))。在其右O_p(1/N)区间内，实际相位
Φ_N(R)=(N−1)aR+2arg(1−qe^(iaR))单调走过至少4π，可选cosΦ=±1的R_N±。
始终定义T_N±=完整Γ(R_N±)，于是τ_N±=O_p(q^(2N)/N)；长度误差O_p(q^(3N)/N)小于主项。
保全部inverse、returns及两边界，得到

\[
 \boxed{|b_p(R_N^\pm)|^2\delta_p(R_N^\pm)
   =\pm\frac{a q^{N+3}}{\pi(1-q^2)}+O_p(q^{2N+2}).}             \tag{15}
\]

这是严格actualcarrier的两号，量级R^−1/2；除原||w||²后为R^−1/2/logR。
只反测固定singleprime模型的统一号，不扩称joint{2,3}或actual Sonin ε的符号。
560的k_R/clipping费用可以比(15)更大，不能用模型符号越过运输误差。

## 5. 成长F_L下一个锁定Γ的真实受限像平均

F_L={p<e^(2L)}，m_L=∏(1−p^−1/2)。固定θ>1，选β∈(0,1)、ε>0使1+ε/2<βθ<θ。
置R0=exp(θe^L)、H0=R0^β、I_L=[R0,R0+H0]，始终取T_R=Γ(R)。严格有

\[
 \frac1{H_0}\int_{I_L}
 \frac{m_L^2\|L D_{F_L}^*H_{T_R}w_R\|^2}{\|w_R\|^2}\,dR
 =O(L^2e^{-L})+O(e^{-ce^L})\longrightarrow0,\quad c>0.           \tag{16}
\]

均值不是逐R或ALL源结论。由(7)同样控制m²(δ_F)_+/||w||²的该平均，不能由此控制负部或实际b权。
当1<θ<2时旧m_L||H_+D_FL_-||→1仍成立，二者共存；旧full-H lower不能据此赋给当前carrier的费用。
但(16)不证明normalized receiver方向上的跨窗norm比小，不作这个额外断言。
还须扣555的强旧范围：β_L/e^L→1，而这里Γ(R)~θe^L、θ>1，处于旧标量比较的有利高频层，
并未覆盖Γ约≤e^L的危险core。这个大小比较不把Fourier频带截断当原compact源。

证明保每笔原norm费：T0=Γ(R0)，先只为估计截D_A到logn≤A=(2+ε)e^L。
系数f_n(t)=n^−1/2·1_(t<logn<t+T0)在L²((0,∞),dt)的norm²=n^−1min(T0,logn)。
已知Montgomery–Vaughan Cor2/3的有限Hilbert-valued形式及δ_n≥1/(2n)给

\[
 \operatorname{av}_{I_L}\|v_A\|^2
 \le C\{L^2+A\Psi(e^A,e^{2L})/H_0\},\qquad
 \Psi(e^A,e^{2L})\le e^{A/2}/m_L.                               \tag{17}
\]

对固定t应用再积分亦得同式；高度起点R0只改系数unitphase，不改norm。
Σn^−1logn≤∏(1−1/p)^−1Σlogp/(p−1)=O(L²)；Rankin计数无未知零点输入。
乘m²/T0，有限和error≤Cexp[−(βθ−1−ε/2)e^L]。
全部inverse尾通过560已付的概率μ_L(logn)=m_Ln^−1/2加回：

\[
 \mu_L(X>A)\le C_\epsilon Le^{-L},\quad
 \frac{m_L^2\|v-v_A\|^2}{\|w\|^2}\le\mu_L(X>A)^2.             \tag{18}
\]

最后完整Γ′=1/R+O(R^−3)，Δ_T=sup|T_R−T0|≤CH0/R0；hard endpoint原norm差恰Δ_T/(2π)，
经D*后至多m^−2Δ_T/(2π)。归一后O(H0/(R0T0))，支付真正T_R，非自由T/R平均。
(17)–(18)只是证明分解，最终receiver仍用完整D。

### 5.1 原范数与实际b权为何仍未付

还原原norm的合法upper保留

\[
 \operatorname{av}\|v\|^2\le C\{L^2+A e^{A/2}/(mH_0)
       +T_0m^{-2}\mu_L(X>A)^2+m^{-2}\Delta_T\}.                  \tag{19}
\]

logm^−2=(2+o1)e^L/L，现有tail证书不足以把(19)写成O(L²)。这是upper失效，非实际lower。
粗乘|b|²≤M²又产生M²/m²，其log=(4+o1)e^L/L；不能由(16)推出实际密度小费。
singleprime(14)的精确抵消不是multiplicative norm公式，multi-prime的ℓ_T耦合不可拆。
固定F的Bohr均值再令F成长也不支付(16)的同步量词；后者有实际但限定的新范围。

## 6. 完整Weil预算和真正未付输入

560同源身份始终保

\[
 2\pi\rho_F(s)=\Gamma(s)-2\sum_{p\in F,k\ge1}
       (\log p)p^{-k/2}\cos(ks\log p)+\epsilon_F(s),             \tag{20}
\]
\[
 Q_W(r)=t_{F_L}(r)-\langle r,K_{F_L,I}r\rangle
  +2|\langle r,\cosh(u/2)\rangle|^2
  -2|\langle r,\sinh(u/2)\rangle|^2.                            \tag{21}
\]

本篇不设置pp/pole为零，除非另给具体source精确条件。Γ/contact从未删去。
原source域为du L²/zeroextension Dlog，载频R的合法源Dlog价约logR，不能用||w||²未经运输替代。
cofinal时560 word/clipping要求N=O(e^L)，谱尾却需N至少M²/m²量级；
这是旧充分certificate缺口，不是actual源误差必要下界。模型receiver均值不能修复这个运输。

独立容量仍缺：实际|b(R)|²与coherent smooth-tail的相关费用；同源Sonin完整逆/载波运输；
ALL complex源、低频/危险core、source coupling及合法全域极限。新一侧upper未闭合这些箭头。
直接要求完整mixed Gram PSD是Weil正性等价；另假设足够强的有利domination仍没有独立来源。
真实RR/evaluation容量必须从同一global section/kernel/局部消失结构独立给出，不能由正J代替。

## 7. 一般g分布与本轮净后果

(3)–(8)适用于真实normal、可逆、因果且逆仍因果的卷积B；实系数再给(9)反射。
有限positive delays/绝对逆质量即可给(9)–(10)，exact collisions必须先coherent合并。
这比ordinary整数类广，但一般对偶关系本身不提供bounded inverse及这些域条件。
(16)另用了ordinary log-spacing、cofinal概率浓缩、diagonal/count及完整Γ变窗；
一般g需分别证明替代前件。连续分布应改用其真实Fourier/Plancherel设施，不免费继承离散MV间距。

新增是实际receiver的完整signed组织、Γ锁定singleprime两号及同步成长的限定归一均值；
外部MV、560 firstmoment/probability和强旧结果归旧，表示/精细upper不冒称新独立算术输入。
局部模型比较更明确；宏观独立容量瓶颈、542+555→557 leading4/5/core/coupling/Ξ未改。
一轮后停止singleprime相位/N和m归一优化，不扩第三prime或继续未知domination标签。
下一仅可准入实际b权的coherent tail，并先验证新finiteEuler比较与原域；无净输入就停，
不得把Σ n||f_n||²=∞的完整smooth级数直接套无限MV。宏观复盘另存，不增加数学轮。

原证明：[实际pair/全逆](../reviews/2026-10-20/receiver-signed/exact-receiver-and-boundary-sign.md)、
[原norm/成长](../reviews/2026-10-20/receiver-signed/receiver-norm-and-growth.md)、
[精确fibre/Γ锁定反测](../reviews/2026-10-20/receiver-signed/independent-model-tests.md)。
MV来源为[原作者PDF](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)印刷74–75、82页；
root本轮核读并目视Cor2/3，Thm2局部gap常数3π/2、Cor2误差3π，未宣称重证全章。
最终消费以fresh独立终审和root前件收据为准。
