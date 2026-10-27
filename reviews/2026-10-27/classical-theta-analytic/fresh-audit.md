# Classical theta analytic源：独立fresh逆审

2026-10-27；/root/ct_fresh独占稿。恢复Goal/STATE/唯一D20261027N及实际next公式，独立目视作者PDF4、21、22、29并复算下面的坐标；另目视PDF25/30相关height公式。**最终限定PASS：两原稿与root冻结稿正确识别literal K失域，未把待付空间费用或条件553规则升级为实际结果。** 当前literal K的ordinary lattice sum未定义，后续P0／空间费用／553消费冻结；这次PASS验收的是失域反测和准确冻结范围。本稿不改STATE/cadence/Git，不预C048/585，不另造候选或修补授权。

## 1. 三个原式在同一规范下的反测

作者PDF4给Q(x)=det(x)，bilinear B(x,y)=tr(x y^iota)，trace-zero矩阵有y^iota=−y；w(z)=[[z,−z²],[1,−z]]。PDF21 Eq5.3字面为

\[
 R(x,z)=|B(x,w(z))|^2/|B(w(z),\overline{w(z)})|.
\]

PDF21 Prop5.1及PDF22 Eq5.8给

\[
 \varphi_\infty^0(x,z)
 =[4\pi(R(x,z)+2Q(x))-1]e^{-2\pi R(x,z)},\qquad
 \varphi_\infty=\varphi_\infty^0e^{-2\pi Q(x)}.
\]

没有把source声明的“Schwartz”当作这些literal表达式可同时成立的证明。

取实际允许的z=i，并以实线性坐标

\[
 x=\begin{pmatrix}a&u+d\\u-d&-a\end{pmatrix},\qquad
 w(i)=\begin{pmatrix}i&1\\1&-i\end{pmatrix}.
\]

直接矩阵乘法给

\[
 Q(x)=d^2-a^2-u^2,\quad B(x,w(i))=-2ia-2u,
 \quad B(w(i),\bar w(i))=-4.
\]

所以字面R=a²+u²，而Q+R=d²。于是

\[
 \boxed{
 \varphi_\infty(\sqrt v\,x,i)
 =[4\pi v(2d^2-a^2-u^2)-1]e^{-2\pi v d^2}.}
\]

它没有transverse Gaussian。沿d=0、a→∞，固定v>0时等于−4πv a²−1，不趋0。PDF22 Eq5.7所称majorant在同一坐标下是

\[
 B(x,x)+2R=2Q+2R=2d^2,
\]

不是正定majorant。这个是原B/Q/R三式的局部兼容性反测，不依赖某个split rational对角矩阵属于实际division代数。

## 2. 实际division lattice也不能避开此问题

实际L=O_B∩V在固定V(R)≅R³中是fullrank格；选择任意Euclidean范数及它的有限covering radius C。取y=(1,0,0)∈ker d，对每个n可选x_n∈L使||x_n−ny||≤C。因此d(x_n)有界，而a(x_n)²+u(x_n)²→∞；可取distinct subsequence。

对每个固定v>0，上框的多项式趋−∞，指数则有严格正的uniform lower，故实际summands沿此序列趋−∞。它们甚至不满足ordinary series必要项测试，不是只缺small-v/Poisson的uniform估计。

还可强化：正项只可能在a²+u²<2d²时发生；在那里||x||²<3d²，正部由C_v(1+||x||²)e^(−(2πv/3)||x||²)支配，其full-lattice和有限。负部由上述子列发散。所以literal普通格点和在该z=i为−∞，不能靠普通重排恢复finite kernel。必要项测试已经足以否定当前source type；强化结论不用于泛排别的regularization。

fullrank论证不用选择新的B/level，不要求L内存在任何指定的split rational ray；compact quotient也不能修复它，因为z=i本身是允许的domain点。与局部源规范的冲突先于source integral或Pan测试。

## 3. 消费冻结和没有得到的结论

PDF29 Eq7.22的当前literal K(iv,z)=Σ_L phi∞(√v x,z)未成为ordinary theta kernel。因此按已准公式在raw K之后施行空间均值P0不能直接定义P0K，Phi_r也尚未取得smooth/Green值域、全du/Dlog费用或Dirichlet/H¹费用。不能先宣布all-zero dual mode或调用553，也不能将预期的原核Schwartz性作为前提循环支付自身。

将R乘2会改变当前冻结公式；它不能无声作为作者原式消费。其它明示regularization、先termwise投影或改用独立规范一致的source也不由本反测自动排除，但必须重新给实际定义、域与完整尾，不能作为这一literal source已经合法的理由。本稿不选择或执行任何修补。

前轮fixed holomorphic Mellin–Bergman源的cusp／Gram／原费与A(Pan)=S证明不依赖这里的literal Gaussian计算，不回滚。§8算术Theta存在性、height/stack/index与半系数继续各按cited依赖处理，不由本局部矛盾升级成“所有算术Theta不存在”。583/582独立原Green结果及旧closed-base纠正保持。

## 4. 无限像及mixed责任的独立审查标准

若另有已合法定义并付全du费的无限目标T:L²(du)→H，那么553最多先给T(P)在T(F)的像闭包中稠密，不能套前轮finite-dimensional closed-image步骤宣布exact T(P)=T(F)。要从Pan mixed根推出整个pullback退化，须实际给目标pairing对该拓扑的连续性，或直接给拉回对原L²的连续性。H¹／Dirichlet的components/locally-constant closed base必须明确；global μ mean-zero不自动删除所有component常数。

当前literal failure意味着这些是条件逻辑，未给当前Phi实际费用或退化定理。即使未来能付款，也不自动支付完整Γ/contact/properpowers/双pole、classic mixed身份、同源537可见性及成长/core/coupling/Ξ。

## 5. 净等级与最终对稿位置

该反测是标准矩阵代数、Gaussian及格点covering-radius的直接应用；没有新的经典Weil正号或whole后果。建议当前literal source/type门按来源／标准审查0数学轮结算，cadence保持2／历史48／cycle16，classic主瓶颈不变。不能以一个归一化反例领取实质方法类边界或完成长期Goal。

已完整核读两原稿及root的literal-normalization-freeze.md：一般z的实正交搬运只将L带成另一fullrank实格，不需它仍是原整格；fullrank覆盖半径反测及正部Gaussian界正确。norm稿明确所有Phi原du／H^m／Dirichlet费用未付、无限像只能推出closure、mixed根延伸须实际连续性；component闭base保留。PDF25/30仅支撑cited形式h(aφ,aψ)=−E(φ,ψ)/4，其中E=−∫Δφ·barψ dμ、实输入后first-linear复化，未免费替换usualenergy缩放或当前Phi自然height。

R_sharp=−B(x_-,x_-)=2R_print是准确的负平面factor定位，原稿/root均未执行修补后Poisson／空间费／Pan或借此继承Th7.4。root拟下一仅做同PDF单x Green规范的一致性比较，可作为独立明示type门；单确认factor2不支付K_sharp全source运输、更不授予数学合同。当前最强classic可消费结果仍542+555→557 whole leading4/5负惯性UPPER，非正性／负谱lower。下一实际行动由root/STATE另定，本稿不产生第二行动权威。

最终绑定为UTF-8、LF规范化SHA256：

* zero-modes-and-poisson.md：731a5892e02551cde865f8aaf3bca74c76a1144c661b5b1945fe9e8616b1b63c（6526 bytes）。
* source-space-fees-and-pan.md：82c515aadcf27771501297166f01eb2daf3399019b7f5f4278528494ae603503（8199 bytes）；旧2bdff版本不消费。
* literal-normalization-freeze.md：96b5f00e19ed8283da6c065949c347834200a042ed42f99c15e737954cc9f773（2546 bytes）。

只有这些版本获得本次有限PASS。任何更改R／Q／φ∞／Green规范、原费或目标pairing的后续消费须另重闭受影响依赖。
