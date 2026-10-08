# 真实高产品 minor shifted covariance：不同作者全文审查

2026-10-08，perron_reviewer。只新增本审查；作者源、冻结输入与 Git 未动。
**限定 PASS：准确有限身份、已付对角及条件联合接口成立。**
没有证明 JSC、新 paid 频率族、whole 四矩、常数预算、比例或无零边界。

已 FULL READ
[324行被审源](hybrid-original-high-product-minor-shifted-covariance-research-high-product.md)，
14620 canonical LF bytes，SHA256
d270d7c6b877a7d993529a9c2b19b426b5f9c2d37eb3e1d50650a56671193ae7。
canonical规则仅统一 CRLF/lone CR，不 trim。

本轮 FULL READ 489（85行，SHA c39081acaf5d1bd22685df4a918d42b1bffa635bb15a09b41b66794654ecdddd）
及246素数腿源（SHA 1790bc3878900e88c89d2ba3b51ba0cf06e85583e353879df0e9a514bfd79b0f）；
337源已全文读取并独审，本轮复核其原 mask、共同参数和准确未付域，
SHA56219e9f136c0f0666c5b1ce028ec4d7d93ad33f5ebd43d5e4a5e34c399677a8。
actual425已在前轮全文读取；本轮重读minor464§7，
其冻结SHA b6018e1254049b77dd5d7f73f4d3a7dc7272d5fe5dd3568f3c5ddf8cf73928b4。

## 1. 实际域与整数 Fourier 合并

真实剩余保留 \(qs>Z\)、最大 prime q、strict \(s,p,r<q\)、
dyadic两端、interior、同-u与全部profile。
旧 \(d\le W\) 的 \(W/(dS)\) 弧和新 \(W<d\le B\) 的 \(1/S\) 弧
均对整数平移不变，所以 remaining mask只依 \(n\bmod q\)。
它保留337的准确两套条件，未改为 \(B/(dS)\)；
\(d=1\) 已使 \(q\mid n\) 不在实际域。

先用 \(\nu\) 零支撑得到共同 \(J_q\)，再作共同参数分离。
真实 \(S_q\) 的 q-dependent interval及 p/r 的 q-prefix始终保留；
这属于实际mask，不是为每个 q,n另选私有系数。
各腿系数的平方和由原 prime 权与 dyadic整数谐和和给 \(O(1)\)，
twists模为1，prime-product至多两有序factor pairs，也包括 \(p=r\)。
原 \(p=s,r=s\) 修正沿337原正能量合同另付，未以signed总界删出子mask。

准确相位为 \(h=qs-pr\)，不是 \(s(qs-pr)\)。
因为 \(qs,pr\in(0,q^2)\)，其支持是 \(-q^2<h<q^2\)；
prime q不整除pr，所以 \(q\nmid h\) 且 \(h=0\) 不可能。
每个 folded residue可有两个实际h，故必须保留正负层。
两h collision的差条件确为
\[
 q(s-s')-(k-k')=j q^2,\qquad j=-1,0,1.
\]
这与已付 physical lattice tails不同；未免费删掉任何alias。

## 2. Parseval unit subtraction与跨q collision

完整 \(q^2\) Parseval给 \(q^2\sum_\gamma|\widetilde D_{q,\gamma}|^2\)。
在 \(n=qj\) 上，\(F=\sum_sA_s\)，G是 k modq 的 additive Fourier 和；
其总能量准确为
\[
 q\left|\sum_sA_s\right|^2
       \sum_{v\bmod q}\left|\sum_{k\equiv v(q)}C_{q,k}\right|^2.
\]
所以源(8)的减项、q因子及符号正确；\(q\nmid h\) 不使该能量消失。

逐h Cauchy和最多两层折叠给 \(\sum_\gamma|\widetilde D|^2\ll S\)，
完整q²能量因此为 \(Q^3S L^C\)。
另独立核源(10)的prime collision计数：
k=k'强制 \(\ell=0,j=0\)，全q费用 \(O(Q)\)；
k≠k'先要求 \(q\mid k-k'\)。
非零 \(|k-k'|<X^2\) 最多有三个不同的 prime 因子 q>\(\sqrt X\)，
否则四个的乘积已大于X²。每个q最多三个j并唯一确定ell。
用真实共同正 envelope \(c_k^+\) 与 \(|A_q(\ell)|\le1\)，
得到至多 \(9(\sum_kc_k^+)^2\ll PRL^C\)。
因此真实结论是 \(Q+PR\ll QS\)，乘q²后仍为 \(Q^3S\)；
没有将PR项或q²因子遗漏为虚假省幂。

## 3. 真正 mask 核及系数对角

\(\mathcal W_q(v)=\sum_{n\in N_q}e(nv/q^2)\) 是Hermitian有限核；
其相应Gram为正能量，但单个核值可以复数或负实部。
准确展开 \(F G\) 平方给源(12)—(13)的
\(A_q(\ell)B_q(t)\mathcal W_q(q\ell-t)\)，符号和全部项正确。
尤其 \(\ell=0,t\ne0\)、\(\ell\ne0,t=0\) 不能按完整周期免费删除。

唯一的系数对角 \((\ell,t)=(0,0)\) 为
\[
 D_\lambda=\sum_q|N_q|(\sum|A_s|^2)(\sum|C_{q,k}|^2)
       \ll Q^2X/S\,L^C.
\]
其余真实和C为实数且可负；\(E=D+C\) 是正能量。
n=a+qj的重排给
\[
 \mathcal W_q(q\ell-t)=
 \sum_{a\in A_{q,S}}e(a\ell/q-at/q^2)
          \sum_{j\in J_{q,a}}e(-jt/q).
\]
jell是整数，故没有残留该相位。a minor mask与实际 j区间仍耦合，
未把它们换成独立矩形。D付款不是原signed频率子族的独立付款。

## 4. 一侧JSC的严格消费与范围

\(\sum_qb_q^2|N_q|\ll QX/S\)，原前因子S/(QX)与同一joint能量
Cauchy准确给 \(|K_{\rm box}(\lambda)|^2\ll S E_\lambda/(QX)\)。
原非负共同参数 envelope可积；再一次参数Cauchy给源(17)。
因此只须 \(\int w C_\lambda\le C Q^3X^{-j}L^{C_0}\)，
不需要绝对值或下界。结合已付D后得到
\[
 |K_{\rm box}|\ll[\sqrt Q+Q\sqrt{S/X}X^{-j/2}]L^C.
\]
条件量词与不可积twist常数排除正确，没有私选不同参数。
这仍是准确raw双腿block的接口，原已付s排除修正继续另加。

在 \(Q=X^u,S=X^w\) 的费用表示中，
\(u+w/2-1/2-j/2<5/7\) 恰等价于 \(j>2u+w-17/7\)。
用 \(u\ge w,u+w\ge1193/700-O(1/L)\)，inf门槛为179/1400；
balanced u=w=1为4/7。sqrtQ费用始终低于5/7。
只有已证明JSC且严格满足门槛的实际boxes可被消费；
源明确尚未证明JSC，也未将局部条件推广为全余项付款。

## 5. 高矩独立Hölder比较

在同一有限正测度上，p=3、4的共轭指数为p/(p−1)≤2；
有限测度嵌入确给
\(\int|FG|\le\|F\|_p N^{1/2-1/p}\|G\|_2\)。
power mean又给 \(\|F\|_p N^{1/2-1/p}\ge\|F\|_2\)。
它比较的是实际范数，正确限制为“不新增算术信息时指数换位无省幂”；
不排除未来高矩证明更强F²、其它G矩或joint分布。
计数测度下将b_q吸收进F后仍是同一实际mask，比较没有换测度。

未发现需改324源的缺口。限定PASS只准入其精确结构、对角和条件接口；
尚缺实际六腿covariance估计，现有whole、常数预算、比例和strip均保持。
