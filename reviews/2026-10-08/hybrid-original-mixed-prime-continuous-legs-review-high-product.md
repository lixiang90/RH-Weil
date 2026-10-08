# 两条 mixed prime／continuous 腿：不同作者全文审查

2026-10-08，high_product_joint。研究轮4，基线 main da5f0df。
只新增本 peer，不改作者源、旧冻结文件、输出、检查器或 Git。
结论：以下最终作者源在其明确 actual signed 范围内数学 PASS。
新付款是两个 mixed 贡献的 polylog 上界；两条偏差同时出现的主项未付，
没有新的 whole、中心常数、比例或无零边界。

## 1. 最终冻结身份与读取范围

逐行 FULL READ [最终 mixed 源](hybrid-original-mixed-prime-continuous-legs-research-checkpoint-audit.md)：
228行／10971 canonical LF bytes，SHA256
7716f0b9452914f24e321fe9bd4d76e1e63d1cae0b31a01e18b761a5f58f8a87。
哈希只将 CRLF/lone CR 转 LF，不 trim，不改变末尾。

此前已 FULL READ 原 scalar370、actual425、slice337、
continuous195、note493；本轮重读492，并回核各源的实际 profile、
共同 \(J_q\)、频率 mask 与输入身份。作者表中的五个绑定均一致。
本次没有消费新的外部定理；源的几何和与 Schur 证明可独立核查。

## 2. 先求导，再恢复共同参数

固定连续腿 \(p\)，原两套 same-\(u\) profiles 都是
\(A(p;q,s,u)B(r;q,s,u)\)。scalar 的 zero-extended \(C^2\) 合同给
\(\|\phi'\|_\infty\le\|\phi''\|_1=O_\phi(1)\)，所以
\(|A|\le1\)、\(|p\partial_pA|\ll_\phi1\) 一致成立。
一次连续分部积分的符号、\(q^2/(2\pi i nN_L)\) 与全部两端项正确。
bulk 准确有三项：权 \(p^{-1/2}\) 的导数、profile 导数、以及 \(xg'(x)\)。
没有丢掉 dyadic endpoint 或 \(p=q\) 的 clipped endpoint。

以 \(y=sn/(qX)\)、\(V(y)=X\nu(2\pi Xy)\) 定义 \(V_1=V/y\)，
独立核算得到
\[
 \frac{2\pi s}{q}\nu(2\pi sn/q)
       \frac{q^2}{2\pi nN_L}
       =\frac{s^2}{N_LX^2}V_1(y).
\]
这是精确等式。\(V_1\) 的支撑远离零，前两阶对数导数仍只有对数损失，
原 \(\nu\)、时间 floor 与 positive height 都没有更换。
共同 Mellin 中唯一的 \(n^{it_\nu}(qX)^{-it_\nu}\) 留在联合和外；
逐 residue Cauchy 时它只作为模1的对角乘子，不对它求导。

连续 IBP 必须在恢复后的 profiles 上先完成。
之后只将 actual \(r/s\) 的未求导 ratio profiles 作原 \(C^2\) Fourier 分离，
将 \(g,xg'\) 作固定 Mellin 分离；这些共同包络仅需 \(L^1\)。
\(\phi'(u+\log(s/p))\) 则在固定当前 \(p\) 后直接留作有界的 \(s\) 系数。
它与 \(n\) 和 actual \(r\) 无关；无需 \(\int|t\widehat\phi(t)|dt\)，
无需 \(\phi''\) 的 sup，也无需跨 \(p,q\) 的固定系数前件。

## 3. 单 \(q\) 残类范数与真实边界

固定 \(q,p,j\) 和公共参数，\(n=a+qj\)、\(0\le a<q\)。
actual \(r\) 是不同整数且 \(r<q\)、\(p\le q\)，故
\(\xi_r=pr/q^2\) 的 circle spacing 至少 \(\delta=p/q^2\)；
跨度不超过 \(p(q-1)/q^2\)，wrap gap 也至少 \(\delta\)。
这包含 \(p=q\) 边界，并不要求连续 endpoint 是整数。

几何和给 Gram entry 的界
\(\min(q,(2\|\xi_r-\xi_{r'}\|)^{-1})\)。
每行按 circle 距离排列、用 harmonic 和，得到
\(O(q+\delta^{-1}\log(2q))\) 的绝对行和。
Schur 因而给源(5)，且由 \(p\asymp P\le q\)，费用为
\(O(q^2L/P)\)。这一证明容许每个 \(q,p,j\) 的真实私有 \(r\) coefficients。
\(e(-jpr/q)\) 只改变其模1相位，全部 \(j\) 统一有效。

endpoint 的 \(r\)-腿含 \(p^{-1/2}b_r/r\)；
\(\sum b_r^2\ll1\) 与 \(PR\asymp QS\) 给
\[
 \|H_{q,p,j}\|_{\ell^2(a)}
    \ll \frac{qL^{1/2}}{PR}\ll \frac{L^{1/2}}S .
\]
bulk 多一个 \(P^{-1}\)，连续区间长度至多 \(P\)，
每个 \(p\) 先使用上述范数与对应的 \(F_{q,p}\)，再作 Minkowski／正积分。
没有把随 \(p\) 改变的 \(F\) 当成一个固定向量提出积分；
clipping 很短也不会产生反长度损失。

严格 \(s<q\) 给完整 residue Parseval
\(\|F_{q,p}\|_2^2\ll q\)，所有 \(s\)-coefficients 均独立于 \(a,j\)。
原 \((q,n,S)\) mask、unit 条件及两端 partial period 只收缩正范数。
共同 \(J_q\) 的 \(j\) 数为 \(O(X/S+1)\)，保留 \(+1\)，并用 \(S\le X\) 吸收。
若 edge 有 \(j=0\)，实际 \(n>0\) 保持；\(n=0\) 只在扩大正范数时添加，
从未在零处定义 \(n^{it_\nu}\)。

由 \(\sum_{q\sim Q}b_q\ll\sqrt Q/N_L\)，实际 box 费用准确为
\[
 \frac{S^2}{N_LX^2}\Big(\frac XS+1\Big)
 \frac{\sqrt Q}{N_L}\frac{\sqrt Q}{S}L^C
 \ll \frac{Q}{N_L^2X}\Big(1+\frac SX\Big)L^C\ll L^C.
\]
全部 dyads、公共参数的 \(L^1\) 包络、same-\(u\) 及四种最大标签
只再付 polylog。这是带真实 \(F\) 相消的 signed 联合付款，
没有从旧 signed 总界截取频率子族。

## 4. 交换腿、删除点与最终消费

交换连续 \(p\)／actual \(r\) 后，phase、spacing 与 normalization 对称。
profiles 本身虽不对称，但 continuous profile 的 ratio 导数仍可留在
对应 \(F\) 的有界 \(s\) coefficient 中，actual ratio 仍只需原 \(C^2\) 包络。
所以两方向的完整合同都成立。

连续腿等于 \(s\) 是 measure-zero，actual 腿等于 \(s\) 必须单独扣回。
恢复后的 IBP 与 \(g\) 支撑直接给该点
\(|G_{0,r=s}|\ll b_s\sqrt q/(N_LX)\)：此处 \(P\asymp q\)。
原正 \(\nu\) 的完整 \(n\) 质量为 \(O_\chi(1)\)，含整数计数 \(+1\)，
故 \(\sum_q b_q\sqrt q/(N_LX)\sum_{s<q}b_s^2
\ll Q/(N_L^2X)\)。另一方向相同。
这没有机械套用 discrete \(h\)-Parseval 到连续积分；
旧 actual graph、nn、chirp 与 physical 桥的付款范围未改动。

准确 bilinear measure identity 给两个 mixed 偏差项均为 \(O(L^C)\)，
因而同一个 actual mask 上
\(K_{\rm dev}=K_{\Delta,\Delta}+O_{\phi,\chi,g}(L^C)\)。
该证明无条件，不用普通 \([R_\theta]\) 或 Dirichlet-\(L\) 全族前件。
它没有证明 fixed Mellin 参数下的 centered \(H\) 正能量省幂，
也没有将此 actual carrier 的贡献替换成 canonical whole。
两条 \(\Delta\mu\) 腿的完整 signed 预算仍未证明。
