# AM 八点证书的无损分离消费：不同作者审查

日期：2026-10-08。审查者：checkpoint_audit。结论：限定数学 **PASS**，未发现阻断。
这是已准入全连续 PC8 证书的新解析消费；不把网格、哈希或编译求值单独当成全域证明。

## 1. 冻结输入与实际阅读

规范身份为 UTF-8，将 CRLF/lone CR 规范为 LF，保留末尾字节。
本轮 FULL READ 下列方法源全部 186 行、PC8 两份审查全部 228/141 行；
483、419 行 AM 解析源及外论文解析审查已全文读过，本轮再核实际计数/平滑段与身份。
外论文仅为方法来源：独读 [2610.08965v1](https://arxiv.org/html/2610.08965v1)
Lemmas 2.1–2.4、Theorem 5.1 的所用证明，不声称本审查全文重放其大型计算。

| 输入 | 行／LF字节 | SHA-256 |
| --- | --- | --- |
| [最终方法源](knausgard-673-method-and-am-comparison-research-perron.md) | 186／11880 | 5ff04f61f68687738d02cb04b2d58d6199a91adb8f5991fe2575f20ebff4cbd5 |
| [483](../../notes/483-admission-of-known-am-eight-point-proportion.md) | 166／7342 | 3ab82cdb257a8555b206f90e59c18fb73f68fe9be0a2de5117bb573056efdb7e |
| [AM 解析源](hybrid-original-eight-point-sqrt-pressure-research-compression.md) | 419／17965 | 94dcf6cde41a78dad81a5ed4d7a1513478bbc09746603a2397b677548fdd4161 |
| [全域区间语义](hybrid-original-am-eight-point-full-certificate-audit-pc8.md) | 228／17120 | 6cea584276b25cfd58fd353f8281986898833ae0a335c8f9033ba99a8154fb46 |
| [最终数值抽取](hybrid-original-am-eight-point-numerical-extraction-review-pc8.md) | 141／14583 | 6a2a01e8a2474b29fd567c110575cd01ebe64cdbcc2cd090f17ff14044ce8e49 |
| [外论文解析审查](../../literature/supplements/2026-10-08-knausgard-2610-08965-analytic-audit.md) | 123／7576 | 0bd2a6aecee5873a4a633c77aa8a2117f6977b6cbb8a0c4ae6fcfccf5d8d2c1d |

另只读核匹配方法源的 knausgard839.tex 与 knausgard839tab2.tex 两项身份；
不因身份匹配声称全文独审 2584 行外论文。方法源第 39 行已改为固定 ε 的 C(f_ε)；
逆替换这一表达式严格恢复旧 SHA b42e63443d4e6bd558094885632c4d843565cd3bda0e1a69f0cdc1ed413a2308。

## 2. 连续 majorant 的独立无网格证明

固定方法源的同一个正偶概率密度 f_AM，I=[−1/2,1/2]，S=Σ|c_j|=6460471/10⁸。
Z₀=√2 sin(1/√2)=∫_I cos(√2u)du≥11/12，且分子≥3/4−S>0。
交替 Taylor 因而给整个 I 上

    f_AM(u) ≤ (12/11)(1−u²+u⁴/6+S).                         (1)

取 θ=4/5、γ=61/100、sinc t=sin(πt)/(πt)，并令
g(u)=γ[sinc(θ(u−1/2))+sinc(θ(u+1/2))]²。
Machin 恒等式和 arctan 交替级数给严格有理包络

    π₋=1231847548/392109375 < π < π₊=5277328977275528/1679825970703125.

这里 atan(1/5) 下/上截至 n=3/4，atan(1/239) 上/下截至 n=0/1。
令 l=16π₋²/25、h=16π₊²/25、v=4u²∈[0,1]。
对 |x|≤θπ，sin(x)/x≥1−x²/6+x⁴/120−x⁶/5040；
从余项首个正项起绝对值递减，初始两项是否递减不影响此方向。
两腿相加，负系数用 h、正系数用 l，得到 H(u)≥q(v)，其中

    q₀=2−h/12+l²/960−h³/161280,
    q₁=(−h/3+l²/40−h³/2688)/4,
    q₂=(l²/60−h³/672)/16,  q₃=−h³/161280.

对于幂系数 a_k，d 次 Bernstein 系数为
β_i=Σ_{k≤i}a_k binom(i,k)/binom(d,k)；其基函数非负且和为 1。
下方精确算术给 q 的四个 Bernstein 系数全部 >6/5，故 q>0，可以平方下界。
六次多项式 γq(v)²−[(12/11)(1+S)−3v/11+v²/88]
的七个 Bernstein 系数全部 >1/50。于是整个 I 有 g−f_AM>1/50；
I 外 f_AM=0≤g。这是一条全域证明，有限检查只认证其有理系数比较。

另核方法源第 93–129 行的完整 Fraction 程序与余项方向、周期约化、正区间除法。
从最终源实际抽取执行，exit 0，stdout：
`PASS 129 exact cells and the continuous derivative bridge`。
该 37 行、1428 字节代码（不计结尾 LF）SHA 为
4b3fe24b7bd1a1d136a073335684eb601950e8e7d207e6f5cbaf57b00078efd1。
它的 129 点 >9/100、全域导数 <16、最近点距 ≤1/512 也独立闭合连续证书。

## 3. 分离、滑窗及固定平滑

g 的 Fourier 支撑为 [−θ,θ]，两矩形卷积在端点为零。
Parseval 给 Λ=(2γ/θ)(1+sinc θ)≤61/32<2。
同降函数的 Chebyshev 积分给 K_MT(t)≥sinc t≥sinc θ>7/30（|t|≤θ）；
AM 扰动 ≤S/Z₀<39/550，故 K_AM(t)>134/825，平方 >1/40>c=805003/10⁸。
这里的核、局部证书及全零点能量都是 AM 自己的窗，没有拼接 MT 能量常数。

PC8 已准入的是全部非负七 gap 上的连续局部证书。
两份审查相接补齐值/导数/凸性表、32 根及所有叶的实区间覆盖、定义桥与数值门；
本轮复用该准入，不重跑大型覆盖。240 项是编译精确求值，不能改称 240 项内核证明。
核对原非负 a_ij、b_r：每种索引跨度 Σ_i a_{i,i+s}≤2，总 Σ_rb_r=B₀=404350/10⁸。
对任意 m 个排序实点的全部 m−7 八点窗相加，每个 gap 费用至多 B₀，
每个无序 pair 权至多 2。因此 E:=Σ_{i≠j}K(y_i−y_j)²≥c(m−7)−B₀span。
m≤7 时右边非正，E≥0 覆盖；首次/末次窗与全部 b_r 均未删。

固定偶光滑 cutoff 后 f_ε=fχ_ε²/m_ε 是概率密度，m_ε→1、d_ε=∥f_ε−f∥₁→0。
直接 majorant 为 g/m_ε；先固定 m_ε>61/64，分离 Gram 的范数 ≤Λ/m_ε<2。
每个核差 ≤d_ε、两核模 ≤1，平方差 ≤2d_ε；方法源的 3d_ε 与 42d_εm 为安全上界。
在所有 n 个简单临界线列中选极大不交 |距离|<θ 的近对，余集必 θ-separated。
每对谱 1±|K_ε|≤2，贡献 J_pair=2|K_ε|²≥2c−6d_ε。
余集不被 φ₂ clipping，J_S=E_S。φ₂(t)=t²−(t−2)₊² 凸，
谱迹 pinching 给 J(U)≥ΣJ_block，不需算子凸，最终

    J(U)≥cn−B₀span(Y)−7c−42d_εn.                            (2)

## 4. 实际全零点消费与范围

原全复零点 Hermitian A 保留离线反射对和重数；tr A=N、
tr A²=(C(f_ε)+o_ε(1))N。P 是 n 个简单临界线单位列之和，Q=A−P。
重复临界线零点至少消耗两个计数单位而正秩至多 1；离线反射对同样正秩至多 1，
所以 p=n₊(Q)≤(N−n)/2。这里不声称 A≥0，也不使用 RH 或本项目 7/8 前件。
独立 minmax 核算：A≤P+Q₊，rank Q₊=p，P≥0；秩 p 上移至多损失 p 个
(2−λ(P))₊² 项，每项 ≤4。于有限环境维数 D 上因此

    tr(A−2I)² ≥ tr(P−2I)₋²−4p
              =4D−4n+tr φ₂(P)−4p.

消去 4D，并用 P 非零谱等于 U 非零谱、φ₂(0)=0，得
tr A²≥4(N−n)+tr φ₂(U)−4p≥2(N−n)+tr φ₂(U)，
即 n≥2N−tr A²+J(U)。这不把离线项当实点 Gram，不增加原辅助零维度。
排序 span(Y)≤Tlog T/(2π)=N(T)+o(N(T))；(2) 的边界 7c/N→0。
必须先固定 ε 令 T→∞，再 ε→0；原 419 源固定双测试函数的全复零点证明给
C(f_ε)→C_AM，不能将 fixed ε 的能量误写为 C_AM。
AM 自己的已准入严格包络 2−C_AM>67216841/10⁸ 因而给

    liminf N₀^s(T)/N(T) ≥ 66812491/99194997
                       ≈0.6735469834229644.               (3)

这是普通 ζ 简单临界线比例的无条件解析推论，依赖原 PC8 完整准入及其明确计算信任边界。
相对外论文所列 1669159/2478195，精确差为 719712074/81941515196805>0。
不把此比较独自称公开最佳/发表纪录，不改原 whole 增长、无零条带或 κ/σ 前件。

## 5. 独立自包含精确复演

以下代码无项目/上游导入、无浮点判断、无写文件；复演的是上面的有限有理证书及账本。
π/Taylor/连续覆盖、固定平滑和实际零点计数分别由上述数学证明负责。

~~~python
from fractions import Fraction as F
from math import comb
def atan_sum(base,last):
    return sum((F((-1)**n,(2*n+1)*base**(2*n+1))
                for n in range(last+1)),F(0))
pi_lo=16*atan_sum(5,3)-4*atan_sum(239,0)
pi_hi=16*atan_sum(5,4)-4*atan_sum(239,1)
assert pi_lo==F(1231847548,392109375)
assert pi_hi==F(5277328977275528,1679825970703125)
cs=[F(x,10**9) for x in [12310798,-15041681,3867664,6489926,
    -992327,5580097,-6846472,3781297,-5670353,3355089,-450523,-218483]]
S=sum(map(abs,cs),F(0)); assert S==F(6460471,10**8)
l=F(16,25)*pi_lo**2; h=F(16,25)*pi_hi**2
q=[2-h/12+l*l/960-h**3/161280,
   (-h/3+l*l/40-h**3/2688)/4,
   (l*l/60-h**3/672)/16,-h**3/161280]
def bernstein(a):
    d=len(a)-1
    return [sum((a[k]*F(comb(i,k),comb(d,k))
                 for k in range(i+1)),F(0)) for i in range(d+1)]
assert min(bernstein(q))>F(6,5)
p=[F(0)]*7
for i,a in enumerate(q):
    for j,b in enumerate(q): p[i+j]+=F(61,100)*a*b
for i,a in enumerate([F(12,11)*(1+S),-F(3,11),F(1,88)]): p[i]-=a
assert min(bernstein(p))>F(1,50)
rows=[[13630830,0,19565904,20317441,45030671,100000000,200000000],
      [29997996,30621878,47766489,79682558,109938656,100000000],
      [37356140,69378121,65335210,79682558,45030671],
      [38030065,69378121,47766489,20317441],
      [37356140,30621878,19565904],[29997996,0],[13630830]]
assert all(x>=0 for row in rows for x in row)
assert all(sum(rows[i][s-1] for i in range(8-s))<=2*10**8
           for s in range(1,8))
br=[28898,57272,75526,80958,75526,57272,28898]
B0=F(sum(br),10**8); assert B0==F(404350,10**8)
c=F(805003,10**8); A0=F(67216841,10**8)
assert F(134,825)**2>F(1,40)>c and F(61,32)<2
new=(A0-B0)/(1-c); assert new==F(66812491,99194997)
assert new-F(1669159,2478195)==F(719712074,81941515196805)>0
print('PASS all-domain Bernstein certificate, span budgets, exact proportion')
~~~

审查程序的成功只记录精确算术与上述有理证书；本轮没有执行大型 AM/Lean native 搜索。
