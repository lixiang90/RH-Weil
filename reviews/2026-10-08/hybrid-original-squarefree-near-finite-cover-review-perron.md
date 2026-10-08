# 八平移平方自由近相关覆盖：不同作者全文审查

2026-10-08，perron_reviewer。限定数学 PASS。
仅新增本审查；没有修改作者源、冻结输入、Git、输出或检查器。

## 1. 冻结范围与全文读取

FULL READ [作者源](hybrid-original-squarefree-near-finite-cover-research-root.md)
全部172行，6750 canonical UTF-8 LF bytes，SHA256：

422c2c6c96f3049c4803e1ffe8bacf8ca4ff12b4115ca3bb9592ec263d90ca86

四份输入此前已全文读过，本次重新核对其身份，并复读原载体、实际系数、
远相关和完整函数差的相关段落。LF只转换CRLF/lone CR，不trim：

| 输入 | 行数 | canonical LF SHA256 |
| --- | --- | --- |
| [425原载体](hybrid-whole-fourth-unit-unit-actual-research-whole.md) | 425 | b3f14cf4ee5659f8e23bd51dc9bf71e853e783bd2d55e42ee8846d6e8d1e41dc |
| [188原ν四阶](hybrid-original-squarefree-carrier-fourth-near-research-perron.md) | 188 | 2142645eed724da49a3e6faae7068adb2c8ca907c196a691f09a2b7a7fd6f3ae |
| [490完整函数差](../../notes/490-original-weighted-mobius-squarefree-conditional-remainder.md) | 118 | a5bf40493c864774da5f8fbecce8d257bc21176a78b16ff1841c89843d4924ef |
| [453固定零点包](hybrid-original-squarefree-signed-zero-gram-research-perron.md) | 453 | 0b126138c7bf42e9be3c4352b099a6ab37d88cef93af20593593c8e849aa2a17 |

## 2. 覆盖常数与实际窗口

对固定正概率密度χ，用每个长度h小区间的积分误差求和，
得到对所有相位一致的
\[
 h\sum_{k\in\mathbb Z}\chi(a-kh)
 =1+O(h\|\chi'\|_1).
\]
在原正core \([6T/5,9T/5]\) 上，χ的全部非零lattice点确实在
\(0\le k<d\) 内：\(s_T=o(T)\)，两端各有固定T比例余量。
于是原floor保持准确，且 \(d\eta\le T\)，大T给
\(\nu_T\ge1/(2T)\)。这一步不用有限采样证明无限高度合同。

八个core是 \([1/5+m/2,4/5+m/2]T\)，相邻重叠 \(T/10\)，
整体从 \(T/5\) 到 \(43T/10\)，确实覆盖 \(J=[T/4,4T]\)。
每点至少一份贡献，平均后的下界准确为 \(1/(16T)\)。
所以作者(8)的常数是16：这里的canonical归一化为
\(T^{-1}\int_J\)，其总质量 \(15/4\)，没有改成J上的概率测度。
每份平移ν及平均W仍各为概率测度。

## 3. 核、固定真实系数和完整远相关

平移密度 \(\nu_T(t-h_m)\) 的Fourier核乘 \(e^{ih_mu}\)。
原 \(e^{iTu}\) 与 \(h_m=(-1+m/2)T\) 准确相消成 \(e^{imTu/2}\)。
作者(10)保留两个有限几何因子与全部floor；每个因子模长至多1。
因此 \(\Psi_{\rm cov}(0)=1\)，负频率为共轭，(11)的实数有限展开正确。

R及其平方系数在八份积分里是同一组 \(r_n,g_\ell\)。
没有在不同时间窗重选X、Y、U、V，没有改写成八个新的截断主项。
原实际系数界 \(\sum|g_\ell|\ll XL^2\)、\(D\ll L^{16}\) 保留。
以原 \(\Delta=1024L^{5/2}/X\)，准确有
\[
 s_T\Delta=2048\pi L^2,\qquad
 e^{-\sqrt{s_T\Delta}/16}=X^{-\sqrt{8\pi}}.
\]
故全部far对的absolute费用为 \(X^{2-\sqrt{8\pi}}L^4\)。
这个正包络允许保留整族far，不依赖signed子族范数或零点枚举。

## 4. 近相关合同及完整函数运输

作者(13)按所有实际系数对准确分成D、完整非对角near及完整far。
near为实数，但其单项实部可正可负；Gram半正定不能逐项使用。
八份near平均等于一个完整combined near，故只要求这个实数和的一侧上界。
若其上界为 \(O(X^{B+\epsilon})\)，\(B\ge0\)，则D和far均可吸收，
正覆盖直接给原canonical \(R\) 的相同增长上界。
这是充分合同，没有支付该算术前件，也不能由单个未平移ν反推。

得到canonical界后，在J消费490的完整差 \(P_H=R+E_\theta\)。
令 \(b=\max(B,c_\theta)\)，L⁴三角不等式给完整增长b；
展开四次方差并用Hölder，其最大费用为
\((3b+c_\theta)/4\)，因为 \(b\ge c_\theta\)。
作者(15)及 \(B<c_\theta\) 时误差占优的说明均正确。
名义 \(c_{7/8}=3/7\) 的旧增长 \(5/7\) 对应旧传递 \(9/14\)。

W的支撑确实伸出J：左沿约 \(3T/(8\sqrt L)\)，
右沿约 \(9T/2+5T/(8\sqrt L)\)。
本审查不把453固定零点公式、J误差或490完整差扩张到W支撑。
作者(15)只在J使用这些输入，避免了这个非法运输。

## 5. 最终限定

未发现需修改作者源的数学问题。限定 PASS：
准确有限覆盖、完整系数核、全部far付款及canonical充分合同成立。
未证明真实combined near省幂，没有新whole增长、中心四阶常数、
零点比例、无零区域或辅助W上的旧固定零点包公式。
