# 高行严格余量证书：root 独立全文审查

2026-10-08。限定 PASS，仅针对冻结 451 高行域的连续代数余量。
不是新的密度、零点比例或无零边界证明。

全文实读
[被审研究源](hybrid-high-bin-strict-certificate-research-twisted.md)，
canonical UTF-8 LF SHA256
f33ace9d5600e5875ea05aa2ae32c0d70cd02610b6637cabcb53633965421138，
6428 bytes / 215 lines。canonical 只转 CRLF/lone CR，不 trim。

## 1. 原对象和连续域

源保留 451 的指定 cubic root、同一个 b_*、h、κ_* 与
y=1/2−q/delta。a 是 row bin；delta=2a−1，不是全族 β_*。
a≥73/86 等价 delta∈[30/43,3/4]，y∈[0,1/2]。
没有用高 bin 取代唯一参考等号点 delta_*≈0.38858。

原式 F=−2JE*=A(y)delta²−B(y)delta+C(y) 和三项 A,B,C
与 [451](../../notes/451-kappa-feedback-cubic-boundary-and-family-continuation.md)
逐项一致，第三项未省略。δ=l+(r−l)u、y=v/2 后的
t_0j、t_1j、t_2j 展开准确，双次数≤(2,3)。
从 power 到 Bernstein 的 binomial 转换公式正确。

## 2. 实际运行与严格区间下界

root 只读检查冻结 Cubic 模块末尾：它形成并打印 report，没有写
旧 output 或其他文件。随后以 Python -B 从被审源抽取并执行完整
embedded code；导入模块的输出被捕获，未改冻结脚本/输出或 cache。

实际结果：
PASS: all twelve Bernstein coefficients exceed 1/25。

这个运行核验完整十二个系数的指定有理根区间 Horner 下端，
分别严格超过正文表中 45、86、161、286、52、99、181、317、
61、113、203、352 除以 1000。每个阈值大于 1/25。
双 Bernstein 基非负且总和为 1，故对所有连续 (u,v)∈[0,1]²
有 F>1/25；不是由有限网格拟合全域。

D≤3、P≤2、J>0，给 J≤5/2。于是 E*=−F/(2J)<−1/125。
该正分母检查是把 F lower 转成 E upper 的必要步骤，源已保留。

## 3. actual κ 与 d 范围

451 的 derivative bound 及 κ_act−κ_*=2Delta 给
h(R_act−R_*)<Delta/25；相对 C(β_*) 的增量为 −Delta。
因此 E_beta(h)<−1/125−24Delta/25。
这不会调用 κ_* 对应的未成立 zero-free 前件。

原 d≤h 的 endpoint slope 为正；h≤d≤h+ζ、
ζ=Delta/32 的费用≤Delta/16。因此中央真实范围仍有
−1/125−359Delta/400 的严格余量。
这只使用 451 已付的范围合同，不推给任意物理 d 或原所有 analytic
losses，不改 451 的已有无零区域。

## 4. 结论范围

若新 raw count 仅改善 a>73/86，这一区域原来已有固定余量，
直接取 min 不能改变原唯一接触点。若它覆盖更低 a，则必须比较
原 final joint envelope，而不能只和最初 raw inverse count 比较。

独立实跑认证的是指定原实嵌入、准确连续多项式及显示余量。
它不认证 primitive AFE、实际零点 density、原无限轮廓、
新 whole prime fourth、[R] 全包、Lean 或 RH。
既有论文、脚本和输出保持不变。
