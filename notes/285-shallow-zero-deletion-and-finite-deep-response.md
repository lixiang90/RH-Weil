# 285. 浅层无限零点删除与有限深右响应

日期：2026-09-06。主线：NCE-8 / B1z；论文归属：Vaughan--Brownian response。

状态：[T/R] 实际无限浅层零点集合、保留端点及高虚部尾的定量删除；
[T] 同一实际物理方向和279晚段的预算转移；
[O] 剩余有限深右零点的带符号四阶预算。
本篇不假设 RH，不把数值验证高度当作全体零点信息，也不声称新颖性。
与280的固定有限模板不同，本篇删除的集合可以增长，且包含无限多个实际零点。

## 1. 同一记录序列和精确目标

固定 \(0<\sigma<\beta<1/2\)，令
\[
 \delta=\beta-\sigma>0,\qquad d=1/2-\sigma>0,
 \qquad L=\log Y,\qquad \ell=\ell(Y)=\max(1,\log\log\log Y).
 \tag{1}
\]
只在充分大 \(Y\) 使用三重对数。沿
[284](284-causal-abel-inverse-and-diagonal-record-selection.md)
的新整数对角记录序列，\(N=Y\in\mathbb N\)，且
\[
 |M|\ge c_*Y^d\ell,
 \qquad P_\beta(N)N^\delta<C_{\rm diag}|M|,
 \qquad c_*>0 .
 \tag{2}
\]
常数与尺度无关。以下估计实际上对任意满足(2)的实际配置
\(Y\le N\le2Y\)、整数 \(N\) 成立；共尾存在性使用284，不再另作选择。
在这一较一般表述中，隐常数也允许依赖所固定的 \(c_*,C_{\rm diag}\)；
沿284指定序列时将其依赖吸收进 \(\sigma,\beta\)。

始终采用实际匹配源
\[
 w_Y(x)=x^{-\sigma}e^{-x/Y},\quad R(x)=\psi(x)-x,
 \quad M=\sum_{2\le n\le N}\Lambda(n)w_Y(n)-\int_1^Nw_Y(x)\,dx,
\]
\[
 f_\xi(x)=w_Y(x)(\cos(\xi\log x)-1),\qquad
 \widehat r(\xi)=\sum_{2\le n\le N}\Lambda(n)f_\xi(n)
                         -\int_1^N f_\xi(x)\,dx.
 \tag{3}
\]
\(-1\) 保留完整中心质量 \(-M\)。\(R\) 右连续，整数 \(N\) 的原子完整计入。

固定两个参数
\[
 A>1/2,\qquad 0<a<3/8,
\]
\[
 U=\sqrt L,\quad T=L^A,\quad
 \vartheta_Y=\frac12+a\frac{\log L}{L},\quad
 V=\sqrt Y\,L^{3(A+1)/4},\qquad
 E=\{\xi:U<|\xi|\le T\}.
 \tag{4}
\]
最终 \(1/2\le\vartheta_Y\le3/4\)、\(V\ge2T\)、\(\log V\asymp_A L\)。
这里 \(T\) 是物理频率上界，\(V\) 是零点虚部上界，不可混同。

对每个实际非平凡零点 \(\rho=b+i\gamma\)，按其重数定义
\[
 I_\rho(\xi)=\frac1\rho\int_2^N x^\rho f'_\xi(x)\,dx,
 \qquad
 Z_{Y,A,a}(\xi)=
 \sum_{\substack{\Re\rho>\vartheta_Y\\|\Im\rho|\le V}}I_\rho(\xi).
 \tag{5}
\]
这是有限、带符号的实际零点和，不用 \(1/2\) 替换任何 \(\Re\rho\)。
零点集合按共轭封闭，故对实数 \(\xi\)，\(Z_{Y,A,a}(\xi)\) 为实数。

对可测函数 \(\Phi\) 定义
\[
 \mathfrak Q_F(\Phi)=\frac1{2\pi}\int_F\frac{|\Phi(\xi)|^4}{\xi^2}\,d\xi,
 \qquad Q_F(r)=\mathfrak Q_F(\widehat r).
 \tag{6}
\]
本篇把(5)当作频率函数，不擅自宣称它是某个新的正源或完备 L 函数。

### 定理285-A [T/R]

沿同一序列(2)，有无条件估计
\[
 \boxed{\quad
 \frac{\mathfrak Q_E(\widehat r-Z_{Y,A,a})}{M^4L}
 \ll_{\sigma,\beta,A,a}
 \frac{1+L^{4a-3/2}(\log L)^8}{\ell^4}+L^{-3/2}
 =O_{\sigma,\beta,A,a}(\ell^{-4})=o(1).
 \quad}
 \tag{7}
\]
从而对任意随尺度变化的可测子带 \(F\subset E\)，一致有
\[
 \boxed{\quad
 \frac{|Q_F(r)^{1/4}-\mathfrak Q_F(Z_{Y,A,a})^{1/4}|}{|M|L^{1/4}}
 \ll_{\sigma,\beta,A,a}\ell^{-1}=o(1).
 \quad}
 \tag{8}
\]
特别，原频带预算与(5)的有限深右带符号预算等价。
这不是声称两个未知能量的归一化差本身为 \(o(1)\)：(8)明确保留四次方根。

## 2. 无条件绝对积分后总和及真实端点 [T/R]

所用外部输入是 zeta 的已知临界带 \(0<\Re\rho<1\)、单位高度零点计数，
以及[282](282-rh-conditional-endpoint-preserving-response-bound.md)
已逐式审计的半权截断显式公式。
来源为[Kedlaya 第9章，Lemma9.4 与 Theorem9.9](https://kskedlaya.org/ant/chap-von-mangoldt.html)。
单位高度计数含重数，因而任意实际零点子集同样满足该上界。

先明确为何可以无条件定义整个积分后的零点和。
282-B 的振幅证明可以取上边界 \(\vartheta=1\)：对所有 \(0<b<1\)，
\[
 g_{b,0}(u)=e^{(b-\sigma)u-e^u/Y},\qquad
 g_{b,1}(u)=(\sigma+e^u/Y)g_{b,0}(u)
       \quad(\log2\le u\le\log N),
\]
零延拓到区间外，仍有
\[
 \|g_{b,j}\|_1+\operatorname{TV}(g_{b,j})\ll_\sigma Y^{1-\sigma},
 \qquad
 \left|\int g_{b,j}(u)e^{ivu}\,du\right|
       \ll_\sigma\frac{Y^{1-\sigma}}{1+|v|}.
 \tag{9}
\]
事实上此处仅用正数 \(1-\sigma>0\) 作 majorant；一阶导数仍只产生
\((e^u/Y)^j\)、\(j=0,1,2\) 的固定线性组合，两个零延拓端点跳跃也保留。
证明不需要一个固定的 \(\Re\rho\le\vartheta<1\) 零自由条带。

对于 \(q=|\xi|\ge1\)，精确换元及282的核求和给
\[
 I_\rho(\xi)=-\frac1\rho\int_{\log2}^{\log N}e^{i\gamma u}
 \{g_{b,1}(u)(\cos(\xi u)-1)+\xi g_{b,0}(u)\sin(\xi u)\}\,du,
 \tag{10}
\]
\[
 |I_\rho(\xi)|\ll_\sigma
 \frac{Y^{1-\sigma}}{1+|\gamma|}
 \left\{\frac1{1+|\gamma|}
 +(1+q)\left(\frac1{1+|\gamma-q|}
                   +\frac1{1+|\gamma+q|}\right)\right\},
 \tag{11}
\]
\[
 \sum_\rho|I_\rho(\xi)|\ll_\sigma
                 Y^{1-\sigma}\log^2(2+|\xi|)<\infty .
 \tag{12}
\]
这是每个固定 \(Y,N,\xi\) 的无条件绝对收敛，不是未证 RH 下的形式零点展开。
相同 majorant 也在紧物理频率区间上给一致收敛。

为保留全部端点，置
\[
 C_\zeta=\frac{\zeta'(0)}{\zeta(0)},\qquad
 T_0(x)=-\tfrac12\log(1-x^{-2}),
\]
\[
 E_N(\xi)=f_\xi(N)R(N),
\]
\[
 \begin{aligned}
 B_{Y,N}(\xi)={}&\Lambda(2)f_\xi(2)-\int_1^2 f_\xi(x)\,dx-f_\xi(2)R(2)\\
 &+C_\zeta(f_\xi(N)-f_\xi(2))
                  -\int_2^N T_0(x)f'_\xi(x)\,dx.
 \end{aligned}
 \tag{13}
\]
则有精确恒等式
\[
 \boxed{\quad
 \widehat r(\xi)=E_N(\xi)+B_{Y,N}(\xi)+\sum_\rho I_\rho(\xi).
 \quad}
 \tag{14}
\]

证明(14)时，先把源分成 \([1,2]\) 与 \((2,N]\)，再作右连续 Stieltjes
分部积分。只在普通积分 \(\int_2^N R(x)f'_\xi(x)\,dx\) 中换成半权 \(R_0\)，
先固定 \(Y,N,\xi\)，再令显式公式高度趋于无穷；282-(13)--(15)的支配收敛
论证及(12)识别这个高度极限。\(N\) 的原子完整留在 \(E_N\)，
\(n=2\) 的原子只在(13)第一项出现一次。

这里 \(|B_{Y,N}(\xi)|\ll_\sigma1\) 对所有频率一致：常数及固定早段直接有界；
平凡项用
\[
 T_0'(x)=-\frac1{x(x^2-1)},\qquad
 \int_2^N T_0 f'_\xi=[T_0f_\xi]_2^N-\int_2^N T_0'f_\xi
\]
和 \(|f_\xi(x)|\le2x^{-\sigma}\) 再分部积分。
不能先用含 \(|\xi|\) 的导数绝对值估计，再声称误差与频率无关。

## 3. 全部浅层零点的统一删除 [T/R]

定义无限子集的积分后和
\[
 Z_{\rm sh}(\xi)=\sum_{\Re\rho\le\vartheta_Y}I_\rho(\xi).
 \tag{15}
\]
它由(12)绝对定义，包括所有 \(\Re\rho\le1/2\) 的实际零点，
还包括深度至多 \(a\log L/L\) 的右半零点；不是固定有限模板。

当 \(\vartheta\in[1/2,3/4]\) 时，282-B 中
\(d_\vartheta=\vartheta-\sigma\in[d,d+1/4]\) 留在固定正紧区间。
其 \(\Gamma(d_\vartheta+j)\) 积分常数、导数系数和端点界一致有界。
所以可对随 \(Y\) 变化的 \(\vartheta_Y\) 仍一致使用
\[
 |Z_{\rm sh}(\xi)|\ll_\sigma
 Y^{\vartheta_Y-\sigma}\log^2(2+|\xi|)
 =Y^d L^a\log^2(2+|\xi|),\qquad |\xi|\ge1.
 \tag{16}
\]
这一步没有假设全部零点都属于浅层；只是对子集使用相同的单位高度上界。

对 \(U\to\infty\)，直接积分或令 \(t=e^v\) 给
\[
 \int_U^\infty\frac{\log^8(2+t)}{t^2}\,dt
       \ll\frac{\log^8(2+U)}U.
 \tag{17}
\]
因此在整个 \(|\xi|\ge U=\sqrt L\)，不只有限带 \(E\)，都有
\[
 \mathfrak Q_{|\xi|\ge U}(Z_{\rm sh})
       \ll_\sigma Y^{4d}L^{4a}\frac{(\log L)^8}{\sqrt L},
\]
\[
 \frac{\mathfrak Q_{|\xi|\ge U}(Z_{\rm sh})}{M^4L}
       \ll_{\sigma,\beta,a}
         \frac{L^{4a-3/2}(\log L)^8}{\ell^4}=o(1).
 \tag{18}
\]
严格限制 \(a<3/8\) 的作用正在最后一步；此估计在 \(a=3/8\)
不支持同样的 little-oh 结论。这里没有从有限模式实验外推无限集合。

顺便，若只删除固定实部范围 \(\Re\rho\le1/2\)，则在整条
\(|\xi|\ge1\) 上已有 \(\mathfrak Q\ll Y^{4d}=o(M^4L)\)。
(18)使用增长的下频率 \(U\)，才允许额外删除上述随尺度缩窄的右侧浅层。

## 4. 无条件高虚部尾及物理/谱高度账本 [T/R]

令
\[
 Z_{\rm hi}(\xi)=
 \sum_{\substack{\Re\rho>\vartheta_Y\\|\Im\rho|>V}}I_\rho(\xi).
 \tag{19}
\]
对 \(1\le q=|\xi|\le T\)、\(V\ge2T\)，(11)中
\(|\gamma\pm q|\ge|\gamma|/2\)，故
\[
 |I_\rho(\xi)|\ll_\sigma
             \frac{Y^{1-\sigma}q}{(1+|\gamma|)^2}
             \qquad(|\gamma|>V).
 \tag{20}
\]
由单位高度计数，
\[
 \sum_{|\gamma|>V}\frac1{(1+|\gamma|)^2}
       \ll\frac{\log(2+V)}V,
\]
\[
 |Z_{\rm hi}(\xi)|\ll_\sigma
          Y^{1-\sigma}|\xi|\frac{\log(2+V)}V
          \qquad(1\le|\xi|\le T).
 \tag{21}
\]
实际上这些上界允许高虚部尾含全部左右零点；取子集不会增大所用绝对和。

必须保留(21)中的 \(|\xi|\) 再积分。由 \(\int_U^T t^2dt\le T^3/3\)，
\[
 \mathfrak Q_E(Z_{\rm hi})
    \ll_\sigma Y^{4-4\sigma}
                   \frac{(\log(2+V))^4 T^3}{V^4},
\]
\[
 \frac{\mathfrak Q_E(Z_{\rm hi})}{M^4L}
    \ll_{\sigma,\beta}
          \frac{Y^2(\log(2+V))^4T^3}{V^4\ell^4L}.
 \tag{22}
\]
代入 \(T=L^A\)、\(V=\sqrt Y L^{3(A+1)/4}\)，有
\(V^4=Y^2L^{3(A+1)}\)、\(\log(2+V)\asymp_A L\)，所以
\[
 \frac{\mathfrak Q_E(Z_{\rm hi})}{M^4L}
       \ll_{\sigma,\beta,A}\ell^{-4}.
 \tag{23}
\]
幂次账本是 \(4+3A-3(A+1)-1=0\)。
首带 \(A=1\) 给 \(V=\sqrt Y L^{3/2}\)，小于280有限高度接口使用的
\(\sqrt Y L^3\)。这里先建立绝对积分后总和，再估它的实际尾部；
不是遗漏截断显式公式端点后得到的虚假小余项。
因为无限和已绝对定义，(5)采用 \(|\gamma|\le V\) 而(19)采用 \(|\gamma|>V\)
没有边界遗漏，不需要额外要求 \(V\) 避开零点虚部。

## 5. 端点预算、四次方根转移及主定理证明 [T]

由整数端点及(2)，
\[
 |E_N(\xi)|\le2w_Y(N)|R(N)|
       \le2P_\beta(N)N^\delta\ll_{\sigma,\beta}|M|.
 \tag{24}
\]
强质量下界使 \(|M|\to\infty\)，所以(13)的固定有界项也可吸收。
于是
\[
 \frac{\mathfrak Q_{|\xi|\ge U}(E_N+B_{Y,N})}{M^4L}
        \ll_{\sigma,\beta}\frac1{UL}=L^{-3/2}.
 \tag{25}
\]
这是在保留真实端点之后估算并删除它，不是把 \(R(N)\) 换成半权或删掉 \(-M\)。

由(12)绝对收敛，(14)可精确分成
\[
 \widehat r-Z_{Y,A,a}=E_N+B_{Y,N}+Z_{\rm sh}+Z_{\rm hi}.
 \tag{26}
\]
对右侧三个块用四次幂三角上界，(18)、(23)、(25)给(7)。
由于 \(a<3/8\)，\(L^{4a-3/2}(\log L)^8\to0\)，且
\(\ell^4 L^{-3/2}\to0\)，故最后可合并为 \(O(\ell^{-4})\)。
再在正测度 \(\mathbf1_Fd\xi/(2\pi\xi^2)\) 上应用 \(L^4\) Minkowski
及反向三角不等式，得到(8)，完成定理285-A。\(\square\)

### 推论285-B：原物理方向不改变

保持原 prime--continuum 正通道 \(p,c\)、总质量 \(S\) 及 Brownian 分母 \(D\)，
写
\[
 W_{\rm phys}(\xi)=|\widehat p(\xi)|^2+|\widehat c(\xi)|^2,
 \qquad \mu=M/S,
\]
\[
 J_{4,F}=\frac1{S^4D}\frac1{2\pi}\int_F
             \frac{|\widehat r|^4W_{\rm phys}}{\xi^2}\,d\xi .
 \tag{27}
\]
[277](277-continuum-channel-coercivity-and-double-discrepancy-interface.md)
的实际连续通道下界给，在 \(|\xi|\ge U\) 上最终一致有
\[
 W_{\rm phys}(\xi)\asymp_\sigma S^2,\qquad D\asymp_\sigma S^2L.
 \tag{28}
\]
故由(8)，
\[
 \boxed{\quad
 J_{4,F}=O(\mu^4)
 \quad\Longleftrightarrow\quad
 \mathfrak Q_F(Z_{Y,A,a})=O(M^4L),\qquad F\subset E.
 \quad}
 \tag{29}
\]
还可只在(27)中将 \(\widehat r\) 换成 \(Z_{Y,A,a}\)，定义辅助数值
\(J_{4,F}^{\rm spec}\)，但绝不替换 \(p,c,S,D\)。同一加权 \(L^4\) 三角式给
\[
 |J_{4,F}^{1/4}-(J_{4,F}^{\rm spec})^{1/4}|
       \ll_{\sigma,\beta,A,a}|\mu|/\ell.
 \tag{30}
\]
这不是新构造的正配置；它只是原物理响应中已严格控制误差的一个替换。
整个真实响应仍可很大，(29)右侧正是未证输入。

## 6. 接入279的实际晚段：不能偷换零点核 [T]

固定
\[
 h>\frac{2A-1}{4\delta},\qquad K=\lfloor N/L^h\rfloor.
 \tag{31}
\]
最终 \(2\le K\le Y/2\)。按279的原半开约定，把整数 \(K\) 的原子只归早段，
并将连续积分一同拆成 \([1,K]\) 与 \((K,N]\)，所有 lag 不平移。
有精确 \(r=r_e+r_l\)，\(M_l=M-M(Y,K)\)。

[279](279-record-controlled-arithmetic-prefix-deletion.md)的已审有限证明只使用
相对历史 guard、整数端点和实际匹配源，不使用 dyadic 尺度。
把其中的 guard 常数替换为(2)的 \(C_{\rm diag}\)，便给
\[
 \frac{Q_E(r_e)}{M^4L}
       \ll_{\sigma,\beta,A,h}L^{2A-1-4h\delta}=o(1),
 \qquad
 \frac{M_l}{M}=1+O_{\sigma,\beta}(L^{-h\delta}).
 \tag{32}
\]
合并(7)与早段的 \(L^4\) 三角式，得到
\[
 \frac{\mathfrak Q_E(\widehat r_l-Z_{Y,A,a})^{1/4}}{|M|L^{1/4}}
 \ll_{\sigma,\beta,A,a,h}
       \ell^{-1}+L^{-h\delta+(2A-1)/4}=o(1).
 \tag{33}
\]
这里(5)的零点核仍是 \(\int_2^N x^\rho f'_\xi(x)dx/\rho\)。
不能因为比较对象改成晚段，就把它未经端点核查地换成 \(\int_K^N\)。
(33)来自实际早段的独立小误差，而不是声称两种零点核完全相同。

279-B的正源分母比较同样保持：\(S_l/S\to1\)、\(D_l/D\to1\)，
且原/晚连续通道在本频带均有双边下界。
因此(29)亦等价于
\[
 Q_F(r_l)=O(M_l^4L)
 \quad\Longleftrightarrow\quad
 J_{4,F}^{\,l}=O(\mu_l^4),\qquad F\subset E,
 \tag{34}
\]
其中晚段指标仍取它本来的 \(S_l,D_l,\mu_l=M_l/S_l\)。
在(31)取等号时只得到有界转移而不是(32)--(33)的 little-oh；本文不偷换此边界。

## 7. 已删除什么，以及唯一保留的算术输入 [T/O]

本篇实际完成的删除有三块：

- 全部 \(\Re\rho\le1/2+a\log L/L\) 的无限积分后零点和，包括整个中心线及左侧；
- 高于 \(V=\sqrt Y L^{3(A+1)/4}\) 的全部剩余虚部尾；
- 完整保留后按实际 guard 控制的锐 cutoff 端点和固定显式公式项。

因此不是只把原任务写成一个未经误差估计的无限零点公式。
剩余集合随 \(Y\) 变化，必须同时满足实部深度与有限虚部条件。
但是其中各项仍带有实际 \(x^{\Re\rho}\)、振荡相位、\(1/\rho\) 及原 \(-1\) 中心化。
它们的有符号交叉项尚未估计。

下一最小输入可固定首带 \(A=1\)、任意固定 \(0<a<3/8\)：
\[
 \boxed{\quad
 \frac1{2\pi}\int_{\sqrt L<|\xi|\le L}
 \left|
   \sum_{\substack{\Re\rho>1/2+a\log L/L\\
                    |\Im\rho|\le\sqrt Y L^{3/2}}}
       \frac1\rho\int_2^N x^\rho
        \frac{d}{dx}\left[w_Y(x)(\cos(\xi\log x)-1)\right]dx
 \right|^4\frac{d\xi}{\xi^2}
       \ll_{\sigma,\beta,a} M^4L .
 \quad}
 \tag{35}
\]
它仍为 **[O]**。若同时接实际晚段，则一般取 \(h>1/(4\delta)\)；
只有 \(\sigma=1/4,\beta=3/8\) 时才简化成 \(h>2\)。
(35)即便解决，也只闭合首个中频子带，不自动覆盖284仍未解决的全部增长中频。

零密度估计可以提供独立计数输入，但不能直接替换(35)。
将(10)绝对化所得单项上界含 \(Y^{\Re\rho-\sigma}\)，
计数上界本身不能把这个幂次换成 \(Y^{1/2-\sigma}\)，也不提供四次方中的有符号相消。
若只用(2)当前保证的质量下界作归一化，对深右零点仍可能出现
\(Y^{\Re\rho-1/2}/\ell\) 的放大因子。
这只是指出该上界的缺口：没有断言实际记录质量等于其下界，
没有证明某个实际零点使(35)失败，也没有排除将更具体的密度信息与真实质量联用。
本篇没有获得能够完成(35)的这种独立估计。

若 RH 成立，(35)中的集合为空，预算当然成立；这不证明(35)与RH等价，
也不证明它严格弱于RH。反过来，存在深右零点不等于(35)失败：
质量分母、相位及多项相消都必须保持。

## 8. 依赖、循环性和审计状态

| 输入 | 证明中的作用 | 删除后的准确缺口 |
|---|---|---|
| 实际强记录质量及独立历史 guard [T/R] | (18)、(23)、(25)的同一真实尺度 | 不能以抽象选择本身制造质量或端点控制 |
| 无条件临界带、单位高度计数和截断显式公式 [R] | (12)、(14)及高虚部绝对尾 | 没有这些输入，不能任意分组无限零点和 |
| 统一 \(\vartheta\in[1/2,3/4]\) 的 BV 常数 [T] | (16)允许浅层阈值随 \(Y\) 变化 | 固定参数估计不经核对不能用于增长/移动集合 |
| \(a<3/8\)、物理带下端 \(\sqrt L\) [T] | (18)保留正的幂次节省 | 边界 \(a=3/8\) 没有本证明所需的节省 |
| \(V\ge2T\) 及 \(V\) 的明确选择 [T] | (20)--(23)将高谱尾量化 | 物理高度与零点高度不可设为同一参数后忽略远尾 |
| 原实际连续正通道 [T] | (28)--(30)接回物理方向且双边等价 | 不可用任意系数Bessel界或新正源代替 |
| 279半开前缀与一般 \(h\) 阈值 [T] | (32)--(34)接同一实际晚段 | 不允许重复计入 \(K\) 原子或忽略尾部中心质量 |

完整 Gamma gluing、Weil 正性、上同调桥梁及一般 L 函数的对应结构仍开放。
本篇仅对 Riemann 实际实正源和所列强记录序列证明定量删除。
未新增或运行数值实验；所有结论来自明确有限积分、不等式及经过控制的无限极限。

主代理已逐式独立审查全部证明，并再次核验所引作者书稿的单位高度计数
与半权显式公式；carrier_audit 另独立复核全文。
重点审查移动实部常数、高谱尾的四幂账本、完整端点及四次方根而非能量差。
gap_exception_audit 完成写作与自审。内部 [T/R] 不等于文献新颖性、
外部同行评审、无条件四阶预算完成或整个研究 Goal 的阶段验收。
