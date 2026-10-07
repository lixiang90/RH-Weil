# 442–445精确代数审计范围

2026-10-07。脚本：scripts/hybrid_high_continuation_exact_audit.py；
结果：output/hybrid-high-continuation-exact-audit.json。
脚本仅读原冻结paper.tex，不构建或编辑math仓库。

连续endpoint证书先将J、P分母清除，作为(delta,y)双变量有理多项式逐系数相等验证，
共12个非零系数；正文444再利用显示的非负分解给整个连续rectangle的余量。
另外16,728个有理频率参数检查原Mellin指数与K重写、fixed/moving reference差、
endpoint→d包络、上端扩展及gap只扣一次。

独立有理数包括：boundary69999/80000，m_ad307/11016000，
zeta307/352512000，扩后余量307/11750400，
floor4327/750000，中间120907/36000000，小行172249/2000000。
Euler域、D1(1/3)、actualsupply亦核准确；给出一条可用fixed absolute z线6064241。

JSON绑定442–445的canonical LF SHA256和原source SHA256。
这些核查认证所显示代数，不能认证physical算术identity、通用moments、全纯/无限乘积、
Mellin轮廓与全族continuation或外部Lean kernel；这些分别由正文及独立读源审查负责。
