# Knausgård 67.3538% 方法与 AM 八点证书：比较及无损分离推论

日期：2026-10-08。作者：perron_reviewer。状态：完整解析推导及轻量连续证书已自检，待不同作者审查。
本源不改既有证书，不执行 535,332,163 盒搜索，也不以有限检查代替全域证明。
新增推论只计实际普通 ζ 的简单临界线零点；不需要本项目的 7/8 无零区域。

## 1. 固定输入、阅读范围与比例口径

以下 SHA-256 均为 CRLF/lone-CR 规范为 LF、保留文件末尾的完整字节身份。

| 输入 | 行／LF字节 | SHA-256 |
| --- | --- | --- |
| [483 接入笔记](../../notes/483-admission-of-known-am-eight-point-proportion.md) | 166／7342 | 3ab82cdb257a8555b206f90e59c18fb73f68fe9be0a2de5117bb573056efdb7e |
| [AM 平方根压力解析源](hybrid-original-eight-point-sqrt-pressure-research-compression.md) | 419／17965 | 94dcf6cde41a78dad81a5ed4d7a1513478bbc09746603a2397b677548fdd4161 |
| [PC8 全域实区间语义审查](hybrid-original-am-eight-point-full-certificate-audit-pc8.md) | 228／17120 | 6cea584276b25cfd58fd353f8281986898833ae0a335c8f9033ba99a8154fb46 |
| [PC8 最终数值抽取审查](hybrid-original-am-eight-point-numerical-extraction-review-pc8.md) | 141／14583 | 6a2a01e8a2474b29fd567c110575cd01ebe64cdbcc2cd090f17ff14044ce8e49 |
| 外论文 knausgard839.tex | 2584／137960 | 7384ba0e91228026ca861deca551734a417e8c13365803f725a93a6dde2e0bca |
| 外论文 knausgard839tab2.tex | 33／1611 | fc6e1afb1ab3d2e14dec2639ad5b2e5546d2a721ec57531a7d983af69225694e |
| [本仓库外论文解析审查](../../literature/supplements/2026-10-08-knausgard-2610-08965-analytic-audit.md) | 123／7576 | 0bd2a6aecee5873a4a633c77aa8a2117f6977b6cbb8a0c4ae6fcfccf5d8d2c1d |

本轮全文重读 483、419 行 AM 解析源、228 行语义审查及 141 行最终抽取审查，
并重读外论文 §5 完整证明、§7 的相关上限证明和附表 2；之前已全文读其 HTML §§1–8。
外源：[arXiv:2610.08965v1](https://arxiv.org/html/2610.08965v1)；
本地 TeX 位于 tmp/pdfs/knausgard-2610-08965-v1/，身份如上。
PC8 固定原源：[d272437e7ebeb17b87c8c3d7cece592aa23785ab](https://github.com/josusanmartin/riemann/blob/d272437e7ebeb17b87c8c3d7cece592aa23785ab/submissions/dani-bound-2026/proof/Solution.lean)，
原始 1,675,641 字节 SHA 012c6ac5f9282158a686500dc0c967bf0a9b00e1a6192734d8f237bb23dd2d5f。
使用的是已准入全域证书，240 项编译求值及七项结构复演不等于 240 项 Lean 内核证明；
外论文 native_decide 的额外计算公理问题保持在已有审查的独立信任范围内。

令 N 为按重数计的全部零点数，n 为简单且在临界线上的零点数。
已准入 483 的 n/N 下界为 118513839290/175971686899；
外论文 Theorem 1.3 为 1669159/2478195。两者相差
24320973366391/436092154614667305，即约 0.0055770261 个百分点。
外论文 83.9004597% 是全部条带的 distinct 比例，不能当成简单临界线比例。

## 2. 改进到底发生在哪里

两方案都有同一个真实全零点 Hermitian 算子 A，保留离线零点、重数和反射配对。
其自身窗口 f 的固定平滑给 tr A=N、tr A²=(C(f_ε)+o(1))N。
将 n 个简单临界线列留在 P，余项 Q=A−P 有正惯性 p 且 N−n≥2p；
阈值 φ₂(t)=t²−(t−2)₊² 的谱不等式给
tr A²≥2(N−n)+tr φ₂(U)，U 为这 n 列的 Gram 矩阵。
因此 J(U):=tr φ₂(U)−n 若满足 J≥xn−b span−o(n)−O(1)，就有
                         liminf n/N ≥ (2−C(f)−b)/(1−x).                 (1)
旧 AM 的 j(t)=(t−1)²−(t−2)₊² 正好是 φ₂(t)−2t+1；
因 tr U=n，tr j(U)=J(U)。此处不向 Gram 矩阵补零维度。

AM 的八点核奖励 c=.00805003、总 gap 费用 B₀=.00404350；
旧装配用 m=152、q=7、τ=8/7、F=2√(τc(m−q))−τ，
得到 x=F/m、b=B₀(m−q)/m。谱 clipping 与分块平均都有损。
外论文第二窗改为十项整数 cosine，使用 θ=.85、质量 Λ<2 的 majorant，
只让 simple 点参与；分离子集完全不被 φ₂ 截断，近对也完全不被截断。
其新局部八点证书有 α=.000627、x=.008722，
零和单-gap 修正 B_r 产生六-gap storage 差 Φ−shift Φ，oscillation Ω=.003882；
叠加后 b=7α=.004389，Ω 仅付一次边界，所有 pair 的跨度权预算仍 ≤2。
这是无损谱装配与局部/storage 证书共同改变，不是单纯改善窗口。

写 A₀=2−C。AM 严格有理包络 A₀> .67216841，外论文仅用 A₀≥.6720526。
同一 (1) 的灵敏度是 ∂p/∂A₀=1/(1−x)、∂p/∂b=−1/(1−x)、∂p/∂x=p/(1−x)。
用已准入旧有理 p、旧 F 下包络 4084939303/3500000000 精确分解新旧差，
能量改变贡献 −.0116828982 个百分点，gap 费用改变 −.0536392229 个百分点，
reward 改变 +.0708991472 个百分点；合计上述 +.0055770261。
三项来自恒等式 Δp=[ΔA₀−Δb+p_old Δx]/(1−x_new)，不是经验归因。

## 3. 保留旧 AM 核的新连续 majorant

令 I=[−1/2,1/2]、Z₀=√2 sin(1/√2)，
f(v)=[cos(√2v)+Σ_{j=1}^{12}c_j cos(2πjv)]/Z₀，零延拓到 I 外，
c_j 的分子（分母 10⁹）为
(12310798,−15041681,3867664,6489926,−992327,5580097,
 −6846472,3781297,−5670353,3355089,−450523,−218483)。
记 S=Σ|c_j|=.06460471<13/200。Z₀≥11/12、f>0、∫f=1，
后两事实也由已准入 AM 源给出。K(t)=∫_I f(v)e^{−2πitv}dv。
取 θ=4/5、γ=61/100、sinc x=sin(πx)/(πx)（sinc 0=1），
                 g(v)=γ[sinc(θ(v−1/2))+sinc(θ(v+1/2))]².             (2)
g≥0；其 Fourier 支撑为 [−θ,θ]，在端点为零（两个矩形 Fourier 因子的卷积）。
Parseval 给 Λ=∫g=(2γ/θ)(1+sinc θ)≤61/32<2，
因为 sin(4π/5)=sin(π/5)≤π/5。下面的有理证书证明 g≥f 于整个 I。

在每个 v=k/256（0≤k≤128），逐项有理 Taylor 区间严格给 g−f>9/100。
全域 |(g−f)'|≤4γπθ+(√2+2πΣj|c_j|)/Z₀<16：
用 sinc x=(1/2)∫_{−1}¹e^{iπxu}du 得 |sinc'|≤π/2、|sinc|≤1；
再用 π<22/7、√2<3/2、Z₀>9/10 即得这个严格有理上界。
偶性和最近网格距离 ≤1/512 因而给 g−f>9/100−16/512>0；
有限网格通过只是该连续证明的一个输入，不独自证明 majorization。

以下自包含 Fraction 检查只验证这个小证书；不导入旧搜索或新论文程序。
cos/sinc 多项式各取 k=0,…,12，余项分别 ≤q¹³/26!、q¹³/27!（q=x²≤π²）；
从第 13 项起绝对值递减，交错余项界合法。相位先按整数周期精确缩到 |x|≤π。
Z₀=sinc(1/√2)，所以它的 q=1/2 是精确有理数。

~~~python
from fractions import Fraction as Q
from math import factorial
def add(a,b): return a[0]+b[0],a[1]+b[1]
def mul(a,b):
    z=[x*y for x in a for y in b]; return min(z),max(z)
def sc(a,k): return mul(a,(k,k))
def dv(a,b):
    assert b[0]>0
    return mul(a,(1/b[1],1/b[0]))
def at(n):
    s=sum(((-1)**k*Q(1,n**(2*k+1)*(2*k+1)) for k in range(24)),Q(0))
    return s,s+Q(1,n**49*49)
pm=add(sc(at(5),16),sc(at(239),-4))  # π=16 atan(1/5)−4 atan(1/239)
pi=(Q(3141592653,10**9),Q(3141592654,10**9))
assert pi[0]<pm[0]<=pm[1]<pi[1]
p2=mul(pi,pi)
def P(q,sinc=False):
    r=(Q(0),Q(0)); z=(Q(1),Q(1))
    for k in range(13):
        r=add(r,sc(z,Q((-1)**k,factorial(2*k+int(sinc))))); z=mul(z,q)
    e=q[1]**13/factorial(26+int(sinc))
    return r[0]-e,r[1]+e
Z=P((Q(1,2),Q(1,2)),True); assert Z[0]>Q(9,10)
cs=[Q(x,10**9) for x in [12310798,-15041681,3867664,6489926,-992327,
    5580097,-6846472,3781297,-5670353,3355089,-450523,-218483]]
th=Q(4,5); ga=Q(61,100)
for k in range(129):
    v=Q(k,256); F=P((2*v*v,2*v*v))
    for j,cj in enumerate(cs,1):
        r=(2*j*v+1)%2-1; F=add(F,sc(P(sc(p2,r*r)),cj))
    F=dv(F,Z)
    H=add(P(sc(p2,th*th*(v-Q(1,2))**2),True),
          P(sc(p2,th*th*(v+Q(1,2))**2),True))
    G=sc(mul(H,H),ga); assert G[0]-F[1]>Q(9,100)
D=4*ga*Q(22,7)*th+(Q(3,2)+Q(44,7)*sum((j*abs(c) for j,c in enumerate(cs,1)),Q(0)))/Q(9,10)
assert D<16
print("PASS 129 exact cells and the continuous derivative bridge")
~~~

近对无需数值表：cos(√2v) 与 cos(2πtv) 在 [0,1/2] 同为递减函数（0≤t≤θ）。
Chebyshev covariance 给 K_MT(t)≥sinc t≥sinc θ；
sin(π/5)≥π/5−(π/5)³/6、π²<10 给 sinc θ>7/30。
扰动核绝对值 ≤S/Z₀<39/550，所以 K(t)>134/825（|t|≤θ），
                     K(t)²>1/40>c.                                  (3)
此下界、(2) 和旧局部证书全部使用同一个 AM13 核，未换成 MT 核。

## 4. 无损滑窗装配、端项与全部真实零点

旧已准入 PC8 证书在所有非负七 gap 上给
Σ_{r=0}⁶b_rg_r+Σ_{0≤i<j≤7}a_ij K(y_j−y_i)²≥c，
c=805003/10⁸；b_r 分子为 (28898,57272,75526,80958,75526,57272,28898)，
分母 10⁸、总和 B₀=404350/10⁸。每个跨度 s 的 Σ_i a_{i,i+s}≤2。
对 m≥8 个有序点的全部 m−7 滑窗叠加，单个 gap 的费用至多 B₀，
单个无序 pair 的累计权至多 2，故正 pair 总能量
                 E≥c(m−7)−B₀ span.                                  (4)
m≤7 时 E≥0 仍满足右式。这里只应用正局部证书，未从 signed 总界限制子集。

固定平滑 f_ε=fχ_ε²/m_ε，m_ε→1，d_ε=∥f_ε−f∥₁→0；
其 Gram U 对角为 1、|U_ij|≤1、|U_ij−K(y_i−y_j)|≤d_ε。
分离子集 S 的指数和用 g≥m_ε f_ε 大筛：U_SS≤(Λ/m_ε)I<2I（先固定 m_ε>61/64）；
因 \widehat g 在所有非零距离 ≥θ 为零，包含等号端点。
于是 φ₂ 在 S 上等于平方，(4) 给
tr φ₂(U_SS)−m≥cm−B₀span(S)−7c−42d_εm：
Σ_s Σ_i a_{i,i+s}≤14，每个平方差 ≤3d_ε，全部滑窗已付。

在全部 n 个简单临界线点中选极大不交 |距离|<θ 点对，剩余 S 是 θ-separated。
每对 2×2 Gram 的谱 1±u≤2，贡献 J_pair=2u²≥2c−6d_ε。
凸谱迹 pinching（不要求 φ₂ 算子凸）把 S 与每个点对相加，得到
                 J(U)≥cn−B₀span(Y)−7c−42d_εn.                        (5)
若 S 空或少于八点，(4) 的同一端项仍覆盖；近对与 S 只组成一次实际列分区。

回到 §2 的全零点 A，不删除离线项、重数或高度端点：
span(Y)≤T log T/(2π)=N(T)+o(N(T))，旧全域能量证明直接适用 f_ε。
先固定 ε 令 T→∞，再 ε→0，将 (5) 代入 (1)，并用 AM 自己的
C_AM=C_MT+Σc_j²(1/2−1/(4π²j²))/(2sin²(1/√2))、
已准入严格包络 2−C_AM>67216841/10⁸，得到无条件解析推论
       liminf N₀^s(T)/N(T) ≥ (67216841−404350)/(10⁸−805003)
                         =66812491/99194997≈0.6735469834229644.        (6)
相较外论文有理比例，精确差为正（约 0.0008783241 个百分点）。
这是旧有限证书配新无损装配的推论；是否属于文献新纪录尚需外部前沿与不同作者复核。

## 5. 实际研究范围及下一命题

外论文 §7 的 .67357/.67383 只限制其第二窗、线性 pair/spread 证书方案；
V(f)≤10B(f) 的 .68185 也是规定窗类的方法上限，不是 ζ 实际比例上限。
它们不排除 (6) 的 AM 窗口组合，也不保证更大核奖励必能改善最终比例。
本项目 7/8 是固定宽条带；离线点的归一化虚部可达 (3/8)log T/(2π)，
不能让离线 Hermitian 项变成实点的正 Gram，或免费降低 Q 的正惯性预算。
要进一步研究，可保持同一 AM 窗口、实际全零点能量和 (2) 的 majorant，
证明 separated 七-gap 上
Σa_ij K(dist)²+αΣg_r+Φ(g₀,…,g₅)−Φ(g₁,…,g₆)≥x，
其中 Φ 有界、跨度预算≤2；叠加给 b=7α，再通过同一个 (1) 评估收益，
才能在不删真实零点的条件下提高 (6)。应直接检验 (A₀−7α)/(1−x)>(A₀−B₀)/(1−c)，
不能只比较局部最小值或忽略 storage 边界。该新证书尚未证明。
