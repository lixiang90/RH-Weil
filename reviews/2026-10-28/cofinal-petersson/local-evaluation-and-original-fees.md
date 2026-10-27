# 固定未平均Pet覆盖塔：显式局部evaluation及原du费用

2026-10-28；/root/pet_local独占原稿，执行[当前唯一准入](../../2026-10-27/raw-theta-mean/next-cofinal-petersson-local-norm-admission.md)。同G20261027／原0c4f；C047预算已耗，不预C048/585，不改STATE/cadence/Git。只核已经冻结的正Gram生成规则，不调level序列、weight、ray或范数归一化。出稿不代root消费；完整Weil高频及极限反测由独立稿/root消费。

## 1. 对象、automorphy与精确测度

固定N0=4D(B)≥4、κ=3/2，Γ_n=Γ(N0 n!)⊂Γ(N0)⊂SL₂(Z)。S_n为相同unitary半整数automorphy向Γ_n限制后的holomorphic cusp sector。所用scalar automorphy满足

\[
 f(\gamma z)=j(\gamma,z)f(z),\qquad
 |j(\gamma,z)|^2=|cz+d|^{2\kappa},
 \quad\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}.
 \tag{1}
\]

固定相容的metaplectic lift／multiplier，不把其phase设为平凡。因Im(γz)=Im(z)/|cz+d|²，|f(z)|²(Im z)^κ与positive hyperbolic measure dxdy/y²的乘积确为Γ_n不变量。全部费用使用准入中已经冻结的、第一变量线性的**原未平均**Petersson积

\[
 \langle f,g\rangle_n=\int_{\Gamma_n\backslash\mathfrak H}
 f(z)\overline{g(z)}y^{3/2}\frac{dx\,dy}{y^2}
 =\int_{\Gamma_n\backslash\mathfrak H}f\bar g\,y^{-1/2}dx\,dy.
 \tag{2}
\]

这里quotient是矩阵群Γ_n作用的通常上半平面quotient；不另除index／volume／2，不偷运算术stack的权。metaplectic central lift只承担(1)的相容性；若其作用令该scalar sector为零，取S_n={0}及空基，以下不等式自动成立，不另挑非零level。未使用算术Theta、7.4或height身份。

每个fixed n的有限维性、两个ray尖点的cuspidal强衰减及固定n全S_exp定义，沿旧[typed-source稿](../../2026-10-27/mellin-bergman-source/typed-source-and-original-fees.md)消费：可有fractional cusp exponents和非平凡phase，仍有各fixed基函数W_(nj)∈S_exp∩L²(dt)。其常数允许依n。本稿证明下面特定compact ray上的n统一价格，绝不假设全线level统一du费。

## 2. Torsion、中心与共同嵌入圆盘

先付quotient角色。若γ∈Γ(N)、N≥4，则γ=I+NA，A为整矩阵，detγ=1给tr A=−N det A，故

\[
          \operatorname{tr}\gamma=2-N^2\det A\equiv2\pmod {N^2}.
 \tag{3}
\]

有限order的整SL₂矩阵有整数trace∈{−2,−1,0,1,2}；(3)仅准trace2，而finiteorder矩阵可对角化，trace2必为I。因此Γ(N)无非平凡torsion。−I不在Γ(N)，故其到PSL₂(R)的投影也注入，不存在由同一中心造成的二重计数。若一个非I元素在H有固定点，其整trace为−1,0,1，或它是−I；均已排除，故作用无椭圆stabilizer。

为当前ray给出更直接的统一注入半径，不以整个非compact quotient的injectivity radius为正作假设。置

\[
 L=17/16,\qquad z=iv,\qquad e^{-L}\le v\le e^L.
\]

对非I的γ∈Γ(N0)，分两种情况。

* 若c≠0，则|c|≥N0≥4，
\[
 y(\gamma z)=\frac{v}{d^2+c^2v^2},\qquad
 \frac{v}{y(\gamma z)}\ge N_0^2v^2\ge16e^{-2L}>1.
\]
上半平面任意路径的hyperbolic长度≥两端log y之差的绝对值，故
\[
 d_{\mathfrak H}(z,\gamma z)\ge\log16-2L>0.
 \tag{4}
\]

* 若c=0，则ad=1，a,d为±1；γ≡I modN0且N0≥4只允许a=d=1。非I给b≠0、|b|≥N0≥4，故
\[
 d_{\mathfrak H}(iv,b+iv)
   =2\operatorname{arsinh}\frac{|b|}{2v}
   \ge2\operatorname{arsinh}(2e^{-L})>0.
 \tag{5}
\]

因此定义明确常数

\[
 \delta=\min\{\log16-17/8,\;2\operatorname{arsinh}(2e^{-17/16})\}>0,
 \qquad \varepsilon=1-e^{-\delta/4}\in(0,1).
 \tag{6}
\]

同一个δ对所有n、所有当前闭ray点以及所有非I γ∈Γ_n都给d_H(z,γz)≥δ。Euclidean圆盘

\[
          D_z=\{w:|w-z|<\varepsilon v\}
 \tag{7}
\]

包含于H；沿z到w直线段积分，d_H(z,w)≤−log(1−ε)=δ/4。因此D_z包含于hyperbolic δ/4盘。若D_z与γD_z相交，三角不等式会给d_H(z,γz)<δ/2，与(4)–(6)冲突。故D_z在每个Γ_n\H中均注入，其不同Γ_n平移互不交。这个半径同时适用于任意t∈[-L,L]，不随n减小；不需要ray的不同t点投影互异，也不要求不同t的圆盘彼此不交。

## 3. Holomorphic均值给unit球总evaluation费用

任意f∈S_n在H上的scalar表示holomorphic，故|f|²的Euclidean圆盘均值满足

\[
 \int_{D_z}|f(w)|^2dA(w)\ge\pi\varepsilon^2v^2|f(z)|^2.
 \tag{8}
\]

D_z内y(w)≤(1+ε)v，且κ−2=−1/2，所以原Pet权的准确方向为

\[
 y(w)^{-1/2}\ge((1+\varepsilon)v)^{-1/2}.
\]

用D_z在quotient中注入及(1)的density不变性，(2)/(8)给

\[
 \|f\|_n^2\ge\int_{D_z}|f(w)|^2 y(w)^{-1/2}dA(w)
 \ge\frac{\pi\varepsilon^2}{\sqrt{1+\varepsilon}}
                      v^{3/2}|f(iv)|^2.
\]

记

\[
 C_{\rm ev}=\frac{\sqrt{1+\varepsilon}}{\pi\varepsilon^2},\qquad
 e_{n,t}(f)=e^{3t/4}f(ie^t),
\]

便实际付清全部complex f、全部n及|t|≤L的

\[
       |e_{n,t}(f)|^2\le C_{\rm ev}\|f\|_n^2.
 \tag{9}
\]

这一步没有把半整数权当weight2；v^(3/2)恰与已经冻结的ray frame平方一致。也没有将Pet二维面积积分误作ray一维范数。

选原Pet正交标准基f_(n1),…,f_(nd_n)，W_(nj)(t)=e_(n,t)(f_(nj))。有限维Riesz／正交基展开直接给

\[
 D_n(t):=\sum_{j=1}^{d_n}|W_{nj}(t)|^2
      =\sup_{\|f\|_n=1}|e_{n,t}(f)|^2
      \le C_{\rm ev}.
 \tag{10}
\]

d_n=0时定义左端0，unit球sup亦按零空间的evaluation norm解释为0。(10)是先对任意unit f付款再取一次sup；不是逐基套(9)而乘d_n，故没有隐藏dimension／cover degree。于是原kernel方向

\[
 B_n(t,u)=\sum_j\overline{W_{nj}(t)}W_{nj}(u)
\]

还有|B_n(t,u)|≤sqrt(D_n(t)D_n(u))≤C_ev于该compact方窗，第一/第二腿的bar位置保持准入公式。

## 4. 全complex compact源的同一原du上界

令I*=(-L,L)。全部r∈L²(I*,dt)以零延拓解释；Cc∞(I*)是本次极限所需的子域。沿已冻结公式

\[
 A_n r=\sum_j\left(\int_{I_*}r(t)\overline{W_{nj}(t)}dt\right)f_{nj},
 \qquad G_n(r,s)=\langle A_n r,A_n s\rangle_n.
\]

这些是有限维Bochner／逐系数积分，不需任何新的noncompact source截断或Pan裁剪。将vector (bar W_(nj)(t))_j作积分，Minkowski及Cauchy–Schwarz给

\[
 \begin{aligned}
 G_n(r,r)^{1/2}
 &=\left\|\left(\int_{I_*}r(t)\overline{W_{nj}(t)}dt\right)_j\right\|_{\ell^2}
 \\&\le\int_{I_*}|r(t)|\sqrt{D_n(t)}dt
 \le\sqrt{C_{\rm ev}}\,\|r\|_{L^1(I_*)}
 \le\sqrt{2L C_{\rm ev}}\,\|r\|_{du}.
 \end{aligned}
\]

因此有明确的同模型、同物理source、同未平均Pet规范的统一价格

\[
 \boxed{\sup_{n\ge1}G_n(r,r)\le C_{I_*}\|r\|_{du}^2,
 \qquad C_{I_*}=\frac{17}{8}
                 \frac{\sqrt{1+\varepsilon}}{\pi\varepsilon^2}<\infty.}
 \tag{11}
\]

并有|G_n(r,s)|≤C_(I*)||r||du||s||du。physical r=e^(t/2)f_phys及du=dt均保原角色；(11)不是对另一个e^t dt或Pet源norm的改写。常数是充分upper，不报sharp／necessary lower，也不报全线、成长I或跨不同weight的统一费。

## 5. 本稿净值及消费边界

此门已支付实际Γ_n／center／halfweight相容性、共同compactray盘、原正Pet测度、unit球总evaluation和全部complex compact源的n统一du费。它不要求任何G_n逐层消noncompact405，因此不能把本稿写成旧fixed A(Pan)=S的重复证明。552全Γ高频对照与逐源n极限的量词另由独立稿/root核；不得先把n依赖的source选入极限。

上述证明只是整数矩阵的显式位移、holomorphic均值、有限维Riesz和Cauchy–Schwarz；建议按标准／最强旧直接合成0数学轮消费，不隐藏新的classic成长预算。没有新算术primitive、整过滤/截面乘法/mixedRR、fullsigned identity或growth/core/coupling/Ξ后果；最强whole leading4/5仍为负惯性UPPER。

若将Pet积除volume/index、给Gram另乘发散level权，unit球及(9)的费用会改变，(11)不能免费搬运。非局部／source适应正族、真实无界arithheight或额外实际数据也不在本冻结family范围。原literalR/K失域与整体Theta/7.4运输冻结保持。本稿无外部PDF／网页／原proof新读或下载，也未执行下一候选。
