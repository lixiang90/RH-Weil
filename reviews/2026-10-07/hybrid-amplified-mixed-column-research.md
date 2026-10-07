# \(ua^6\) 对实际 \(\mu\times1\times1\) mixed 列的放大、spike 保留与原矩费用

2026-10-07。新研究。**支付了整个 actual mixed column 的 exact sixth-power transfer、原 tuple/合并列范数、natural masks、positive physical slot 的保留及原矩调用的连续前向指数。没有支付新的 \(\chi>0\)，没有新边界。** 放大本身合法；缺口不是简单的 product 非封闭，也不是列范数爆炸。

本轮开始时 main 为 1a51f5767f217c3dc02cd97ff2233d25cd8dd186，工作区 clean。本报告只新增此文件；三份正式论文、450–453、既有审查/脚本/output 和外部 math 源未修改。

## 1. 固定源与实际对象

只读源为
E:/codex-build/math/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/build/paper.tex，
固定 commit adc7f1241b42e322a6451854ab7e4b4c146bf78a。
本轮实际重算 canonical LF SHA256：

~~~text
42a5ee0febca59fd1def55cfd6c6808c322ef4237d7726303ea52f711deac6a3
~~~

canonical LF 仅作 CRLF、孤立 CR→LF。全文通用 source lemmas 仍为明确 [R]，没有在此认证 whole kernel/whole chain。

关键实际原句及行号：

- 590–606、627–639：固定 \(S\)、primary ideals、所有 residue powers 的零延拓；六整除指数仍为 coprimality mask。
- 705–726：中心归一化 \(M,S\)、原 masks 和 two plain factors 的同一完整 row character。
- 4348–4366、4385–4416、4423–4431：primitive buffered-bin bounds、polynomial-size deleted Euler products、原 dyadic pointwise bounds和真实 finite-height Mellin argument。
- 6940–7002、12492–12521：固定 \(\Theta\) coefficient lists、underlying disjoint supports、displayed moving radicals与共同 puncture，禁止外加的 row-dependent column coefficients。
- 7663–7795、7934–7967：generic reflected-energy 的实际 completed/dual input 与 coefficient independence；任意 \(\beta(n,b)\) 只出现在已经得到的规定 dual form 中。
- 9231–9268、9311–9314：marked moment 的准确 squarefree \(\mu\) coefficient、一次原 prime product、两个 strict widths及禁止额外 residual \(b(n)\) 的原句。
- 12343–12475：原 no-slot raw moment、scale supremum、\(ua^6\) identity、injectivity、rowwise profile/height费用。
- 12531–12578：原 plain fourth moment；\(\kappa<3/4\) 的调用须使用已冻结450扩展证明，不能改写原句的范围。
- 14997–15013、15064–15170：原 physical \(Q_i\)、实际 amplitude bins、一次 whole-slot selection、共同 character orientation 与高度。

固定一个 actual critical joint stratum，写
\[
 D=U^\ell,\quad X_s=U^m,\quad
 Q_u=\prod_{i\in I}Q_{u,i},\qquad P_i=U^{w_i},\quad z=\sum_{i\in I}w_i,
\]
\[
 Q_{u,i}=P_i^{-1/2}
 \sum_{p\in\mathcal P_i}c_i(p)\psi_u(p)W_i(q_p/P_i),\qquad
 \psi_u(n)=\nu(n)\chi_n(u)^\varepsilon.
\]
选中的 \(c_i\)、underlying supports、physical parameters与原 profiles 均保留。\(\nu\) 和 \(\varepsilon\) 在当前 row sum 内固定；不同 witness 可以有不同 Fourier heights。目标正是
\[
 H_{\rm mix}=\sum_{u\in C}
 |M_u(D;W_L)|^2|S_u(X_s;W_s)|^4|Q_u|^2.
 \tag{1}
\]
原 core、同一 \(\psi/\rho\) 与共同高度准入来自
[上一实际 mixed 推导](hybrid-critical-neighborhood-mixed-witness-research.md)；
本报告不以 target 定义新 coefficients 或新算子。

## 2. 行放大确实 injective；增加的零不能擦掉

取 good primary ideal \(a\)，\(q_a\le A\)，令 \(v=ua^6\)。原 \(u\) 的所有 prime valuations ≤5。由 source 12437–12444：
\[
 (u,a)\longmapsto v
\]
injective，包括 \(u\) 的单位；不要求 \((u,a)=1\)。各 prime valuation 的余数 modulo six 恢复 \(u\)，商恢复 \(a\)。

零延拓给准确恒等式
\[
 \psi_v(n)=\psi_u(n)1_{(n,a)=1}.
 \tag{2}
\]
原 \(S\) 和 \(u\) 的自然零仍在；\(a\) 只增加 \(\operatorname{rad}a\) 上的 redundant zeros。不能把 \(\psi_v\) 换成其 primitive inducing character而漏掉这些零。

\(F((ua^6)^{1/6})=F(u^{1/6})\)，所以在 prime-to-\(a\) ideals 上 primitive inducing character不变。固定 \(\nu\) 不变，原 \(\Theta\) exclusion/nonprincipal资格也不变。原 conductor bound仍为 \(C_{\mathcal A}U\)，新增 deleted radical 的 norm最多
\[
 q_{\operatorname{rad}(ua)}\le q_{\operatorname{rad}u}\,q_{\operatorname{rad}a}
 \ll UA.
\]
这里 conductor不增长到 \(UA^6\)，不等于可以把输出的 row-count width \(UA^6\) 免费改成 \(U\)。

自然 \(\chi_n(v)\) 的零是允许的 varying row zeros。若将 \(a\) 的零从它抽出为 \(\rho_v\)，再称为 arbitrary row-dependent puncture，便越过原 class。保持(2)的自然零即可避免这一错误。固定 \(a\) 时将它作共同 puncture另行调用 plain 是允许的选择，但随后须把所有 \(a\) 外层求和；不能既冻结 \(a\) 用原 row width、又领取 broadened-row amplification 的计数收益。

## 3. 整个 mixed column 的 exact identity

令 \(\mathcal B=\operatorname{rad}a\)。原 source 12427–12428 给
\[
 M_u(D;W_L)=
 \sum_{d\mid\mathcal B}\mu(d)\psi_u(d)q_d^{-1/2}
 M_v(D/q_d;W_L).
 \tag{3}
\]
每个 plain factor 需拆掉列的完整 \(a\)-part，不限 squarefree：
\[
 S_u(X_s;W_s)=
 \sum_{h\mid a^\infty}\psi_u(h)q_h^{-1/2}
 S_v(X_s/q_h;W_s).
 \tag{4}
\]
非空 annular support使有效 \(h\) 有限。证明就是唯一分解列 \(n=hn'\)，\((n',a)=1\)，然后使用(2)。若 \(u,a\) 共 primes，相关外部 \(\psi_u(d)\) 或 \(\psi_u(h)\) 自动为零；无需添 \((u,a)=1\)。

原 prime slot精确分裂为
\[
 Q_{u,i}=Q_{v,i}+R_{u,a,i},\qquad
 R_{u,a,i}=P_i^{-1/2}
 \sum_{\substack{p\in\mathcal P_i\\p\mid a}}
 c_i(p)\psi_u(p)W_i(q_p/P_i).
 \tag{5}
\]
\(Q_{v,i}\) 保留完全相同的 underlying list 和 fixed coefficients。新 \((p,a)=1\) 恰来自其 natural zero，而不是新 external mask。\(R_i\) 的 \(p\mid a\) 是 row/amplifier-dependent scalar部分，不能再塞入 source 的 fixed prime-slot coefficient。

因此
\[
\begin{split}
 M_u(D)S_u(X_s)^2Q_u
 ={}&\sum_{J\subseteq I}
 \sum_{\substack{d\mid\mathcal B\\h_1,h_2\mid a^\infty}}
 \frac{\mu(d)\psi_u(dh_1h_2)}
 {\sqrt{q_dq_{h_1}q_{h_2}}}\\
 &\times M_v(D/q_d)S_v(X_s/q_{h_1})S_v(X_s/q_{h_2})
 Q_{v,J}\prod_{i\notin J}R_{u,a,i}.
\end{split}
 \tag{6}
\]
这是整个 \(\mu\times1\times1\) tuple列的保留，不只是逐个 \(M\) 的 identity。没有新 \((d,h_1)=1\)、\((h_1,h_2)=1\) 等 pairwise gcd限制；它们都可能共享 \(a\) 的 primes。

对于固定有限 \(|I|\)，有
\[
 \prod_{p\mid a}
 \frac{1+q_p^{-1/2}}{(1-q_p^{-1/2})^2}
 \ll_\epsilon q_a^\epsilon,\qquad
 |R_{u,a,i}|\ll_{\epsilon,\mathcal A}q_a^\epsilon P_i^{-1/2}.
 \tag{7}
\]
第一式是(3)和两份(4)的准确 \(L^1\) coefficient mass。对充分大 primes，每个 local factor ≤\(q_p^\epsilon\)，有限小 primes进入常数；不要求 \(a\) squarefree，也不产生 \(A^{c}\) 的固定 power损失。平方后删除 slot有真实 \(P_i^{-1}\) 因子。

## 4. 原列范数、fiber及 column sixth-power compression

不带 slots 时，原 normalized tuple
\[
 (DX_s^2)^{-1/2}\mu(r)
 W_L(q_r/D)W_s(q_b/X_s)W_s(q_c/X_s)
\]
的 squared \(\ell^2\) mass为 \(O(1)\)，由三个 annular ideal counts直接得到。合并 \(N=rbc\) 后，一般不是原 \(M\) 或原 \(S\)，但范数仍不爆炸：
\[
 \sum_N|\beta(N)|^2\ll_\epsilon(DX_s^2)^\epsilon.
 \tag{8}
\]
每个 fiber最多 \(d_3(N)\)，故按 fiber Cauchy 后使用 divisor bound即可。加入有限一次原 slots同理；total column scale为
\[
 T_{\rm col}=DX_s^2\prod_{i\in I}P_i=U^{\ell+2m+z}.
\]
原独立 profiles及所有 ratio norm twists仍在 coefficients中。

(6)的每个 term重新 normalized 的 tuple \(\ell^2\) 仍 \(O(1)\)，grouped \(\ell^2\) 仍 \(T_{\rm col}'{}^\epsilon\)，其中
\[
 T_{\rm col}'=
 \frac{DX_s^2\prod_{i\in J}P_i}{q_dq_{h_1}q_{h_2}}.
 \tag{9}
\]
外部根因子和被删除 slots 的 \(P_i^{-1/2}\) 就是全部 normalization成本。不能把 \(X_s\) 的两个原 scale变成一个 scale后忘掉单独 annuli。

具体 fiber也可算清：对某 prime的 exponent \(e\)，\(r\) exponent0有 \(e+1\) 个 positive tuples，exponent1有 \(e\) 个 negative tuples，共 \(2e+1\) 个。没有 profiles时 local sum为1，裸 \(\mu*1*1=1\)。独立 annular tests、truncated inverse cutoff、实际不同 Fourier heights使各项的权重不同，不能从这个裸恒等式推出该 actual block是 plain。

若另对 grouped column作 \(N=c b^6\)、\(0\le v_p(c)\le5\) 的压缩，则准确 character为
\[
 \chi_N(u)=\chi_c(u)\,1_{(u,b)=1}.
 \tag{10}
\]
列的 radical必须保留为 \(\operatorname{rad}(cb)\)，scale是 \(q_cq_b^6\)。固定 ray phase \(\nu(N)=\nu(c)\nu(b)^6\) 也必须保留，不假定任意 \(\nu\) 的六次幂为1。只保留 \(c\) 的 map不是injective；即便保留 \((c,b)\)，\(c\) 也可含 powers2–5，而非 squarefree \(\mu(c)\) column。新的 \(1_{(u,b)=1}\) 不能因 exponent6的primitive phase为1就删除。行 injectivity不解决这一 column问题。

## 5. exact amplified transfer及高度

将(6)按(7)作 weighted Cauchy，平均 \(q_a\le A\)。原 source的 good ideal count至少 \(c_{\mathcal A}A\)。再用行 injectivity，得到
\[
\begin{split}
 H_{\rm mix}\ll_\epsilon A^{-1+\epsilon}
 \sum_{\substack{v\\q_v\ll UA^6}}\sum_{J\subseteq I}
 \left(\prod_{i\notin J}P_i^{-1}\right)
 \sup_{\substack{0<D'\le D\\0<X_1',X_2'\le X_s}}
 |M_v(D')S_v(X_1')S_v(X_2')Q_{v,J}|^2 .
\end{split}
 \tag{11}
\]
右侧可先只含实际 image rows，再按正性扩大；相应 rowwise tests由唯一恢复的 \(u\) 定义。(11)是新支付的有效 inequality，不是已支付的 mixed raw moment。

缩短 scales时，原 profile argument保持相同：
\[
 q_{dn'}/D=q_{n'}/(D/q_d),\quad
 q_{hn'}/X_s=q_{n'}/(X_s/q_h).
\]
所有 \(\sigma_u,\gamma_u-\nu_+\)、\(\gamma_u-\nu_-\)、physical heights和common orientation原样保留，没有强迫 \(\nu_+=\nu_-\)。cutoff \(W_L\)仍是原 stratum的 test；不能改成新的 detector cutoff。

joint scale supremum若已有其对应 moments，可由三变量 logarithmic Sobolev支付，derivatives只是 \(-W/2-yW'\) 等有限 tests。非空 scales位于 bounded log-ranges，unit/空区间直接处理；loss为 polylog和固定 \((1+T_1)^B\)。原 source 12400–12408只证明 single \(M\) scale supremum；12457–12475允许有限 test参数。它们没有单独证明(11)中 product的 mixed scale moment。必须先有 uniform mixed raw输入，才可应用相同 Sobolev argument。

## 6. 新增零仍保留 positive physical slots和近原尺度 spikes

这是比“product不封闭”更具体的 positive结果。固定原 mesh、positive selected slots与有界 amplifier exponent \(A\le U^{p_{\max}}\)，故 \(w_{\min}=\min_{i\in I}w_i>0\) 固定。由(7)，先选足够小的 divisor loss，可对所有 \(a\) 一致得到
\[
 |R_{u,a,i}|\ll U^{-w_i/4}.
\]
实际 selected slot有 \(g_i>0\)、\(|Q_{u,i}|\ge P_i^{g_i}\ge1\)。因此充分大 \(U\) 时
\[
 |Q_{v,i}|\ge\tfrac12|Q_{u,i}|,\qquad
 |Q_{v,I}|^2\ge 4^{-|I|}|Q_{u,I}|^2.
 \tag{12}
\]
这使用实际短 prime列表和原 coefficients，不借 cancellation或 prime independence。自然 deletion不能使 positive slot的 spike在放大后消失。zero-length bounded slots需直接计数；当前 positive physical slots不是这种情况。

还可保留近原尺度的 witness spike。原 \(\psi_v\) 与 \(\psi_u\) primitive buffered bins相同；新增 mask norm为 polynomial \(UA\)。由 source 4348–4366 的 deleted-product bounds及原有限高度 Mellin证明，原 bin pointwise bounds对这些 presentations仍成立，loss可任意小。特别在当前 \(m<1/2\) 范围，缩短尺度后
\[
 |M_v(U^{\ell-t})|\ll U^{\delta(\ell-t)/2+\epsilon},\quad
 |S_v(U^{m-t})|\ll U^{\delta(m-t)/2+\epsilon}.
\]
这里 conductor仍按 \(U\)，polynomial deleted radical只付小量；不是假定 output宽度 \(UA^6\) 的全新零点信息。

固定 \(\tau_s>0\)。在(3)中 \(q_d\ge U^{\tau_s}\) 的全部项，结合 \(q_d^{-1/2}\) 与此 pointwise bound，最多为
\[
 U^{\delta\ell/2-(1+\delta)\tau_s/2+\epsilon}\,A^\epsilon;
\]
(4)中 \(q_h\ge U^{\tau_s}\) 同理。先令 detector/real/divisor losses充分小于 \(\tau_s\)，它们不足以承担原 saturated factor。因此对每个 amplifier \(a\)，分别存在
\[
 d\mid\operatorname{rad}a,\quad h\mid a^\infty,\qquad
 q_d,q_h\le U^{\tau_s},
\]
使某个 \(M_v(D/q_d)\)、\(S_v(X_s/q_h)\)仍保留原 saturation，只有可任意小的 exponent loss。两个 plain copies可使用同一个 \(h\)。联同(12)，放大行上确有近原 lengths的同时 inverse/plain/prime spikes。

有限 dyadic subdivision与 rowwise Sobolev可以支付选择 scales；不得把选中的 scale直接当作 fixed across rows。这个结论没有产生独立 covariance saving，却消除了“新增 gcd删除全部spikes”的错误捷径。

## 7. 将原 marked/plain合同代入的真实前向指数

下面只优化可明确调用的原 moments加原 pointwise bounds，不声称所有 mixed机制的最优性。令
\[
 UA^6=U^\eta,\quad \eta\ge1,\qquad
 E(\eta)=\eta-\frac{\eta-1}{6}=\frac{1+5\eta}{6}.
\]
固定 \(\eta\) 范围，严格 margins/小量先付后可以逼近以下 zero-loss exponents。primitive \(\Theta\)资格保留；plain在 \(\kappa<3/4\) 时用冻结450扩展，且必须取 \(\kappa_{\rm act}=2\beta_*-1\)。

**marked加plain pointwise。** 对 retained primes总长 \(z'\)，output marked moment的实际两条件是
\[
 \ell+2z'<\eta,\qquad 2\ell+8z'<3\eta.
 \tag{13}
\]
因此
\[
 \eta_M=\max\{1,\ell+2z',(2\ell+8z')/3\}.
\]
pointwise两份 \(S\)的 squared费用 \(U^{2\delta m}\)。减去真实 combined saturation后，count rate为
\[
 R_M^{\rm amp}(z')=E(\eta_M)-\delta\ell-2qz'.
 \tag{14}
\]
当前 \(\ell>1\)，在 \(z'\le\ell/2\) 时 \(\eta_M=\ell+2z'\)，故
\[
 \frac{dR_M^{\rm amp}}{dz'}=\frac53-2q>0.
\]
在更大 \(z'\) 时第二 width可能主导，导数为 \(20/9-2q>0\)。因为 \(2q\le\delta\le\kappa\le5/6\)，两区间uniform严格正。最佳是 \(z'=0\)：
\[
 R_M^{\rm amp}(0)=\frac{1+5\ell}{6}-\delta\ell=L(\ell).
 \tag{15}
\]
删除 slots的 \(P_i^{-1}\) scalar terms在(11)中只更易支付；全 retained term始终存在，不能把所有 terms都替成删除所得gain。

**plain加inverse pointwise。** 真正 output budget为
\[
 2m+6\kappa_{\rm act}z'\le\eta .
\]
fixed coefficients、mesh、whole orientation及自然零不变。相应
\[
 \eta_P=\max\{1,2m+6\kappa_{\rm act}z'\},\quad
 R_P^{\rm amp}(z')=E(\eta_P)-2\delta m-2qz'.
 \tag{16}
\]
在原 \(z_P=(1-2m)/(6\kappa_{\rm act})\) 以下，rate随 \(z'\)下降；超过它后
\[
 \frac{dR_P^{\rm amp}}{dz'}=5\kappa_{\rm act}-2q
 \ge4\kappa_{\rm act}>0.
\]
因此最佳仍是原 capacity：
\[
 R_P^{\rm amp}(z_P)=1-2\delta m-2qz_P.
 \tag{17}
\]
若 physical supply更小，最大合法 \(z'\)相应截断；不能因此改善(17)。固定 \(a\) 后用原 row width和common puncture作plain调用，也只回到同一原预算；它没有额外 \(A^{-1}\)收益。

这些是连续公式；不是信任网格。允许两个有效 bounds作 Hölder/interpolation只得到原两条费用的凸组合，不能低于其中最小值。联合 covariance bound或新 mixed raw theorem没有被包含在这个比较中。

## 8. 临界数字、列范数-only输入及准确未付 raw toll

在冻结451的 reference root \(e\) 上，
\[
 657e^3-954e^2+21e+20=0,\quad
 \kappa_*=\frac56-\frac e2,\quad
 \delta_*=\frac{5-9e}{6+18e},\quad q_*=\delta_*/2,
\]
\[
 \ell=t_0=\frac{1+3e}{8e},\quad
 r_0=\frac2{3\delta_*}-1,\quad m=t_0-r_0,\quad
 z_P=\frac{1-2m}{6\kappa_*}.
\]
这里只显示 reference limiting point；所有实际 theorem调用取 \(\kappa_{\rm act}\)。

冻结的 equalities给
\[
 E(\ell)-\delta_*\ell=\frac23,\qquad
 2\delta_*m+2q_*z_P=\frac13.
 \tag{18}
\]
因此现有放大 inverse moment乘其余 pointwise fees准确给
\[
 E(\ell)+2\delta_*m+2q_*z_P
 =1+\delta_*\ell.
\]
没有未用的正 margin。若反而把全部 \(z_P\)放进 amplified marked，count为
\[
 \frac23+\left(\frac53-\delta_*\right)z_P>\frac23.
\]

本轮不写文件的 Fraction sign/bisection仅核对这些公式的数值方向：
\[
 \ell=1.124227146786\ldots,\quad m=0.408593527003\ldots,\quad
 z_P=0.040629755884\ldots,
\]
\[
 1+\delta_*\ell=1.436855955655\ldots,\quad
 R_M^{\rm amp}(z_P)=0.718594879649\ldots.
\]
此临时计算没有运行旧脚本、写新JSON或认证实际无穷均值。

仅知道(8)–(9)的 column \(\ell^2\)范数并不够。即使假设一个比当前已引原合同更强的 idealized arbitrary-column large sieve
\[
 \sum_{q_v\ll H}|{\cal C}_v|^2
 \ll(H+T_{\rm col})(HT_{\rm col})^\epsilon,
\]
(11)优化 \(\eta\ge1\)后也只给
\[
 \min_\eta\{\max(\eta,s)-(\eta-1)/6\}
 =E(s),\qquad s=\ell+2m+z_P>1.
 \tag{19}
\]
reference上 \(E(s)=1.818369963897\ldots\)，比所需 exponent高
\(0.381514008242\ldots\)。此处是明确的 conditional comparison，未宣称该 generic sextic large sieve已由源证明。它说明只修 column norm或用裸 length×mass无法支付(1)所需 saving；不证明所有结构化方法不可能。

真正可检验的新输入可写得更弱于“mixed raw无损”：取 \(\eta>\ell\)任意固定小量，结构 row family保留 \(q_{\mathrm{sf}_6(v)}\asymp U\)、原 primitive bin与 \(\Theta\)排除、自然 \(v\)-zeros，必须均匀于 actual三个 tests、一次原 slots及 derivative class。若能证明
\[
 \sum_{v\in{\cal V}(U,U^\eta)}
 \sup_{D',X_1',X_2'}|M_v(D')S_v(X_1')S_v(X_2')Q_{v,I}|^2
 \ll U^{\eta+\gamma+\epsilon}(1+T_1)^B,
 \tag{20}
\]
并同样支付删除-slot terms，则 amplification给 exponent
\(E(\eta)+\gamma\)。在 \(\eta\downarrow\ell\) 的 reference center，所需恰是
\[
 \gamma<1-R_0=\frac13,\qquad
 \chi=\frac13-\gamma-O(\eta-\ell)>0.
 \tag{21}
\]
现有 marked加其余pointwise仅支付 \(\gamma=1/3\)，正好没有 \(\chi\)。(20)必须在不依赖 live columns/selected maximizers的结构 family上证明；不能只在 target-defined core上重述所需(1)。

## 9. generic low原句为何没有支付(20)

9311–9314明确不允许额外 residual coefficient，即便它row-independent；canonical column仍为指定 squarefree Gauss/\(\mu\)类型。grouped \(\beta(N)\)有(8)的好范数，不因此准入该 theorem。

7934–7967中的 arbitrary bounded \(\beta(n,b)\)处于已经完成 exact marked-reflection后的特定 dual form：
squarefree \(n\)、cube/whole \(b\)、quadratic row coupling \(\chi_{k_{\rm res}}(nb)^3\)、slot coupling \(\chi_P(n)^{-2}\) 和两个规定zero masks。原 \(\mu\times1\times1\) sextic column不能跳过completion/reflection便被认作此 dual input。必须实际计算三列共同profile的Euler/Gauss反射、所有 norm variables和row-slot phases，再验证独立性、retained dyads和共同separating measure。

裸 \(\mu*1*1=1\)也不支付它。三个独立 Mellin coordinates对应
\(L_{\rm orig}(s_0,\psi)^{-1}L_{\rm orig}(s_1,\psi)L_{\rm orig}(s_2,\psi)\)；
实际长/短 witness heights不同，原 annular/truncated profiles不迫使 \(s_0=s_1=s_2\)。只在共同argument上取消的Euler identity不能替代完整三变量 integral或某个选中的 block。

下一准确机制因此是(20)中的 structured mixed raw toll：在上述原三列completion/shifted-divisor correlation中证明 \(\gamma<1/3\)，包括 actual unequal Fourier heights、natural extra \(a\)-zeros和一次原 \(Q_i\)。它可以使用已付 column norm/transfer与(12)的slot保留，但不能从原 low theorem的通用名字或任意 \(\beta\)字样免费领取。

## 10. 参数顺序与结论

先固定 actual core neighborhood、finite slot count/coefficients、amplifier \(\eta\)范围及需要的 strict widths；如有新 \(\chi\)，再令 scale-retention/real/witness/whole-slot losses远小于 \(\chi\)。固定mesh与physical positive \(w_{\min}\)后选 divisor losses，统一有限 logarithmic derivatives与joint Sobolev orders；再选 cumulative height allowance内的 \(T_1=U^\tau\)，最后 external tail order和height threshold。没有固定 \(B\)之前反过来选\(\tau\)，也没有追加独立height预算。当前(20)未证，故这一顺序只是准确后续接口而非新whole-chain certification。

已支付：exact full-column \(ua^6\) transfer；无pairwise gcd新假设；全部natural zeros和normalizations；原 tuple/合并列范数；positive slots的uniform保留与近原尺度同时spikes；原 marked/plain调用的真实连续前向优化。

未支付：\(\gamma<1/3\) 或任何 actual \(\chi>0\)、三变量 mixed反射/covariance、全域continued high预算及任何新boundary。结果没有编辑冻结稿，也没有证明 RH/RR、Weil算术桥或简单临界线比例改进。新边界仍需全域完整证明、独立两审和新的正式论文。
