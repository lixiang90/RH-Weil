# 独立Rgeom的单x Green current：对数奇点、delta与范围

2026-10-27；/root/ng_delta独占稿。执行STATE唯一[负平面／单x规范门](../classical-theta-analytic/next-negative-plane-green-normalization-admission.md)，恢复D20261027O及literal冻结。这里只核明确不同的Rgeom版本，不能把下述结论写回原literal R，也不移植作者Prop5.1／Th7.4作为证明。出稿不代root消费；不改STATE、cadence或Git，不预C048/585。

## 1. 对象与原ddc／体积规范

固定实tracezero矩阵

\[
 x=\begin{pmatrix}a&b\\c&-a\end{pmatrix},\qquad
 q=Q(x)=-a^2-bc\ne0,
 \qquad z=s+iy\in D=\mathbf C\setminus\mathbf R.
\]

B(x,y)=tr(xy^iota)按复双线性延拓，w(z)=[[z,−z²],[1,−z]]。当前项目独立定义

\[
 R=R_g(x,z)=-B(\operatorname{pr}_{z,-}x,
                  \operatorname{pr}_{z,-}x)
 =\frac{|p_x(z)|^2}{2y^2},
 \qquad p_x(z)=cz^2-2az-b.
 \tag{1}
\]

它是2R_print，而不是将旧literal归一化改名。μ和ddc沿原约定：

\[
 \mu=\frac1{2\pi}\frac{i}{2}
       \frac{dz\wedge d\bar z}{y^2}
     =\frac{ds\wedge dy}{2\pi y^2},
 \qquad dd^c=-\frac1{2\pi i}\partial\bar\partial.
\]

因此对光滑f直接用dz∧dbarz=−2i ds∧dy得到

\[
 dd^cf=\frac{\Delta_E f}{4\pi}ds\wedge dy
       =\frac12\Delta_h f\,\mu,
 \qquad \Delta_h=y^2(\partial_s^2+\partial_y^2).
 \tag{2}
\]

这是两半平面各自的复定向；y²使μ在两个组件都为正。没有把lower half的Dirac另加负号。所有current测试函数compact支撑于D，不引入实轴或无穷远边界项。

本稿复用已库56页作者PDF的原μ/ddc约定，实际目视PDF22页首并核原PDF raw SHA256为47ff2ff6f5151081dd029a1df680377b88d58fc09d6629f3a2b2c3b78bab0f54；原式/版本范围承上轮记录。没有下载新文献或核原外部证明。

## 2. Q>0的两点各simple，局部余项确实光滑

若q>0，则c不能为0，因为c=0会给q=−a²≤0。p_x的判别式为−4q，因此它的两个根是

\[
 z_\pm=\frac{a\pm i\sqrt q}{c},\qquad
 p'_x(z_\pm)=\pm2i\sqrt q\ne0.
\]

由于c为非零实数，两个根分居上下半平面。若c<0只是交换哪一个带“+”标签；没有改变根的重数。于是Dx={z_+,z_-}作为D中的零点集，各点的复解析重数为1。

固定其中一个z0，令z1为另一根。由(1)，在z0的小复邻域

\[
 R(z)=|z-z_0|^2 A(z),\qquad
 A(z)=\frac{|c(z-z_1)|^2}{2y^2}>0.
 \tag{3}
\]

A光滑正，且A(z0)=|p'_x(z0)|²/(2(Im z0)²)=2q/(Im z0)²。邻域闭包可取在同一半平面内，因此没有y=0奇性。

对于t>0，β1(t)=∫_1^∞e^(−tu)du/u；在0附近有

\[
 \beta_1(t)=-\gamma-\log t+E(t),\qquad
 E(t)=\sum_{k\ge1}\frac{(-1)^{k+1}t^k}{k\,k!}.
 \tag{4}
\]

E是解析函数，E(0)=0。这可由β1'(t)=−e^(−t)/t及其Taylor级数逐项积分得到；不需把“log主项”当作仅形式渐近。代入(3)给

\[
 \xi_g(x,z)=\beta_1(2\pi R(z))
 =-\log|z-z_0|^2+H(z),
 \quad H=-\gamma-\log(2\pi A)+E(2\pi R).
 \tag{5}
\]

H在z0处为C∞实函数，所以ξ局部可积，且除了一个log奇点外无隐藏current项。

## 3. delta系数由平面分布直接付清

在复定向平面，\(\Delta_E\log|z-z_0|^2=4\pi\delta_{z_0}\)。可由删去半径ε圆盘后的Green恒等式直接得到：小圆外法向通量为4π；光滑测试函数的非常数部分在ε→0时消失。结合(2)/(5)，

\[
 dd^c[\xi_g]=-\delta_{z_0}+dd^cH
 \quad\text{于z0邻域}.
 \tag{6}
\]

故每个Dx点的delta质量恰为−1。全D的修正项为

\[
 \delta_{D_x}=\delta_{z_+}+\delta_{z_-},
\]

不是每点2、每点1/2或上下相消。这里的质量是在未取商的D上，未包含任何arithmetic cycle次数、stabilizer／stack权或height的1/2；这些不能从局部delta读数中取得。

## 4. Q<0时D内无奇点

若q<0且c≠0，则p_x的判别式−4q为正实数，根都在实轴。若c=0，则q=−a²<0使a≠0，p_x为有唯一实根的一次式。两种情形都使p_x(z)在D内非零，因此R>0、ξ_g在D上C∞、Dx为空；无delta项。q=0及x=0不属于本单x门，不凭本稿为theta的零项或非零isotropic输入补定义。

## 5. 离Dx公式与current的闭合

为对齐另一独占微分稿，本稿另以(1)直接核如下两恒等式，而非引用原作者的Green命题：

\[
 |\nabla_hR|^2=4R(R+2q),\qquad
 \Delta_hR=6R+8q.
 \tag{7}
\]

简便代数核法是置A0=cs²−2as−b、t0=cs−a、U=A0/y、V=cy。于是cA0−t0²=q、R=(U−V)²/2+2t0²、R+2q=(U+V)²/2，且R_s=2t0(U+V)/y、R_y=(V²−U²)/y。平方及二阶微分给(7)，对所有q正负同时成立。

在R>0，F(R)=β1(2πR)满足

\[
 F'(R)=-\frac{e^{-2\pi R}}R,\quad
 F''(R)=e^{-2\pi R}
           \left(\frac{2\pi}R+\frac1{R^2}\right).
\]

(7)和链式法则给

\[
 \Delta_hF=2[4\pi(R+2q)-1]e^{-2\pi R}.
\]

结合(2)得到离Dx的光滑方程。其右侧在Dx也光滑；(5)/(6)已经完整核出左侧的唯一分布奇项。因此对每个固定x、q≠0，在整个D上有独立修补版本的current恒等式

\[
 \boxed{dd^c[\xi_g(x,\cdot)]+\delta_{D_x}
 =[4\pi(R_g(x,\cdot)+2Q(x))-1]
      e^{-2\pi R_g(x,\cdot)}\,\mu.}
 \tag{8}
\]

q<0时该式就是全D的光滑方程；q>0时两点delta各按(6)相消。局部相容性成立不恢复旧literal K的Schwartz性。

## 6. √v x缩放：delta不随v乘权

对任意固定v>0，p_(√v x)=√v p_x、Q(√v x)=v q、R_g(√v x,z)=vR_g(x,z)。Dx及其simple重数不变。在z0邻域，

\[
 \beta_1(2\pi vR)
 =-\log|z-z_0|^2
  -\gamma-\log(2\pi vA)+E(2\pi vR).
\]

相对(5)只有光滑项改变，特别−log v是空间常数。因此current系数仍每点−1。完整scaled式是

\[
 dd^c[\beta_1(2\pi vR_g(x,\cdot))]+\delta_{D_x}
 =[4\pi v(R_g(x,\cdot)+2Q(x))-1]
       e^{-2\pi vR_g(x,\cdot)}\,\mu.
 \tag{9}
\]

δ_Dx前没有v、1/v或v^(3/4)，右侧也未加theta的e^(−2πvQ)因子。式(9)对每个v>0精确成立，但本稿未估v→0/∞的全格点／空间uniform尾。

## 7. 已付范围、未付运输与净值

已付的是项目独立Rgeom版本、任意固定实x且Q(x)≠0、D的两个组件上的局部Green current及全部系数/缩放；标准微分、β1积分与平面log分布直接证明，没有借未知ζ零点或原作者Prop5.1。普通norm／源成长量词不是本结果的对象；无数值、crop、格点求和或时间积分误差。

尚未得到固定x在Γ\D上的下降、stabilizer／orbifold质量、全格点K_g、Poisson零模、P0/Phi、physical全S_exp／du-Dlog费用、非零性、405/Pan消去、537同源非根、自然height／Th7.4比较、整过滤/截面/mixedRR或完整经典Γ/contact/properpowers/双pole身份。不能把(8)称为新的完整Green源或primitive容量；原literal下游冻结保持。

这只是来源规范的标准局部修补，建议0数学轮，无新classic whole或growth/core/coupling/Ξ后果；wholeleading4/5仍是已知负惯性UPPER。若root拟继续，须另给明确K_g实际格点公式和可判的零模／空间原费用首门，先扣553强旧；本稿未执行这些步骤，也不产生新数学合同或paper链授权。
