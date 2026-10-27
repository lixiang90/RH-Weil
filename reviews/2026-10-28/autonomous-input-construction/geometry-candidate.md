# 自主构造尝试：整数绕数到degree-zero线，未形成合格输入

2026-10-28；unit_height独占研究稿。恢复STATE／D20261028N、同G20261027、前沿、原553及已止recipe，check/show通过。本次实际尝试一个新源规则，再先行自筛；不是等待用户给公式，不是库存／宏观复述。只写本稿，不web／PDF／数值，不改STATE／cadence／合同／Git或其他稿。

**结果：构造出了一个明确、非解析的整数源规则及真实非零degree-zero线载体，但它在最便宜的537幅度测试即失败。因此没有形成可准数学的几何candidate。** 这份失败尝试不作为新方法类反例、来源章或后继合同；不改换阈值／载体／幅度继续修补。

## 1. 实际尝试的对象与源公式

为避免再把非proper覆盖上的flat方程或矩阵ordered数据当primitive，先选一个本来就有非零degree-zero线的紧复曲线

\[
 E=\mathbb C/\Lambda,\qquad \Lambda=\mathbb Z+i\mathbb Z,
 \quad P=\sqrt2\bmod\Lambda,\quad
 \mathscr P=\mathcal O_E([P]-[0]).
\]

\(\mathscr P^n\) 对每个非零整数n非平凡：principal degree-zero divisor在复环面上的点和须落在Λ，因而 \(n([P]-[0])\) principal会迫 \(n\sqrt2\in\Lambda\)，不可能。这个必要条件亦可由基本平行四边形上对 \(zf'/f\) 的边界积分得到。这里只把它当真实几何载体；没有给E指定独立算术模型、全有限位cycle或经典Weil比较。

原physical \(r=e^{u/2}f\in S_{\exp}(\mathbb R;\mathbb C)\)。因r两端趋0，\(\gamma_r(u)=1+r(u)\) 以两端共同值1成为一点紧化后的闭路径。一次固定源规则为

\[
 n(r)=
 \begin{cases}
 \displaystyle\frac1{2\pi i}\int_{\mathbb R}
                 \frac{r'(u)}{1+r(u)}du,
      &1+r(u)\ne0\quad\forall u,\\[4pt]
 0,&\exists u:\ 1+r(u)=0 ,
 \end{cases}
 \qquad
 J(r)=\mathscr P^{\,n(r)}. \tag{1}
\]

第一支是整数绕数；第二支是明示的固定补定义，保证写出一个全S_exp集合映射，而非把零穿越源暗中删掉。这个补定义本身没有独立算术根据，也不会被解释为primitive定理。r为complex；不把它换成real截面或bare f。

(1)读取整条源路径的非解析整数数据，不是原rank2 holonomy变参、旧谱商、未知正H或一个正Gram。输出有整数Cartier divisor \(n(r)([P]-[0])\)，不是把复权cycle叫整除子。它也没有预设其degree-zero类就是所需算术primitive。

规则确非恒零：取光滑实θ，u≤0时θ=0、u≥1时θ=1且中间从0增到1，令
\(r(u)=e^{2\pi i\theta(u)}-1\)。这是complex compact源，γ绕0一周，故n=1、J非平凡。这里仅验证候选有实际输出，不以对象非零充当Weil输入。

## 2. 域与费用自筛

非零穿越支内，\(\delta_r=\inf_u|1+r(u)|>0\)：在两端趋1，余下紧区间连续且不为零。因此积分绝对收敛，并有真实充分上界

\[
 |n(r)|\le\frac{\|r'\|_1}{2\pi\delta_r}
 \le\frac{p_{N,1}(r)}{\pi N\delta_r},\qquad N>0. \tag{2}
\]

小于δ_r的uniform路径扰动不改绕数。全S_exp中这些是实际强费用／gap依赖；没有付globaldu或zero-extension Dlog统一费用。fixed支撑[-L,L]至多由
\(\|r'\|_1\le\sqrt{2L}\|r'\|_2\) 付一阶强费，不能把H¹范数偷写成du／Dlog。

因此不能直接声称(1)满足553的globaldu连续桥假设；它还在零穿越处显式不连续。这里确实试了非analytic／强费用允许范围，而非再次假定一个有界线性读出。但这种类型差不保证它有新净信息，下一门直接否决。

## 3. 最便宜可证伪门：537全族的小幅度

若 \(\|r\|_\infty<1\)，则路径1+r完全在以1为中心、半径小于1的圆盘内。用 \(1+tr\)、0≤t≤1给不穿0的收缩，故

\[
 n(r)=0,\qquad J(r)=\mathcal O_E. \tag{3}
\]

取一个固定非零 \(r_o\in C_c^\infty((-17/16,17/16);\mathbb C)\)，可取原双polezero
\(r_o=(D^2-\tfrac14)(u\phi)\)，φ非零偶非负且支撑足够小。旧537不是只给一个大样本，而是该固定窗的全部complex非零源，故对任意ε≠0，

\[
 Q_\zeta(\varepsilon r_o)
 =|\varepsilon|^2Q_\zeta(r_o)>0.
\]

固定任意 \(0<|\varepsilon|<\|r_o\|_\infty^{-1}\)，(3)却给
\[
 J(\varepsilon r_o)=\mathcal O_E. \tag{4}
\]

于是这个源规则在原positive-control窗的一整个非空幅度范围内把非根送unit。任何只通过J的类／同对象mixed配对、并在unit为零的读出，都没有这些源的非零二次响应。不能用大幅度时某个n≠0抵消此门，也不能在幅度变化时重选branch或metric补回raw r，否则已是另一个带额外数据的规则。

**在此停止。** 没有继续构造Green、sections、height、mixedRR或讨论如何把它假设成 \(Q_\zeta\)。本次没有证明一个新Weil负源，也没有全几何no-go。

## 4. 全405／noncompact与553角色不挪用

这份候选是要求精确几何源响应的尝试，不是一个已给误差趋零的正D′近似族；不能借“D′层不必消Pan”跳过自己的非根责任。

全405关系仍包含原真实noncompact \(p=(D^2-\tfrac14)H\)、H>0，以及全部固定physical平移和复线性组合。构造时曾考虑用复路径的相位图测试 \(q+i\eta q'\)。**本文没有把q′从平移span的拓扑闭包升级成真实exact Pan，也不消费该预想为反例。** 若要使用导数，须核原E／Euler的exact来源；仅知道Weil根或某范数闭包不足。

无需该升级也有合法exact控制：\(q\) 与每个 \(\tau_hq\) 是旧405／553已付的实际physical关系，故有限组合 \(q-\tau_hq\) 及其固定复倍数亦是实际关系。但本候选已经在(4)失败，本文不再用差商推进一般winding反测、也不声称它已经通过全Pan。没有裁尾或以compact源与Pan交零代替全关系。

553和原holonomy系数级责任同样保留：若后来从某个新构造提取出globaldu／Hlog连续的必要系数，应单独扣553；不能拿整个map非analytic来免责。本次实际J在强拓扑零附近已经常值，故所有沿固定源幅度的局部变化都为零；这没有供给新的经典二次mixed信息，亦不需要借whole-map du有界性才能否决。

## 5. strongest-old净比较与最终状态

- **不同的实际数据：** 紧genus1载体有非零Pic⁰，绕数给整数divisor并能非零；这比只写一个smooth-flat方程或positive fiber metric具体，也不是原矩阵族换参数。
- **不能成为独立输入之处：** 该规则仍把整条source压成一个局部常值整数标记。574／575已经要求非平凡线与有效Cartier设施必须配合同一源的关系／非根响应，不能把carrier非零重验收为容量；(3)–(4)只是对本规则执行这项旧门。任取genus1也没有自然产生经典Γ/contact、全部properpowers、双pole或算术整模型。
- **最便宜净后果：** 无须读新来源、求RR或等待用户数据，就能自主拒绝这份实际尝试。它未形成可交给数学合同的source／mixed输入；不把这个toy失效记成新的strict方法边界或数学轮。

本次产出是一次真实构造及前置否决，而不是“假设所需map／RR存在”的条件清单。对允许的非analytic、source-adapted或有强费用路线没有全类排除。当前仍无合格几何candidate；不改阈值、E／P、补定义或加metric来续此recipe，不造下一来源章／合同。

原whole leading4/5仍为负惯性UPPER；独立净signed／corecross／同一非零primitive容量和Ξ未付。长期Goal保持原完成强度，自主研究不转交用户；本支不改管理或计轮。
