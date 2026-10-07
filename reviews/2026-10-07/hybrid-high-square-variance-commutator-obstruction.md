# 原 high 平方方差的严格非零下界：PSD 与实际交换子

2026-10-07。twisted_research。独立推导，待全文独审。
本稿只新增文件，不修改465、旧推导、math、脚本、输出或 Git。
新结论是原 flat 对象的 q_T 有严格非零下界，因而465的
q_T≤1/1600充分前件不可达到。它不是原 fourth-budget 不可改善的证明。

## 1. 同一实际矩阵与前件

沿用原 X=T/(2π)、L=log X、d=⌊XL⌋、E、P、Q、even C² taper。
H=E*B_HE为genuine high primes的原 finite Hermitian channel。
W=E*M_wE是同high素数的原 bounded diagonal multiplication，
w≥0。令

Γ=H²−W，q_T=||Γ||HS²/d，
K_T=||[H,W]||HS²/d，M_T=||W||op。

来源：
[454](../../notes/454-original-background-and-weighted-prime-mixed-traces.md)
的全部log-range加权二矩、commutator与投影泄漏；
[high parity稿](hybrid-high-parity-gram-and-mobius-completion-research-radial.md)
的actual Γ定义；
[465](../../notes/465-centered-high-square-joint-fourth-budget.md)
的同对象W。465最终修订输入canonical SHA为
a9290d2d847c2a3f7942b26353bd1582a68b391e481acc109c4ac18d3d750464。

本稿全部估计不需要[R]、H⁴ bounded、低四矩或新的素数相关。

## 2. 任意有限PSD W的严格不等式

在H的eigenbasis中记特征值λ_i、w_i=W_ii∈[0,M_T]，
Δ_i=λ_i²−w_i，
r_i=Σ_{j≠i}|W_ij|²。定义

x_T=d⁻¹Σ_iΔ_i²，
y_T=d⁻¹Σ_{i≠j}|W_ij|²，
μ_T=d⁻¹TrΓ=d⁻¹Σ_iΔ_i。

因为H²在此basis对角，而Γ_off=−W_off，严格有

q_T=x_T+y_T。                                          (1)

交换子直接计算给

K_T=d⁻¹Σ_{i,j}(λ_i−λ_j)²|W_ij|²
   ≤4d⁻¹Σ_iλ_i² r_i。                                 (2)

W²≤M_TW给
r_i≤w_i(M_T−w_i)≤M_T²/4。
再用λ_i²=w_i+Δ_i≤M_T+Δ_i，负Δ_i项可以删除，得到

K_T≤4M_T y_T+M_T² d⁻¹Σ_iΔ_i^+。                       (3)

注意(3)是特定eigenbasis中的有限PSD估计，没有对H²与W平方排序。
由Δ^+=(|Δ|+Δ)/2及标量Cauchy，

K_T≤4M_T y_T+(M_T²/2)√x_T+(M_T²/2)|μ_T|。             (4)

该有限式不预设q_T有界。

## 3. 原trace与commutator准入

454的physical high二矩给Tr(E*B_H²E)=d〈w〉+o(d)。
TrH²=Tr(E*B_H²E)−||QB_HE||HS²，后项o(d)，
而TrW=d〈w〉准确。因此

μ_T→0。                                                (5)

actual commutator必须保留内部P：

[W,H]−E*[M_w,B_H]E
 =−E*M_wQB_HE+E*B_HQM_wE。

其HS≤2||B_H||op||QM_wE||HS
≪√(X log(2L))/L=o(√d)。
physical D=[M_w,B_H]的shift coefficient恰是
φ(u)φ(u+s)[w(u)−w(u+s)]。
w及原φ的一二阶derivative L1统一有界，所以同原乘法/shift leakage
给||QDE||HS²≪X log(2L)/L²=o(d)。

454的weighted二矩首先给||DE||HS=O(√d)，再比较上述HS小误差。
因此平方范数差为o(d)，没有循环使用待证的actual界。
其实际极限为

Kψ=a⁻²∫_{−1/2}^{1/2}ψ(v)
       Σ_{ε=±1}∫_{1/2}^1
       r ψ(v+εr)[d_H,ψ(v)−d_H,ψ(v+εr)]² dr dv。        (6)

区间外ψ为零。此式保留共同profile和实际zero-extended translations。
不同prime frequencies的Hilbert、carrier、sum alias全部由454支付，
故K_T→Kψ，而非只对formal physical reference计算一个常数。

## 4. Flat常数的独立精确积分

flat仍保留原endpoint taper。d_H(v)=t(t+1)/2，t=|v|，
uniform Mertens界与a_L→1给

M_T≤||w||∞≤3/8+o(1)。                                 (7)

有限w在端点为零；(7)仅为asymptotic sup bound，未把它当作每个T
exact M_T=3/8。对r∈[1/2,1]，非零正shift的t∈[r−1/2,1/2]，
d_H(t)−d_H(r−t)=(2t−r)(r+1)/2。
两signs给

K1=2∫_{1/2}^1 r∫_{r−1/2}^{1/2}
       [(2t−r)(r+1)/2]² dt dr
  =(1/6)∫_{1/2}^1r(r+1)²(1−r)³dr
  =41/10080。                                          (8)

本次Fraction展开有理多项式独立核到该常数。

## 5. 严格排除465的Q前件

如果limsupq_T≤Q，(4)–(8)首先给粗充分限制

41/10080≤4MQ+(M²/2)√Q，M=3/8。

Q=1/1600时右边等于69/25600，严格小于41/10080；
两者差为2213/1612800>0。因此

limsupq_T≤1/1600不可能。                              (9)

该结论否定的是原flat对象上的这个额外前件。
465的有限代数、conditional implication与LP比例公式仍正确；
其“下一实际付款目标”现已依466调整，不能当作已证可达的方差目标。

## 6. 更精确的统一非零下界

还可保留x_T+y_T=q_T，在固定q上优化(4)：

f_M(q)=max_{0≤x≤q}[4M(q−x)+(M²/2)√x]
      ={
         (M²/2)√q，                       q≤M²/256；
         4Mq+M³/64，                      q≥M²/256。
       }                                                (10)

最优interior x=M²/256。每个有限T都满足
K_T≤f_{M_T}(q_T)+(M_T²/2)|μ_T|。
若liminfq_T有限，沿取得该liminf的subsequence传极限即可；
若liminf无穷，下界当然成立。
因K1>M³/32=27/16384，反解在第二段，严格得

liminfq_T≥(41/10080−27/32768)/(3/2)
         =33479/15482880
         =0.002162323805390212…>1/1600。                (11)

因此这是actual high square variance的非零下界，
不是通用模型矩阵的反例或physical R范数下界替代。

## 7. 仍允许的研究方向

(11)没有给q_T的upper，也没有给whole fourth的必要最小常数。
465的粗Cauchy envelope在较大q上可能失效，但更准确joint covariance
或commutator可在不改变实际原对象的情况下改善整个31/22预算。
尤其Γ与low平方残差的相关可以支付或排除某些粗√(q e)的最坏情形。

本稿不从这个下界推断新比例不可能、当前原路线无效或RH结论；
它只证明一个此前提出的足够小Q目标在实际同flat配置中不可达到。
