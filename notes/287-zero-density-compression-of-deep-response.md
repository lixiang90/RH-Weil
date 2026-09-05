# 287. 零密度输入压缩实际深右响应的谱高度

日期：2026-09-06。主线：NCE-8 / B1z；论文归属：Vaughan--Brownian response。

状态：[R] 正式预印本中的统一实际零密度定理；
[T/R] 全高度加权谱尾及四分之一次幂高度删除；
[N] 仅计数包络的一般多重集合类边界；
[O] 剩余有限深右带符号响应。
本篇使用实际 zeta 的独立零密度估计，真正缩小285的谱高度，不假设 RH。
它没有解决剩余首中频，也没有证明新颖性或完整 Weil 配置的存在性。

## 1. 同一实际序列与主结论

固定 \(0<\sigma<\beta<1/2\)，置
\[
 d=1/2-\sigma>0,\quad \delta=\beta-\sigma>0,\quad
 L=\log Y,\quad \ell=\max(1,\log\log\log Y).
 \tag{1}
\]
沿284已经独立构造的同一整数对角记录序列，\(Y=N\)，
\[
 |M|\ge c_*Y^d\ell,\qquad
 P_\beta(N)N^\delta<C_{\rm diag}|M|,\qquad c_*>0.
 \tag{2}
\]
所有常数均与尺度无关；不重新选择 cutoff。
实际 \(w_Y(x)=x^{-\sigma}e^{-x/Y}\)、连续项、正通道 \(p,c\)、
总质量 \(S\) 及 Brownian 分母 \(D\) 都保持285的定义。
写
\[
 f_\xi(x)=w_Y(x)(\cos(\xi\log x)-1),\qquad
 \widehat r(\xi)=\sum_{2\le n\le N}\Lambda(n)f_\xi(n)
                         -\int_1^N f_\xi(x)\,dx,
\]
\[
 I_\rho(\xi)=\frac1\rho\int_2^N x^\rho f_\xi'(x)\,dx.
 \tag{3}
\]
零点按实际重数计，\(-1\) 与完整整数端点没有删除。

固定 \(A>1/2\)、\(0<a<3/8\)，置
\[
 U=\sqrt L,\quad T=L^A,\quad
 \vartheta_Y=\frac12+a\frac{\log L}{L},\quad
 E=\{\xi:U<|\xi|\le T\},
\]
\[
 \boxed{\quad B_A=\frac{7+3A}{8},\qquad
           V_{\rm dens}=Y^{1/4}L^{B_A}.\quad}
 \tag{4}
\]
最终 \(V_{\rm dens}\ge2T\)，且 \(V_{\rm dens}\le Y^{5/16}\)。
定义新的有限实际带符号和
\[
 Z_{\rm dens}(\xi)=
 \sum_{\substack{\Re\rho>\vartheta_Y\\|\Im\rho|\le V_{\rm dens}}}I_\rho(\xi).
 \tag{5}
\]
对可测函数 \(\Phi\) 和可测频带 \(F\)，记
\[
 \mathfrak Q_F(\Phi)=\frac1{2\pi}\int_F\frac{|\Phi(\xi)|^4}{\xi^2}\,d\xi,
 \qquad Q_F(r)=\mathfrak Q_F(\widehat r).
 \tag{6}
\]

### 定理287-A [T/R]

沿同一实际强记录序列(2)，无条件有
\[
 \boxed{\quad
 \frac{\mathfrak Q_E(\widehat r-Z_{\rm dens})}{M^4L}
      \ll_{\sigma,\beta,A,a}\ell^{-4}=o(1).\quad}
 \tag{7}
\]
因此对任意随尺度变化的可测 \(F\subset E\)，一致有
\[
 \frac{\left|Q_F(r)^{1/4}-\mathfrak Q_F(Z_{\rm dens})^{1/4}\right|}
      {|M|L^{1/4}}
     \ll_{\sigma,\beta,A,a}\ell^{-1}=o(1).
 \tag{8}
\]
通过原实际物理方向，
\[
 \boxed{\quad
 J_{4,F}=O(\mu^4)
 \quad\Longleftrightarrow\quad
 \mathfrak Q_F(Z_{\rm dens})=O(M^4L),\qquad \mu=M/S.\quad}
 \tag{9}
\]
首带 \(A=1\) 的谱高度由285的 \(\sqrt Y\,L^{3/2}\) 降至
\[
 \boxed{\quad V_{\rm dens}=Y^{1/4}L^{5/4}.\quad}
 \tag{10}
\]
这仍远大于物理频率 \(T=L\)，没有声称已经只剩 \(|\Im\rho|\asymp L\)
的共振零点。剩余有限和仍未知，(9)不是已完成的四阶预算。

## 2. 主源版本、统一范围与所用弱化 [R/T]

使用 Chourasiya--Simonič 的正式预印本
[An explicit form of Ingham's zero density estimate，arXiv:2507.15184v2](https://arxiv.org/html/2507.15184v2)，
版本日期2025-09-30。已核对 Corollary 1 与 Table 1；不把它称作已正式发表论文。
其16个闭区间覆盖 \(b\in[1/2,1]\)，对 \(H\ge3\cdot10^{12}\)，
\[
 {\cal N}(b,H)\le
 \mathfrak B_1H^{3(1-b)/(2-b)}(\log H)^{e(b)}
       +\mathfrak B_2(\log H)^2+\mathfrak B_3\log H,
 \quad e(b)=\frac{7-5b}{2-b}\in[2,3].
 \tag{11}
\]
\({\cal N}(b,H)\) 计 \(0<\Im\rho\le H,\Re\rho\ge b\)，含重数；
表中三个常数的全局最大值分别为 \(46.06,9.461,167.8\)。
这是本篇真正调用的外部结果。1940年的经典工作只作来源背景，
不拿旧版本的对数指数替换(11)。

加大一个固定常数后，可把所需不等式统一延伸到全部 \(H\ge2\)：
有限区间 \(2\le H\le3\cdot10^{12}\) 用有限总零点数控制；
不需要把有限验证高度解释成 RH。由(11)得到两种独立可用的上界：
\[
 \boxed{\quad {\cal N}(b,H)
       \ll H^{3(1-b)}\log^3(2H).\quad}
 \tag{12}
\]
以及更贴近右端 \(b=1\) 的形式
\[
 \boxed{\quad {\cal N}(b,H)
       \ll \log^2(2H)\,[H\log(2H)]^{3(1-b)}.\quad}
 \tag{13}
\]
两式对全部 \(1/2\le b\le1,\ H\ge2\) 统一。
为核对(13)，令 \(x=1-b\in[0,1/2]\)，则
\[
 \frac{3(1-b)}{2-b}=\frac{3x}{1+x}\le3x,\qquad
 e(b)=2+\frac{3x}{1+x}\le2+3x.
 \tag{14}
\]
加性对数项由 \(\log^2(2H)\) 吸收，且括号中的幂至少为1。
(12)与(13)各有用途：后者在左端可能更粗，不能不加区分地称为处处更强。

## 3. 保留真实实部的谱尾权重 [T]

定义非负、绝对收敛的谱权重
\[
 {\cal H}(Y,V)=
 \sum_{\substack{\Re\rho\ge1/2\\|\Im\rho|>V}}
          \frac{Y^{\Re\rho-\sigma}}{|\Im\rho|^2},
 \qquad Y\ge4,\quad V\ge2.
 \tag{15}
\]
收敛先由无条件临界带及单位高度计数保证；本节不靠待证密度尾估计定义它。
负虚部由共轭对称计入，后续与 \({\cal N}\) 的比较至多多出因子2。

对 \(b=\Re\rho\in[1/2,1)\)，\(b-\sigma\in[d,1-\sigma]\)
位于固定正紧区间。282-B的证明因此给保留真实幂次的统一 BV 界
\[
 \|g_{b,j}\|_1+\operatorname{TV}(g_{b,j})
       \ll_\sigma Y^{b-\sigma},\qquad j=0,1,
 \tag{16}
\]
其中 \(g_{b,j}\) 是282-(8)的零延拓振幅，两个端点跳跃均计入。
这里没有把 \(Y^{b-\sigma}\) 先放大成 \(Y^{1-\sigma}\)。
为独立核对一致性，置 \(v=b-\sigma\in[d,1-\sigma]\)，直接写
\[
 g_{b,0}(u)=e^{vu-e^u/Y},\qquad
 g_{b,1}(u)=(\sigma+e^u/Y)g_{b,0}(u)
       \quad(\log2\le u\le\log N).
\]
由于 \(N\le2Y\)，
\(\int g_{b,0}\le(2Y)^v/v\ll_\sigma Y^v\)，
且一阶导数只产生 \(v,e^u/Y,(e^u/Y)^2\) 的有界系数。
两个振幅的内部导数积分及端点值均为 \(O_\sigma(Y^v)\)，从而得到(16)。
对零延拓作一次 BV 分部积分给
\(\left|\int g_{b,j}(u)e^{itu}\,du\right|
 \ll_\sigma Y^{b-\sigma}/(1+|t|)\)，没有随 \(b\to1\) 发散的常数。
由(3)的 \(1/\rho\)、BV Fourier 衰减及 \(|\gamma|>V\ge2T\)，
\[
 |I_\rho(\xi)|\ll_\sigma
       \frac{Y^{b-\sigma}|\xi|}{|\gamma|^2}
       \qquad(1\le|\xi|\le T,\ |\gamma|>V).
 \tag{17}
\]
因而对任何子集 \({\cal Z}\subset\{\Re\rho\ge1/2,\ |\Im\rho|>V\}\)，
\[
 \left|\sum_{\rho\in{\cal Z}}I_\rho(\xi)\right|
       \ll_\sigma |\xi|\,{\cal H}(Y,V)
       \qquad(1\le|\xi|\le T,\ V\ge2T).
 \tag{18}
\]
保留 \(|\xi|\) 后积分，得到
\[
 \frac{\mathfrak Q_E\!\left(\sum_{\rho\in{\cal Z}}I_\rho\right)}{M^4L}
       \ll_{\sigma,\beta}\frac{T^3}{\ell^4L}
           \left(\frac{{\cal H}(Y,V)}{Y^d}\right)^4.
 \tag{19}
\]
这里仅用了 \(\int_U^T t^2dt\le T^3/3\) 及同一质量下界(2)。
这解释为何需要实际实部加权的尾，而不是只数尾部有多少个零点。

## 4. Layer cake 与全部 dyadic 高度的通用尾界 [T/R]

### 引理287-B

只使用较弱密度式(12)，对全部 \(Y\ge4,V\ge2\)，有
\[
 \frac{{\cal H}(Y,V)}{Y^d}
 \ll (1+L)\log^3(2V)
          \left(\frac{\sqrt Y}{V^2}+V^{-1/2}\right).
 \tag{20}
\]
特别，这不是仅在固定幂次 \(G=Y^v\) 上成立的单块估计。

证明。把 \(|\gamma|>V\) 精确分为
\((G,2G]\)，其中 \(G=2^jV,\ j\ge0\)。
记该块满足 \(\Re\rho\ge b\) 的零点数为 \({\cal N}_G(b)\)。
则由(12)
\[
 {\cal N}_G(b)\le2{\cal N}(b,2G)
       \ll G^{3(1-b)}\log^3(2G).
 \tag{21}
\]
对一个实部 \(b_\rho\ge1/2\)，有精确分层恒等式
\[
 Y^{b_\rho-\sigma}
 =Y^d+L\int_{1/2}^{b_\rho}Y^{b-\sigma}\,db.
\]
因此该块的权重 \({\cal H}_G\) 满足
\[
 {\cal H}_G\le G^{-2}
 \left\{Y^d{\cal N}_G(1/2)
       +L\int_{1/2}^1Y^{b-\sigma}{\cal N}_G(b)\,db\right\}.
 \tag{22}
\]
端点 \(b=1/2\) 的零点由第一项完整计入。
令 \(u=b-1/2\)，代入(21)，得
\[
 \frac{{\cal H}_G}{Y^d}
 \ll \log^3(2G)G^{-1/2}
       \left\{1+L\int_0^{1/2}e^{u(L-3\log G)}\,du\right\}.
 \tag{23}
\]
指数关于 \(u\) 线性，所以积分至多为两个端点值最大值的一半。于是
\[
 \frac{{\cal H}_G}{Y^d}
 \ll (1+L)\log^3(2G)
             \left(G^{-1/2}+\frac{\sqrt Y}{G^2}\right).
 \tag{24}
\]
此式包括 \(G=Y^{1/3}\)，没有除以可能为零的 \(L-3\log G\)。

对固定 \(r>0\) 及 \(k=2,3\)，还直接有
\[
 \sum_{j\ge0}
 \frac{\log^k(2^{j+1}V)}{(2^jV)^r}
 \ll_{r,k}\frac{\log^k(2V)}{V^r}.
 \tag{25}
\]
因为 \(\log(2^{j+1}V)\le(1+j)\log(2V)\)，
剩下 \(\sum_{j\ge0}(1+j)^k2^{-rj}<\infty\)。
把(24)对所有块求和，用 \(r=1/2,2\) 的(25)，即得(20)。
正项分层与求和可以用 Tonelli；没有在某个高度之后丢弃未估尾部。\(\square\)

仅凭这个较弱版本，取 \(V=Y^{1/4+\varepsilon}\)、\(0<\varepsilon<1/12\)，
就有 \({\cal H}/Y^d\ll_\varepsilon Y^{-2\varepsilon}L^4\)，
从而物理多对数带的误差得到幂次节省。下面进一步保留对数精度。

## 5. 双高度区间：去掉一个 \(L\)，再保留右端对数指数 [T/R]

置
\[
 X=Y^{5/16},\qquad 2\le V\le X .
 \tag{26}
\]
仍按块的下端 \(G=2^jV\) 分成 \(G\le X\) 和 \(G>X\) 两类；
若某一块跨过 \(X\)，它照其下端归类，证明中的密度上界一直使用 \(2G\)，
没有截去该块的一部分。

### 5.1 仅用(12)也能消去分层带来的 \(L\)

若 \(G\le X\)，则
\[
 L-3\log G\ge L/16>0,\qquad
 L\int_0^{1/2}e^{u(L-3\log G)}\,du
       \le16 e^{(L-3\log G)/2}.
 \tag{27}
\]
且 \(G^{-1/2}\le\sqrt Y/G^2\)，因为 \(G\le X<Y^{1/3}\)。
所以(23)给每个低块
\[
 {\cal H}_G/Y^d\ll\sqrt Y\,\log^3(2G)/G^2.
 \tag{28}
\]
由(25)，全部低块之和至多 \(C\sqrt Y\log^3(2V)/V^2\)。

对高块 \(G>X\) 使用(24)。第一高块的下端在 \((X,2X]\)；
再用(25)求所有高块，得到
\[
 \sum_{G>X}{\cal H}_G/Y^d
 \ll (1+L)\log^3(2X)
          \left(\frac{\sqrt Y}{X^2}+X^{-1/2}\right)
 \ll Y^{-1/8}L^4.
 \tag{29}
\]
最后两个幂分别是 \(Y^{-1/8}\) 和 \(Y^{-5/32}\)。
故仅使用统一 \(\log^3\) 版本也已有
\[
 {\cal H}(Y,V)/Y^d
 \ll \frac{\sqrt Y\,\log^3(2V)}{V^2}+Y^{-1/8}L^4.
 \tag{30}
\]
这一步明确包括 \(G\ge Y^{1/3}\) 及任意更高的高度，不在那里换回不够用的粗界。

### 5.2 利用v2的右端对数指数：主估计

现在低块使用(13)。写 \(L_G=\log(2G)\)，把 \(2G\) 与 \(G\) 的固定因子
统一吸收，则
\[
 {\cal N}_G(b)\ll L_G^2(GL_G)^{3(1-b)}.
 \tag{31}
\]
代回同一个精确分层式(22)，令 \(u=b-1/2\)，得到
\[
 \frac{{\cal H}_G}{Y^d}
 \ll L_G^{7/2}G^{-1/2}
       \left\{1+L\int_0^{1/2}e^{uD_G}\,du\right\},
 \quad D_G=L-3\log G-3\log L_G.
 \tag{32}
\]
对于 \(G\le X\)，一致有
\[
 D_G\ge L/16-3\log(\log(2X))\ge L/32>0
 \tag{33}
\]
在充分大 \(Y\) 时成立。因此积分项至多 \(32e^{D_G/2}\)，常数项也不大于
这个量级。关键的端点计算为
\[
 L_G^{7/2}G^{-1/2}e^{D_G/2}
       =\frac{\sqrt Y\,L_G^2}{G^2}.
 \tag{34}
\]
故每个低块的上界进一步变为 \(C\sqrt Y\log^2(2G)/G^2\)。
对这些块用(25)的 \(k=2\) 版本求和；高块仍用已经证明的(29)。
由此得到主谱尾引理
\[
 \boxed{\quad
 \frac{{\cal H}(Y,V)}{Y^d}
 \ll \frac{\sqrt Y\,\log^2(2V)}{V^2}
                +Y^{-1/8}L^4,\qquad 2\le V\le Y^{5/16}.
 \quad}
 \tag{35}
\]
这一步没有在左端错误地把 \(\log^{7/2}\) 当作 \(\log^3\)；
(32)中先完整保留它，再由右端积分产生的 \(L_G^{-3/2}\) 精确消去。
高区不使用(31)，因此没有额外对数损失被隐藏在无限尾中。

## 6. 新高度、四阶误差与285的接口 [T/R]

先令 \(V=Y^{1/4}L^B\)，其中 \(B\) 固定。
最终 \(2T\le V\le Y^{5/16}\)、\(\log(2V)\asymp_B L\)，故(35)给
\[
 {\cal H}(Y,V)/Y^d
       \ll_B L^{2-2B}+Y^{-1/8}L^4.
 \tag{36}
\]
对实际深右高尾
\[
 Z_{\rm hi}^{(V)}(\xi)
   =\sum_{\substack{\Re\rho>\vartheta_Y\\|\Im\rho|>V}}I_\rho(\xi),
 \tag{37}
\]
应用(19)及 \((x+y)^4\le8(x^4+y^4)\)，得到完整账本
\[
 \frac{\mathfrak Q_E(Z_{\rm hi}^{(V)})}{M^4L}
 \ll_{\sigma,\beta,A,B}
       \frac{L^{7+3A-8B}+Y^{-1/2}L^{15+3A}}{\ell^4}.
 \tag{38}
\]
主项来自 \(4(2-2B)+3A-1=7+3A-8B\)。
取 \(B=B_A=(7+3A)/8\) 正好令此幂次为零，故
\[
 \mathfrak Q_E(Z_{\rm hi}^{(V_{\rm dens})})/(M^4L)
           \ll_{\sigma,\beta,A}\ell^{-4}.
 \tag{39}
\]

为保留较弱输入下的可审计备份，三个版本分别给：

| 所用已证谱尾界 | 足够的 \(B\)，使 \(V=Y^{1/4}L^B\) | 首带 \(A=1\) |
|---|---:|---:|
| 全高度粗界(20)，只用(12) | \((15+3A)/8\) | \(9/4\) |
| 双区去 \(L\) 的(30)，只用(12) | \((11+3A)/8\) | \(7/4\) |
| v2右端对数精度的(35) | \((7+3A)/8\) | \(5/4\) |

三行都独立足够得到 \(O(\ell^{-4})\) 高尾误差；主定理使用最后一行。
没有把最后一行的改善追溯到v1或未核验的经典对数指数。

剩余拼接严格沿285的已审精确恒等式
\[
 \widehat r=E_N+B_{Y,N}
       +\sum_{\Re\rho\le\vartheta_Y}I_\rho
       +Z_{\rm dens}+Z_{\rm hi}^{(V_{\rm dens})}.
 \tag{40}
\]
其中 \(E_N=f_\xi(N)R(N)\) 是完整右连续端点；
\(B_{Y,N}\) 是285-(13)列出的固定早段、常数及平凡零点项。
无限和由282/285的积分后绝对收敛定义，因而可以使用(40)的分组；
不是拿有限高度显式公式丢掉端点误差。

285已经独立证明
\[
 \frac{\mathfrak Q_{|\xi|\ge U}
       (\sum_{\Re\rho\le\vartheta_Y}I_\rho)}{M^4L}
 \ll \frac{L^{4a-3/2}(\log L)^8}{\ell^4},
 \qquad
 \frac{\mathfrak Q_{|\xi|\ge U}(E_N+B_{Y,N})}{M^4L}
 \ll L^{-3/2}.
 \tag{41}
\]
本篇不改变这些证明，也不把浅层零点限制成有限集合。
把(39)、(41)代回(40)，四次幂三角式给
\[
 \frac{\mathfrak Q_E(\widehat r-Z_{\rm dens})}{M^4L}
 \ll
 \frac{1+Y^{-1/2}L^{15+3A}+L^{4a-3/2}(\log L)^8}{\ell^4}
       +L^{-3/2}
 \ll \ell^{-4}.
 \tag{42}
\]
这证明(7)。加权 \(L^4\) 的反向三角不等式给(8)，而不是两个未知能量
之间的加性 \(o(M^4L)\) 差。

在 \(F\subset E\) 上，277的实际通道比较给
\[
 |\widehat p|^2+|\widehat c|^2\asymp_\sigma S^2,
 \qquad D\asymp_\sigma S^2L.
 \tag{43}
\]
所以 \(J_{4,F}/\mu^4\asymp Q_F(r)/(M^4L)\)，结合(8)得到(9)。
若定义谱辅助响应，只允许将原积分中的 \(\widehat r\) 换成 \(Z_{\rm dens}\)；
\(p,c,S,D\) 仍是原实际源，而不是另造一个正配置。

同样，若
\[
 K=\lfloor N/L^h\rfloor,\qquad h>(2A-1)/(4\delta),
 \tag{44}
\]
可重用279已审有限前缀证明，误差根界为
\(O(L^{-h\delta+(2A-1)/4})=o(1)\)。
因此(9)也等价于共同半开截断下的实际晚段预算。
这里 \(K\) 原子只归早段，lag 不平移；(3)的零点积分仍为 \(\int_2^N\)，
不能仅因比较对象变成晚段而未经端点核查地换成 \(\int_K^N\)。

## 7. 计数包络的边界与下一最小输入

### 7.1 统一多重集合类的一条边界 [N]

下面只说明“计数包络 + 最低质量尺度”对绝对谱尾的限制，不是实际 zeta
下界，不是单个固定亚纯函数的反例，也不证明外部密度定理达到最优。

固定 \(0<v<1/4\)。对每个充分大 \(Y\)，令
\[
 G=2Y^v,\qquad b=1-\frac1{\log G},\qquad
 {\cal Z}_Y=\{b+iG,b-iG,1-b+iG,1-b-iG\}.
 \tag{45}
\]
四元多重集合有共轭及临界线反射对称，单位高度计数有统一常数。
对 \(t\in[1/2,1]\)，其正虚部累计计数至多1（用2也足够）；
在 \(H<G\) 时为零，在 \(H\ge G\) 时，被(12)、(13)的同一个固定常数上界覆盖。
因此这些包络和对称性本身不排除该族。

其右半绝对谱尾满足
\[
 \frac1{Y^d}
 \sum_{\substack{\rho\in{\cal Z}_Y\\\Re\rho\ge1/2\\|\Im\rho|>Y^v}}
        \frac{Y^{\Re\rho-\sigma}}{|\Im\rho|^2}
 =\frac12Y^{1/2-2v}\exp\!\left(-\frac{L}{\log G}\right)
       \longrightarrow\infty.
 \tag{46}
\]
因为 \(L/\log G\to1/v\)，正幂次支配该固定正因子；
即使再除以 \(\ell(Y)\)，仍然趋于无穷。
所以在此统一多重集合类内，不能仅凭上述计数/对称性就把
\(|\gamma|>Y^v\) 的绝对权重压到 \(o(Y^d\ell)\)。
该族依赖 \(Y\)，没有被冒充为实际 zeta 的固定零点集合；
它也未加入实际 zeta 的全部额外性质，特别没有加入独立零自由区域。
从(46)不能推出实际带符号四阶响应的下界。

### 7.2 首带剩余输入 [O]

本篇的新最小目标可固定 \(A=1\)：
\[
 \boxed{\quad
 \frac1{2\pi}\int_{\sqrt L<|\xi|\le L}
 \left|
 \sum_{\substack{\Re\rho>1/2+a\log L/L\\
                 |\Im\rho|\le Y^{1/4}L^{5/4}}}
       \frac1\rho\int_2^N x^\rho
          \frac{d}{dx}\{w_Y(x)(\cos(\xi\log x)-1)\}\,dx
 \right|^4\frac{d\xi}{\xi^2}
       \ll_{\sigma,\beta,a}M^4L .
 \quad}
 \tag{47}
\]
这是仍未证明的实际有限带符号预算。首带晚段接口的一般条件是
\(h>1/(4\delta)\)；\(\sigma=1/4,\beta=3/8\) 时才成为 \(h>2\)。
即使(47)完成，也只解决整个增长中频的第一子区间。

新密度输入确实控制了高谱尾，但没有自动删除低虚部零点及
\(2L<|\gamma|\le Y^{1/4}L^{5/4}\) 的非共振部分。
例如直接以(20)取 \(V=2L\)，上界仍含 \(\sqrt Y/L^2\)；
不能把该不够用的上界称为物理共振局部化。
历史 guard 控制真实时间路径，并未在本篇中被证明控制各谱模式的绝对加权和。
后续若用相位相消、更精确密度或真实质量联用，须再给独立估计。

RH使(47)的集合为空，但本篇不证明(47)与RH等价，也不证明其严格弱于RH。
存在深右零点同样不自动使(47)失败；286已经提示实际质量归一化和带符号相位
必须保留。绝不能把单项中的 \(Y^{\Re\rho-\sigma}\) 无理由换成 \(Y^d\)。

## 8. 依赖与审计状态

- 外部算术输入固定为上述v2 Corollary 1/Table 1 的统一密度定理 [R]；
  不把正式预印本当作外部同行审计已经完成。
- (22)--(35)给独立的实部分层与全高度求和；临界高度及其后的无限尾均已处理。
- 285的浅层、端点误差与原物理通道保持原证明和同一序列，不重新假设完整正性。
- 本篇只优化了已明确需要的实际深右谱尾，没有得到新的零密度纪录或零自由区域。
- 一般 L 函数、函数域与上同调配置不在本篇自动适用范围内。
- 本篇未以有限零点实验作证；主代理和独立代理已全文逆向审计通过，
  并各自核对外部v2的范围、指数和表格常数。
  审计特别检查了 \(b\ge1/2\) 的BV一致性、\(1\le|\xi|\le T\)、
  跨越 \(X\) 的dyadic块、无限高尾、三种对数账本和原通道四次方根转移。
  内部证明不等于文献新颖性、完整中频预算或整个研究 Goal 的阶段验收。
