# 独立Rgeom单x Green规范：fresh逆审

2026-10-27；/root/ng_fresh独占稿。恢复Goal/STATE/latestD20261027O及唯一singlex准入，实际目视作者PDF4、21、22相关定义，独立复算下列恒等式。**最终有限PASS：两原稿已按实际最终版本完整核读，R_g的单x current、两组件delta及√v缩放闭合；完整theta/源费用和原literal消费仍冻结。** 不改STATE/cadence/Git，不预C048/585，不执行完整K/Phi/Poisson/原费用或下一候选。

## 1. 规范和离奇点的直接核算

保持D=C\R、Q(x)=det(x)、B(x,y)=tr(xy^ι)及B(x,x)=2Q(x)。当前独立版本是

\[
 R=R_g=-B(\operatorname{pr}_{z,-}x,\operatorname{pr}_{z,-}x)
       =-\frac{2|B(x,w)|^2}{B(w,\bar w)}
       =2R_{\rm print},
 \quad x\in V(\mathbb R),\ Q(x)\ne0.
\]

它不是把作者literal比值无声重解释为正确。源文μ和ddc逐字给

\[
 \mu=\frac1{2\pi}\frac{i\,dz\wedge d\bar z}{2y^2}
     =\frac{ds\,dy}{2\pi y^2},\qquad
 dd^c=-\frac1{2\pi i}\partial\bar\partial.
\]

因此在任一半平面，按复取向有

\[
 dd^c f=\frac1{4\pi}\Delta_E f\,ds\,dy
        =\frac12\Delta_h f\,\mu,
 \qquad\Delta_h=y^2(\partial_s^2+\partial_y^2).
\]

独立核矩阵表达：对x=[[a,b],[c,−a]]及z=s+iy，置p(z)=cz²−2az−b，则

\[
 R=\frac{|p(z)|^2}{2y^2},\qquad Q=-a^2-bc.
\]

在z=i写b=u+d、c=u−d、ρ=a²+u²，直接求导得

\[
 R=2\rho,\quad R_s=4ad,\quad R_y=-4ud,
 \quad\Delta_h R=4\rho+8d^2=6R+8Q,
 \quad |\nabla R|_h^2=16\rho d^2=4R(R+2Q).
\]

这些式子也可直接由一般(s,y)表达核得；实Möbius作用与conjugation保Q、R及hyperbolic算子，所以对两半平面全部z成立。这里的Q>0、Q<0并未通过改变模型处理。

由β1的积分定义，F_v(R)=β1(2πvR)满足

\[
 F_v'(R)=-e^{-2\pi vR}/R,\qquad
 F_v''(R)=e^{-2\pi vR}(2\pi v/R+1/R^2).
\]

链式法则给

\[
 \Delta_h F_v
 =2[4\pi v(R+2Q)-1]e^{-2\pi vR}.
\]

因此离Dx时恰有ddc ξ_v=φ_g⁰(√v x,z)μ，其中ξ_v=β1(2πvR)。2π、4π、ddc的1/2和Q的二次缩放均未吸入变量；这一步是项目直接微分核算，不借作者Prop5.1作为前提。

## 2. Q正负、log主项与两组件delta质量

若Q>0，则c≠0，p(z)判别式为−4Q<0，两根z_±=(a±i√Q)/c分居上下半平面，且p'(z_±)=±2i√Q≠0。在每根z0的邻域，p(z)=(z−z0)h(z)，h(z0)≠0，所以

\[
 R=|z-z_0|^2 A(z),\qquad
 A(z)=|h(z)|^2/(2y^2)>0
\]

光滑。β1(t)+log t在t=0有收敛的普通幂级数延拓，故

\[
 \xi_v(z)=-\log|z-z_0|^2+g_v(z),
 \qquad g_v\text{在}z_0\text{光滑}.
\]

不是只有一个未控O(log)误差。以小圆盘自身的外向单位法向为约定，∫_(∂Bε)∂_n log|z−z0|² ds=4π；因此Δ_E log|z−z0|²=4πδ_z0，按上述ddc得ddc log|z−z0|²=δ_z0，故ξ_v的点质量为−δ_z0。每半平面各一单位质量；整个D的δ_Dx为两点之和，不在某一个点人为乘2。v>0只在光滑项中增加−log v等，不改变质量。

Q<0时p的根均在实轴或无有限根；D内R>0，所以ξ_v光滑且Dx为空。此结论包括c=0的线性情形，不把实轴端点或无穷远补进D。所有current测试在D内compact support，不存在自动新增的边界delta。

结合离Dx身份和精确光滑余项，对每个固定实x、Q(x)≠0和每个v>0，可在D上得到独立版本的局部current式

\[
 dd^c\beta_1(2\pi vR_g(x,z))+\delta_{D_x}
 = [4\pi v(R_g(x,z)+2Q(x))-1]
        e^{-2\pi vR_g(x,z)}\mu.
\]

它等价于所有R/Q/φ都以√v x代入，Dx保持不变；没有从unscaled方程漏掉vQ。x=0或Q=0不在本门，未将theta常项的特殊规范藏进此证明。

## 3. 可解除的局部前件和继续冻结的责任

该计算只确认明示独立R_g版本的单x Green/current规范。原literal R/K失域的反测保留；没有改写其版本，也没有由局部相容性解冻作者Th7.4或算术height身份。

当前未构造quotient上的完整格点和，不支付格点/Poisson/dual零模、全部空间导数、P0／时间交换、全S_exp原du／Dlog／强源费用、自然Dirichlet/height范数、全部noncompact Pan及537同源非根。单个x的Dx/current不自动变成可下降的global arithmetic类；Γ稳定子、orbifold与全部尾未在本门处理。

净分类仍是标准局部规范修补0数学轮，不改变经典独立primitive/RR、完整Γ/contact/properpowers/双pole、signedgrowth/actualq/core/coupling/Ξ和最强旧whole leading4/5负惯性UPPER。局部成功不能完成长期Goal或授予新合同；下一是否有完整源input/test/net由root按STATE决定。

## 4. 实际终稿对齐及版本绑定

已完整核读ng_off的一般坐标U/V/t导数与β1链式法则，以及ng_delta的simple roots、正smooth A、解析β1余项、平面delta、Q<0与√v质量。两稿在同一B/Q/R_g、μ/ddc、两半平面和量词上相容，未发现需要改动的实质错误；上述是本审稿独立复算的闭合链，不是只对照相同结论标签。

最终绑定为UTF-8、LF规范化SHA256：

* local-differential-identity.md：bfef064c6a198e5b999448bc392c34d9dd57c1f7bf0710a1ca3d2acc81345407（5757 bytes）。
* log-singularity-delta-and-scope.md：1d225569f5cc2c3ca910ecfa453a6eacb25f4611649f43b9266d0d2ee49feaa7（7056 bytes）。

只有以上版本获本次有限PASS。任何B/Q/R、μ/ddc、v缩放、delta或域的语义改动必须重新核对，不能用本稿预验尚未出现的版本。出稿仍不代root消费；经典主瓶颈与原Goal完成门未变。
