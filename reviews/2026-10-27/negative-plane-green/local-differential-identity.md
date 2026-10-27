# 独立负平面规范：单x Green的离除子微分恒等式

2026-10-27；/root/ng_off独占原稿。恢复Goal／STATE／D20261027O及唯一[单x规范门](../classical-theta-analytic/next-negative-plane-green-normalization-admission.md)。本稿只核明确不同的R_g版本；不修改原作者literal R，不解冻其K，不作完整theta／P0／Phi／Poisson／空间费用或新source候选，不改STATE/cadence/Git。出稿不代root最终消费。

## 1. 原对象、规范与直接坐标

固定实trace-zero空间V_R及B(x,y)=tr(x y^iota)、Q(x)=det x，B(x,x)=2Q(x)。D=C\R，z=s+iy，y≠0。沿上一门已定位的负平面B正交投影定义

\[
 R=R_g(x,z)=-B(x_-,x_-)
 =-\frac{2|B(x,w(z))|^2}{B(w(z),\overline{w(z)})}.
\]

它是独立项目规范，等于2R_print；这条定义不继承作者Prop5.1或Th7.4。本稿实际目视已库PDF21/22，仅核原μ、ddc和β1定义／约定，下面的微分结论直接推导。

写

\[
 x=\begin{pmatrix}a&b\\c&-a\end{pmatrix},\quad
 p_x(z)=cz^2-2az-b,\quad q=Q(x)=-a^2-bc.
\]

由w(z)=[[z,−z²],[1,−z]]直接有B(x,w(z))=p_x(z)、B(w(z),barw(z))=−4y²。因此

\[
 \boxed{R(x,z)=\frac{|p_x(z)|^2}{2y^2}.}                 \tag{1}
\]

保持原规范

\[
 \mu=\frac1{2\pi}\frac{i}{2}\frac{dz\wedge d\bar z}{y^2}
     =\frac{ds\wedge dy}{2\pi y^2},\qquad
 dd^c=-\frac1{2\pi i}\partial\bar\partial.
\]

对任何实或复smooth标量f，直接用dz∧dbarz=−2i ds∧dy及∂bar∂f=(f_ss+f_yy)dz∧dbarz/4，得

\[
 dd^c f=\frac{f_{ss}+f_{yy}}{4\pi}ds\wedge dy
       =\frac12\Delta_h f\,\mu,
 \quad \Delta_h=y^2(\partial_s^2+\partial_y^2).           \tag{2}
\]

这是在上下半平面各自的复定向下同一公式；μ没有由于y<0变成负形式。Δ_h采用其L²特征值非正的符号，未换成−Δ_h。

## 2. 两个关键微分恒等式：一般x、一般z直接核算

置

\[
 A=cs^2-2as-b,\quad t=cs-a,\quad U=A/y,\quad V=cy.
\]

有A_s=2t、t_s=c及

\[
 cA-t^2=q,\qquad
 R=\frac{A^2}{2y^2}-cA+\frac{c^2y^2}{2}+2t^2
  =\frac{(U-V)^2}{2}+2t^2,\qquad
 R+2q=\frac{(U+V)^2}{2}.                              \tag{3}
\]

特别是R≥0且R+2q≥0。由(3)求一阶导数：

\[
 R_s=2t(A/y^2+c)=\frac{2t(U+V)}y,\qquad
 R_y=-\frac{A^2}{y^3}+c^2y=\frac{V^2-U^2}{y}.
\]

因此

\[
 \begin{aligned}
 |\nabla_hR|^2
 &=y^2(R_s^2+R_y^2)\\
 &=(U+V)^2\bigl[4t^2+(U-V)^2\bigr]
 =\boxed{4R(R+2q)}.                                  \tag{4}
 \end{aligned}
\]

二阶导数同样直接为

\[
 R_{ss}=\frac{2cA+4t^2}{y^2}+2c^2,\qquad
 R_{yy}=\frac{3A^2}{y^4}+c^2.
\]

于是

\[
 \Delta_hR=\frac{3A^2}{y^2}+2cA+4t^2+3c^2y^2
           =\boxed{6R+8q},                           \tag{5}
\]

最后一步只用cA−t²=q。这不是仅在某个positive orbit或z=i的验证；它对全部实a,b,c及y≠0逐字成立，包含q<0。没有用数值样本或未知外部几何比较。

## 3. β1链式法则与离Dx的精确系数

令β1(u)=∫_1^∞e^(−uv)dv/v，u>0。把积分变量改成β1(u)=∫_u^∞e^(−w)dw/w即可直接得β1′(u)=−e^(−u)/u。对R>0设

\[
 F(R)=\beta_1(2\pi R),\quad
 F'(R)=-\frac{e^{-2\pi R}}R,\quad
 F''(R)=e^{-2\pi R}\left(\frac{2\pi}R+\frac1{R^2}\right).
\]

结合(4)/(5)，

\[
 \begin{aligned}
 \Delta_hF(R)
 &=F''(R)|\nabla_hR|^2+F'(R)\Delta_hR\\
 &=e^{-2\pi R}\bigl[8\pi(R+2q)-2\bigr]\\
 &=2[4\pi(R+2q)-1]e^{-2\pi R}.
 \end{aligned}                                       \tag{6}
\]

所以按原μ及ddc规范，离Dx精确有

\[
 \boxed{
 dd^c\beta_1(2\pi R_g(x,z))
 =[4\pi(R_g(x,z)+2Q(x))-1]e^{-2\pi R_g(x,z)}\mu.}      \tag{7}
\]

没有剩余factor2、half或符号可吸收入μ。标量rhs中的4π和常数−1由同一链式法则同时确定，不能只确认Gaussian的正定性就免费取得(7)。

## 4. Q正负与v缩放范围

本门假定q≠0。若q>0，必c≠0，p_x的两根为(a±i√q)/c，各有一个在上下半平面，且均为simple root。R的零集就是Dx。因此(7)在D\Dx成立；对数奇点和delta质量由独立ng_delta稿另核，本稿不单独把离除子等式升级为完整current结算。

若q<0，p_x的根均在实轴（包括退化为线性时的情形），D内没有零；也可由R+2q≥0推出R≥−2q>0。因此F(R)在整个D smooth，(7)本身已是D上普通smooth形式等式，delta项为空。不处理q=0的退化／x=0 theta常项，亦不把它与单x Green奇点合并。

对每个v>0，取x_v=√v x，则q_v=vq、R_v=vR、Dx_v=Dx。由于(4)/(5)在x的全部实系数成立，原样给

\[
 \Delta_hR_v=6R_v+8q_v,\quad
 |\nabla_hR_v|^2=4R_v(R_v+2q_v),
\]

从而在D\Dx（q<0时整个D）有

\[
 \boxed{
 dd^c\beta_1(2\pi vR_g(x,z))
 =[4\pi v(R_g(x,z)+2Q(x))-1]
       e^{-2\pi vR_g(x,z)}\mu.}                      \tag{8}
\]

这里v同时缩放R与Q；没有把q换成v²q或遗漏constant−1，也不改变原μ。∀fixed x,q≠0、∀v>0的精确恒等式不等于任何cofinal source/window/level的uniform norm估计。

## 5. 消费角色与净值

本稿付款是明确R_g版本的离除子局部规范：对象为一个固定x在D上的smooth形式／局部current候选；物理源r尚未进入，没有取得ALLcomplex S_exp的源map、du／Dlog／强源费、格点尾／空间范数、Pan／537运输或height身份。原literal K及其所有下游消费仍冻结，不能将(7)/(8)写回旧式而声称旧证明自动有效。

所有计算是直接实矩阵代数、微分及β1的基本链式法则，建议标准来源修补0数学轮。若delta稿亦闭合，只重新闭合该独立单x版本，不给完整K／Phi、算术整过滤／mixedRR、经典Γ/contact/properpowers/双pole或signedgrowth/core/coupling/Ξ。最强旧wholeleading4/5仍是负惯性UPPER；经典主瓶颈未改。本稿不选择下一动作或授予新数学合同。
