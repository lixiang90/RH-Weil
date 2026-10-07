# 448 规范准入、局部Gram与低素数压缩独立审查

2026-10-07。审查人 twisted_research。**限定 PASS。** 本轮直接阅读全文，核对
两个物理对象各自的floor维数、窗、mask、finite k、平方根系数和正规化。
没有仅沿用旧报告摘要。canonical准入依赖明确[R]；局部finite Schur及低Lambda
full-compression付款无条件。它们不构成完整四矩、零点比例或RH证明。

审查对象：`notes/448-canonical-type-i-admission-finite-gram-and-low-prime-fourth-norm.md`。
canonical LF SHA256（CRLF和单独CR换为LF后UTF-8）：

`6a7219f929cc50a721227c722fd9553eb7eba1ed9d4dd432bd971b39c2e6eafa`。

已复核最终措辞：gap常数、每侧第j个近邻和a_L的固定正上下界均准确化；
这三项不改变正文公式或下述限定PASS结论。

## 1. 输入、版本与链接

外部原source固定提交`adc7f1241b42e322a6451854ab7e4b4c146bf78a`，September-30
`paper.tex` canonical LF SHA256为
`42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3`，与正文及
本地源匹配。原1531–1620的logarithmic-control/deleted Euler范围已重读。

AF v2本地PDF字节SHA256：
`6de3b156342e7b4a802c34f8ef40432567e9dabe006938da04233f19fc4ef444`。
在线原文[AF v2 §2](https://arxiv.org/html/2608.13637v2#S2)用于核准Fourier约定、
原taper、alpha_k、d、a_L及Poisson恒等式。
[Montgomery–Vaughan Corollary 3](https://personal.science.psu.edu/rcv4/personal/Publications/s2-8-1-73.pdf)
仅用来支付短Dirichlet polynomial的普通均值，不被当成signed四点相关渐近。

本文引用的三个新报告最终canonical LF版本均匹配其正式全文审查中的绑定：

| 文件 | SHA256 |
|---|---|
| `hybrid-response-type-i-admission-and-type-ii-gap.md` | `6d3eedd9607fd797989731eacbcc2f76c3e6c6da6ade88bfc6798ca2e456d251` |
| `hybrid-finite-ratio-gram-baseline.md` | `cf0c8ade19ef0a6aec04f663a57319d2e2f0ba26cde765a7024584ce79d7008a` |
| `type-i-and-low-lambda-full-response-review.md` | `0714ce3c96a2dd6ea8e2d1b185e1b2dec2ba107d9f00c181783be2ee6df86278` |

正文六个本地链接（446两次、241及三个报告）均解析到现有文件。
原238–240哈希已在上述报告逐稿绑定。没有认证外部[R]整条证明链或Lean构建。

## 2. §1–3：两个物理对象、theta范围与canonical准入

正文准确区分fixed balanced ratio synthesis与AF整个height-axis finite compression。
其原AF维数D=floor(XL)且T=2pi X，tau_k=T+2pi k/L全部在[T,2T)内。
round与floor各有自己的exact kernel；正文没有把两者当成同一有限恒等式。
K_(XL,D)(Xv)的首参数和carrier正确，未漏L、改sinc或删除背景。

216/238变量代换u=z+log(a/b)给F_(a,b)的第三窗恰为phi(log b-z)^2。
同一coprime off-support mask先于channels固定；fixed-b有限interval cuts及
Hilbert BV仅是canonical步骤的前件，Schur步骤不多加该前件。high cell中I=J；
正文给pq ghost例且明确不保证空mask非零，非vacuous说明准确。

theta须在(1/2,1)：可以固定theta<sigma_0<sigma<1，且sharp Perron左线
sigma-1/2>0，不跨s=0；原高度分母可统一写1+|t|，常数依赖这些固定gaps。
全primitive family、punctured presentation、q_eff及多项式范围都保留。没有把
canonical coefficients扩大成任意divisor列或response权重。

完全乘性的chi_b给(4)真实truncated convolution。shifted mu/Lambda Perron后只对
实权作Abel，mu边界对U统一；Lambda的V^(1-sigma)/(1+|t|)峰仍在(6)(7)。
poly-height order先固定，再缩小analytic conductor/height小幂，原报告的合同足以
支付horizontal joins及sharp endpoint，未出现同一error的二次相消。

principal处L_bD_b=-L_b'确实没有simple-pole项；(10)double-pole留数的
A_b=r_bM_U(1)及B_b=r_b(M_U'(1)-M_U(1)D_(<=V)(1))准确，无额外Laurent常数。
若半整数主项改回原实x，导数为x^(-1/2+i tau)(A_b log x+B_b)，费用
O(Y^(-1/2)log^C X)已小于(9)误差。full Lambda的D_b仅simple pole、留数1，
前缀主项亦准确；删除Euler factors不改变该留数。

Hilbert BV之后对b只付绝对sum Lambda(b)/sqrt b<<sqrt Y，先分别完成
S_I和S_Lambda的canonical a-sums，再用精确S_II=S_Lambda-S_I。
所以(14)对所有r,s成立；对任意epsilon先选足够小fixed gap并重新命名小幂。
没有把b-dependent a-error再次套b的canonical相消。theta=69999/80000时
3theta/2=209997/160000，与正文数字吻合；该依赖范围仍是明确[R]。

## 3. §4：(18)有限Schur范围与费用

两侧coprime使(a,b)->a/b单射；不同atoms的非零整数ad-bc给
|Delta s|>=1/(C²Y²)。fixed balanced cell使log-ratio跨度O(1)<L/2，故
所选floor有限几何级数准确受min(1,C/(X|Delta s|))控制。carrier模为1，
cosine取实部不会增大上界。

按两侧排序，harmonic row sum至多O(1+(Y²/X)log Y)。feature Cauchy加
2v_i v_j<=v_i²+v_j²给G_rr<=B A_rr；没有假设features正交或舍去ghost。
J和II的divisor majorant给A_rr<<X^epsilon，H^D与同atom空间的两个Cauchy
遂给(18)。Y=X^(3/4)产生X^(1/2+epsilon)，epsilon的重新命名合法。

这是比(14)强的无条件粗界，正文正确修正了成果定位。范围仅fixed cell；
重复ratios须先合并，cross-cell alias及共同shell centering的额外mass项未自动
覆盖。正文明确没有用这些粗界闭合raw o(L^4)，也没有把充分Bessel界当成必要条件。

## 4. §5：(19)碰撞项、(22)所有L/N与tail

Q_Z²只含prime-power pairs。不同prime bases的整数唯一分解给两个排列；
同prime的额外碰撞与重复相同n的修正总量均被
sum_p(log p)^4 sum_(r>=2)(r-1)^2 p^(-r)控制，uniform Z下有限。
所以(19)的O(1)正确，既未漏prime-power collisions，也不是只有prime-prime时成立。
coefficients支持m<=Z²，普通MV均值的完整(X+Z²)费用保留，sharp cutoff未改变。

原Fourier/Plancherel给F*F<=1，原Poisson给sum_(k in Z)|f_k(t)|²=a_LL²。
M是bounded real multiplier；逐单位eigenvector的标量x^4 Jensen使用补0质量，
Tr(F*MF)^4<=Tr(F*M^4F)正确，无operator-convex错误。
以P=(2pi/(a_LL))F*MF及F=U_F/sqrt(2pi L)计算，J内正积分系数准确是

\[
 (2\pi/(a_LL))^4\,(a_LL^2)/(2\pi L)\,\pi^{-4}
 =8/(\pi a_L^3L^3).
 \tag{1}
\]

由MV得(X/L³)log^4(2Z)(1+Z²/X)，因N~XL，恰等于
O(N(log(2Z)/L)^4(1+Z²/X))。不存在漏乘N或少除L。

J=[T/2,3T]外距每个tau_k至少T/2；C²尾给sum_k integral_(Jc)|f_k|²
<<D X^(-3)。全height |Q_Z|<<sqrt Z给M^4<<Z²，额外系数
(2pi/(a_LL))^4/(2pi L)~L^(-5)；结合D~XL得到Z²/(X²L⁴)，与(22)一致。
低height峰未被删去，正Jensen积分的分割也没有冒充矩阵四迹的无cross-term分拆。

Z=exp(sqrt L)满足Z<=sqrt X，主项o(N)，故Schatten-4范数o(N^(1/4))正确。
H_>四范数O(N^(1/4))仍是独立未支付前件；只有该前件下非交换telescoping和
Schatten Hölder才给(23)。它不能从二矩、(14)或(18)推出，正文范围正确。

## 5. §6：完整affine fibers与结论

gcd(a,b)=1给h=ad-bc的全部解d=d_0+bj、c=c_0+aj，方向无误。
两对均coprime时h=0强制(c,d)=(a,b)，恰为同atom reference；high cell内j区间
仅O(1)长，但全部h tail和carrier仍需联合求和。正文W与外层coefficients保留
四个平方根正规化、six-window和masks，未把第二个Lambda当作任意canonical测试。

正文(24)只是准确定位余项，不宣称joint prime-forms渐近。241的fiber-first准则
被保留；局部Gram原physical vector的净预算、共同centering及global alias账本
仍开放。全文没有提高比例、构造完整Chern/Weil positivity或宣称RH。

结论：448可以按其有限[T]/[T/R]范围保存。这里PASS包括逐式付款和范围声明，
不提升所引用[R]的验收等级。本审查只新增本文件，不修改448或旧notes/math/Git。
