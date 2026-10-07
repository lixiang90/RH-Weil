# Type-I canonical 准入、低 Lambda full-compression 与 affine fibers 全文审查

2026-10-07。审查人 twisted_research。**限定 PASS（授权修订后的版本）。**
全文核对本轮 Type-I 报告§1–12及238–240物理定义，特别重新推导§7的四范数尺度、
§9的完整 affine fibers 与正规化。原报告 contour bound 的新颖性比较已修正，
K参数已准确化；未改旧notes、math或已提交论文。

本结论仅认证下述有限数学范围：相对于明确[R]的 canonical 前缀/生成函数准入；
无条件的短 Lambda 多项式实际压缩付款；合法 coprime ghost mask 下的有限比值
基线与 affine 映射。没有认证完整 signed fourth trace、相关猜想、零点比例、
外部[R]证明链、Lean、RH或global all-cells closure。

## 1. 最终版本与来源绑定

canonical LF SHA256均按CRLF及单独CR转LF、UTF-8无BOM计算；PDF为原始字节哈希。

| 对象 | SHA256 |
|---|---|
| `hybrid-response-type-i-admission-and-type-ii-gap.md`，授权修订后 | `6d3eedd9607fd797989731eacbcc2f76c3e6c6da6ade88bfc6798ca2e456d251` |
| `hybrid-finite-ratio-gram-baseline.md`，本轮独立推导 | `cf0c8ade19ef0a6aec04f663a57319d2e2f0ba26cde765a7024584ce79d7008a` |
| 238 | `d46a8fca611f24ba3c647cfc9b2db6240d1a2a2d0372242b7b51d745bd22c82d` |
| 239 | `b35398ecdfbe65ce2ea04856a5e66f6676d61cc109b3de48e855b514db0cfa20` |
| 240 | `1867e490fed07598e4f6c44952352d2c3a7a0dc4b066b6c1720e8a96d3a0ed8a` |
| 本地AF v2 PDF | `6de3b156342e7b4a802c34f8ef40432567e9dabe006938da04233f19fc4ef444` |
| 已提交69999正式论文 | `92ba93da7cc568579b0b982bcd712e1382af749d05460c1fa4c8b25064df66d6` |
| 447（另一个条件边界，未并入69999论文） | `35d0f11bd822bdf7862dc821f2b02628b3a41778ff9633cb27a9bcbf5d3431b1` |

原 Type-I 报告审查前哈希为
`9df1916312562d6bfcacc62166ebeae1cb8b26853bfe72d7e098904aa7a5abc2`。
根代理明确授权修订尚未提交的新报告；本轮仅改成果比较、补有限Schur基线及
核参数/floor-round范围，没有重写其canonical证明。

外部source是OpenAI/math固定提交`adc7f1241b42e322a6451854ab7e4b4c146bf78a`的
`E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex`，
canonical LF SHA256为
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`。
本轮重读1531–1620的logarithmic control/deleted Euler前件。

原AF固定版本为 [Alpöge–Furman v2](https://arxiv.org/html/2608.13637v2)，
本地文件`literature/baseline/2026-alpoge-furman-6725-v2.pdf`。
在线核对§2.1–2.3的原窗、Fourier、grid、a_L、有限矩阵及Poisson恒等式；
§7.2仅用于界定高矩的公开方法范围，不作为新相关估计输入。

## 2. 238–240、same mask与实际six-window

216-(8)有P_(a,b)(u)=phi(u)phi(u-log(a/b))phi(log a-u)^2。
238的u=z+log(a/b)准确给

\[
 F_{a,b}(z)=\phi(z+\log(a/b))\phi(z)\phi(\log b-z)^2.
 \tag{1}
\]

所以 Type-I 报告(1)的右端log b准确，六窗重叠及原平方根系数
Lambda(a)Lambda(b)/(4pi²sqrt(ab))均保留。mask取1_(a,b)=1并乘预先固定的
factor/aperture interval cuts，在原不同prime-base support上准确等于physical mask。
它是238允许的一种明确off-support extension，不能推广到任意channel依赖mask。

固定b时a-cut有固定有限数目边界，(1)只在第一个phi上对log a微分，Hilbert-valued
BV成本统一。因此canonical a-prefix与实际feature的Abel步骤合法。
χ_b(a)=1_(a,b)=1是完全乘性的natural zero extension；它绝非smooth profile。

238-(40)和(42)给精确S_Lambda=S_I+S_II及同atom matrix A_rs。
239共同linear shell centering与此physical quotient交换，240的
T*B_cent T仍只是原response的pullback。这些定义没有因出现mu而产生独立saving。

**核与维数修正：** 原238的K_(Q,D)(t)在本尺度应Q=XL，故精确物理核是

\[
 K_{XL,D}\!\left(X\log\frac{ad}{bc}\right)
 =\frac1D\sum_{k=0}^{D-1}\cos\left[
  \left(2\pi X+\frac{2\pi k}{L}\right)\log\frac{ad}{bc}\right].
 \tag{2}
\]

原新报告§9曾写未定义K_(X,D)，若按238字面解释会漏L；已修正。
238的round(XL)与AF实际d=floor(XL)不是相同exact kernel，但所有本轮估计对
所选整数D=XL+O(1)的各自精确核逐式成立。低Lambda压缩使用AF自己的真实d。

## 3. §3–6 canonical J与ghost费用

J=mu_(<=U)*1*Lambda_(>V)，high cell中I=J，II=Lambda-J。
自然χ_b的完全乘性给真实Dirichlet series

\[
 \mathcal J_b=M_{U,b}L_b(D_b-D_{<=V,b}),\qquad D_b=-L_b'/L_b.
 \tag{3}
\]

U=V=Y^(1/4)不是square-root空分解。若a=pq，p,q>max(U,V)而约Y^(1/2)，
则J(a)=log p+log q，Lambda(a)=0，II(a)=-log(pq)；只要此合法ghost pair位于
选定cell即可实际非零。不能单凭UV<Y声称每个任意空mask内必有非零通道。

固定theta<sigma_0<sigma<1，gap、q/U/V的固定多项式范围先定，conductor记全
primitive及deleted rad(b)。shifted mu Perron直接针对mu(n)χ(n)n^(-it)，然后只对
实权n^(-sigma)作Abel，因此没有隐藏|t|导数；sigma>sigma_0保证M_U边界对U统一。
同一shifted Lambda Perron和实权Abel保留
V^(1-sigma-it)/(1-sigma-it)峰，误差积分由固定gap对V统一。它不能全换成
high-height subpower。

L_bD_b=-L_b'使(3)在L零点可去，但[R]用于其强边界，不能从可去性自动取得强界。
fixed high tau~X下，真实卷积峰需
integral dt/((1+|t|)(1+|t-tau|))<<log H/X付款，报告(11)正确。

principal double pole的A_b、B_b及(13)留数亦正确：-L_b'无simple pole，
剩余B_b=r_b(M_U'(1)-M_U(1)D_(<=V)(1))；没有删除ghost peak。
半整数sharp Perron、divisor majorant和fixed polynomial H的量词次序已明确。
Hilbert BV付款后，仅以denominator绝对sum Lambda(b)/sqrt b<<sqrt Y求和。
所以(15)(16)是合法但弱的conditional contour bound；不能再把其b-dependent
a-error作为b的canonical固定系数序列。

## 4. §7低Lambda full-compression：重新推导尺度

令Q_Z(t)=sum_(n<=Z) Lambda(n)n^(-1/2+it)，0<Z<=X^(1/2)。Q_Z²的系数c_m
保留sharp截断，m<=Z²。不同prime bases只有两排列；同一prime上的碰撞与对角
修正的总绝对费用被sum_p(log p)^4 sum_(r>=2)(r-1)^2 p^(-r)<infty控制。因此

\[
 \sum_m|c_m|^2=2\left(\sum_{n\le Z}\frac{\Lambda(n)^2}{n}\right)^2+O(1)
 \ll\log^4(2Z).
 \tag{4}
\]

原 [Montgomery–Vaughan Hilbert inequality，Corollary 3](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)
允许任意有限coefficients；对height interval J的平移仅把c_m乘unit phase。
使用其length Z²的普通Dirichlet polynomial均值，准确给
integral_J|Q_Z|^4<<(X+Z²)log^4(2Z)。不需把sharp prefix改成smooth，也不声称长
four-prime response可由该均值闭合。这里没有截去MV中的off-diagonal费用Z²。

AF原Fourier约定为hat f(t)=integral f(u)e^(-iut)du，真实a_L=||phi||²/L，
0<a_L~1，alpha_k=T+2pi k/L，d=floor(TL/(2pi))~N~XL。
令U_Fz=sum z_k hat phi(t-alpha_k)，F=U_F/sqrt(2pi L)。原support和grid的
Plancherel给F*F<=1，原Poisson恒等式给sum_(k in Z)|f_k(t)|²=a_LL²。

M=-pi^(-1)Re Q_Z为真实bounded Hermitian multiplier。对F*MF的每个单位
eigenvector，把缺失质量1-||Fv||²放在0，标量x^4的Jensen给
Tr(F*MF)^4<=Tr(F*M^4F)。不调用错误的operator-convex x^4。
P_(<=Z)=(2pi/(a_LL))F*MF。令mathcal B_J与mathcal B_(Jc)为该Jensen正积分
在J和Jc的两项，故Tr P_(<=Z)^4<=mathcal B_J+mathcal B_(Jc)，J内有准确尺度

\[
 \mathcal B_J
 \le\frac{8}{\pi a_L^3L^3}\int_J|Q_Z(t)|^4dt
 \ll N\left(\frac{\log(2Z)}L\right)^4(1+Z^2/X).
 \tag{5}
\]

这里只将Jensen所得正积分分为J/Jc，并非任意矩阵加法的四次迹可逐块无cross-term拆分。

取J=[T/2,3T]，T=2pi X。J外仍保留tau~0的峰；C²原窗尾给
sum_k integral_(Jc)|f_k|²<<dX^(-3)，全高度|Q_Z|<<sqrt Z。
乘原正规化(2pi/(a_LL))^4/(2pi L)，准确得到

\[
 \operatorname{Tr}P_{<=Z}^4
 \ll N\left(\frac{\log(2Z)}L\right)^4(1+Z^2/X)
      +\frac{Z^2}{X^2L^4}.
 \tag{6}
\]

因此原报告(20)没有漏L或N；例如Z=exp(sqrt L)时右边o(N)，
||P_(<=Z)||_4=o(N^(1/4))。要稳定转移完整response第四迹，必须另外已有
||H_>||_4=O(N^(1/4))。非交换telescoping及Schatten Hölder才给o(N)差。
原(21)准确保留此未支付前件，不能从二矩或Type-I弱幂界推它。

## 5. §8合法factor与§9 affine fibers

AP角色展开的ell1费用为1，principal main需除phi(q)；unit-group additive phase
由有限群Parseval有ell1<=sqrt(phi(q))，非unit项另付。原表保留这些费用正确。
moving natural mask必须记完整q_eff；全q一致不等于跨q或跨b的dispersion。

对mask内(a,b)=1及h=ad-bc，整数解准确为

\[
 d=d_0+b\ell,\qquad c=c_0+a\ell,\qquad ad_0-bc_0=h.
 \tag{7}
\]

因为h整数且gcd(a,b)=1，存在d_0,c_0；一般解(7)无遗漏。c,d~Y且a,b~Y使
每个固定h的允许ell区间长度O(1)，但h并不限于core。原off-diagonal fiber为

\[
 \sum_{\ell}\Lambda(d_0+b\ell)\Lambda(c_0+a\ell)
 \mathcal W_{a,b,h}(\ell)
 K_{XL,D}\left(X\log\frac{a(d_0+b\ell)}{b(c_0+a\ell)}\right).
 \tag{8}
\]

报告mathcal W明确包含(4pi²)^(-2)(abcd)^(-1/2)、fixed masks与原six-window。
外层Lambda(a)Lambda(b)或Vaughan替换系数仍按原原子式保留，不能把其中另一
Lambda因子当成canonical定理允许的任意测试系数。

h=0时，**两对均coprime**强制(c,d)=(a,b)，恰为238同atom reference。若取消
第二对coprime，这个断言会失败；当前mask前件足够。对J/II ghost atoms也同理。
core尺度|h|~Y²/X=X^(1/2)来自log-resolution；全部tail和carrier留在(8)。
239共同centering仍在physical quotient后施加，没有偷偷改成逐fiber绝对预算。

原报告§10的N_v^(1-theta)>X，是该单factor移线bound要有power-small
relative error的门槛，绝非所有可能方法的no-go。实际N_v<=Y，core width
N_v/X甚至<1，因此不能用连续PNT main替代整数fiber。

## 6. 成果比较修正与I–II有限升级

审查发现原(16)只相对最粗l1²预算改善3/16。同一固定coprime balanced cell
已有更强无条件基线：不同log ratios间距>=1/(C²Y²)，其跨度O(1)<L/2；
原有限几何核<=min(1,C/(X|Delta s|))。排序、harmonic sum及feature Cauchy
给G_rr<<(1+(Y²/X)log Y)A_rr。J与II divisor majorant给A_rr<<X^eps，故

\[
 |G_{rs}|+|G_{rs}-A_{rs}|\ll_\epsilon X^{1/2+\epsilon},\quad
 r,s\in\{I,II,\Lambda\}.
 \tag{9}
\]

已独立写出逐式推导，根代理另核spacing、carrier、mask及feature范围；此处不把
自己新写的baseline宣称为另外一位作者的独立证明。原Type-I报告按授权补入(16a)，
明确弱contour界不是最佳Gram预算或新的国际算术saving。

在相同mask/BV下，可以对full canonical Lambda numerator独立作其simple-pole
Perron估计，再用精确S_II=S_Lambda-S_I。全导子theta输入因此给

\[
 |G_{I,II}|+G_{II,II}\ll_\epsilon X^{3\theta/2+\epsilon}.
 \tag{10}
\]

每个a-sum分别完成canonical估计后，均只对b付绝对和；没有同一b-dependent error
的第二次相消。使用69999论文明确[R]时指数209997/160000；另引用447自己的[R]
及条件continuation时为21/16-3t_c/8。这些都弱于(9)，仍不能得raw o(L^4)。
本比较不说明strip对任何联合相关估计都无作用；它只定位这一个合法但粗接口。

fixed-cell范围必须保留：删coprime需先合并重复ratios；跨cells的log-ratio跨度可
达到L，原grid会有alias，不能把(9)直接推广global；共同shell-centering的额外
mass项亦不能不付账本便加进(9)。没有为joint fiber中的两个prime forms证明渐近。

## 7. 可晋级到448的准确内容

可以保存为新note的有限结果是：canonical J的natural-mask真实准入和ghost
double-pole/height峰费用；经典短Lambda多项式进入AF实际finite compression的
o(N)四范数付款；同固定cell的有限比值基线；以及上述条件mixed延拓的准确范围。
短Lambda部分无条件，但完整第四迹稳定仍依赖H_>四范数前件。canonical部分明确
依赖全导子无零与uniform reciprocal/logarithmic control [R]。

不能晋级：新的简单临界线比例、完整四矩常数、全部mixed/cells闭合、原source[R]
整链正确性、Lean认证或RH。无条件(9)及条件(10)都远大于所需raw o(L^4)。
下一算术缺口仍是原physical vector与共同centering后的跨label signed correlation，
而不是把已付款的弱幂界分别相加。

本轮已完成授权审查与有限推导，停止扩展；不编辑README、旧论文/notes/math或Git。
