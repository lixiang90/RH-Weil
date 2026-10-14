# 完整physical row的下一来源准入筛选

2026-10-14；来源准备，零数学轮；不创建C021，不改Goal/STATE/cadence/Git。
本稿接C020的实际结论：fullcofactor flat-ell2 Gram可消，但actual alpha=1的
label质量随Y增长；无rate的trace不能胜过最强旧O(log^6Y)，完整Weil净值未付。
下一门改读真实physical row的mixed来源，不继续扩大薄head或重付flat trace。

## 1. 原件与实际核读范围

一级作者论文：D. A. Goldston、C. Y. Yildirim，
*Higher correlations of divisor sums related to primes I: Triple correlations*。
固定[arXiv math/0111212v1](https://arxiv.org/abs/math/0111212v1)，
提交2001-11-19，arXiv页面列58页；
[固定PDF URL](https://arxiv.org/pdf/math/0111212v1)，
[同版本HTML](https://arxiv.org/html/math/0111212v1)。
另核[期刊原PDF](https://math.colgate.edu/~integers/d5/d5.pdf)，
Integers 3 (2003), A05，66页，首页出版日期2003-04-22。
HTML自动生成的Date字段不作论文修订日期。
此处实际核读§1 definitions/Theorems1.1、1.3、1.4，以及§4 Theorem4.1与
通向(4.6)的AP证明机制；没有声称两排版版本全文证明等同，也没有复下载/冻结PDF或生成假hash。
固定URL与核读条款已可恢复；需要归档时分别固定两版本，不以最新版替换。

一级原声明的准确限制：

    Thm1.1, 1≤k≤3:
      max_i |j_i|≪R^epsilon, R≫N^epsilon,
      S_k=(C_k(a) S(j)+o1)N(log R)^(k-r)+O(R^k).

    Thm1.3, k≥2, a_r=1:
      max_i |j_i|≪R^(1/k),
      N^epsilon≪R≪N^[min(theta/(k−1),1/k)−epsilon],
      mixedS_k−S_k=O(R^k)+O(N/log^b N),
      b=A/2−4^(k−3/2)+2^(k−1)−1.

theta来自原(1.30) prime-AP平均误差；theta=1/2可无条件消费，theta=1不当已知。
Thm1.4允许去掉来自pure相关的1/k上限，但仍保max|j_i|≪R^epsilon及
R≪N^[theta/(k−1)−epsilon]。它不自动修复本稿的成长shift。
§4.1(4.5)有native W_R(j)及明确R/shift条件；(4.6)是mixed-with-actual-Lambda
分支。不能把其语法或proof中省写的条件解释成全j/log-critical R已认证。
作者§1明确保留未知的Lambda(n)Lambda(n+j)非零shift槽；这里没有prime-twin定理。

本仓title/arxivID检索未见此前消费该来源；这是筛选信息，不是全球优先权或新净值证明。
Bettin--Chandee已由旧092/220--222/229等审计，不换label再登记来源。

## 2. actual I_U分解先核对象，不能用代理替代physical row

旧164 V=1给

    I_U(n)=sum_(d|n,d≤U) mu(d)log(n/d),
    II_U(n)=Lambda(n)−I_U(n).

定义同一cutoff的两个真实有限除数和

    Lambda_U(n)=sum_(d|n,d≤U) mu(d)log(U/d),
    a_U(n)=sum_(d|n,d≤U) mu(d).

逐项log(n/d)=log(U/d)+log(n/U)，故对每个n≥1、U≥1精确有

    I_U(n)=Lambda_U(n)+log(n/U)a_U(n).              (1)

这是原Lambda_R定义在R=U的代入；a_U修正必须保留。
不能把I_U直接换成Lambda_U，也不能对一个只有big-O误差的Lambda_R相关公式
求R导数以免费获得a_U相关。Lambda_U不只支撑primepowers；实际Lambda仍保全部properpowers。
(1)是旧对象的精确整理，零轮，不登记新的算术抵消。

## 3. 唯一下一对象：完整triangular mixed核及可付误差门

原du Hilbert源、h=1/T、sqrtY≤T≤2sqrtY、|tau|≤T、Y<n≤2Y，置

    s_n=n^(−1/2−i tau)e^(−n/Y),
    E_n(u)=1_[logn−h,logn](u),
    p(f)=sum_(Y<n≤2Y) f(n)s_n E_n,
    c(u)=integral_Y^(2Y) v^(−1/2−i tau)e^(−v/Y)E_v(u)dv.

这是原prime--continuum共同feature，而不是flat label norm。
原TypeI/II关系给p(Lambda)−c=p(I_U)+p(II_U)−c。
例如actual mixed项完整写成

    <p(Lambda),p(I_U)>
      =sum_j sum_(Y<n,n+j≤2Y) Lambda(n) I_U(n+j) w_j(n),

    w_j(n)=[n(n+j)]^(−1/2)e^(−(2n+j)/Y)
            exp[−i tau log(n/(n+j))]
            [h−|log(n/(n+j))|]_+ .                 (2)

内积对第一变量线性；所有交叉、两端cutoff、正负j和properpowers保持。
核支撑需要|j|≤C Y/T，即平方根高度下j范围为O(sqrtY)，不是fixedshift。
分段权w_j的sup/总BV是O(h/Y)：相位导数费用|tau j|/Y²≤C/Y，
并有明确endpoint及positive-part kink。不能删phase、把一个点态main term代全prefix
weighted估计，也不能把source参考的正Gram升级completeQ正性。

一个有信息值且可判的来源准入门是：原AP/除数证明是否给(2)所需的
每个|j|≤CY/T、每个prefix z∈[Y,2Y]的实际mixed误差E_j(z)，并保(1)两分量；
总运输费用必须显式小于强旧完整账本，而非仅逐个shift o(Y)。
若有uniform sup|E_j(z)|≤E(Y,U)，summation-by-parts及全j求和最多收费

    C(h/Y)(Y/T)E(Y,U)=C E(Y,U)/T².                 (3)

因此若真付E=O(U²)+O(Y/log^A Y)，在冻结U≈T/log²T时(3)为
O(log^−4Y)+O(log^−A Y)。这只是明确的**若付则**费用，不是本稿证明了该E；
paper stated conditions目前未给它。native W_U(j)主项可先保为真实有限算术和，
不能免费换成singularseries或continuum，更不能宣称由mixed槽推出actualLambda--Lambda槽。

## 4. 为什么尚不准入新合同

令N≈Y、R=U≈sqrtY/log²Y、k=2、theta=1/2。原Thm1.3要求R≤N^(1/2−epsilon)
以及|j|≪sqrtR；冻结R不满足固定epsilon幂距，actual j≈sqrtY也远超sqrtR。
Thm1.1/1.4的R^epsilon shift不覆盖同一完整j范围。
这些是原声明的真实miss，不是RH输入，不以通过finite sample补量词。

允许继续原§4的具体AP机制审查：能否在完整j范围直接保W_U(j)并付原log-critical
cutoff的BV/error、非coprime residues和prime-power修正；这不等于paper定理已经扩大。
经典Bombieri--Vinogradov的log level损失、(1)的a_U修正与actualLambda--Lambda未付槽
须列入账本。改变R/U会引入原shell或TypeI/II gauge转移，不自动消除core责任。
本文没有给出一个已经核准、独立且完整支付physical row的来源定理。

唯一下一动作：先按(1)–(3)重组完整Lambda/I_U/continuum原核，然后核该一级原证明
是否真实覆盖全部j、R、prefix/BV误差及最强旧后果；如只复现旧工具或漏主要槽，
来源入口零轮停，不新建C021、不能连续换paper制造宏观推进。
若取得新的同源mixed算术付款，再决定准入一个短合同；completeQ/Γ/双pole/wholecore
与actualζ/Ξ净后果仍需另付，宏观Goal保持open。
