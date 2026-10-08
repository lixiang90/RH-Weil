# 480 小一次素因子归约与完整四矩传递：独立数学全文审查

2026-10-08。审查人：checkpoint_audit。结论：**限定 PASS**。

本轮全文实读最终480共185行、新自然子族研究源329行、476共96行、479共140行，
并重新实核旧最大prefix源及前轮独审的冻结哈希。
旧最大prefix完整证明在本会话前轮已全文实读，本轮复用其数学审查，不重跑旧覆盖。
任务指定工作基线为main 3ea9b39；480正文保留其479研究起点0cb98a7。
本审查只写此新文件，不改源、旧审查、检查器、输出或Git。

## 1. 最终 canonical 绑定与准入边界

canonical UTF-8 LF 只统一CRLF和孤立CR，不trim，不改变EOF。

| 被审文本或使用的冻结依赖 | canonical LF SHA256 | 字节 / 行 |
|---|---|---:|
| [最终480](../../notes/480-original-type-ii-single-prime-part-and-whole-moment-transfer.md) | 13a6cbd697ad960cdb97543090861373f21b6970710bc2d247edac59bb08e791 | 7993 / 185 |
| [完整自然子族研究源](hybrid-original-type-ii-small-single-prime-part-fourth-research-radial.md) | f0b740a85b09f70b68653bf3ec06288150876f1f761920ffb1107620fbf44580 | 11658 / 329 |
| [该源前轮不同作者全文独审](hybrid-original-type-ii-small-single-prime-part-fourth-review-checkpoint-audit.md) | 2066698dfe4079c6a174369cd48e05986d52a14177466f7b38b25fad4c2adb2f | 8197 / 151 |
| [476完整增长前件](../../notes/476-original-fourth-growth-five-sevenths-with-ivic-density.md) | 179829dd25f92ff187359f73455aafad9f957d714df13cf871db47a76e9408b6 | 4448 / 96 |
| [479实际因子归约](../../notes/479-original-type-ii-factor-reduction-and-diagonal-gauge.md) | 6b6e15f8a3a83d62e1d472cbeaa86a894c9e01740ccd682fc79ec99c2ec5a559 | 7029 / 140 |
| [旧完整因子证明和最大prefix引理](hybrid-original-type-ii-short-lambda-factor-fourth-research-radial.md) | b39876e0b9d91a06de57d1069cf6adac676252bd1fe737186bb065716015abb0 | 21261 / 524 |

数学结论保持原signed scalar、genuine-prime m、实际b_V(k)、positive-height窗、
normalizer和共同sharp product endpoints。
第2节子族估计不调用零自由输入；第3节完整增长矩传递则明确消费476在
原[R_{7/8}]下给出的whole上界。这是保留的额外前件，不能从子族估计免费推出。
本文件不绑定尚未完成的检查器版本，也不宣称已经运行其--check。

## 2. 自然分解、零项与全端点成本

逐valuation检查s(k)=prod_{v_p(k)=1}p、t(k)=k/s(k)：
s squarefree、t squarefull且互素，分解唯一；k non-squarefull准确等价于s>=2。
指数3或5的prime全在t，不能用按奇偶valuation定义的squarefree kernel代替s。

rad(k)<=V时所有非零Möbius divisors均已收入原有限和，故b_V(k)=0。
仅使用逆否命题b_V(k)!=0=>rad(k)>V，不假设其逆命题。
互素性及rad(t)^2|t给非零项k=st>V^2/s；对s<=S，严格有k>V^2/S。
480已明确采用从K0=V^2/S起的真实开左闭右dyads K=2^jK0，
因此非空带确有K>=K0及MK<X，无起始dyad跨阈值的遗漏。

squarefull计数及sum_{s<=S}s^{-1/2}给每带O(sqrt(KS))。
真实|b_V(k)|<=tau(k)的subpower upper乘k^{-1/2}，得外L1费用
X^eta sqrt(S)。只在upper中取绝对值，原定义的signed系数不变。
固定k后的m整数区间仍是
(max(M,M0,Y/k), min(2M,X/k)]，先判空再作为两个实际prime-prefix之差。
使用q=Lambda*1_prime自身的最大prefix引理，不能由完整Lambda多项式删项推出。

每带第四均值费用为X^eta S^2(1+M^2/X)。非空带M<XS/V^2，
所以完整子族费用为X^epsilon(S^2+XS^4/V^4)。有限O(log^2 X)带在norm层
合并、再付log^8 X；各固定损失先细分，能吸收到任意最终固定epsilon。

对S=floor(X^{1/20})，S^2<=X^{1/10}、V>=X^{1/8}/2给
XS^4/V^4<=16X^{7/10}。完整四矩7/10、与旧17/24的差1/120，
以及norm差17/96-7/40=1/480均独立重算正确。
R0=D_S+R1是原整数标签的准确分区，不重复已付s=1部分。
合成P_H-R1=(P_H-R0)+D_S后整体误差norm仍为17/96；
两向粗第四矩coupling的常数8来自一次两项不等式，没有连续误乘。

## 3. 完整第四矩 additive 转移的独立证明

在同一测度dt/T和完整窗J_T上记A=||F||_4、C=||G||_4、D=||F-G||_4。
Minkowski先给C<=A+D；反向三角给|A-C|<=D。
故还可不经逐点展开而直接得到
\[
 |\mathcal M_F-\mathcal M_G|=|A^4-C^4|
 \le4D\max(A,C)^3\le4D(A+D)^3.
\]
480的逐点四次差及Hölder给同一界，对复值signed scalar也成立。
测度J_T/T的质量不是1，不影响上述同一测度的Minkowski或Hölder。

前件须理解为：对每个任意先固定的损失eta>0都有
D<<X^{c/4+eta}及M_F<<X^{B+eta}，且c<B固定。
于是A<<X^{B/4+eta/4}，C<<X^{B/4+eta}，先支付G的完整norm；
差值费用为X^{(3B+c)/4+4eta}。
为任意最终epsilon>0，可先取eta=epsilon/8，所有损失严格在最终epsilon内。
常数依赖这些固定参数，不把某个固定较大的epsilon反复当成零损失。

476与479先给M_PH<<X^{B+epsilon}、||P_H-R0||_4<<X^{17/96+epsilon}。
17/24<B=5/7，所以R0完整norm先由Minkowski支付。
同理480第2节支付R1完整norm。因此应用于F=R0,G=R1时，
未知余项的范数前件没有被忽略，也没有从signed子集单调性取上界。

独立Fraction复算：
\[
 \frac{3(5/7)+17/24}{4}=\frac{479}{672},
 \quad \frac57-\frac{479}{672}=\frac1{672};
 \qquad
 \frac{3(5/7)+7/10}{4}=\frac{199}{280},
 \quad \frac57-\frac{199}{280}=\frac1{280}.
\]
两式均是完整窗口第四均值的additive误差，误差仍为正增长幂。
最终epsilon小于对应余量时，差除以X^{5/7}趋零。
这里没有非零主项或下界前件，故不能据此推出两实际第四矩之比趋1。

## 4. 固定delta族、floor与更大准确截断

研究源§5(18)及其证明对全部整数2<=S<=V一致，依赖常数不随S改变。
其真实dyads、实际b_V、两移动端点及外权证明均适用，所以可代入随X变化的S。
令固定0<delta<3/56，a_delta=3/56-delta。
因为0<a_delta<1/8，X足够大时floor(X^{a_delta})>=2且小于V；
所需X0允许依赖delta。用S<=X^{a_delta}和V>=X^{1/8}/2即已支付floor，
不需把floor替成精确幂等式。

两项成本指数是2a_delta与1/2+4a_delta。
后者严格较大，其差为1/2+2a_delta>1/2。因此
\[
 d_\delta=\frac12+4a_\delta=\frac57-4\delta< B,
 \qquad \mathcal M_{D_{S_\delta}}\ll X^{d_\delta+\epsilon}.
\]
R_delta=R0-D_{S_delta}仍为s(k)>S_delta的准确signed剩余。
既有R0完整norm及D子族norm先给R_delta完整norm，然后第三节引理给
(3B+d_delta)/4=B-delta，亦即所列R0/R_delta additive误差。

与P_H的合成第四误差幂为c_delta=max(17/24,B-4delta)，准确有
\[
 c_\delta=B-4\min(\delta,1/672),
 \qquad (3B+c_\delta)/4=B-\min(\delta,1/672).
\]
所有delta和epsilon先固定；不声称delta(X)趋零时的一致常数。
归一化趋零差另须最终epsilon<delta或min(delta,1/672)，与480量词一致。

两个特例独立重算：

- delta=1/280：a=1/20，d=7/10，R0转移幂199/280，P_H转移幂479/672。
- delta=1/672：a=5/96，d=17/24，两个转移幂均479/672；
  合成P_H-Rsharp的norm仍为17/96。

5/96-1/20=1/480。两个floor之比渐近为X^{1/480}，没有更改U,V或原mask。
在显示成本max(2a,1/2+4a)内，要不超过17/24，必须a<=5/96；
在a=5/96时两项均满足。这证明的是该upper估计族内的最大截断幂，
不能排除更强算术估计，也不是完整四矩问题的全局最优性。

## 5. 结论范围与后续检查器边界

最终Rsharp仍包含原k>V中的全部squarefree k，因为此时s(k)=k>V>Ssharp。
balanced genuine-prime m乘prime k亦仍存在。
已付的是完整小s自然子族和已有whole预算下的误差转移；
尚未付的是Rsharp完整signed mixed4的改进、whole常数四矩或whole更低增长幂。
原MT简单比例、引用输入下sigma_*、Hecke全族深度与kappa前件没有得到新反馈。

本轮用独立数学推导及内存Fraction核全部转移指数、两特例和严格余量。
有限有理检查不能认证无限解析估计；均值引理和476增长前件依赖上述
实读证明及已明确保留的引用输入，不因程序PASS而自动成立。
未重新执行旧大核、七点覆盖或外部解析证明。
480的未来检查器/检查点需在其最终版本另作独立审查；本PASS限于上表绑定的数学文本。
