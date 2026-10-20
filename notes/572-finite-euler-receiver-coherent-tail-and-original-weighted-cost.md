# 572. 有限Euler后的真实receiver：完整相干尾与原加权范数费用

2026-10-20，C035，同G20261014／0c4f≤538固定基线。
先执行cycle14规定的一次系数/原域来源门；完整finite-height尾出现可判净费后准入一轮。
三份独占证明、来源、fresh独审和root消费统一结算，不以文件或工具数计轮。

**新增结果：实际bar b_F有限Euler差分后的coherent系数给无condition的对角O(L^4)。
更关键的是，完整相干尾在明确θ>2e的同步高度区间内可以付清，得到实际|b_F(R)|²
加权receiver的原dy范数平方平均O(L^4)，没有m_F²归一化，未截真实inverse/returns。
这关闭571的一个模型高频费用缺口；actual Sonin运输、其余模型主项尾、危险核心与全源容量仍未付。**

## 1. 同一个物理对象、完整Γ与实际Euler权

在原H=L²(R,dy)、U_a f(y)=f(y−a)，先固定finite F，令

\[
 B_F=\prod_{p\in F}(I-p^{-1/2}U_{\log p}),\quad D_F=B_F^{-1},\quad
 b_F(R)=\prod_{p\in F}(1-p^{-1/2}e^{-iR\log p}).                    \tag{1}
\]

P_T=1_(0,T)、L_-=1_(-∞,0)、H_+=1_(T,∞)，w_(R,T)=e^(iRy)1_(0,T)/√(2π)，
v= L_-D_F*P_Tw、u=H_+D_FP_Tw。实际消费始终锁定

\[
 T_R=\Gamma(R)=\Re\psi(1/4+iR/2)-\log\pi=2\theta'(R)>0.            \tag{2}
\]

Γ不是裸log定义。模型G_T=P_T B*B P_T和双边界S_T按571不变；
δwin=〈w,(G_T^−1−S_T)w〉不同于actual Sonin ε_F，也不同于原Weil源r。
本文V=L²((0,∞),dt)、t=−y是receiver的原dy坐标，不是du/zeroextension Dlog源范数。

## 2. Euler后必须先按实际delay coherent合并

令N_F为F-smooth正整数，包括1，rad(F)=∏_(p∈F)p。完整D_F给

\[
 \overline{b_F(R)}v_{R,T}(-t)=\frac{e^{-iRt}}{\sqrt{2\pi}}
       \sum_{n\in N_F}a_{n,T}(t)e^{iR\log n},\quad t>0,            \tag{3}
\]
\[
 \boxed{a_{n,T}(t)=n^{-1/2}
   \sum_{\substack{d\mid\operatorname{rad}(F)\\d\mid n}}\mu(d)
          1_{\{t<\log(n/d)<t+T\}}.}                            \tag{4}
\]

μ(d)d^−1/2与(n/d)^−1/2已合为n^−1/2，不能再多添d权。
每个同n的全部divisor相加后才平方，不沿(d,m)自由label分别平方。a_1=0。
对fixedfiniteF，Σ||a_n,T||_V≤√T Σ2^ω(n)n^−1/2<∞，故原V中绝对一致收敛，重排合法。

若n>1，y=logn、h=lograd(n)，完整Euler差分给两边界协同支撑

\[
 \operatorname{supp}a_{n,T}\subset
 ([y-h-T,y-T]\cup[y-h,y])\cap[0,\infty).                       \tag{5}
\]

当窗口含全部divisor delays，Σμ=0；两段可重叠，支撑窄本身不付coherent尾。
同一原norm有

\[
 |b_F(R)|^2\|v_{R,T}\|^2=\frac1{2\pi}
        \left\|\sum_n a_{n,T}e^{iR\log n}\right\|_V^2.           \tag{6}
\]

外面的t调制是酉的，只在该norm等式中消去，未把R从系数/phase中抹掉。

## 3. 无m/M费用的完整对角与真实原域负测

设D_F(T)=Σ||a_n,T||²。按S=supp(n)分组，Σ_(supp(n)=S)n^−1=∏_(p∈S)(p−1)^−1。
整线有限差分∏_(p∈S)(I−τ_logp)1_(0,T)先做最小prime p的差分，norm²恰2min(T,logp)，
其余每次最多乘4；限制t>0只降低norm。因此严格有

\[
 D_F(T)\le2\sum_{p\in F}\frac{\min(T,\log p)}{p-1}
     \prod_{\substack{q\in F\\q>p}}\left(1+\frac4{q-1}\right).    \tag{7}
\]

对F⊂{p<X}，Mertens product比值给乘积≤C(logX/logp)^4；
Σ_p[(p−1)(logp)^3]^−1有限，故

\[
 \boxed{\sup_{T>0}D_F(T)\le C(\log X)^4,\qquad
 F_L=\{p<e^{2L}\}:\ D_{F_L}(T)=O(L^4).}                       \tag{8}
\]

这是完整无限n的实际b权对角，非粗M²乘旧diagonal；暂不支付有限高度offdiagonal。
单prime n=p^k、k充分大时

\[
 n\|a_{n,T}\|_V^2=2\min(T,\log p)>0,
 \qquad\sum_{n\in N_F}n\|a_{n,T}\|_V^2=\infty.                 \tag{9}
\]

所以直接用ordinary gap≥1/(2n)的无限MV充分域仍不合法。
这只排粗充分域：singleprime真实gap=logp可合法用无限Cor2。
一般fixedF的BMS/Matveev多log下界也给δ_logn≥c_F(1+logn)^−M_F，
从而Σδ_logn^−1||a_n,T||²有限；已知深定理及其费用均归原来源。
现有该显式constant随|F_L|剧增，不证本轮同步区间小费，也不是actualerror下界。
本轮下面另付cofinal尾，不依靠该巨大的fixedF Diophantine常数。

## 4. 有限高度：截断位置在Euler后，不是D之前

定义Z_(j,F)(s)=Σ_(n∈N_F)j^ω(n)n^−s=∏_(p∈F)(1+(j−1)p^−s)/(1−p^−s)。
对每个系数，Minkowski给

\[
 \|a_{n,T}\|_V\le n^{-1/2}2^{\omega(n)}\sqrt{\min(T,\log n)}.     \tag{10}
\]

先固定T=T0，仅为估计将(3)的**Euler后coherent频率**截到logn≤A。
有限Hilbert-valued MV、ordinary integer log-gap和(8)给任意R0,H0>0

\[
 \operatorname{av}_{[R_0,R_0+H_0]}
 \left\|\sum_{\log n\le A}a_{n,T_0}e^{iR\log n}\right\|_V^2
 \le C L^4+\frac{C A}{H_0}e^{A/2}Z_{4,F_L}(1/2).                 \tag{11}
\]

确切MV余费是Σn||a_n||²/H0≤AΣ_(logn≤A)4^ω(n)/H0，再用finite Rankin界。
它不是O(diagonal/H0)，也不是不合法的无限MV套用。
若先截D到A再乘bar b，频率会扩到A+lograd(F)，不能套(11)的同一截断尾。
本文先fixedfiniteF绝对重排，再使用已证uniform费用到cofinal F_L。

## 5. 完整相干尾在原dy范数内付清

对每个R，Euler后全尾均有

\[
 \left\|\sum_{\log n>A}a_{n,T_0}e^{iR\log n}\right\|_V
 \le\sqrt{T_0}\,S_{2,L}(A),\quad
 S_{2,L}(A)=\sum_{\log n>A}2^{\omega(n)}n^{-1/2}.                 \tag{12}
\]

这是实际coherent尾的充分upper，不是actual tail lower。对0<α<1/2，
S2(A)≤e^−αA Z_(2,F_L)(1/2−α)。取fixed k>0、α=k/(2L)，PNT/Abel在s∈[1/4,3/4]
的统一范围给Σ_(p<X)p^−s=(1+o1)X^(1−s)/((1−s)logX)。
证明先用π(t)的ALL-t相对误差包络，fixedhead在该紧s范围一致可忽略，再Abel；
不能将fixedα结果直接搬到α(L)。于是

\[
 \log Z_{2,F_L}(1/2-k/(2L))=(2e^k+o(1))e^L/L,
 \qquad\log Z_{4,F_L}(1/2)=(4+o(1))e^L/L.                     \tag{13}
\]

前式log[(1+q)/(1−q)]的三次及以上项，在L充分大使3s>1后共同O1；
后式二次及以上至多O(L)，均低于e^L/L。所有o1在fixed k下使用。
取A=c e^L、c>4e、k=log(c/4)>1，则

\[
 S_{2,L}(c e^L)\le
 \exp\{-[d(c)+o(1)]e^L/L\},\quad
 d(c)=\frac c2\left(\log\frac c4-1\right)>0.                    \tag{14}
\]

T0~θe^L时完整未归一尾的平方费用≤T0 exp{−[2d(c)+o1]e^L/L}=o1。
每个log n>A的项都已加回，没有第二个未支付的无限tail，也没有m^−2隐藏归一。

## 6. 严格锁定T=完整Γ(R)的同步成长结论

固定θ>2e，选β∈(0,1)、c满足4e<c<2βθ，令

\[
 R_0=\exp(\theta e^L),\quad H_0=R_0^\beta,\quad
 R\in I_L=[R_0,R_0+H_0],\quad T_R=\Gamma(R),\quad T_0=\Gamma(R_0).
                                                                    \tag{15}
\]

(11)的finite-height余费≤C A exp{−(βθ−c/2)e^L+(4+o1)e^L/L}=o1，
与(14)全尾合并，固定T0的实际b权原dy平均≤Cθ L^4+o1。
最后支付移动端点：Γ′(R)=1/R+O(R^−3)，Δ_T=sup|T_R−T0|≤C H0/R0，
hard endpoint原carrier norm差平方恰|T_R−T0|/(2π)。因此

\[
 |b_F(R)|^2\|v_{R,T_R}-v_{R,T_0}\|^2
 \le (M_F/m_F)^2\Delta_T/(2\pi)=o(1),                          \tag{16}
\]

因为log(M²/m²)=(4+o1)e^L/L远低于(1−β)θe^L。完整Γ未被log近似替代定义。
所有实际逆尾和端点均付后得到本轮主结论

\[
 \boxed{\operatorname{av}_{I_L}|b_{F_L}(R)|^2
          \|L_-D_{F_L}^*P_{T_R}w_{R,T_R}\|_{dy}^2
       \le C_\theta L^4+o(1).}                              \tag{17}
\]
\[
 \operatorname{av}_{I_L}
  \frac{|b_{F_L}(R)|^2\|v_{R,T_R}\|^2}{\|w_{R,T_R}\|^2}
       =O_\theta(L^4e^{-L})\longrightarrow0.                    \tag{18}
\]

这是actual |b|²权的原物理norm，未改Hilbert范数，亦非571的m²归一结论。
免费除|b|²仍可能重新引入m^−2；未加权v或du/Dlog源的小费没有由此证明。
height平均不等逐R/ALL高度，也不控制receiver方向上的另一个算子放大率。
θ>2e只是这组l1-tail/MV充分certificate的范围，不是必要阈值或方法类不可能性。

## 7. 两个clean receiver的相位必须协同运输

保571实际全J逆：K=L_-B_FD_F*H_+、J=[[I,K],[K*,I]]，
δwin=||v||²+||u||²−〈(v,u),J^−1(v,u)〉≤min(||v||²,||u||²)。
若左取V=bar b v而右取U=b u，实系数反射R_T给U=e^(iRT)R_TV。
令η=bar b/b，C_b=diag(I,ηI)，则共同scalar bar b(v,u)=C_b(V,U)，所以精确有

\[
 |b|^2\delta_{\rm win}=
 \|V\|^2+\|U\|^2-\langle(V,U),J_b^{-1}(V,U)\rangle,
 \quad J_b=C_b^*JC_b=
 \begin{pmatrix}I&\eta K\\\bar\eta K^*&I\end{pmatrix}.          \tag{19}
\]

不能独立clean两边后仍沿用原K读cross；相位不改谱gap，但改cross配对。
J_b^−1的全部returns、完整G_T逆及两边界没有被截断。由一侧upper直接得到

\[
 \operatorname{av}_{I_L}|b_F(R)|^2(\delta_{\rm win}(R))_+
       =O_\theta(L^4),\qquad
 \operatorname{av}_{I_L}\frac{|b_F|^2(\delta_{\rm win})_+}{\|w_R\|^2}\to0.
                                                                    \tag{20}
\]

未支付负部、absoluteδ或全源有利符号。正向upper免坏gap分母，不等于所有inverse费用都免gap。

## 8. 成长尺度、危险core及完整Weil预算

θ>2e属于旧555 β_L~e^L、Γ~θe^L已经有利的高频范围，未覆盖θ≤1危险core。
本轮实际关闭的是模型actualb weightedreceiver完整尾/原费用门，
不是actual Sonin G_F/k_R的cofinal运输，也不是整个S_T的bulk/两单边界主项成长trace尾。
这些piece没有因估计G_T^−1−S_T就一并付清。旧word/clipping certificate缺口仍在，
它是充分证书不能用，不能升级成actual误差必要lower。

完整源身份保持560原式

\[
 2\pi\rho_F(s)=\Gamma(s)-2\sum_{p\in F,k\ge1}
  (\log p)p^{-k/2}\cos(ks\log p)+\epsilon_F(s),                  \tag{21}
\]
\[
 Q_W(r)=t_F(r)-\langle r,K_{F,I}r\rangle
   +2|\langle r,\cosh(u/2)\rangle|^2
   -2|\langle r,\sinh(u/2)\rangle|^2.                          \tag{22}
\]

μ(d)来自有限Euler numerator的coherent差分，不代−ζ′/ζ的完整素数幂。
Γ/contact、所有properpowers和双pole未删、未设零。本轮没有具体r的额外矩消失条件。
δwin不等ε_F；原receiver dy、carrier w、Sonin k_R与source du/Dlog保各自角色。

独立性来自已知PNT/Mertens/MV与实际系数/全尾原norm证明，不预设未知零点位置。
这是一个新的模型费用输入；独立global RR/effectivity容量仍须同源sections/kernel、
全Γ/pp/pole/mixed身份、原域误差、低频/core/coupling及全源覆盖，不能由(17)自动输出。
若直接要求全部完整Weil Gram PSD仍是等价改写；独立证明这样的Gram正性才是新正性输入。
strongest-old542+555→557 whole leading4/5、core/通常Ξ与Goal完成门未改。

## 9. 一般g适用前件和停止

finiteEuler系数/两边界phase运输可用于真实有界可逆因果卷积及其因果逆；
一般g的exact collisions必须先按实际值合并。ordinary unique factorization、Mertens product、
local log-spacing、Z_j的Euler算式和PNT的moving-exponent增长分别是额外输入。
连续g需要自身Fourier/Plancherel或renewal tail设施，不继承离散label对角和MV间距。
将这些可独立检验的分析条件付清，只推出本篇模型fee，并不等于Weil正型或一般RH。

C035一轮后停止c/β/θ阈值、L次幂或singleprime参数优化；付费nonfinitecompact、Γ-relative、
source-adapted、不同全逆组织与独立几何容量保留。下一须新actual source/transport输入或
真实globalmap＋独立RR预算；不能把本模型upper重复命名为容量继续续约。

原证明：[系数/原域/对角](../reviews/2026-10-20/euler-receiver/coefficients-domain-and-diagonal.md)、
[完整尾/有限高度](../reviews/2026-10-20/euler-receiver/weighted-tail-and-height-cost.md)、
[独立控制/协同/容量](../reviews/2026-10-20/euler-receiver/independent-control-and-capacity.md)。
已知MV和BMS原件的本轮/历史阅读范围另存来源记录；不声称重证外部深定理。
最终root消费以fresh终审和前件收据为准。
