# 原 actual 全背景 cubic 的无 bounded-fourth 前件相对恢复

2026-10-08。作者 compression_bridge。新严格补充，待另一作者全文独审。
只新增本文件，不修改冻结 mixed source、旧来源、math、Goal 或 Git。

设 a_T=TrH⁴/d 为原 genuine-high第四矩。本稿得到

\[
 \boxed{\left|\frac1d\operatorname{Tr}(A C_\Lambda^3)\right|
       \ll\frac{\sqrt{a_T}+1}{L}+o(1).}                 \tag{1}
\]

不先假 a_T 有界。因此较弱的 a_T=o(L²) 已够使此 cubic趋零；
完整四矩比例转换仍需另付适当的常数预算。本稿不提供该预算。

## 1. 原对象、冻结前件与归一化

沿用原 d=floor(XL)、X=T/(2π)、L=logX、finite E、所有 middle P。
H与C_L为原高/低 genuine-prime channels，C=C_pr=H+C_L，
P_pp=C_Λ−C 是全部 original proper powers的原finite差。
A=A0+R_T 是 actual Γ/pole背景减I，A0=E*M_hE。

| 完整输入 | canonical UTF-8 LF SHA-256 |
|---|---|
| [454 actual背景/二矩](../../notes/454-original-background-and-weighted-prime-mixed-traces.md) | 8ab99d60c1b748dc561cac57ee498057a0c9fb19b9778a041261b1bad0750db7 |
| [455 whole proper powers](../../notes/455-whole-proper-power-fourth-norm-and-prime-equivalence.md) | 6bf2025dcc8f56d7b35d9c8b764ac2ff3b911a6e054bf9c496042c7f3e11ce41 |
| [462 entire low4](../../notes/462-original-low-prime-fourth-path-constant.md) | 868adfeb0d742043f39bd08e0783d66b7a9db11316067b0b3b43d80150cdf680 |
| [static high cubic](hybrid-parity-weighted-high-cubic-research.md) | 2f883e521bd8f729084530aa8273acc397b528ce66392df1d7a803e53b43bbae |
| [entire mixed cubic](hybrid-background-entire-mixed-cubic-research-compression.md) | 19c715587681c95c3e8750e4751a30bff798b372f68dc516f029c0a5e71020dd |

最后两源依赖原 fixed-gap[R] θ<9/10。顺序为先固定原profile、θ与
θ<a<9/10，再令T趋无穷；无新的moving family或coefficient准入。
canonical只将CRLF与lone CR转LF，不trim。N/d→1，以下统一以d归一化。

记 ||K||_(p,d)=d^(-1/p)||K||_(S_p)，||K||_(∞,d)=||K||op。
归一化 Schatten Hölder为 |Tr(K1…Kr)|/d≤∏||Ki||_(pi,d)，
Σ1/pi=1。有限归一化单调性给 ||K||_(2,d)≤||K||_(4,d)。

454、455和462已付

\[
 \|A\|_{op}=O(1),\quad\|R_T\|_{op}=O(L^{-1}),\quad
 \epsilon_T:=\|P_{pp}\|_{4,d}=O(L^{-1}),\quad
 c_T:=\operatorname{Tr}C^2/d=O(1),\quad
 \ell_T:=\operatorname{Tr}C_L^4/d=O(1).                 \tag{2}
\]

c_T无需任何high4前件：原整个Λ二矩已付，且
||C||_(2,d)≤||C_Λ||_(2,d)+||P_pp||_(2,d)≤O1+ε_T。
Hermitian H、C_L、C的第四矩均非负。Schatten Minkowski给

\[
 f_T:=\operatorname{Tr}C^4/d
 \le(a_T^{1/4}+\ell_T^{1/4})^4\le8(a_T+\ell_T),
 \quad \sqrt{f_T}\ll\sqrt{a_T}+1.                    \tag{3}
\]

这里没有把原finite channels替换为physical词，也没有声称 f_T有界。

## 2. static全部三次项与actual R_T

mixed source付清 C_L³、三种HLL与三种HHL，共七个有low的原finite词。
static high source给 |Tr A0H³|/d≪sqrt(a_T)/L，无boundedhigh4前件。
因此存在原已付 r_T→0，使

\[
 |\operatorname{Tr}(A_0 C^3)|/d
 \ll\sqrt{a_T}/L+r_T.                                \tag{4}
\]

actual Γ/pole误差不能取粗三次 S4预算 f_T^(3/4)。用已付二矩，
将 R_TC³分成(R_TC)C²，两边取 normalized S2：

\[
 |\operatorname{Tr}(R_TC^3)|/d
 \le\|R_TC\|_{2,d}\|C^2\|_{2,d}
 \le\|R_T\|_{op}\sqrt{c_T}\sqrt{f_T}
 \ll(\sqrt{a_T}+1)/L.                                \tag{5}
\]

(4)–(5)故已恢复 actual背景配原prime cube的相对界，未先写无条件o。

## 3. 全七个proper-power非交换词

令 P=P_pp，仅在本节为书写简便，绝不改变原carrier projection。
准确展开

\[
 (C+P)^3-C^3=C^2P+CPC+PC^2+CP^2+PCP+P^2C+P^3.         \tag{6}
\]

记 M_T=||A||op=O1。下面每个有限迹只用 cyclicity与 Hölder：

| 词 | 归一化迹预算 | 采用的Schatten配对 |
|---|---|---|
| Tr AC²P/d | M_T sqrt(f_T) ε_T | AC²的S2；P的S2≤ε_T |
| Tr ACPC/d=Tr CACP/d | M_T sqrt(f_T) ε_T | CAC的S2≤||C||4·||AC||4；P的S2 |
| Tr APC²/d=Tr C²AP/d | M_T sqrt(f_T) ε_T | C²的S2；AP的S2 |
| Tr ACP²/d | M_T sqrt(c_T) ε_T² | AC的S2；P²的S2=ε_T² |
| Tr APCP/d=Tr PAPC/d | M_T sqrt(c_T) ε_T² | PAP的S2≤||P||4·||AP||4；C的S2 |
| Tr AP²C/d=Tr CAP²/d | M_T sqrt(c_T) ε_T² | CA的S2；P²的S2 |
| Tr AP³/d | M_T ε_T³ | AP的S2≤M_Tε_T；P²的S2=ε_T² |

表中所有S2、S4均采用第1节的d归一化，所以指数和严格为1；
无多余d因子。P为Hermitian原proper-power差，||P²||_(2,d)=ε_T²；
C同理 ||C²||_(2,d)=sqrt(f_T)。没有交换 A、C、P，也没有漏掉CPC/PCP。
全部七词因此给

\[
 \left|\operatorname{Tr}A(C_\Lambda^3-C^3)\right|/d
 \le M_T\{3\sqrt{f_T}\epsilon_T
        +3\sqrt{c_T}\epsilon_T^2+\epsilon_T^3\}
 \ll(\sqrt{a_T}+1)/L.                                \tag{7}
\]

结合(4)、(5)、(7)即得(1)。原proper powers、全height、Gamma与pole
都在actual恢复中；未知high4只以真实 a_T出现在相对费用里。

## 4. 结论范围

若 a_T=o(L²)，(1)给 Tr A C_Λ³/d→0。若 a_T bounded，则自然包含在内，
并可供整个centered四矩的常数预算使用，去除454中此前的Cauchy cubic
附加费用。若只知 a_T有增长幂上界，本稿不能推出cubic趋零。

这里没有付清 a_T的任何新上限，未付 whole31、distinct22或Γ目标预算。
它只降低 actual cubic恢复所需的增长前件，并提供准确relative误差；
不会自行产生更高零点比例、无零边界或RH证明。
