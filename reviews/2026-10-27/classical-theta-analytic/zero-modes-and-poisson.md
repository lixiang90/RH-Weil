# Classical theta实际首门：literal R使核失去Schwartz性，Poisson门冻结

2026-10-27；/root/ct_zero独占原稿。执行STATE唯一actual K/Phi type首门，不改STATE/cadence/Git，不预C048/585。下述是对已库作者PDF实际印式的规范核查及标准格点反测；不是对所有Kudla–Millson theta或修正版本的否定。出稿不代root消费。

## 1. 原件、实际模型与字面规范

复用Kudla作者PDF `literature/local/2026-10-27-joint-tower/kudla-cdm-revised-author.pdf`，56页、887943字节，raw SHA256 `47ff2ff6f5151081dd029a1df680377b88d58fc09d6629f3a2b2c3b78bab0f54`。本稿实际抽取并目视PDF4–6、20–22、29的相关定义/陈述；不读§9–11、不消费原定理证明。PDF6只用首段proper模型陈述，p-adic uniformization不作本稿输入。

PDF4定义：B_R≃M₂(R)，V=tracezero，Q(x)=ν(x)=det(x)=−x²；

\[
 B(x,y):=(x,y)=\operatorname{tr}(xy^\iota),\qquad
 B(x,x)=2Q(x),\qquad y^\iota=\operatorname{tr}(y)-y.
\]

PDF4的w(z)为[[z,−z²],[1,−z]]，D≃C\R。PDF5设O_B maximal order、Γ=O_B^×，M(C)≃Γ\D；从该页起假D(B)>1，PDF6述proper。actual L=O_B∩V是V_R中的full rank3格。此处不要求L含split rational line，也不将division模型换成M₂(Q)。

PDF21(5.3)的**literal**规范是

\[
 R_{\rm print}(x,z)=|B(x,w(z))|^2\,|B(w(z),\overline{w(z)})|^{-1}.
\]

同页Prop5.1及PDF22(5.8)把scalar coefficient给为

\[
 \varphi^0_\infty(x,z)=
 [4\pi(R_{\rm print}(x,z)+2Q(x))-1]e^{-2\pi R_{\rm print}(x,z)},
 \qquad \varphi_\infty=\varphi^0_\infty e^{-2\pi Q}.
\]

PDF22(5.7)另将B(x,x)+2R_print称为majorant。PDF29(7.22)在τ=iv时的native scalar式因此是

\[
 K(iv,z)=\sum_{x\in L}\varphi_\infty(\sqrt v x,z).
 \tag{1}
\]

这些印式不能在未经直接核算时同时当作“正定majorant／Schwartz coefficient”的已付事实。没有额外v^(3/4)可修复这个矛盾。

## 2. 精确二维退化：不是尾估计的常数问题

在z=i，写任意x∈V_R为

\[
 x=\begin{pmatrix}a&u+d\\u-d&-a\end{pmatrix},\qquad
 Q(x)=d^2-a^2-u^2.
\]

此时w(i)=[[i,1],[1,−i]]，由原B=−tr(xy)直接得

\[
 B(x,w(i))=-2ia-2u,\qquad B(w(i),\overline{w(i)})=-4,
 \qquad R_{\rm print}(x,i)=a^2+u^2.
\]

记ρ=a²+u²，则

\[
 B(x,x)+2R_{\rm print}(x,i)=2d^2,
 \qquad Q(x)+R_{\rm print}(x,i)=d^2.
 \tag{2}
\]

所以所谓majorant在整个实二维平面d=0上为零。literal coefficient精确为

\[
 \boxed{\varphi_\infty(\sqrt v x,i)
  =[4\pi v(2d^2-\rho)-1]e^{-2\pi v d^2}.}
 \tag{3}
\]

取x=diag(a,−a)便是(−4πv a²−1)，不衰减。这个实坐标计算是检查印式的精确反例，尚不以该线中有实际division格点作为前提。

## 3. actual full rank L同样发散：无需rational isotropic向量

给V_R选正定欧氏规范|x|_E²=ρ+d²。任何full rank格L有有限covering radius C：每个y∈V_R有x∈L使|x−y|_E≤C。这可由任取L基的有界基本平行多面体直接得到。

固定非零y∈ker d并令|y|_E=1。对一列n_j→∞、相邻间隔>2C+1，选actual x_j∈L满足|x_j−n_jy|_E≤C。于是x_j互异、

\[
 |d(x_j)|\le C,\qquad
 \rho(x_j)\ge(n_j-C)^2-C^2\longrightarrow\infty.
\]

对每个固定v>0，(3)的指数因子至少e^(−2πvC²)>0，而多项式部分趋−∞。故(1)的actual格点summand不趋0，不能是通常收敛或absolute／normal收敛的theta和。

还可按同一式核其正部，以避免暗含“或许有常规条件抵消”。summand为正必有ρ<2d²，因此|x|_E²=ρ+d²<3d²。在该区域

\[
 0<(4\pi v(2d^2-\rho)-1)e^{-2\pi vd^2}
 \le 8\pi v|x|_E^2 e^{-(2\pi v/3)|x|_E^2}.
\]

右侧在full rank L可和；证明只需格点壳数O((1+R)^3)与正定Gaussian衰减。另一方面，上述x_j的负部单项绝对值趋∞，故负部总和∞。所以literal(1)的正部有限、负部无限，任何有限格点耗尽的总和均趋−∞。±x配对也无用，因为summand为偶函数。

对一般z∈D，取h∈GL₂(R)使h·i=z（下半平面同理）。conjugation preserves Q/B，R_print随w的projective缩放不变；h^−1Lh仍是full rank3实格。将以上论证应用此格，得到每个fixed z、v>0均有同一失败。它不依赖Γ\D是否连通、covolume常数、level或L是否包含特定实射线。

## 4. Poisson零模和P0责任的正确状态

当前literal φ∞不是Schwartz函数；(1)在每个v>0已不成立为通常函数。因此没有在本稿可合法调用的ordinary Poisson式、dual lattice Gaussian或covolume leading term，不能继续报small-v双指数尾，更不能把large-v的formal x=0项−1当完整kernel的已付渐近。

P0^zK被定义在raw K之后；当前raw K未定义，故“减空间均值”没有现成对象可作用。若另选termwise subtraction、截断有限部、分布或其他regularization，那是必须另给定义、拓扑、空间交换及原费用的新对象，不被本反测一概排除，也不能沿用同一个(1)假装已自动付款。

物理Φ_r=int r(t)e^(3t/4)P0K(i e^t,z)dt的全域、du／Dlog／强源费、H¹／Dirichlet和全部Pan测试在当前literal规范下均冻结；并非已证明某个合法map只是“费用无界”。在源map尚未定义时，553的bounded-reader门还不能被当作已经执行的Pan结论。没有得到新的primitive类、height正号或经典Weil身份。

## 5. canonical修补只作明确定位，不在本稿运输

由B本身可无歧义定义z对应负二平面的正平方norm：

\[
 R_\sharp(x,z):=-B(\operatorname{pr}_{z,-}x,
                         \operatorname{pr}_{z,-}x).
\]

因B(w,w)=0、B(w,barw)<0，负投影直接算得

\[
 R_\sharp(x,z)=-\frac{2|B(x,w)|^2}{B(w,\bar w)}
              =2R_{\rm print}(x,z).
\]

在z=i它是2ρ，B(x,x)+2R_sharp=2(d²+ρ)才正定。这准确定位一个factor2语义修补；不是将印式重新解释为已正确。若采用R_sharp，须明确新版本并核其φ⁰／ξ=β₁(2πR)／ddc-current／μ及height相容性；不能只改一个R符号就声称已付整条算术Green链。本稿不执行修补后source运输、Poisson、费用、非零性或Pan测试，不自动换ray/B/level/weight。

净分类建议：标准规范直接核对＋full lattice初等发散反测，0数学轮。实际选择改变为先冻结当前literal source，再由root判断是否为可明确付费的同source规范修补；不领取所有theta方法边界或新的classic whole／primitive／RR／growth/core/coupling/Ξ后果。最强经典负惯性whole4/5UPPER与长期Goal完成门均未改。
