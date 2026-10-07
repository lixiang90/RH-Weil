# 整族行权重与两个 parity Gram 的四阶盲方向：有限信息审计

2026-10-08。作者 radial_review。新完整推导，待其他作者独立全文审查。
基线 88e86a35a3dc2c7988ec1fabe0fde6c485a1fc0b；原已提交文件全部冻结。

结论：当前已经付款的整族 weighted high second、所有固定 smooth
rowweight 的 Γ 中心化、whole low 的16个 parity 四词，以及两个
Δ_j 与 Z_j 的分量正交，仍不单独供应 entire prime fourth 的统一有限上界。
下面给出精确 finite tensor 检验，它同时保留最新470的 q 与 entire
parity gap 必要下界。新的盲方向与这些 rowweight、low residual、
anticommutator 测试同时正交，不能由再做同类 scalar Cauchy 消除。

这是 trace/Gram 信息接口的限制，不是实际素数算子的实现或反例。
它没有实现原 scalar sharp prime coefficients、原单份 interval carrier、
零点 feature 或 partial-Weil 惯性账本。尤其不从 fourth 无界推出所有
比例证书失效；大谱尾本身也可能给零侧账本提供额外信息。
本稿没有得到新的实际比例、无零边界或 RH 证明。

## 1. 同对象输入与所检验的准确接口

沿用原有限 Hermitian 矩阵 H、L、W、V 与实际 involution U，记
normalized trace τ=Tr/d，以及

\[
 \Gamma=H^2-W,\qquad \Delta=L^2-V,\qquad Z=(HL+LH)/2,
 \quad B_{\rm e,o}=(B\pm UBU)/2.                         \tag{1}
\]

以下输入均保持其已审范围，不重证底层分析：

| 冻结输入 | canonical UTF-8 LF SHA-256 |
| --- | --- |
| [454 whole weighted second](../../notes/454-original-background-and-weighted-prime-mixed-traces.md) | 8ab99d60c1b748dc561cac57ee498057a0c9fb19b9778a041261b1bad0750db7 |
| [462 whole low fourth](../../notes/462-original-low-prime-fourth-path-constant.md) | 868adfeb0d742043f39bd08e0783d66b7a9db11316067b0b3b43d80150cdf680 |
| [whole low parity 源](hybrid-whole-low-parity-fourth-research-root.md) | 02328b4cfaf902fc0f0d60e37f27989808aaae6bb88e6410c8d120a44487969d |
| [marked13 与两个 parity Gram 源](hybrid-parity-split-schur-and-even-anticommutator-research-radial.md) | b9fff88ede3374b488dccddf9cfea3f92f386e98594c385dda51ce210b784d20 |
| [no-growth positive-tail gap 源](hybrid-positive-tail-whole-high-parity-gap-research-compression.md) | 568f2c80d9773db7c13bc3605e7d56ed032e3fba7f5d4dc7c34bbea5ac7cb611 |
| [470 centered spectral variance](../../notes/470-centered-spectral-variance-excludes-small-high-residual.md) | 729ddbed2b2d2af08e21e5f1ebabfb5663f906c702f52b13f81aac224402a93a |
| [此前谱信息与窄窗审计](../2026-10-07/hybrid-spectral-low-high-information-and-narrow-window-research-compression.md) | 46aa87f3ab12e7399dd33bc4c6833fbe7362b31781c1ec018d538fd2ffe21f4f |

canonical 只作 CRLF、lone CR 转 LF，不 trim 或改 EOF。
本稿新增的 finite 论证不需要 [R]；把已付 marked13 输入作为数据时，
仍继承其准确 conductor-one [R] 与 bounded-q sharp 恢复范围。

检验的数据接口包含：

1. W、V 的 bounded positive row-diagonal 与完整 scalar marginal；
   所有已付 τ(FHG H)，其中 F、G 是固定 admissible rowweight
   或对应 finite 矩阵；这不只保留一个 commutator 常数。
2. 对所有已付固定 smooth rowweight F 的 τ(ΓF)→0，包含 W、
   V 的准入测试；high U-parity 的 normalized HS 误差趋零。
3. entire low 的每个 parity 四词、weighted low second，以及
   Γ_j 与 Δ_j 的 covariance、Z_j 的 norm、c 和 k。
4. 每个已付 one-H marked13 的零极限，及 bounded-q 下
   \(\langle\Delta_{\rm e},Z_{\rm e}\rangle,
     \langle\Delta_{\rm o},Z_{\rm o}\rangle\to0\)。
   已付的 odd-H 零 trace 也可一并保留。

接口只指这些有限 trace/Gram 量及其极限，不包含未付的
scalar prime 四重系数相关，也不声称包括全部原 carrier leakage
定量率。两个来源中尚未付的 entire31 数值 b 不是已知输入。

## 2. 精确 finite word 引理：先固定 fiber 再取高度极限

任取整数 m≥3。在 m 维辅助空间上定义

\[
 A_m=\operatorname{diag}\!\left(\sqrt{m/2},-\sqrt{m/2},
                  0,\ldots,0\right),\qquad
 \sigma_m(B)=\operatorname{Tr}B/m,\qquad \gamma_m=m/2 .
 \tag{2}
\]

直接有限计算给

\[
 \sigma_m(A_m)=\sigma_m(A_m^3)=0,\quad
 \sigma_m(A_m^2)=1,\quad \sigma_m(A_m^4)=\gamma_m.
 \tag{3}
\]

在 d m 维空间，置

\[
 \widetilde H=H\otimes A_m,\quad
 \widetilde L=L\otimes I_m,\quad
 \widetilde W=W\otimes I_m,\quad
 \widetilde V=V\otimes I_m,\quad
 \widetilde U=U\otimes I_m,\quad
 \widetilde F=F\otimes I_m.                              \tag{4}
\]

normalized trace 为 \(\widetilde\tau=\tau\otimes\sigma_m\)。
若 finite word 的高因子是 H，其他每个因子均为 L 或某 F，且高因子
总数为 j，则严格保留原次序：

\[
 \widetilde\tau(\widetilde B_1\cdots\widetilde B_s)
       =\tau(B_1\cdots B_s)\,\sigma_m(A_m^j).            \tag{5}
\]

引理同样适用于 H_e、H_o，因为其放大正好是 H_e⊗A_m、H_o⊗A_m。
因此含零或两个高因子的词精确保留；含一个或三个高因子的词变为
准确零。所有零目标的 fixed marks 词因而仍满足其已付结论。

这里每个模型都先固定 m，再令原高度 T→∞。没有把 fixed-m 的
o_m(1)免费用于 m=m(T)，也不需要新的移动截断 tail 合同。

若只为解释压缩次序，形式上可取 \(\widetilde E=E\otimes I_m\)、
\(\widetilde P=P\otimes I_m\)，高 physical operator 换为
\(B_H\otimes A_m\)。这样每个内部 P 都仍准确保留，(5)不删除投影。
但这已是 fiber-valued coefficient 的不同表示，绝不是原 scalar
prime 算子或原 carrier 的实现；不能将该解释用于验证原 raw/tail
估计。更具体地，(4)的 W⊗I_m 是为保留已付 row-test 数据而选定的
center；若字面把每个 prime factor 都 tensor A_m，其原 same-prime
quadratic diagonal 会变为 W⊗A_m²，而不是这里的 center。
因此本构造不保持原 same-prime operator 定义。下文的信息结论
仅用(4)–(5)，不将这种定义差异当成小误差。

## 3. 整族 weighted second、中心化和全部 low 数据保持

任意 finite F、G 都严格有

\[
 \widetilde\tau(\widetilde F\widetilde H
                       \widetilde G\widetilde H)
   =\tau(FHG H),\qquad
 \|[\widetilde H,\widetilde F]\|_{2,dm}^2
   =\|[H,F]\|_{2,d}^2 .                                \tag{6}
\]

所以原完整 weighted transition kernel 的所有已付测试、K_HW，
以及 0≤W≤M 的常数和 W 的所有 scalar moments 都保持。
functional calculus 也准确有
f(W⊗I_m)=f(W)⊗I_m，故这不是只保留有限个 f(W)。

置 \(\widetilde\Gamma=\widetilde H^2-\widetilde W\)，则

\[
 \widetilde\tau(\widetilde\Gamma\widetilde F)
       =\tau(\Gamma F).                                \tag{7}
\]

Γ 对整个已付固定 smooth rowweight 类的中心化完全保持。
high parity 的误差也精确保留：

\[
 \|\widetilde H+\widetilde U\widetilde H\widetilde U\|_{2,dm}
       =\|H+UHU\|_{2,d}.                               \tag{8}
\]

所有只含 L、U、rowweights 的有限词不变，特别是完整16-label
low parity fourth、weighted low second、V/Vo/Ve 与 residual 常数。
这比此前只匹配几个 scalar low moments 的反模型更强。

finite anticommutator 和 low residual 满足
\(\widetilde Z=Z\otimes A_m,\widetilde\Delta=\Delta\otimes I_m\)。
对 j=e,o，完整关系为

\[
 \begin{gathered}
 \langle\widetilde\Gamma_j,\widetilde\Delta_j\rangle
       =\langle\Gamma_j,\Delta_j\rangle,\qquad
 \|\widetilde Z_j\|_{2,dm}^2=\|Z_j\|_{2,d}^2,\\
 \langle\widetilde\Delta_j,\widetilde Z_j\rangle=0,\qquad
 \langle\widetilde\Gamma_j,\widetilde Z_j\rangle=0 .
 \end{gathered}                                         \tag{9}
\]

后一行因(3)的 first/third moments 而为精确零，不只是 o(1)。
前一行没有改动 actual c 的 covariance：

\[
 \widetilde c=c,\quad\widetilde k=k,\quad
 \widetilde e=e,\quad
 \widetilde z=z=c-k/4,\quad
 \widetilde b=\widetilde\eta=0 .                        \tag{10}
\]

因此两个 PSD Gram 自动合法。该模型并非用未付款的 c 或 k 数值
冒充 actual input；它恰保留任意基序列当时的 finite c、k。

## 4. 新四阶盲方向及最新470下界保持

令 \(D_m=A_m^2-I_m\)。这是新方向的准确有限描述：

\[
 \sigma_m(D_m)=\sigma_m(D_m A_m)=0,\qquad
 \sigma_m(D_m^2)=\gamma_m-1,\qquad
 \widetilde\Gamma=\Gamma\otimes I_m+H^2\otimes D_m .
 \tag{11}
\]

I_m、A_m、D_m 在 auxiliary HS 空间两两正交。
H²⊗D_m 对所有 rowweight F⊗I_m 和 low residual Δ_j⊗I_m
同时不可见，也与 Z_j⊗A_m 正交。
因此即使加入整个 fixed smooth rowweight 家族，或同时使用两个
parity Schur，其 HS 成本仍不能被这些向量检测。
这不是不合法地将 \(\Delta\perp Z\)拆成分量；(9)直接验证两个分量。

记 \(a=\tau H^4,q=\tau\Gamma^2\)，有限正交给

\[
 \widetilde a=\gamma_m a,\qquad
 \widetilde q=q+(\gamma_m-1)a .                         \tag{12}
\]

更一般地，置 \(A_{{\rm sq},j}=(H^2)_j\)，有

\[
 \|\widetilde\Gamma_j\|_{2,dm}^2
    =\|\Gamma_j\|_{2,d}^2
           +(\gamma_m-1)\|A_{{\rm sq},j}\|_{2,d}^2 .
 \tag{13}
\]

所以分量 r 会改变，不能说保留其原数值或旧 Q 前件。
这并未越过470最新必要约束。令
\(g=\tau(\Gamma U\Gamma U)=q_e-q_o\)，则

\[
 \widetilde g=g+(\gamma_m-1)\tau(H^2 U H^2 U)\ge g .
 \tag{14}
\]

最后一步是 PSD trace 的正性：
H²≥0、UH²U≥0，故 τ(H² UH²U)≥0；不要求它们交换。
因 m≥3，(12)、(14)使 q 和 entire parity gap 都不减。
基序列若满足470的
\(\liminf q,\liminf g\ge q_*=(\sqrt{104899}-275)/15120\)，
放大模型仍满足这两个最新 whole 下界。
它也不会把已排除的 Q=1/350 修复为可达条件。

## 5. 带符号31与负 commutator 不消除这个方向

Hermitian finite 循环展开、没有先取绝对值，准确给

\[
 F=\tau(H+L)^4=a+e+6c-k+4b+4\eta ,
 \tag{15}
\]
\[
 \boxed{\widetilde F=\gamma_m a+e+6c-k.}               \tag{16}
\]

而 \(\|HL-LH\|_{2,d}\le2\|HL\|_{2,d}\)，严格有 k≤4c。
所以

\[
 \widetilde F\ge\gamma_m a
              \ge\gamma_m(\tau H^2)^2.                \tag{17}
\]

即使已经令 entire31 的 signed term b 精确为零，并保留负项 −k
与完整 c 的联动，leading high fourth 仍独立增加。
实际 flat high second \(\tau H^2\to1/6\)，给
\(\liminf\widetilde F\ge\gamma_m/36\)。

对任何基序列，uniform-upper 信息障碍的量词有两个情形：

* 若其 actual a 无界，因 low fourth 已付有界，normalized Schatten
  反三角给 \(F^{1/4}\ge(a^{1/4}-e^{1/4})_+\)；
  从已付这些数据本来就不能得到统一有限 F。
* 若存在 a 有界的基子列，先固定任意 m，再沿该子列。
  每个 tensor 模型都有 bounded q，故所有标明 bounded-q 的 split
  Gram 输入仍在其准确域内；但(17)的有限常数可随 m 任意大。
  因此不存在仅由本稿所列共同 trace/Gram 极限供应的统一有限 F 上界。

第二点不声称每个模型 q 都小；恰相反，q 随固定 m 增大。
它检验的是可达 q≥q_* 域中整个 moment-information class，而不是
再次提出某个未付或已排除的 small-q 合同。

还可用全 residual 显示 signed completion 的盲点。置
\(\mathcal D=W+V,\mathcal R=\Gamma+\Delta+2Z\)，finite 恒等式为

\[
 (H+L)^2=\mathcal D+\mathcal R,\qquad
 F=\tau\mathcal D^2+2\tau(\mathcal D\mathcal R)
                         +\|\mathcal R\|_{2,d}^2 .
 \tag{18}
\]

在本模型中

\[
 \widetilde{\mathcal R}
   =(\Gamma+\Delta)\otimes I_m+H^2\otimes D_m+2Z\otimes A_m ,
 \tag{19}
\]

三项 auxiliary modes 两两正交。因此

\[
 \|\widetilde{\mathcal R}\|_{2,dm}^2
    =\|\Gamma+\Delta\|_{2,d}^2+(\gamma_m-1)a+4\|Z\|_{2,d}^2 .
 \tag{20}
\]

原 centered rowweight 与 split orthogonality 没有使(20)里的盲成本
变成负数；它准确显示为什么再联合现有 scalar Cauchy 不能完成 upper。

## 6. 正系数变体与模型作用域的边界

障碍也不完全依赖 auxiliary 的负特征值。可改取
\(A_m^+=\operatorname{diag}(\sqrt m,0,\ldots,0)\ge0\)：
其 normalized second 仍为1、fourth 为 m，含零或两个 H 的词仍
精确保留。含一个或三个 H 的已付零目标，先固定 m 后仍为零极限，
只是 finite 不再全为准确零。

low 全词不变，所有 Γ rowweight 与 ΓΔ 中心化同样保持。
normalized Schatten 反三角直接给

\[
 \widetilde F^{1/4}\ge
                  \left((ma)^{1/4}-e^{1/4}\right)_+ . \tag{21}
\]

所以其共同 bounded-a 子列也不能供应独立于 m 的 finite upper。
该变体可保留 fiber-valued coefficient 的 positive semidefinite
性质，却仍没有构造原 scalar prime system。
对 genuine scalar coefficient 的唯一性、prime row phases、实际
carrier frequency 排布、raw operator/tail rates，均不作模型结论。

尤其新的辅助维数 dm 不是原 \(d=\lfloor X\log X\rfloor\) 的同一个
scalar interval basis。不能把(4)的 normalized identity 宣称为
原 physical 算子准入、全高度 raw/good replacement 或根系数合同。
上界失败只针对第1节精确定义的 scalar/Gram 信息接口。

## 7. 新的最窄实际付款目标

本检验没有否定利用真实 scalar prime structure 的机会。
它精确定位需要超出当前 static rowweight 测试的内容：
控制 Γ 在 high-square 方向的四阶量，或等价地控制完整
balanced genuine-prime 四重系数的 signed covariance。
finite 恒等式

\[
 q=\tau(\Gamma H^2)-\tau(\Gamma W)                     \tag{22}
\]

说明 \(\tau(\Gamma f(W))\to0\) 对所有固定 f 仍没有支付
\(\tau(\Gamma H^2)\) 的 upper。后者在(11)的新增 mode 上正好有
成本 \((\gamma_m-1)a\)。H² 本身不是固定 rowweight。

实际后续研究须使用 scalar once-prime coefficient、共同路径的相位/
congruence、原有限 P 的真实 fourth compression gap，或零侧 feature
几何。把 negative commutator 和两个 parity Schur 再做同类优化，
不能在没有这些新输入时绕过本稿的 finite 盲方向。
本结论不排除其他惯性证书，亦不把某个 abstract model 当成实际零点配置。

## 8. 有限核对与独立范围

另用内存中的 rational complex Hermitian 4×4 H、L、W、V，
U=diag(1,1,−1,−1)，辅助 m=8、A=diag(2,−2,0,…,0)：
32条 exact Sympy identities 全通过，包含两个方向 commutator
quadratic、四种 rowweight、ΓΔ 的两 parity、Z norm、q、g 与 whole F。
没有运行旧审计、写入输出或改动冻结文件。
这些小矩阵仅核对(5)–(16)的 finite 代数，不认证 prime asymptotic、
未知第四矩或任何 RH/比例合同；正文的证明不依赖该数值实例。
